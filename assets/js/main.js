/* Minimalna logika: meni, slanje forme i merenje konverzija. */
(function () {
  "use strict";

  /* Klasa .js govori CSS-u da sme da sakrije meni iza dugmeta.
     Bez JavaScript-a meni ostaje otvoren i sve je i dalje dostupno. */
  document.documentElement.classList.add("js");

  /* Meni na telefonu. */
  var navBtn = document.querySelector(".nav-btn");
  var navBox = document.getElementById("glavni-meni");
  if (navBtn && navBox) {
    navBtn.addEventListener("click", function () {
      var open = navBox.classList.toggle("open");
      navBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    /* Zatvaranje tasterom Esc i klikom izvan menija. */
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && navBox.classList.contains("open")) {
        navBox.classList.remove("open");
        navBtn.setAttribute("aria-expanded", "false");
        navBtn.focus();
      }
    });
    document.addEventListener("click", function (e) {
      if (!navBox.classList.contains("open")) { return; }
      if (navBox.contains(e.target) || navBtn.contains(e.target)) { return; }
      navBox.classList.remove("open");
      navBtn.setAttribute("aria-expanded", "false");
    });
  }

  /* Jedno mesto za slanje događaja. Radi i sa Google Analytics 4 (gtag)
     i sa Google Tag Manager-om (dataLayer). Ako nijedan nije postavljen,
     poziv se tiho ignoriše — ništa se ne lomi. */
  function track(name, params) {
    params = params || {};
    try {
      if (typeof window.gtag === "function") {
        window.gtag("event", name, params);
      }
      if (Array.isArray(window.dataLayer)) {
        var d = { event: name };
        for (var k in params) { if (params.hasOwnProperty(k)) d[k] = params[k]; }
        window.dataLayer.push(d);
      }
    } catch (err) { /* merenje nikad ne sme da sruši stranicu */ }
  }

  /* Gde je korisnik kliknuo: zaglavlje, hero, donja traka, podnožje… */
  function place(el) {
    var zone = el.closest(".callbar, .hdr, .hero, .quote, .cta, .ftr, .sec");
    if (!zone) { return "ostalo"; }
    if (zone.classList.contains("callbar")) { return "donja traka"; }
    if (zone.classList.contains("hdr")) { return "zaglavlje"; }
    if (zone.classList.contains("hero")) { return "vrh strane"; }
    if (zone.classList.contains("cta")) { return "poziv na akciju"; }
    if (zone.classList.contains("ftr")) { return "podnožje"; }
    return "sadržaj";
  }

  /* Klik na telefon, Viber i WhatsApp. */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[href]");
    if (!a) { return; }
    var href = a.getAttribute("href") || "";
    if (href.indexOf("tel:") === 0) {
      track("poziv_telefonom", { kanal: "telefon", pozicija: place(a),
                                 strana: location.pathname });
    } else if (href.indexOf("viber:") === 0) {
      track("poruka_viber", { kanal: "viber", pozicija: place(a),
                              strana: location.pathname });
    } else if (href.indexOf("wa.me") > -1 || href.indexOf("whatsapp") > -1) {
      track("poruka_whatsapp", { kanal: "whatsapp", pozicija: place(a),
                                 strana: location.pathname });
    } else if (href.indexOf("mailto:") === 0) {
      track("poruka_email", { kanal: "email", pozicija: place(a),
                              strana: location.pathname });
    }
  }, true);

  /* Forma za upit.

     Poruka „Hvala“ se prikazuje tek kada server potvrdi da je upit primljen.
     Ako adresa za slanje nije upisana (action ostane "#"), forma to kaže
     otvoreno i nudi telefon — ne pravi se da je nešto poslato.
     Događaj za statistiku šalje se samo kod uspešnog slanja, da brojevi
     konverzija ne budu lažni. */
  var forms = document.querySelectorAll("form[data-quote]");
  Array.prototype.forEach.call(forms, function (f) {
    var ok = f.querySelector("[data-ok]");
    var err = f.querySelector("[data-err]");
    var dugme = f.querySelector("button[type=submit]");

    function poruka(el, tekst) {
      if (!el) { return; }
      if (tekst) { el.textContent = tekst; }
      el.hidden = false;
      el.setAttribute("role", "status");
    }
    function sakrij() {
      if (ok) { ok.hidden = true; }
      if (err) { err.hidden = true; }
    }

    f.addEventListener("submit", function (e) {
      var akcija = f.getAttribute("action") || "#";
      var kvar = f.querySelector("[name=kvar]");
      var opstina = f.querySelector("[name=opstina]");
      var foto = f.querySelector("[name=foto]");
      var podaci = {
        kanal: "forma",
        vrsta_kvara: kvar ? kvar.value : "",
        opstina: opstina ? opstina.value : "",
        sa_fotografijom: !!(foto && foto.files && foto.files.length),
        strana: location.pathname
      };

      /* Nema adrese za slanje — ne šaljemo nikuda i ne lažemo korisnika. */
      if (akcija === "#" || akcija === "") {
        e.preventDefault();
        sakrij();
        poruka(err, "Forma još nije povezana. Pozovite nas — javljamo okvirnu cenu odmah.");
        return;
      }

      /* Bez fetch-a (vrlo star pregledač) pustimo običan POST na server. */
      if (typeof window.fetch !== "function") {
        track("slanje_upita", podaci);
        return;
      }

      e.preventDefault();
      sakrij();
      if (dugme) { dugme.disabled = true; dugme.textContent = "Šaljem…"; }

      fetch(akcija, {
        method: "POST",
        body: new FormData(f),
        headers: { "Accept": "application/json" }
      }).then(function (r) {
        if (!r.ok) { throw new Error("status " + r.status); }
        track("slanje_upita", podaci);
        poruka(ok);
        f.reset();
      }).catch(function () {
        poruka(err);
      }).then(function () {
        if (dugme) { dugme.disabled = false; dugme.textContent = "Tražim procenu"; }
      });
    });
  });
})();
