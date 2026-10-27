# -*- coding: utf-8 -*-
"""Sastavljanje HTML stranica."""

import json
from datetime import date

BUILD_DATE = date.today().isoformat()
from theme import SITE

# ---------------------------------------------------------------- navigacija
OPSTINE_NAZIVI = [
    "Stari grad", "Vračar", "Savski venac", "Novi Beograd", "Zemun", "Voždovac",
    "Zvezdara", "Palilula", "Čukarica", "Rakovica", "Grocka", "Surčin",
    "Obrenovac", "Barajevo", "Lazarevac", "Mladenovac", "Sopot",
]

NAV2 = [
    ("vodovodne-instalacije-i-popravke", "Instalacije i popravke"),
    ("servis-bojlera", "Bojleri"),
    ("servis-ugradnih-vodokotlica-geberit", "Ugradni vodokotlići i Geberit"),
    ("sanitarije-i-kupatila", "Sanitarije i kupatila"),
    ("renoviranje-kupatila", "Renoviranje kupatila"),
    ("za-firme", "Za firme"),
    ("radovi", "Radovi"),
    ("blog", "Saveti"),
    ("o-nama", "O nama"),
]

NAV = [
    ("odgusenje-kanalizacije-beograd", "Odgušenje"),
    ("detekcija-curenja-vode-beograd", "Detekcija curenja"),
    ("snimanje-kanalizacije-kamerom", "Snimanje kamerom"),
    ("hitne-intervencije-beograd", "Hitno 0–24"),
    ("vodoinstalaterske-usluge", "Sve usluge"),
    ("cenovnik", "Cenovnik"),
    ("lokacije", "Lokacije"),
    ("kontakt", "Kontakt"),
]

FOOTER_USLUGE = [
    ("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije"),
    ("odgusenje-sudopere-beograd", "Odgušenje sudopere"),
    ("odgusenje-wc-solje-beograd", "Odgušenje WC šolje"),
    ("masinsko-odgusenje-kanalizacije", "Mašinsko odgušenje"),
    ("detekcija-curenja-vode-beograd", "Detekcija curenja vode"),
    ("servis-ugradnih-vodokotlica-geberit", "Ugradni vodokotlići i Geberit"),
]

FOOTER_LOKACIJE = [
    ("lokacije/vodoinstalater-novi-beograd", "Vodoinstalater Novi Beograd"),
    ("lokacije/vodoinstalater-zemun", "Vodoinstalater Zemun"),
    ("lokacije/vodoinstalater-vozdovac", "Vodoinstalater Voždovac"),
    ("lokacije/vodoinstalater-zvezdara", "Vodoinstalater Zvezdara"),
    ("lokacije", "Sve lokacije"),
]

SVG_PHONE = (
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
    '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a1 1 0 0 1-1.1 1A16 16 0 0 1 4 5.1 1 1 0 0 1 5 4z"/></svg>'
)
SVG_TICK = (
    '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M20 6 9 17l-5-5"/></svg>'
)
SVG_CHAT = (
    '<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9 9 0 0 1-4.2-1L3 20l1.2-4.4A8.4 8.4 0 0 1 3 11.5 8.4 8.4 0 0 1 12 3a8.4 8.4 0 0 1 9 8.5z"/></svg>'
)


def url(slug: str) -> str:
    """Apsolutni put stranice unutar sajta."""
    return "/" if slug == "" else "/%s/" % slug


def full(slug: str) -> str:
    return SITE["domain"] + url(slug)


def depth_prefix(slug: str) -> str:
    """Relativni prefiks do korena (za asset putanje na lokalnom pregledu)."""
    if slug == "":
        return ""
    return "../" * (slug.count("/") + 1)


