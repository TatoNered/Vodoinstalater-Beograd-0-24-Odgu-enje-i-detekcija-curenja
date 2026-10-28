/* Minimalna logika: slanje forme i merenje konverzija. */
(function () {
  "use strict";

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

  /* Forma za upit — bez bekenda samo pokazuje poruku. */
  var forms = document.querySelectorAll("form[data-quote]");
  Array.prototype.forEach.call(forms, function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var kvar = f.querySelector("[name=kvar]");
      var opstina = f.querySelector("[name=opstina]");
      var foto = f.querySelector("[name=foto]");
      track("slanje_upita", {
        kanal: "forma",
        vrsta_kvara: kvar ? kvar.value : "",
        opstina: opstina ? opstina.value : "",
        sa_fotografijom: !!(foto && foto.files && foto.files.length),
        strana: location.pathname
      });
      var ok = f.querySelector("[data-ok]");
      if (ok) {
        ok.hidden = false;
        ok.setAttribute("role", "status");
      }
      f.reset();
    });
  });
})();
