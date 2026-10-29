# -*- coding: utf-8 -*-
"""Jedan izvor cena za ceo sajt.

Zašto postoji ovaj fajl
-----------------------
Cene su ranije bile upisane rukom na svakoj strani, pa se isti posao na dve
strane pojavljivao sa dve cene. Ovde je svaka usluga zapisana jednom i sve
ostalo se iz toga računa: tabele, kartice, cene u title i description i cene
u strukturnim podacima (schema).

Kako se menja cena
------------------
Promeni brojeve u CENE i pokreni  python3 build.py  — cena se menja svuda.
build.py posle sastavljanja proverava da na stranicama nema ni jednog broja
koji ne postoji u ovom fajlu, pa se razlika između strana ne može vratiti
neopaženo.

Zapis
-----
ključ: (naziv usluge, najniža cena, najviša cena)
  najviša = None   →  otvoren gornji kraj, prikazuje se „od 3.000“
  oba None         →  „po proceni“ (cena se ne može znati unapred)

Sve cene su u dinarima i odnose se na RAD majstora. Izlazak, pregled i
materijal su zasebne stavke — vidi IZLAZAK, PREGLED i MATERIJAL ispod.
"""

# ------------------------------------------------------------------ cene rada
CENE = {
    # --- odgušenje i kanalizacija ---
    "odgusenje_sudopere":    ("Odgušenje sudopere", 3000, 3500),
    "odgusenje_lavaboa":     ("Odgušenje lavaboa", 3000, 3500),
    "odgusenje_wc":          ("Odgušenje WC šolje", 3000, 3500),
    "odgusenje_kade":        ("Odgušenje kade ili tuš kabine", 3000, 3500),
    "odgusenje_slivnika":    ("Odgušenje podnog slivnika", 3000, None),
    "odgusenje_sifona":      ("Odgušenje sifona bez mašine", 3000, None),
    "masinsko_odgusenje":    ("Mašinsko odgušenje kanalizacije", 3500, 7000),
    "odgusenje_vertikale":   ("Odgušenje vertikale u zgradi", 6000, 8000),
    "odgusenje_spoljne":     ("Odgušenje spoljne kanalizacije i šahtova", 8000, None),
    "odgusenje_pritisak":    ("Odgušenje pod visokim pritiskom", 10000, None),
    "snimanje_kamerom":      ("Snimanje kanalizacije kamerom", 6000, 8000),

    # --- detekcija curenja ---
    "detekcija_zona":        ("Detekcija, jedna ograničena zona", 5000, 12000),
    "detekcija_vise":        ("Detekcija, više prostorija ili složen razvod", 10000, 18000),
    "detekcija_termo":       ("Detekcija termovizijskom kamerom", 5000, None),
    "detekcija_geofon":      ("Detekcija geofonom i akustičnom opremom", 7000, None),
    "detekcija_zemlja":      ("Detekcija curenja u zemlji", 10000, 25000),
    "curenje_u_zidu":        ("Pronalaženje curenja u zidu", 5000, 12000),
    "curenje_ispod_poda":    ("Pronalaženje curenja ispod poda", 6000, 15000),
    "curenje_od_komsije":    ("Utvrđivanje curenja koje dolazi od komšije", 5000, 12000),
    "sanacija_curenja":      ("Sanacija pronađenog curenja", None, None),

    # --- ventili, slavine, creva ---
    "zamena_ventila":        ("Zamena ugaonog ili zapornog ventila", 2400, 4000),
    "zamena_ugaonog":        ("Zamena ugaonog ventila", 2400, 3500),
    "zamena_zapornog":       ("Zamena zapornog ventila u stanu", 3500, None),
    "zamena_baterije":       ("Zamena baterije (slavine)", 2500, None),
    "zamena_kartuse":        ("Zamena kartuše u jednoručnoj bateriji", 2200, None),
    "zamena_zaptivki":       ("Zamena zaptivki u staroj slavini", 2000, None),
    "zamena_creva":          ("Zamena fleksibilnog creva", 2000, None),
    "zamena_sifona":         ("Zamena sifona", 2500, None),
    "povezivanje_masine":    ("Povezivanje veš ili sudo mašine", 2500, None),

    # --- sanitarija i kupatilo ---
    "sanitarija_montaza":    ("Montaža i zamena sanitarija", 2500, None),
    "montaza_wc":            ("Montaža WC šolje", 3500, None),
    "montaza_lavaboa":       ("Montaža lavaboa", 3000, None),
    "montaza_kade":          ("Montaža kade ili tuš kabine", 6000, None),
    "renoviranje_kupatila":  ("Renoviranje kupatila, vodoinstalaterski deo", 20000, 60000),

    # --- cevi i instalacije ---
    "zamena_deonice":        ("Zamena deonice vodovodne cevi", 6000, None),
    "popravka_pukle_cevi":   ("Popravka pukle cevi", 4000, None),
    "razvod_kupatilo":       ("Razvod vodovoda u kupatilu", 12000, None),

    # --- vodokotlići ---
    "servis_vodokotlica":    ("Servis vodokotlića — ugradnog ili nadgradnog", 2000, 5000),
    "podesavanje_mehanizma": ("Podešavanje mehanizma bez zamene delova", 2000, None),
    "zamena_plovka":         ("Zamena plovka", 2500, None),
    "zamena_zvona":          ("Zamena zvona i ispusnog mehanizma", 3000, None),
    "zamena_ulivnog":        ("Zamena ulivnog ventila", 3000, None),
    "popravka_tipke":        ("Popravka ili zamena aktivacione tipke", 2500, None),
    "kompletan_servis_kotlica": ("Kompletan servis mehanizma", 3500, 5000),
    "servis_nadgradnog":     ("Servis nadgradnog vodokotlića", 2000, None),
    "zamena_nadgradnog":     ("Zamena nadgradnog vodokotlića", 3000, None),

    # --- bojleri ---
    "servis_bojlera":        ("Servis bojlera i čišćenje kamenca", 3000, 6000),
    "zamena_grejaca":        ("Zamena grejača u bojleru", 4000, None),
    "zamena_termostata":     ("Zamena termostata", 3500, None),
    "zamena_sig_ventila":    ("Zamena sigurnosnog ventila", 2500, None),
    "zamena_anode":          ("Zamena magnezijumske anode", 3000, None),
    "demontaza_bojlera":     ("Demontaža starog bojlera", 2500, None),
    "montaza_bojlera":       ("Montaža novog bojlera", 5000, None),
    "sanacija_prikljucaka":  ("Sanacija priključaka na bojleru", 2500, None),

    # --- hitno ---
    "ispumpavanje":          ("Ispumpavanje vode iz podruma", None, None),
    "zatvaranje_vode":       ("Zatvaranje vode i privremeno rešenje", 2500, None),
}