# ---------------------------------------------------------------- strukturni podaci
def ld_plumber() -> dict:
    return {
        "@type": ["Plumber", "LocalBusiness"],
        "@id": SITE["domain"] + "/#firma",
        "name": SITE["name"],
        "url": SITE["domain"] + "/",
        "telephone": SITE["phone_href"],
        "email": SITE["email"],
        "image": SITE["domain"] + "/assets/img/og.jpg",
        "priceRange": "RSD 2.000–40.000",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["address"],
            "addressLocality": SITE["city"],
            "postalCode": SITE["postal"],
            "addressCountry": "RS",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lon"]},
        "areaServed": [{"@type": "City", "name": "Beograd"}] + [
            {"@type": "AdministrativeArea", "name": n} for n in OPSTINE_NAZIVI
        ],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59",
        }],
        "sameAs": ["[GOOGLE PROFIL URL]", "[FACEBOOK URL]", "[INSTAGRAM URL]"],
        "logo": {
            "@type": "ImageObject",
            "@id": SITE["domain"] + "/#logo",
            "url": SITE["domain"] + "/assets/img/og.jpg",
            "width": 1200,
            "height": 630,
            "caption": SITE["name"],
        },
        "founder": {"@id": SITE["domain"] + "/#vlasnik"},
        "employee": {"@id": SITE["domain"] + "/#vlasnik"},
        "currenciesAccepted": "RSD",
        "paymentAccepted": "Gotovina, uplata na račun",
        "knowsLanguage": ["sr", "en"],
        "slogan": "Cena se dogovara pre početka rada.",
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Vodoinstalaterske usluge u Beogradu",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n},
                 "priceCurrency": "RSD"}
                for n in ("Odgušenje kanalizacije", "Detekcija curenja vode",
                          "Snimanje kanalizacije kamerom", "Hitne intervencije 0-24",
                          "Popravka pukle cevi", "Servis bojlera",
                          "Servis ugradnog vodokotlića", "Renoviranje kupatila")
            ],
        },
    }


def ld_breadcrumbs(crumbs, page_slug=None) -> dict:
    items = []
    for i, (slug, label) in enumerate(crumbs, start=1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": label,
            "item": full(slug),
        })
    out = {"@type": "BreadcrumbList", "itemListElement": items}
    if crumbs:
        out["@id"] = full(crumbs[-1][0]) + "#putanja"
    return out


def ld_faq(page) -> dict:
    faq = page["faq"]
    return {
        "@type": "FAQPage",
        "@id": full(page["slug"]) + "#faq",
        "inLanguage": "sr-Latn-RS",
        "isPartOf": {"@id": full(page["slug"]) + "#strana"},
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq
        ],
    }


def ld_article(page) -> dict:
    return {
        "@type": "Article",
        "@id": full(page["slug"]) + "#clanak",
        "isPartOf": {"@id": full(page["slug"]) + "#strana"},
        "headline": page["h1"],
        "description": page["desc"],
        "inLanguage": "sr-Latn-RS",
        "mainEntityOfPage": {"@type": "WebPage", "@id": full(page["slug"])},
        "datePublished": page.get("published", "2026-01-15"),
        "dateModified": page.get("modified", page.get("published", "2026-01-15")),
        "author": {"@id": SITE["domain"] + "/#vlasnik"},
        "publisher": {"@id": SITE["domain"] + "/#firma"},
    }


def ld_service(page) -> dict:
    data = {
        "@type": "Service",
        "@id": full(page["slug"]) + "#usluga",
        "isPartOf": {"@id": full(page["slug"]) + "#strana"},
        "name": page["h1"],
        "serviceType": page.get("service_type", page["h1"]),
        "url": full(page["slug"]),
        "provider": {"@id": SITE["domain"] + "/#firma"},
        "areaServed": ({"@type": "AdministrativeArea", "name": page["area"]}
                       if page.get("area") else {"@type": "City", "name": "Beograd"}),
    }
    offer = page.get("offer")
    if offer:
        data["offers"] = {
            "@type": "Offer",
            "priceCurrency": "RSD",
            "priceSpecification": {
                "@type": "PriceSpecification",
                "priceCurrency": "RSD",
                "minPrice": offer[0],
                "maxPrice": offer[1],
            },
            "availability": "https://schema.org/InStock",
            "url": full(page["slug"]),
            "validFrom": BUILD_DATE,
        }
    return data


