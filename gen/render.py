# -*- coding: utf-8 -*-
"""Sastavljanje HTML stranica."""

import json
from datetime import date

BUILD_DATE = date.today().isoformat()
from theme import SITE
import prices

# ---------------------------------------------------------------- navigacija
OPSTINE_NAZIVI = [
    "Stari grad", "Vračar", "Savski venac", "Novi Beograd", "Zemun", "Voždovac",
    "Zvezdara", "Palilula", "Čukarica", "Rakovica", "Grocka", "Surčin",
    "Obrenovac", "Barajevo", "Lazarevac", "Mladenovac", "Sopot",
]

NAV2 = [
    ("vodovodne-instalacije-i-popravke", "Instalacije i popravke"),
    ("servis-bojlera", "Bojleri"),
    ("servis-vodokotlica-beograd", "Vodokotlići — ugradni i nadgradni"),
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

# Podnožje nosi sve glavne usluge, u dve kolone. Strane na koje je ranije
# vodilo samo nekoliko linkova iz teksta (zamena bojlera, lavabo, kada,
# slavine i ventili, cevi) sada su dostupne sa svake strane sajta.
FOOTER_USLUGE = [
    ("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije"),
    ("odgusenje-sudopere-beograd", "Odgušenje sudopere"),
    ("odgusenje-lavaboa", "Odgušenje lavaboa"),
    ("odgusenje-wc-solje-beograd", "Odgušenje WC šolje"),
    ("odgusenje-kade-i-tus-kabine", "Odgušenje kade i tuš kabine"),
    ("masinsko-odgusenje-kanalizacije", "Mašinsko odgušenje"),
    ("snimanje-kanalizacije-kamerom", "Snimanje kanalizacije kamerom"),
]

FOOTER_USLUGE2 = [
    ("detekcija-curenja-vode-beograd", "Detekcija curenja vode"),
    ("curenje-vode-od-komsije", "Curenje vode od komšije"),
    ("popravka-i-zamena-vodovodnih-cevi", "Popravka i zamena cevi"),
    ("zamena-slavina-i-ventila", "Zamena slavina i ventila"),
    ("servis-vodokotlica-beograd", "Vodokotlići — ugradni i nadgradni"),
    ("zamena-bojlera", "Zamena bojlera"),
    ("sanitarije-i-kupatila", "Montaža i zamena sanitarija"),
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
SVG_VIBER = (
    '<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M12 2.6c4.3 0 7.4 2.8 7.4 7 0 4.3-3.1 7.1-7.4 7.1-.6 0-1.2 0-1.8-.1l-3.1 2.6c-.3.3-.8 0-.8-.4v-2.5'
    'C4.3 15.1 3 13 3 9.6c0-4.2 3.1-7 7.4-7z"/>'
    '<path d="M9.3 7.2c.4-.1.8.1 1 .5l.5 1c.2.3.1.7-.2.9l-.4.3c-.1.1-.2.3-.1.5.3.7.9 1.3 1.6 1.6.2.1.4 0 .5-.1'
    'l.3-.4c.2-.3.6-.4.9-.2l1 .5c.4.2.6.6.5 1-.1.6-.6 1.1-1.2 1.2-2.4.3-5-2.3-4.7-4.7.1-.6.6-1.1 1.2-1.2z"/>'
    '<path d="M13 6.4c1.9.2 3.2 1.5 3.4 3.4"/></svg>'
)
SVG_CHAT = (
    '<svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9 9 0 0 1-4.2-1L3 20l1.2-4.4A8.4 8.4 0 0 1 3 11.5 8.4 8.4 0 0 1 12 3a8.4 8.4 0 0 1 9 8.5z"/></svg>'
)


from urllib.parse import urlparse

def _base(domen: str) -> str:
    """Putanja do korena sajta. Na GitHub Pages sajt stoji u podfolderu."""
    if "[" in domen:
        raise SystemExit(
            "\ngen/theme.py: PREVIEW je False, a DOMEN je još popunjivač (%s).\n"
            "Upiši pravi domen, na primer:  DOMEN = \"https://vodoinstalater-0-24.rs\"\n"
            % domen)
    return (urlparse(domen).path or "").rstrip("/") + "/"


BASE = _base(SITE["domain"])


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
    # U sameAs idu samo popunjene adrese. Popunjivač bi bio zapis o firmi
    # koji vodi nikuda, a to je gore nego da ga nema.
    mreze = [u for u in ("[GOOGLE PROFIL URL]", "[FACEBOOK URL]", "[INSTAGRAM URL]")
             if not u.startswith("[")]
    data = {
        "@type": ["Plumber", "LocalBusiness"],
        "@id": SITE["domain"] + "/#firma",
        "name": SITE["name"],
        "legalName": SITE["legal_name"],
        "url": SITE["domain"] + "/",
        "telephone": SITE["phone_href"],
        "email": SITE["email"],
        # Raspon se računa iz gen/prices.py — ranije je bio upisan rukom i
        # nije pratio cene (renoviranje ide do 60.000, a u razmetanju je
        # stajalo 40.000).
        "priceRange": prices.raspon_firme(),
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
        # Logotipa nema, pa se „logo“ ne upisuje — ovo je slika za deljenje.
        "image": {
            "@type": "ImageObject",
            "@id": SITE["domain"] + "/#slika",
            "url": SITE["domain"] + "/assets/img/og.jpg",
            "width": 1200,
            "height": 630,
            "caption": SITE["name"],
        },
        "currenciesAccepted": "RSD",
        "paymentAccepted": "Gotovina, uplata na račun",
        "knowsLanguage": ["sr", "en"],
        "slogan": "Cena se dogovara pre početka rada.",
        # Posle uklanjanja Person-čvora iskustvo je glavni signal o tome
        # ko stoji iza posla, pa stoji i u opisu firme.
        "description": ("Vodoinstalaterska služba u Beogradu sa %s iskustva u zanatu. "
                        "Odgušenje kanalizacije, detekcija curenja vode, snimanje kamerom "
                        "i hitne intervencije 0–24, sa računom i pisanom garancijom na rad."
                        % SITE["iskustvo"]),
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Vodoinstalaterske usluge u Beogradu",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n},
                 "priceCurrency": "RSD"}
                for n in ("Odgušenje kanalizacije", "Detekcija curenja vode",
                          "Snimanje kanalizacije kamerom", "Hitne intervencije 0-24",
                          "Popravka pukle cevi", "Servis vodokotlića",
                          "Zamena slavina i ventila", "Renoviranje kupatila")
            ],
        },
    }
    if mreze:
        data["sameAs"] = mreze
    return data


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
        "author": {"@id": SITE["domain"] + "/#firma"},
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
    # Cena u razmetanju dolazi iz gen/prices.py, i to samo iz usluga koje su
    # napisane na toj strani. Gornja granica se upisuje jedino kada je i na
    # strani napisana — kod cene „od 6.000“ maxPrice se ne izmišlja.
    offer = page.get("offer")
    if page.get("cene"):
        offer = prices.ponuda(*page["cene"])
    if offer:
        spec = {
            "@type": "PriceSpecification",
            "priceCurrency": "RSD",
            "minPrice": offer[0],
        }
        if offer[1] is not None:
            spec["maxPrice"] = offer[1]
        data["offers"] = {
            "@type": "Offer",
            "priceCurrency": "RSD",
            "priceSpecification": spec,
            "availability": "https://schema.org/InStock",
            "url": full(page["slug"]),
            "validFrom": BUILD_DATE,
        }
    return data


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
        "primaryImageOfPage": {"@id": SITE["domain"] + "/#slika"},
        "dateModified": page.get("modified", BUILD_DATE),
    }
    if page.get("schema") == "article":
        data["@type"] = ["WebPage", "ItemPage"]
    return data


