# -*- coding: utf-8 -*-
"""Generator statičkog sajta. Pokretanje:  python3 build.py  (iz foldera gen/)"""

import os
import re
import shutil
import sys
from datetime import date

from render import SITE, NAV, BASE, page_html, popuni, url
from theme import CSS, JS

import og
import prices
import content1
import content2
import content3
import content4
import content5
import content6
import locations
import blog

# Сайт собирается в корень репозитория: GitHub Pages отдаёт корень ветки.
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Эти файлы и папки генератор не трогает никогда.
NEVER_TOUCH = {".git", ".github", "gen", "README.md", ".gitignore", "preview"}

PAGES = (content1.PAGES + content2.PAGES + content3.PAGES + content4.PAGES + content5.PAGES + content6.PAGES
         + locations.PAGES + blog.PAGES)

TODAY = date.today().isoformat()

# prioriteti za sitemap
PRIO = {
    "": ("1.0", "weekly"),
    "odgusenje-kanalizacije-beograd": ("0.9", "monthly"),
    "detekcija-curenja-vode-beograd": ("0.9", "monthly"),
    "hitne-intervencije-beograd": ("0.9", "monthly"),
    "cenovnik": ("0.9", "monthly"),
    "kontakt": ("0.8", "monthly"),
    "vodoinstalaterske-usluge": ("0.8", "monthly"),
    "lokacije": ("0.7", "monthly"),
    "garancija": ("0.7", "yearly"),
    "radovi": ("0.7", "monthly"),
    "politika-privatnosti": ("0.2", "yearly"),
    "popravka-pukle-cevi": ("0.8", "monthly"),
    "renoviranje-kupatila": ("0.8", "monthly"),
    "odgusenje-lavaboa": ("0.8", "monthly"),
    "odgusenje-kade-i-tus-kabine": ("0.8", "monthly"),
    "zamena-slavina-i-ventila": ("0.8", "monthly"),
    "popravka-i-zamena-vodovodnih-cevi": ("0.8", "monthly"),
}


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def out_path(slug):
    return os.path.join(OUT, "index.html") if slug == "" \
        else os.path.join(OUT, slug, "index.html")


def check(pages):
    """Provere pre pisanja: duplikati, dužine title/description, mrtvi linkovi."""
    problems = []
    slugs = [p["slug"] for p in pages]
    for s in set(slugs):
        if slugs.count(s) > 1:
            problems.append("duplikat slug-a: %r" % s)

    seen_title, seen_desc = {}, {}
    for p in pages:
        # Dužina se meri posle zamene [TELEFON] i [EMAIL]: pravi broj je
        # duži od popunjivača, pa bi inače title tiho prešao granicu.
        t, d = popuni(p["title"]), popuni(p["desc"])
        if len(t) > 65:
            problems.append("title %d znakova (>65): %s" % (len(t), p["slug"] or "/"))
        if not (110 <= len(d) <= 175):
            problems.append("description %d znakova: %s" % (len(d), p["slug"] or "/"))
        if t in seen_title:
            problems.append("isti title: %s i %s" % (seen_title[t], p["slug"]))
        if d in seen_desc:
            problems.append("isti description: %s i %s" % (seen_desc[d], p["slug"]))
        seen_title[t], seen_desc[d] = p["slug"], p["slug"]
        if p["body"].count("<h1") or p["h1"] not in p["body"]:
            pass
    return problems


def check_links(pages, html_by_slug):
    known = {p["slug"] for p in pages}
    bad = []
    for slug, html in html_by_slug.items():
        base = slug.split("/")[:-1] if "/" in slug else []
        depth = slug.count("/") + 1 if slug else 0
        for href in re.findall(r'href="([^"]+)"', html):
            if href.startswith(("http", "tel:", "mailto:", "#", "viber:", "[")):
                continue
            if href.startswith("assets/") or "assets/" in href:
                continue
            # razreši relativnu putanju u odnosu na dubinu stranice
            href_clean = href.split("#")[0]
            if not href_clean:
                continue
            up = len(re.findall(r"\.\./", href_clean))
            rest = href_clean.replace("../", "").strip("/")
            if up != depth and not (depth == 0 and up == 0):
                bad.append("%s -> %s (pogrešna dubina)" % (slug or "/", href))
                continue
            if rest not in known:
                bad.append("%s -> %s (nepostojeća strana)" % (slug or "/", href))
    return bad


PRICE_RE = re.compile(r"\b\d{1,3}\.\d{3}\b")