# ------------------------------------------------- stavke koje nisu rad
# Klijent je tražio da rad, izlazak, pregled i dodatni troškovi budu
# razdvojeni i da formulacija bude ista na svim stranama. Ovo su jedine
# formulacije koje se koriste na sajtu.
IZLAZAK = ("Ne naplaćuje se kada radimo intervenciju. Ako posle pregleda odustanete "
           "od posla — [CENA IZLASKA] RSD, i to vam kažemo unapred, na telefonu.")
PREGLED = ("Pregled i utvrđivanje uzroka ulaze u cenu intervencije. Posebno se "
           "naplaćuje samo dijagnostika instrumentima kao samostalna usluga — "
           "snimanje kanalizacije kamerom ili detekcija curenja.")
MATERIJAL = ("Materijal i rezervni delovi naplaćuju se posebno, po nabavnoj ceni. "
             "Iznos kažemo pre nego što bilo šta kupimo.")
HITNOST = ("Za intervencije noću, vikendom i praznikom važi ista cena kao u "
           "redovnom terminu. Doplate za hitnost nema.")

# Kratke varijante za tabele i kartice.
IZLAZAK_KRATKO = "ne naplaćuje se uz intervenciju"
IZLAZAK_ODUSTANAK = "[CENA IZLASKA]"
PREGLED_KRATKO = "ulazi u cenu intervencije"
MATERIJAL_KRATKO = "po nabavnoj ceni"
HITNOST_KRATKO = "nema"


