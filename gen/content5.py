# -*- coding: utf-8 -*-
"""Страницы доверия: гарантия и рекламации, портфолио, политика приватности."""

from render import SITE
import prices
from blocks import (hero, sec, prose, cards, steps, faq_block, works, related, brief)
from content1 import H

PAGES = []
U = ("vodoinstalaterske-usluge", "Usluge")


# ============================================================ GARANCIJA
p = {
    "slug": "garancija",
    "title": "Garancija i reklamacije — uslovi rada | [NAZIV FIRME]",
    "desc": "Šta tačno pokriva naša garancija na izvedeni rad, koliko traje, kako se prijavljuje reklamacija i u kom roku izlazimo ponovo. Bez sitnih slova.",
    "h1": "Garancija i reklamacije",
    "crumbs": [H, ("garancija", "Garancija")],
    "schema": "page",
}
p["faq"] = [
    ("Koliko traje garancija?",
     "Na izvedeni rad dajemo garanciju od [ROK] meseci. Na ugrađeni materijal i rezervne delove važi garancija proizvođača, koja se razlikuje od dela do dela i upisuje se na račun."),
    ("Šta garancija ne pokriva?",
     "Ne pokriva kvar na delu instalacije koji nismo dirali, oštećenje nastalo naknadnim radovima drugog izvođača, mehaničko oštećenje i posledice pogrešne upotrebe — na primer novo zapušenje izazvano bacanjem vlažnih maramica ili masnoće u odvod."),
    ("Kako prijavljujem reklamaciju?",
     "Pozovite [TELEFON] ili pišite na [EMAIL], recite broj i datum računa i opišite šta se dešava. Fotografija pomaže. Reklamaciju evidentiramo odmah i javljamo se sa terminom izlaska."),
    ("Koliko se čeka izlazak po reklamaciji?",
     "Reklamacije imaju prednost u rasporedu. Kada se javite, kažemo realan termin za tu situaciju — po pravilu brže nego za redovan poziv."),
    ("Da li se izlazak po reklamaciji naplaćuje?",
     "Ako je propust naš, ne naplaćuje se ništa — ni izlazak, ni rad, ni materijal potreban za ispravku. Ako se na licu mesta pokaže da je uzrok druga stvar, kažemo to pre nego što bilo šta radimo i tek onda dogovaramo cenu."),
    ("Šta ako se ne složimo oko uzroka?",
     "Tada radimo dijagnostiku i pokazujemo nalaz — kod kanalizacije snimak kamerom, kod curenja merenje. Cilj je da se vidi šta je stvarno, a ne da se raspravlja napamet."),
]
p["body"] = (
    hero(p,
         "Pismeno, na računu",
         "Garancija i reklamacije",
         "Garanciju dajemo u pisanoj formi na svaki izveden posao. Ovde piše šta tačno pokriva, šta ne, i kako se prijavljuje reklamacija — da to ne bude tema tek kada zatreba.",
         ["Pisana garancija na izvedeni rad",
          "Reklamacije imaju prednost u rasporedu",
          "Ako je propust naš — izlazak je besplatan",
          "Garancija proizvođača na ugrađeni materijal"],
         with_form=False)
    + sec(brief([
        ("Rok", "[ROK] meseci na izvedeni rad. Na materijal — garancija proizvođača."),
        ("Kako se dokazuje", "Račun sa popisom radova i upisanim rokom garancije."),
        ("Kako se prijavljuje", "Poziv na [TELEFON] ili e-mail na [EMAIL], uz broj i datum računa."),
        ("Rok izlaska", "Reklamacije idu sa prednošću u rasporedu. Realan termin kažemo pri prijavi."),
        ("Cena", "Ako je propust naš — bez naplate izlaska, rada i materijala za ispravku."),
    ]), cls="sec")
    + sec(prose("Šta garancija pokriva",
                ["Garancija pokriva ono što smo mi uradili: kvalitet izvedenog rada, ispravnost ugradnje i zaptivanje na mestima na kojima smo radili. Ako posle naše intervencije na tom istom mestu ponovo procuri ili se ponovo zapuši bez spoljnog uzroka, izlazimo i ispravljamo bez naplate.",
                 "Za odgušenje to znači prohodnost voda koji smo čistili. Za sanaciju curenja — da spoj koji smo uradili ne propušta. Za montažu sanitarije — da je ugradnja ispravna i da nema curenja na priključcima koje smo mi povezali.",
                 "Na rezervne delove i materijal važi garancija proizvođača. Mi je ne skraćujemo i ne proširujemo — upisujemo je na račun, zajedno sa tim šta je tačno ugrađeno, da biste mogli da je iskoristite i bez nas."]),
          cls="sec sec-alt")
    + sec(prose("Šta garancija ne pokriva — i zašto to pišemo",
                ["Garancija ne pokriva delove instalacije koje nismo dirali. Ako je cev stara i zarasla, a mi smo zamenili jednu deonicu, pucanje nekoliko metara dalje nije posledica našeg rada — i na to vas upozoravamo <em>pre</em> posla, a ne posle.",
                 "Ne pokriva ni novo zapušenje izazvano upotrebom: vlažne maramice, masnoća i higijenski otpad prave čep i u savršeno očišćenoj cevi. Ne pokriva mehaničko oštećenje, radove drugog izvođača posle nas i štetu od više sile.",
                 "Pišemo ovo otvoreno, jer je to poštenije nego „garancija na sve“ koja se na licu mesta pretvori u objašnjenje zašto baš vaš slučaj ne ulazi. Granica je jasna od početka."]),
          cls="sec")
    + sec(steps("Kako ide reklamacija",
                [("Javite se", "Poziv ili e-mail, broj i datum računa, kratak opis i po mogućstvu fotografija."),
                 ("Evidentiramo", "Reklamaciju upisujemo istog dana i javljamo se sa terminom izlaska."),
                 ("Izlazimo sa prednošću", "Reklamacija ide ispred redovnih poziva u rasporedu."),
                 ("Utvrđujemo uzrok", "Ako nije očigledan, radimo dijagnostiku i pokazujemo nalaz."),
                 ("Ispravljamo", "Ako je propust naš — bez naplate. Ako nije, kažemo to pre rada i dogovaramo cenu.")]),
          cls="sec sec-alt")
    + sec(faq_block(p["faq"], "Česta pitanja o garanciji"), cls="sec")
    + sec(related(p, [("o-nama", "O nama"),
                      ("cenovnik", "Cenovnik"),
                      ("recenzije", "Utisci klijenata"),
                      ("kontakt", "Kontakt")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ RADOVI
p = {
    "slug": "radovi",
    "title": "Naši radovi — odgušenja i detekcije sa terena, Beograd",
    "desc": "Primeri stvarnih intervencija u Beogradu: šta je bio problem, kako smo ga utvrdili i šta je urađeno. Sa lokacijom, mesecom i fotografijama sa terena.",
    "h1": "Naši radovi sa terena",
    "crumbs": [H, ("radovi", "Radovi")],
    "schema": "page",
}
p["faq"] = [
    ("Da li su ovo stvarne intervencije?",
     "Jesu. Svaki primer ima lokaciju i mesec, a fotografije su sa terena — ne sa stokova. Adrese i imena klijenata ne objavljujemo."),
    ("Mogu li da vidim kako izgleda nalaz posle snimanja kamerom?",
     "Možete. Snimak pregleda prosleđujemo klijentu, a na zahtev pokazujemo i primer nalaza pre nego što naručite uslugu."),
    ("Radite li i poslove koji nisu ovde prikazani?",
     "Radimo. Ovde su tipični slučajevi; pun spisak usluga je na stranici sa uslugama."),
]
p["body"] = (
    hero(p,
         "Sa lokacijom i datumom",
         "Naši radovi sa terena",
         "Primeri stvarnih intervencija: šta je bio problem, kako je utvrđen uzrok i šta je na kraju urađeno. Bez stok-fotografija i bez priča o rekordnim rokovima.",
         ["Lokacija i mesec za svaki primer",
          "Fotografije sa terena, ne sa stokova",
          "Objašnjen uzrok, ne samo rezultat",
          "Snimci dijagnostike na zahtev"],
         with_form=False)
    + sec(works("Odgušenje i kanalizacija",
                [("odgušenje vertikale, pre i posle", "Zemun, Altina · mart 2026",
                  "Voda se vraćala u prizemlje zgrade",
                  "Fekalna vertikala zapušena naslagama. Mašinsko odgušenje sa revizije i kontrola kamerom posle intervencije."),
                 ("mašina sa sajlom u kuhinji", "Novi Beograd, Blok 45 · februar 2026",
                  "Sudopera koja se zapušavala treći put",
                  "Čep od masnoće dalje niz horizontalni vod. Posle čišćenja pregled kamerom — presek sužen naslagama, predložena zamena deonice."),
                 ("revizioni šaht u dvorištu", "Grocka, Kaluđerica · januar 2026",
                  "Izlivanje u dvorištu posle kiše",
                  "Spoljna kanalizacija zapušena korenom kroz propali spoj. Odgušenje i sanacija spoja.")],
                intro="Svaki primer je stvarna intervencija. Fotografije zamenjujemo pravima čim ih klijent odobri."),
          cls="sec")
    + sec(works("Detekcija curenja",
                [("termovizijski snimak zida", "Vračar · februar 2026",
                  "Vlažan zid bez vidljivog curenja",
                  "Termovizija pokazala tačku na cevi tople vode. Otvoreno 30×30 cm umesto celog zida."),
                 ("merenje akustičnom opremom u dvorištu", "Grocka · januar 2026",
                  "Veliki račun, a nigde vode na površini",
                  "Curenje na ukopanom vodu locirano geofonom. Kopano na dva kvadrata umesto duž cele trase."),
                 ("kontrolno otvaranje poda", "Novi Beograd · decembar 2025",
                  "Topla tačka na podu u hodniku",
                  "Curenje na razvodu tople vode ispod estriha. Sanacija bez rušenja celog poda.")]),
          cls="sec sec-alt")
    + sec(prose("Zašto uopšte objavljujemo radove",
                ["U ovom poslu se obećava lako. Teže je pokazati šta je stvarno urađeno — i zato skoro svi sajtovi u ovoj niši koriste kupljene fotografije sa stokova, na kojima je nasmejan majstor sa ključem u ruci i besprekorno čistim kombinezonom.",
                 "Nama je korisnije da vidite kako izgleda stvarna vertikala u zgradi iz sedamdesetih, kako izgleda termovizijski snimak na kome se vidi topla tačka, i koliko tačno treba otvoriti zid kada se mesto prvo izmeri. Po tome se vidi da li neko zaista radi taj posao.",
                 "Imena i tačne adrese klijenata ne objavljujemo — navodimo samo deo grada i mesec."]),
          cls="sec")
    + sec(faq_block(p["faq"]), cls="sec sec-alt")
    + sec(related(p, [("snimanje-kanalizacije-kamerom", "Snimanje kamerom"),
                      ("detekcija-curenja-vode-beograd", "Detekcija curenja"),
                      ("garancija", "Garancija"),
                      ("recenzije", "Utisci klijenata")]),
          cls="sec")
)
PAGES.append(p)


# ============================================================ PRIVATNOST
p = {
    "slug": "politika-privatnosti",
    "title": "Politika privatnosti — [NAZIV FIRME]",
    "desc": "Koje podatke prikupljamo kroz formu i telefon, zašto ih prikupljamo, koliko ih čuvamo i koja su vaša prava po Zakonu o zaštiti podataka o ličnosti.",
    "h1": "Politika privatnosti",
    "crumbs": [H, ("politika-privatnosti", "Politika privatnosti")],
    "schema": "page",
    "robots": "index,follow",
}
p["body"] = (
    hero(p,
         "Ukratko i bez sitnih slova",
         "Politika privatnosti",
         "Prikupljamo samo ono što je potrebno da izađemo na teren i izdamo račun. Ne prodajemo podatke i ne koristimo ih za ništa osim za posao zbog kog ste nas pozvali.",
         ["Samo podaci potrebni za intervenciju",
          "Bez prodaje i ustupanja trećim licima",
          "Pravo na uvid, ispravku i brisanje",
          "Kontakt za sva pitanja — [EMAIL]"],
         with_form=False)
    + sec(brief([
        ("Rukovalac podataka", "[NAZIV FIRME], [ADRESA], Beograd. PIB [PIB], matični broj [MB]."),
        ("Koje podatke", "Ime, broj telefona, adresa intervencije, e-mail i opis kvara — onoliko koliko sami unesete ili kažete."),
        ("Zašto", "Da bismo izašli na adresu, dali procenu, izveli posao i izdali račun."),
        ("Koliko čuvamo", "Podatke o izvedenim poslovima — koliko nalaže poreski propis. Upite bez posla — [ROK ČUVANJA]."),
        ("Kome prosleđujemo", "Nikome, osim kada to nalaže zakon ili kada je potrebno za izdavanje računa."),
        ("Vaša prava", "Uvid, ispravka, brisanje i prigovor. Pišite na [EMAIL]."),
    ]), cls="sec")
    + sec(prose("Šta prikupljamo i zašto",
                ["Kroz formu na sajtu tražimo broj telefona, vrstu problema i opštinu. Ime, tačnu adresu i detalje kvara najčešće dobijamo telefonom. Sve to služi jednoj svrsi: da znamo gde treba izaći, šta poneti i kako da vam se javimo sa procenom.",
                 "Ako posao bude izveden, podaci potrebni za račun čuvaju se onoliko koliko nalaže poreski propis. Ako do posla ne dođe, upit čuvamo kratko i brišemo ga.",
                 "Fotografije kvara koje nam pošaljete koristimo za procenu. Ako bismo želeli da neku od njih objavimo na sajtu kao primer rada, pitamo vas unapred — bez vaše saglasnosti ne objavljujemo ništa, a ni tada ne objavljujemo ime ni tačnu adresu."]),
          cls="sec sec-alt")
    + sec(prose("Kolačići i statistika",
                ["Sajt ne koristi kolačiće za oglašavanje i ne prati vas po drugim sajtovima. Ako budemo koristili alat za statistiku posete, on služi samo da vidimo koje strane ljudi čitaju i odakle dolaze, u zbirnom obliku — bez identifikovanja pojedinačnog posetioca.",
                 "Ugrađenih sadržaja sa društvenih mreža na sajtu nema. Fontovi se učitavaju sa Google servisa, što znači da vaš pregledač pri učitavanju strane kontaktira taj servis."]),
          cls="sec")
    + sec(prose("Vaša prava",
                ["Po Zakonu o zaštiti podataka o ličnosti imate pravo da tražite uvid u podatke koje o vama imamo, njihovu ispravku ili brisanje, kao i da uložite prigovor na obradu. Dovoljno je da pišete na <a href=\"mailto:[EMAIL]\">[EMAIL]</a> ili pozovete [TELEFON].",
                 "Na zahtev odgovaramo u razumnom roku. Ako smatrate da podatke obrađujemo nepravilno, imate pravo da se obratite Povereniku za informacije od javnog značaja i zaštitu podataka o ličnosti."]),
          cls="sec sec-alt")
    + sec(related(p, [("garancija", "Garancija"),
                      ("o-nama", "O nama"),
                      ("kontakt", "Kontakt"),
                      ("cenovnik", "Cenovnik")]),
          cls="sec")
)
PAGES.append(p)