# red tabele cena:  <td>naziv</td><td class="num">cena</td>
ROW_RE = re.compile(r"<td>([^<]+)</td><td class=\"num\">([^<]+)</td>")
# kartica sa cenom: <h3>naziv</h3>…<div class="price">cena RSD</div>
CARD_RE = re.compile(r"<h3>([^<]+)</h3><p>[^<]*</p><div class=\"price\">([^<]+)</div>")


def _kljuc_po_nazivu():
    """Naziv usluge → ključ u prices.py, za proveru po imenu."""
    out = {}
    for k, (ime, _, _) in prices.CENE.items():
        out[ime.lower()] = k
    return out


def check_price_names(html_by_slug):
    """Ista usluga po imenu mora da ima istu cenu na svim stranama.

    Klijent je tražio da cene budu usklađene. Provera uzima naziv iz reda
    tabele ili kartice i, ako se taj naziv nalazi u prices.py, zahteva da
    napisana cena bude tačno ona iz prices.py.
    """
    po_nazivu = _kljuc_po_nazivu()
    bad = []
    for slug, html in sorted(html_by_slug.items()):
        body = html.split("<main", 1)[-1].split("</main>", 1)[0]
        for ime, cena in ROW_RE.findall(body) + CARD_RE.findall(body):
            k = po_nazivu.get(ime.strip().lower())
            if not k:
                continue
            treba = prices.prikaz(k)
            ima = cena.replace(" RSD", "").strip()
            if ima != treba:
                bad.append("%s: „%s“ → %s, a u prices.py je %s"
                           % (slug or "/", ime.strip(), ima, treba))
    return bad


def check_prices(pages, html_by_slug):
    """Cene na stranicama moraju da postoje u gen/prices.py.

    Klijent je tražio da jedna usluga ima jednu cenu svuda. Jedini način da to
    ostane tako posle svake izmene je provera na sastavljanju: svaki broj koji
    izgleda kao cena mora da bude granica neke usluge iz prices.py. A maxPrice
    u razmetanju ne sme da bude cena koje na samoj strani nema.
    """
    dozvoljeni = prices.dozvoljeni_brojevi()
    bad = []
    by_slug = {p["slug"]: p for p in pages}
    for slug, html in sorted(html_by_slug.items()):
        body = html.split("<main", 1)[-1].split("</main>", 1)[0]
        body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
        for n in sorted(set(PRICE_RE.findall(body))):
            if n not in dozvoljeni:
                bad.append("%s: cena %s nije u prices.py" % (slug or "/", n))
        # minPrice/maxPrice iz schema moraju da se vide na strani.
        # Čita se iz gotovog HTML-a, a ne iz opisa strane: tako provera važi
        # i kada se cena u razmetanju računa iz prices.py. Ranije je gledala
        # samo staro polje "offer" i propuštala sve strane sa "cene".
        p = by_slug.get(slug) or {}
        offer = p.get("offer")
        if p.get("cene"):
            offer = prices.ponuda(*p["cene"])
        ld = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        if ld:
            spec = re.search(r'"priceSpecification":\{(.*?)\}', ld.group(1))
            if spec:
                lo = re.search(r'"minPrice":(\d+)', spec.group(1))
                hi = re.search(r'"maxPrice":(\d+)', spec.group(1))
                offer = (int(lo.group(1)) if lo else None,
                         int(hi.group(1)) if hi else None)
        if offer:
            vidljivi = set(PRICE_RE.findall(body))
            for val, ime in ((offer[0], "minPrice"), (offer[1], "maxPrice")):
                if val is None:
                    continue
                txt = "{:,}".format(val).replace(",", ".")
                if txt not in vidljivi:
                    bad.append("%s: %s %s nema na strani" % (slug or "/", ime, txt))
    return bad


def check_siroce(pages):
    """Folderi koji su ostali posle preimenovanja strane.

    Generator briše samo ono što je sam napravio u ovom prolazu. Kada se
    nekoj strani promeni adresa, stari folder ostane u repozitorijumu sa
    starim sadržajem i bude objavljen. Ovo ga prijavi.
    """
    zive = {p["slug"].split("/")[0] for p in pages if p["slug"]}
    bad = []
    for ime in sorted(os.listdir(OUT)):
        put = os.path.join(OUT, ime)
        if not os.path.isdir(put) or ime in NEVER_TOUCH or ime in zive:
            continue
        if os.path.isfile(os.path.join(put, "index.html")):
            bad.append("folder /%s/ nije ni jedna strana — ostatak posle "
                       "preimenovanja, obriši ga" % ime)
    return bad