def ld_person() -> dict:
    return {
        "@type": "Person",
        "@id": SITE["domain"] + "/#vlasnik",
        "name": SITE["owner"],
        "jobTitle": "Vodoinstalater, vlasnik",
        "worksFor": {"@id": SITE["domain"] + "/#firma"},
        "knowsAbout": [
            "odgušenje kanalizacije", "detekcija curenja vode",
            "inspekcija kanalizacije kamerom", "vodovodne instalacije",
            "servis bojlera", "ugradni vodokotlići",
        ],
    }


def ld_website() -> dict:
    return {
        "@type": "WebSite",
        "@id": SITE["domain"] + "/#sajt",
        "url": SITE["domain"] + "/",
        "name": SITE["name"],
        "inLanguage": "sr-Latn-RS",
        "publisher": {"@id": SITE["domain"] + "/#firma"},
    }


def ld_webpage(page) -> dict:
    data = {
        "@type": "WebPage",
        "@id": full(page["slug"]) + "#strana",
        "url": full(page["slug"]),
        "name": page["title"],
        "description": page["desc"],
        "inLanguage": "sr-Latn-RS",
        "isPartOf": {"@id": SITE["domain"] + "/#sajt"},
        "about": {"@id": SITE["domain"] + "/#firma"},
        "breadcrumb": {"@id": full(page["slug"]) + "#putanja"},
        "primaryImageOfPage": {"@id": SITE["domain"] + "/#logo"},
        "dateModified": page.get("modified", BUILD_DATE),
    }
    if page.get("schema") == "article":
        data["@type"] = ["WebPage", "ItemPage"]
    return data


# ---------------------------------------------------------------- delovi šablona
def head(page) -> str:
    slug = page["slug"]
    pre = depth_prefix(slug)
    is_art = page.get("schema") == "article"

    graph = [ld_plumber(), ld_person(), ld_website(), ld_webpage(page),
             ld_breadcrumbs(page["crumbs"], page["slug"])]
    if page.get("faq"):
        graph.append(ld_faq(page))
    if page.get("schema") == "service":
        graph.append(ld_service(page))
    if is_art:
        graph.append(ld_article(page))
    ld = ('<script type="application/ld+json">%s</script>'
          % json.dumps({"@context": "https://schema.org", "@graph": graph},
                       ensure_ascii=False, separators=(",", ":")))

    robots = page.get("robots",
                      "index,follow,max-image-preview:large,"
                      "max-snippet:-1,max-video-preview:-1")
    og_type = "article" if is_art else "website"
    art_meta = ""
    if is_art:
        art_meta = (
            f'\n<meta property="article:published_time" content="{page.get("published", BUILD_DATE)}">'
            f'\n<meta property="article:modified_time" content="{page.get("modified", page.get("published", BUILD_DATE))}">'
            f'\n<meta property="article:publisher" content="{SITE["domain"]}/">'
        )
    return f"""<!doctype html>
<html lang="sr-Latn-RS">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{page['title']}</title>
<meta name="description" content="{page['desc']}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{full(slug)}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="sr_RS">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{page['title']}">
<meta property="og:description" content="{page['desc']}">
<meta property="og:url" content="{full(slug)}">
<meta property="og:image" content="{SITE['domain']}/assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{SITE['name']} — vodoinstalater u Beogradu">{art_meta}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{page['title']}">
<meta name="twitter:description" content="{page['desc']}">
<meta name="twitter:image" content="{SITE['domain']}/assets/img/og.jpg">
<meta name="twitter:image:alt" content="{SITE['name']} — vodoinstalater u Beogradu">
<meta name="twitter:site" content="{SITE['twitter']}">
<meta name="theme-color" content="#0F2436">
<link rel="icon" href="{pre}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{pre}assets/img/favicon.svg">
<link rel="alternate" type="application/rss+xml" title="{SITE['name']} — saveti" href="{SITE['domain']}/feed.xml">
<link rel="stylesheet" href="{pre}assets/css/style.css">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" media="print" onload="this.media='all'"
      href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Manrope:wght@400;500;600;700&display=swap">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Manrope:wght@400;500;600;700&display=swap"></noscript>
{ld}
</head>
<body>
<a class="skip" href="#main">Preskoči na sadržaj</a>
"""