# ---------------------------------------------------------------- delovi šablona
def analitika() -> str:
    """Kod za statistiku — samo u bojevoj verziji (PREVIEW = False).

    Na probnoj adresi se ne ubacuje, da poseta na njoj ne ulazi u izveštaje.
    Upisuje se ono što je popunjeno u theme.py: GA4 ili GTM. Događaji za
    telefon, Viber, WhatsApp i formu već postoje u main.js i rade sa oba.
    """
    if SITE.get("preview"):
        return ""
    ga = SITE.get("ga4_id") or ""
    gtm = SITE.get("gtm_id") or ""
    if gtm:
        return (
            "\n<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':"
            "new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],"
            "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
            "j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;"
            "f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','%s');</script>"
            % gtm)
    if ga:
        return (
            '\n<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>'
            "\n<script>window.dataLayer=window.dataLayer||[];"
            "function gtag(){dataLayer.push(arguments);}gtag('js',new Date());"
            "gtag('config','%s');</script>" % (ga, ga))
    return ""


def head(page) -> str:
    slug = page["slug"]
    pre = depth_prefix(slug)
    is_art = page.get("schema") == "article"

    graph = [ld_plumber(), ld_website(), ld_webpage(page),
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
    if SITE.get("preview"):
        robots = "noindex,nofollow"
    og_type = "article" if is_art else "website"
    # twitter:site se piše samo ako nalog postoji — popunjivač u meta tagu
    # je lošiji od izostavljenog taga.
    tw = SITE.get("twitter") or ""
    tw_site = ("" if tw.startswith("[") or not tw
               else f'\n<meta name="twitter:site" content="{tw}">')
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
<meta name="twitter:image:alt" content="{SITE['name']} — vodoinstalater u Beogradu">{tw_site}
<meta name="theme-color" content="#0F2436">
<link rel="icon" href="{pre}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{pre}assets/img/favicon.svg">
<link rel="alternate" type="application/rss+xml" title="{SITE['name']} — saveti" href="{SITE['domain']}/feed.xml">
<link rel="stylesheet" href="{pre}assets/css/style.css">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" media="print" onload="this.media='all'"
      href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Manrope:wght@400;500;600;700&display=swap">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Manrope:wght@400;500;600;700&display=swap"></noscript>
{ld}{analitika()}
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
    <a class="btn-tel" href="tel:{SITE['phone_href']}">{SVG_PHONE}{SITE['phone_display']}</a>
    <button class="nav-btn" type="button" aria-expanded="false" aria-controls="glavni-meni">
      <span class="nav-ico" aria-hidden="true"></span>Meni
    </button>
    <div class="nav-box" id="glavni-meni">
      <nav class="nav" aria-label="Glavni meni">
        {nav}
      </nav>
      <nav class="nav2" aria-label="Ostale usluge">
      {nav2}
      </nav>
    </div>
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
    # Spisak opština u formi dolazi iz istog spiska kao i lokacijske strane,
    # da se ne desi da strana postoji a opštine nema u padajućem meniju.
    opstine_opcije = "".join("<option>%s</option>" % n for n in OPSTINE_NAZIVI)
    # Dok adresa za slanje nije upisana u theme.py, forma to kaže otvoreno
    # umesto da se pravi da je upit poslat.
    endpoint = SITE.get("form_endpoint") or ""
    akcija = endpoint or "#"
    napomena = "" if endpoint else (
        '\n    <p class="fine" style="color:#B23A17"><strong>Forma još nije povezana.</strong> '
        'Dok se ne poveže, najbrže je telefonom: '
        f'<a href="tel:{SITE["phone_href"]}">{SITE["phone_display"]}</a>.</p>')

    # Skrivena polja. Pristupni ključ traži Web3Forms; Formspree i sopstvena
    # skripta ga prosto ignorišu, pa isti HTML radi sa oba.
    skriveno = []
    if SITE.get("form_kljuc"):
        skriveno.append('<input type="hidden" name="access_key" value="%s">' % SITE["form_kljuc"])
    naslov = "Upit sa sajta — %s" % (page["slug"] or "početna")
    skriveno.append('<input type="hidden" name="subject" value="%s">' % naslov)
    skriveno.append('<input type="hidden" name="strana" value="/%s/">' % page["slug"])
    # Zamka za botove: čovek ovo polje ne vidi i ne popunjava. Web3Forms
    # odbacuje upit kada je „botcheck“ čekiran, Formspree kada „_gotcha“ nije
    # prazno — zato stoje oba.
    skriveno.append('<input type="checkbox" name="botcheck" tabindex="-1" '
                    'autocomplete="off" style="display:none" aria-hidden="true">')
    skriveno.append('<input type="text" name="_gotcha" tabindex="-1" '
                    'autocomplete="off" style="display:none" aria-hidden="true">')
    skrivena_polja = "\n    ".join(skriveno)
    return f"""<aside class="quote" id="upit">
  <h2>{title}</h2>
  <p class="sub">{sub}</p>
  <form data-quote action="{akcija}" method="post" enctype="multipart/form-data">
    {skrivena_polja}
    <label for="{sid}-ime">Vaše ime</label>
    <input id="{sid}-ime" name="ime" type="text" autocomplete="name" placeholder="Ime i prezime">
    <label for="{sid}-kvar">Šta se dešava?</label>
    <select id="{sid}-kvar" name="kvar">
      <option>Zapušena kanalizacija ili odvod</option>
      <option>Curenje vode, vlažan zid</option>
      <option>Vodokotlić — ugradni ili nadgradni</option>
      <option>Kvar na bojleru</option>
      <option>Pukla cev — hitno</option>
      <option>Nešto drugo</option>
    </select>
    <label for="{sid}-opstina">Opština</label>
    <select id="{sid}-opstina" name="opstina">
      <option value="">Izaberite opštinu</option>
      {opstine_opcije}<option>Ostalo</option>
    </select>
    <label for="{sid}-tel">Vaš broj telefona</label>
    <input id="{sid}-tel" name="telefon" type="tel" inputmode="tel" autocomplete="tel" placeholder="06x xxx xxxx" required>
    <label for="{sid}-opis">Kratak opis <span style="font-weight:400;color:#5B7286">(opciono)</span></label>
    <textarea id="{sid}-opis" name="opis" placeholder="Na primer: voda se vraća u kadu, zgrada, treći sprat."></textarea>
    <label for="{sid}-foto">Fotografija kvara <span style="font-weight:400;color:#5B7286">(opciono)</span></label>
    <input id="{sid}-foto" name="foto" type="file" accept="image/*,video/*" capture="environment">
    <button class="btn btn-primary" type="submit">Tražim procenu</button>
    <p class="fine" data-ok hidden>Hvala — upit je poslat. Javljamo se na navedeni broj.</p>
    <p class="fine" data-err hidden style="color:#B23A17">Upit nije poslat. Pokušajte ponovo ili nas
      pozovite na <a href="tel:{SITE['phone_href']}">{SITE['phone_display']}</a>.</p>{napomena}
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
    u2 = "\n      ".join(f'<li><a href="{pre}{s}/">{l}</a></li>' for s, l in FOOTER_USLUGE2)
    lk = "\n      ".join(f'<li><a href="{pre}{s}/">{l}</a></li>' for s, l in FOOTER_LOKACIJE)
    return f"""<footer class="ftr">
  <div class="ftr-in">
    <div class="ftr-col">
      <div class="ftr-brand">{SITE['name']}</div>
      <p>{SITE['address']}, {SITE['city']}</p>
      <p>Radno vreme: 00–24, svaki dan</p>
      <p>{SITE['iskustvo'].capitalize()} iskustva u zanatu</p>
    </div>
    <div class="ftr-col">
      <h3>Odgušenje i kanalizacija</h3>
      <ul>
      {u}
      </ul>
    </div>
    <div class="ftr-col">
      <h3>Curenje, cevi i popravke</h3>
      <ul>
      {u2}
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
  <div class="ftr-bot"><div>© 2026 {SITE['name']}.
    · <a href="{pre}politika-privatnosti/">Politika privatnosti</a>
    · <a href="{pre}garancija/">Garancija i reklamacije</a>
    <span class="ftr-pravno">Usluge pruža {SITE['legal_name']}, {SITE['address']}, {SITE['city']} ·
    PIB {SITE['pib']} · matični broj {SITE['mb']}</span></div></div>
</footer>

<div class="callbar">
  <a class="c-tel" href="tel:{SITE['phone_href']}">{SVG_PHONE}Pozovite</a>
  <a class="c-ask" href="{pre}kontakt/#upit"><span class="c-ask-l">Pitajte za cenu</span><span class="c-ask-s">Upit</span></a>
  <a class="c-msg c-viber" href="{SITE['viber']}" aria-label="Pišite nam na Viber">{SVG_VIBER}</a>
  <a class="c-msg" href="{SITE['whatsapp']}" aria-label="Pišite nam na WhatsApp">{SVG_CHAT}</a>
</div>

<script src="{pre}assets/js/main.js" defer></script>
</body>
</html>
"""


# U tekstu strana telefon i mejl se pišu kao [TELEFON] i [EMAIL], jer stoje
# usred rečenice. Ovde se zamenjuju vrednostima iz SITE, da ne moraju da se
# traže po fajlovima kada se broj promeni.
ZAMENE = {
    "[TELEFON]": SITE["phone_display"],
    "[EMAIL]": SITE["email"],
    "[NAZIV FIRME]": SITE["name"],          # ime pod kojim firma nastupa
    # Dok nije popunjeno, ovo je zamena samog sobom — popunjivač ostaje
    # vidljiv, umesto da se pretvori u ime brenda.
    "[PRAVNO IME]": SITE["legal_name"],     # pun naziv iz APR-a
    "[GODINA]": SITE["godina_cenovnika"],
    "[ISKUSTVO]": SITE["iskustvo"],       # „20 godina“ — menja se na jednom mestu
}


import re as _re

# Link čija adresa je još popunjivač (href="[GOOGLE PROFIL URL]") ne sme da
# ode na sajt — to je mrtav link. Dok se adresa ne upiše, ostaje samo tekst.
_MRTAV_LINK = _re.compile(r'<a href="\[[^"]*\]"[^>]*>(.*?)</a>', _re.S)


_TOKEN = _re.compile("|".join(_re.escape(k) for k in sorted(ZAMENE, key=len, reverse=True)))


def popuni(text: str) -> str:
    # Jedan prolaz: zamena nikad ne ulazi u sledeću zamenu. Bez toga bi
    # [PRAVNO IME], dok je još popunjivač, bilo pretvoreno u ime brenda.
    text = _TOKEN.sub(lambda m: ZAMENE[m.group()], text)
    return _MRTAV_LINK.sub(r"\1", text)


def page_html(page) -> str:
    # Призыв к контакту в конце каждой страницы, кроме служебных.
    zavrsni = "" if page["slug"] in ("politika-privatnosti", "kontakt") else cta(page)
    return popuni(
        head(page)
        + header(page)
        + crumbs(page)
        + '<main id="main">\n'
        + page["body"]
        + zavrsni
        + "</main>\n"
        + footer(page)
    )