def sitemap(pages):
    rows = []
    for p in sorted(pages, key=lambda x: x["slug"]):
        if "noindex" in p.get("robots", ""):
            continue
        prio, freq = PRIO.get(p["slug"], ("0.6", "monthly"))
        last = p.get("modified") or p.get("published") or TODAY
        rows.append(
            "  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n"
            "    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>"
            % (SITE["domain"], url(p["slug"]), last, freq, prio)
        )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">\n'
            .replace("www.sitemap.org", "www.sitemaps.org")
            + "\n".join(rows) + "\n</urlset>\n")


def rss(pages):
    import email.utils, datetime
    arts = [p for p in pages if p.get("schema") == "article"]
    arts.sort(key=lambda p: p.get("published", ""), reverse=True)
    items = []
    for p in arts:
        y, m, d = (p.get("published") or TODAY).split("-")
        pub = email.utils.format_datetime(
            datetime.datetime(int(y), int(m), int(d), 9, 0, tzinfo=datetime.timezone.utc))
        loc = SITE["domain"] + url(p["slug"])
        items.append(
            "    <item>\n      <title>%s</title>\n      <link>%s</link>\n"
            "      <guid isPermaLink=\"true\">%s</guid>\n      <pubDate>%s</pubDate>\n"
            "      <description>%s</description>\n    </item>"
            % (popuni(p["h1"]), loc, loc, pub, popuni(p["desc"])))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
            '  <channel>\n'
            '    <title>%s — saveti vodoinstalatera</title>\n'
            '    <link>%s/blog/</link>\n'
            '    <description>Praktični saveti o zapušenjima, curenju vode i hitnim situacijama.</description>\n'
            '    <language>sr-Latn-RS</language>\n'
            '    <atom:link href="%s/feed.xml" rel="self" type="application/rss+xml"/>\n'
            '%s\n  </channel>\n</rss>\n'
            % (SITE["name"], SITE["domain"], SITE["domain"], "\n".join(items)))


if SITE.get("preview"):
    # Временный адрес на GitHub Pages. Пускать сюда поиск нельзя: это черновик
    # с заглушками вместо реквизитов, и он уводил бы вес с будущего домена.
    ROBOTS = """User-agent: *
Disallow: /
"""
else:
    ROBOTS = """User-agent: *
Allow: /

Sitemap: %s/sitemap.xml
""" % SITE["domain"]


NOT_FOUND = """<!doctype html>
<html lang="sr-Latn-RS"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Stranica nije pronađena — %(name)s</title>
<meta name="robots" content="noindex,follow">
<link rel="stylesheet" href="%(base)sassets/css/style.css">
</head><body>
<section class="hero"><div class="hero-in"><div class="hero-main">
<p class="pill"><i></i>404</p>
<h1>Ova stranica ne postoji</h1>
<p class="lead">Moguće je da je adresa pogrešno otkucana ili da je strana premeštena.
Ako vam hitno treba majstor, najbrže je telefonom.</p>
<div class="cta-row">
  <a class="btn btn-primary" href="tel:%(tel)s">Pozovite %(phone)s</a>
  <a class="btn btn-ghost" href="%(base)s">Na početnu</a>
</div>
<ul class="ticks">
  <li><a href="%(base)sodgusenje-kanalizacije-beograd/">Odgušenje kanalizacije</a></li>
  <li><a href="%(base)sdetekcija-curenja-vode-beograd/">Detekcija curenja vode</a></li>
  <li><a href="%(base)shitne-intervencije-beograd/">Hitne intervencije 0–24</a></li>
  <li><a href="%(base)scenovnik/">Cenovnik</a></li>
</ul>
</div></div></section>
</body></html>
""" % {"name": SITE["name"], "tel": SITE["phone_href"],
       "phone": SITE["phone_display"], "base": BASE}