def header(page) -> str:
    pre = depth_prefix(page["slug"])
    items = []
    for s, label in NAV:
        cur = ' aria-current="page"' if page["slug"] == s else ""
        items.append(f'<a href="{pre}{s}/"{cur}>{label}</a>')
    nav = "\n        ".join(items)
    items2 = []
    for s, label in NAV2:
        cur = ' aria-current="page"' if page["slug"] == s else ""
        items2.append(f'<a href="{pre}{s}/"{cur}>{label}</a>')
    nav2 = "\n      ".join(items2)
    return f"""<header class="hdr">
  <div class="hdr-in">
    <a class="logo" href="{pre or '/'}">{SITE['name']}</a>
    <nav class="nav" aria-label="Glavni meni">
        {nav}
    </nav>
    <a class="btn-tel" href="tel:{SITE['phone_href']}">{SVG_PHONE}{SITE['phone_display']}</a>
  </div>
  <div class="nav2-wrap">
    <nav class="nav2" aria-label="Ostale usluge">
      {nav2}
    </nav>
  </div>
</header>
"""


def crumbs(page) -> str:
    if page["slug"] == "":
        return ""
    pre = depth_prefix(page["slug"])
    out = []
    last = len(page["crumbs"]) - 1
    for i, (s, label) in enumerate(page["crumbs"]):
        if i == last:
            out.append(f"<li>{label}</li>")
        else:
            href = pre if s == "" else f"{pre}{s}/"
            out.append(f'<li><a href="{href}">{label}</a></li>')
    return '<nav class="crumbs" aria-label="Putanja"><ol>%s</ol></nav>\n' % "".join(out)


def quote_form(page, title="Procena pre dolaska",
               sub="Opišite kvar ili pošaljite fotografiju — javljamo okvirnu cenu i kada možemo da izađemo.") -> str:
    sid = "q-" + (page["slug"].replace("/", "-") or "home")
    pre = depth_prefix(page["slug"])
    return f"""<aside class="quote" id="upit">
  <h2>{title}</h2>
  <p class="sub">{sub}</p>
  <form data-quote action="#" method="post">
    <label for="{sid}-ime">Vaše ime</label>
    <input id="{sid}-ime" name="ime" type="text" autocomplete="name" placeholder="Ime i prezime">
    <label for="{sid}-kvar">Šta se dešava?</label>
    <select id="{sid}-kvar" name="kvar">
      <option>Zapušena kanalizacija ili odvod</option>
      <option>Curenje vode, vlažan zid</option>
      <option>Ugradni vodokotlić ili Geberit</option>
      <option>Kvar na bojleru</option>
      <option>Pukla cev — hitno</option>
      <option>Nešto drugo</option>
    </select>
    <label for="{sid}-opstina">Opština</label>
    <select id="{sid}-opstina" name="opstina">
      <option>Novi Beograd</option><option>Zemun</option><option>Voždovac</option>
      <option>Zvezdara</option><option>Palilula</option><option>Čukarica</option>
      <option>Rakovica</option><option>Vračar</option><option>Stari grad</option>
      <option>Savski venac</option><option>Surčin</option><option>Grocka</option>
      <option>Obrenovac</option><option>Ostalo</option>
    </select>
    <label for="{sid}-tel">Vaš broj telefona</label>
    <input id="{sid}-tel" name="telefon" type="tel" inputmode="tel" autocomplete="tel" placeholder="06x xxx xxxx" required>
    <label for="{sid}-opis">Kratak opis <span style="font-weight:400;color:#5B7286">(opciono)</span></label>
    <textarea id="{sid}-opis" name="opis" placeholder="Na primer: voda se vraća u kadu, zgrada, treći sprat."></textarea>
    <label for="{sid}-foto">Fotografija kvara <span style="font-weight:400;color:#5B7286">(opciono)</span></label>
    <input id="{sid}-foto" name="foto" type="file" accept="image/*,video/*" capture="environment">
    <button class="btn btn-primary" type="submit">Tražim procenu</button>
    <p class="fine" data-ok hidden>Hvala — javljamo se na navedeni broj.</p>
    <p class="fine">Raspitivanje je besplatno i ne obavezuje vas na uslugu.
      Broj telefona koristimo samo da vam se javimo sa procenom —
      <a href="{pre}politika-privatnosti/">politika privatnosti</a>.</p>
  </form>
</aside>"""


