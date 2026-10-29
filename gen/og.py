# -*- coding: utf-8 -*-
"""Slika za deljenje (Open Graph / Twitter): assets/img/og.jpg, 1200×630.

To je slika koja se vidi kada se link sajta pošalje na Viber, WhatsApp,
Facebook ili u mejlu. U meta tagovima je bila upisana, a fajla nije bilo.

Tekst se uzima iz SITE u theme.py, pa kada se upišu pravo ime firme i broj
telefona, slika se sama ispravi pri sledećem `python3 build.py`.

Potreban je Pillow:  pip3 install --break-system-packages pillow
Ako Pillow nije instaliran, build to kaže i preskače pravljenje slike —
postojeći fajl ostaje kakav je.
"""

import os

W, H = 1200, 630
BG = (15, 36, 54)        # #0F2436 — ista boja kao zaglavlje sajta
BRAND = (200, 64, 26)    # #C8401A
WHITE = (255, 255, 255)
MUTED = (164, 185, 201)

# Fontovi se traže u redu: prvo oni koji podržavaju naša slova (č, ć, š, ž, đ).
KANDIDATI_BOLD = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
]
KANDIDATI_REG = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    "C:/Windows/Fonts/arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
]


def _font(putevi, size):
    from PIL import ImageFont
    for p in putevi:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def _uklopi(draw, tekst, font_putevi, max_w, pocetna, min_vel=34):
    """Smanjuje font dok tekst ne stane u zadatu širinu."""
    vel = pocetna
    while vel > min_vel:
        f = _font(font_putevi, vel)
        if draw.textlength(tekst, font=f) <= max_w:
            return f
        vel -= 2
    return _font(font_putevi, min_vel)


def napravi(putanja, site):
    """Pravi sliku. Vraća True ako je napravljena, False ako Pillow nema."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return False

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Tanka traka u boji brenda duž leve strane i blagi akcent u dnu.
    d.rectangle([0, 0, 14, H], fill=BRAND)
    d.rectangle([0, H - 8, W, H], fill=BRAND)

    pad = 88
    max_w = W - pad * 2

    # Nadnaslov
    f_pill = _font(KANDIDATI_BOLD, 30)
    d.text((pad, 92), "DEŽURNI VODOINSTALATER", font=f_pill, fill=BRAND)

    # Ime firme — najveći red
    ime = site["name"]
    f_ime = _uklopi(d, ime, KANDIDATI_BOLD, max_w, 92, 46)
    d.text((pad, 150), ime, font=f_ime, fill=WHITE)

    # Glavna linija
    f_h = _uklopi(d, "Vodoinstalater Beograd 0–24", KANDIDATI_BOLD, max_w, 72, 40)
    d.text((pad, 262), "Vodoinstalater Beograd 0–24", font=f_h, fill=WHITE)

    # Šta radimo
    f_sub = _font(KANDIDATI_REG, 36)
    d.text((pad, 356), "Odgušenje kanalizacije · Detekcija curenja vode", font=f_sub, fill=MUTED)
    d.text((pad, 404), "Hitne intervencije, svih sedam dana", font=f_sub, fill=MUTED)

    # Telefon u okviru
    tel = site["phone_display"]
    f_tel = _font(KANDIDATI_BOLD, 54)
    tw = d.textlength(tel, font=f_tel)
    bx, by = pad, 490
    d.rounded_rectangle([bx, by, bx + tw + 72, by + 86], radius=14, fill=BRAND)
    d.text((bx + 36, by + 14), tel, font=f_tel, fill=WHITE)

    os.makedirs(os.path.dirname(putanja), exist_ok=True)
    img.save(putanja, "JPEG", quality=86, optimize=True, progressive=True)
    return True