HTACCESS = """# Preusmeravanja i keširanje — Apache
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404.html

<IfModule mod_rewrite.c>
  RewriteEngine On
  # https
  RewriteCond %{HTTPS} off
  RewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]
  # bez www
  RewriteCond %{HTTP_HOST} ^www\\.(.+)$ [NC]
  RewriteRule ^(.*)$ https://%1/$1 [R=301,L]
  # uvek sa kosom crtom na kraju
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_URI} !(/$|\\.)
  RewriteRule ^(.*)$ /$1/ [R=301,L]
</IfModule>

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType image/svg+xml "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType text/html "access plus 0 seconds"
</IfModule>
"""


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#0F2436"/>
<path d="M20 18h10a8 8 0 0 1 0 16h-4v12h-6V18zm6 6v4h4a2 2 0 0 0 0-4h-4z" fill="#C8401A"/>
<circle cx="44" cy="42" r="5" fill="#C8401A"/>
</svg>
"""


def main():
    problems = check(PAGES)

    # Удаляем только то, что сами создали в прошлый раз — rmtree по корню
    # репозитория снёс бы .git и генератор вместе с сайтом.
    generated = {"index.html", "sitemap.xml", "robots.txt", "feed.xml",
                 "404.html", ".htaccess", ".nojekyll", "assets"}
    generated |= {p["slug"].split("/")[0] for p in PAGES if p["slug"]}

    # Slika za deljenje se pravi samo ako je Pillow instaliran. Da se ne bi
    # izgubila na mašini bez Pillow-a, sačuvamo je pre brisanja assets/.
    og_stara = None
    _og = os.path.join(OUT, "assets", "img", "og.jpg")
    if os.path.isfile(_og):
        with open(_og, "rb") as f:
            og_stara = f.read()
    for name in sorted(generated - NEVER_TOUCH):
        path = os.path.join(OUT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)

    html_by_slug = {}
    for p in PAGES:
        html_by_slug[p["slug"]] = page_html(p)

    bad = check_links(PAGES, html_by_slug)
    bad += check_siroce(PAGES)
    cene_bad = check_prices(PAGES, html_by_slug) + check_price_names(html_by_slug)

    for slug, html in html_by_slug.items():
        write(out_path(slug), html)

    write(os.path.join(OUT, "assets", "css", "style.css"), CSS)
    write(os.path.join(OUT, "assets", "js", "main.js"), JS)
    write(os.path.join(OUT, "assets", "img", "favicon.svg"), FAVICON)

    # Slika za deljenje. Tekst na njoj dolazi iz SITE, pa se posle upisivanja
    # pravog imena i telefona sama ispravi.
    og_path = os.path.join(OUT, "assets", "img", "og.jpg")
    og_ok = og.napravi(og_path, SITE)
    if not og_ok and og_stara is not None:
        os.makedirs(os.path.dirname(og_path), exist_ok=True)
        with open(og_path, "wb") as f:
            f.write(og_stara)
    write(os.path.join(OUT, "sitemap.xml"), sitemap(PAGES))
    write(os.path.join(OUT, "feed.xml"), rss(PAGES))
    write(os.path.join(OUT, "robots.txt"), ROBOTS)
    write(os.path.join(OUT, "404.html"), NOT_FOUND)
    write(os.path.join(OUT, ".htaccess"), HTACCESS)
    write(os.path.join(OUT, ".nojekyll"), "")

    print("Stranica: %d" % len(PAGES))
    print("Izlaz:    %s" % OUT)
    if problems:
        print("\n— Upozorenja (meta) —")
        for x in problems:
            print("  •", x)
    if bad:
        print("\n— Mrtvi/pogrešni linkovi —")
        for x in bad:
            print("  •", x)
    if cene_bad:
        print("\n— Cene (gen/prices.py) —")
        for x in cene_bad:
            print("  •", x)
    if not og_ok:
        print("\n— Slika za deljenje —")
        print("  • assets/img/og.jpg nije napravljen: nema Pillow-a.")
        print("    Instalacija:  pip3 install --break-system-packages pillow")
        if og_stara is not None:
            print("    Postojeća slika je sačuvana.")
    # Pred puštanje u rad: stvari koje se lako zaborave.
    pred_start = []
    if not SITE.get("preview"):
        if not SITE.get("form_endpoint"):
            pred_start.append("form_endpoint u theme.py je prazan — forma ne šalje upite.")
        if not (SITE.get("ga4_id") or SITE.get("gtm_id")):
            pred_start.append("ga4_id/gtm_id u theme.py su prazni — statistike nema.")
        prazna = [k for k, v in SITE.items()
                  if isinstance(v, str) and "[" in v and "]" in v]
        if prazna:
            pred_start.append("U SITE su ostali popunjivači: " + ", ".join(sorted(prazna)))
        # Popunjivači u tekstu strana — ono što posetilac stvarno vidi.
        u_tekstu = set()
        for html in html_by_slug.values():
            telo = html.split("<main", 1)[-1].split("</main>", 1)[0]
            u_tekstu |= {m for m in re.findall(r"\[[A-ZŠĐČĆŽ@][^\]]*\]", telo)}
        if u_tekstu:
            pred_start.append("Na stranicama se i dalje vide: "
                              + ", ".join(sorted(u_tekstu)[:8]))
    if pred_start:
        print("\n— Pred puštanje u rad —")
        for x in pred_start:
            print("  •", x)
    if not problems and not bad and not cene_bad:
        print("Provere: sve čisto.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