def cta(page, title="Treba vam vodoinstalater?",
        text="Recite šta se dešava i u kom ste delu grada — javljamo okvirnu cenu i kada možemo da izađemo.") -> str:
    pre = depth_prefix(page["slug"])
    return f"""<section class="cta">
  <div class="cta-in">
    <div class="cta-txt">
      <h2>{title}</h2>
      <p>{text}</p>
    </div>
    <div class="cta-row" style="margin:0">
      <a class="btn btn-primary" href="tel:{SITE['phone_href']}">{SVG_PHONE}Pozovite {SITE['phone_display']}</a>
      <a class="btn btn-ghost" href="{pre}kontakt/">Pošaljite upit</a>
    </div>
  </div>
</section>
"""


def footer(page) -> str:
    pre = depth_prefix(page["slug"])
    u = "\n      ".join(f'<li><a href="{pre}{s}/">{l}</a></li>' for s, l in FOOTER_USLUGE)
    lk = "\n      ".join(f'<li><a href="{pre}{s}/">{l}</a></li>' for s, l in FOOTER_LOKACIJE)
    return f"""<footer class="ftr">
  <div class="ftr-in">
    <div class="ftr-col">
      <div class="ftr-brand">{SITE['name']}</div>
      <p>{SITE['address']}, {SITE['city']}</p>
      <p>Radno vreme: 00–24, svaki dan</p>
      <p>PIB {SITE['pib']} · Matični broj {SITE['mb']}</p>
    </div>
    <div class="ftr-col">
      <h3>Usluge</h3>
      <ul>
      {u}
      </ul>
    </div>
    <div class="ftr-col">
      <h3>Lokacije</h3>
      <ul>
      {lk}
      </ul>
    </div>
    <div class="ftr-col">
      <h3>Kontakt</h3>
      <p><a class="btn-tel" href="tel:{SITE['phone_href']}">{SVG_PHONE}{SITE['phone_display']}</a></p>
      <p><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
      <p><a href="{pre}o-nama/">O nama</a> · <a href="{pre}radovi/">Radovi</a><br>
      <a href="{pre}garancija/">Garancija</a> · <a href="{pre}za-firme/">Za firme</a><br>
      <a href="{pre}recenzije/">Utisci</a> · <a href="{pre}blog/">Saveti</a></p>
    </div>
  </div>
  <div class="ftr-bot"><div>© 2026 {SITE['name']}. Sva prava zadržana.
    · <a href="{pre}politika-privatnosti/">Politika privatnosti</a>
    · <a href="{pre}garancija/">Garancija i reklamacije</a></div></div>
</footer>

<div class="callbar">
  <a class="c-tel" href="tel:{SITE['phone_href']}">{SVG_PHONE}Pozovite</a>
  <a class="c-ask" href="{pre}kontakt/#upit">Pitajte za cenu</a>
  <a class="c-msg" href="{SITE['whatsapp']}" aria-label="Pišite nam na WhatsApp">{SVG_CHAT}</a>
</div>

<script src="{pre}assets/js/main.js" defer></script>
</body>
</html>
"""


def page_html(page) -> str:
    return (
        head(page)
        + header(page)
        + crumbs(page)
        + '<main id="main">\n'
        + page["body"]
        + "</main>\n"
        + footer(page)
    )