# ------------------------------------------------------------------ pomoćne
def _fmt(n: int) -> str:
    return "{:,}".format(n).replace(",", ".")


def prikaz(key: str) -> str:
    """Cena kako se piše na sajtu: „3.000–3.500“, „od 6.000“ ili „po proceni“."""
    _, lo, hi = CENE[key]
    if lo is None:
        return "po proceni"
    if hi is None:
        return "od " + _fmt(lo)
    return "%s–%s" % (_fmt(lo), _fmt(hi))


def c(key: str) -> str:
    """Isto kao prikaz() — kraće ime za upotrebu u tekstu."""
    return prikaz(key)


def rsd(key: str) -> str:
    """Cena sa oznakom valute: „od 6.000 RSD“."""
    return prikaz(key) + " RSD"


def od(key: str) -> str:
    """Samo donja granica: „od 3.000“ — za naslove i uvodne rečenice."""
    lo = CENE[key][1]
    return "po proceni" if lo is None else "od " + _fmt(lo)


def do(key: str) -> str:
    """Samo gornja granica: „do 60.000“."""
    hi = CENE[key][2]
    return "" if hi is None else "do " + _fmt(hi)


def broj(key: str, granica: str = "min") -> str:
    """Goli broj bez „od“: 3.000."""
    _, lo, hi = CENE[key]
    n = lo if granica == "min" else hi
    return "" if n is None else _fmt(n)


def opseg(a: str, b: str) -> str:
    """Opseg preko dve usluge: od najniže cene a do najviše cene b."""
    lo = CENE[a][1]
    hi = CENE[b][2] or CENE[b][1]
    return "%s–%s" % (_fmt(lo), _fmt(hi))


def naziv(key: str) -> str:
    return CENE[key][0]


def red(key: str, naziv_override: str = None):
    """Jedan red tabele cena: (naziv, cena)."""
    return (naziv_override or CENE[key][0], prikaz(key))


def tabela(*keys):
    """Više redova za price_table(). Element može biti ključ ili (ključ, naziv)."""
    out = []
    for k in keys:
        if isinstance(k, tuple):
            out.append(red(k[0], k[1]))
        else:
            out.append(red(k))
    return out


def ponuda(*keys):
    """Opseg cena za schema.org Offer — samo iz cena koje su na toj strani.

    Ako bilo koja od navedenih usluga ima otvoren gornji kraj („od 6.000“),
    maxPrice se ne upisuje: na strani ta gornja granica nije napisana, pa je
    ni u strukturnim podacima ne izmišljamo.
    """
    pairs = [(CENE[k][1], CENE[k][2]) for k in keys if CENE[k][1] is not None]
    if not pairs:
        return None
    lo = min(p[0] for p in pairs)
    hi = None if any(p[1] is None for p in pairs) else max(p[1] for p in pairs)
    return (lo, hi)


def raspon_firme() -> str:
    """priceRange za LocalBusiness — od najjeftinije do najskuplje usluge.

    Računa se iz CENE, da ne ostane zapisan broj koji više ne odgovara
    cenovniku.
    """
    lows = [lo for _, lo, _ in CENE.values() if lo is not None]
    his = [hi or lo for _, lo, hi in CENE.values() if lo is not None]
    return "RSD %s–%s" % (_fmt(min(lows)), _fmt(max(his)))


def dozvoljeni_brojevi():
    """Svi brojevi koji smeju da se pojave kao cena — za proveru u build.py."""
    out = set()
    for _, lo, hi in CENE.values():
        if lo is not None:
            out.add(_fmt(lo))
        if hi is not None:
            out.add(_fmt(hi))
    return out
