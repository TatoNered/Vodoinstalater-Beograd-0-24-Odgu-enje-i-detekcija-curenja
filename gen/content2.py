# -*- coding: utf-8 -*-
"""Sadržaj: detekcija curenja, kamera, hitne intervencije, Geberit."""

from blocks import (hero, sec, prose, cards, steps, price_table, faq_block,
                    works, chips, related, brief)
from content1 import H, OPSTINE_CHIPS

PAGES = []


# ============================================================ DETEKCIJA — HUB
p = {
    "slug": "detekcija-curenja-vode-beograd",
    "title": "Curenje vode — detekcija bez razbijanja | od 5.000 RSD",
    "desc": "Curenje vode u stanu ili dvorištu: detekcija termovizijskom kamerom i geofonom, bez nepotrebnog razbijanja zidova i pločica. Beograd, okvirno od 5.000 RSD.",
    "h1": "Curenje vode — detekcija i lociranje u Beogradu",
    "crumbs": [H, ("detekcija-curenja-vode-beograd", "Detekcija curenja vode")],
    "schema": "service",
    "service_type": "Detekcija curenja vode",
    "offer": (5000, 25000),
}
p["faq"] = [
    ("Garantujete li da ćete naći tačno mesto curenja?",
     "Cilj je da se zona suzi na metar ili manje, i to u najvećem broju slučajeva uspeva. Kod složenih razvoda, debelih estriha i ukopanih vodova ponekad je potrebno kontrolno otvaranje ili dodatno merenje, i to vam kažemo pre nego što počnemo."),
    ("Zašto ne otvorite odmah tamo gde je fleka?",
     "Zato što voda putuje. Mesto gde se pojavila vlaga često je nekoliko metara dalje od mesta gde cev propušta — voda ide niz cev, ispod estriha ili kroz spoj u pločicama. Otvaranje po fleci je najčešći razlog za nepotrebno obijanje."),
    ("Koliko traje detekcija?",
     "Pregled jedne jasno ograničene zone u stanu traje obično sat do dva. Veći objekti, dvorišni vodovi i kombinacija više metoda traju duže."),
    ("Da li detekcija uključuje i popravku?",
     "Ne, to su dve stavke. Posle detekcije kažemo šta je uzrok i koliko košta sanacija, pa vi odlučujete da li radimo odmah ili kasnije."),
    ("Kako da znam da uopšte imam curenje?",
     "Najpouzdaniji test: zatvorite sve slavine i uređaje koji troše vodu i pogledajte vodomer. Ako se brojčanik i dalje pomera, negde ima curenja. Drugi znaci su vlažan zid, buđ, neobjašnjivo veliki račun i topla tačka na podu kod curenja na toploj vodi."),
    ("Radite li detekciju u dvorištu i ispod betona?",
     "Radimo. Za ukopane vodove koristimo geofon i akustičnu opremu, a kod toplih instalacija i termoviziju. To je zahtevniji posao i cena je viša nego za pregled jedne prostorije."),
]
p["body"] = (
    hero(p,
         "Prvo dijagnostika, pa popravka",
         "Curenje vode — detekcija i lociranje u Beogradu",
         "Vlaga na plafonu, mokar zid, buđ ili veliki račun za vodu — a ne vidi se odakle curi. Opremom lociramo mesto pre nego što se išta obija — tako se otvara dvadesetak centimetara umesto cele prostorije.",
         ["Termovizijska kamera i akustična oprema",
          "Geofon za ukopane i podne vodove",
          "Nalaz sa objašnjenjem i predlogom sanacije",
          "Okvirna cena od 5.000 RSD"])
    + sec(brief([('Šta je', 'Lociranje mesta curenja opremom, pre nego što se bilo šta obija.'), ('Oprema', 'Termovizijska kamera, akustično merenje i geofon, uz proveru pritiska po deonicama.'), ('Cena', 'Jedna zona u stanu 5.000–12.000 RSD. Složen razvod 10.000–18.000. Ukopani dvorišni vod 10.000–25.000.'), ('Koliko traje', 'Pregled jedne ograničene zone obično sat do dva.'), ('Rezultat', 'Obeleženo mesto, objašnjen uzrok i cena sanacije. Popravka se dogovara posebno.')]), cls="sec")
    + sec(prose("Zašto se ne otvara tamo gde je fleka",
                ["Voda retko izlazi tamo gde cev propušta. Ona putuje niz cev, ispod estriha, kroz spoj između pločica i po konstrukciji, pa se pojavi na mestu gde joj je najlakše da izađe. Zbog toga je obijanje po vidljivoj vlazi najskuplja greška: često se otvori pola kupatila, a cev je bila u hodniku.",
                 "Detekcija radi obrnuto. Prvo se sužava zona: proverava se pritisak u instalaciji, odvajaju se deonice, meri se temperatura površina i sluša zvuk vode u cevima. Tek kada se mesto locira, otvara se tačno tu i onoliko koliko je potrebno za popravku.",
                 "Posle pregleda dobijate nalaz: koja instalacija propušta, gde tačno i šta je sledeći opravdan korak. Ako je reč o problemu na kanalizaciji, a ne na vodovodu, radi se <a href=\"../snimanje-kanalizacije-kamerom/\">pregled kamerom</a>, jer se curenje iz kanalizacije drugačije otkriva."]),
          cls="sec")
    + sec(cards("Vrste detekcije koje radimo",
                [("detekcija-curenja-vode-bez-razbijanja", "Detekcija bez razbijanja",
                  "Osnovni pristup: lociranje mesta pre otvaranja, da se obija samo tamo gde je potrebno.", "5.000–12.000 RSD"),
                 ("detekcija-curenja-vode-u-zemlji", "Detekcija curenja u zemlji",
                  "Dvorišni i ukopani vodovi, priključak do vodomera, curenje bez vidljivog traga na površini.", "10.000–25.000 RSD"),
                 ("detekcija-geofonom-i-termovizijom", "Geofon i termovizijska kamera",
                  "Oprema i metode: kada se koristi akustika, kada termovizija i zašto se kombinuju.", "5.000–18.000 RSD"),
                 ("", "Curenje u zidu",
                  "Vertikalni razvod u zidu, spojevi iza pločica, curenje na toploj i hladnoj vodi.", "5.000–12.000 RSD"),
                 ("", "Curenje ispod poda i estriha",
                  "Podno grejanje, razvod u podu i curenje ispod keramike bez vidljivog izvora.", "6.000–15.000 RSD"),
                 ("", "Voda curi od komšije ili kod komšije ispod",
                  "Vlaga na plafonu ili na zidu, a ne zna se čije je. Merimo i dajemo nalaz koji možete pokazati komšiji i upravniku.", "po proceni")],
                intro="Metod biramo prema tome gde je instalacija i da li je reč o toploj ili hladnoj vodi.",
                page=p),
          cls="sec sec-alt")
    + sec(steps("Kako izgleda pregled",
                [("Razgovor i priprema", "Pitamo kada se vlaga pojavila, da li vodomer registruje potrošnju i gde prolaze cevi."),
                 ("Merenje i suženje zone", "Proveravamo pritisak, odvajamo deonice i merimo opremom koja odgovara vrsti instalacije."),
                 ("Lociranje i obeležavanje", "Mesto se obeležava na licu mesta, uz objašnjenje šta je uzrok."),
                 ("Nalaz i predlog sanacije", "Dobijate nalaz i cenu popravke. Odlučujete da li radimo odmah.")],
                intro="Pre dolaska je korisno da pripremite podatak o tome kada je vlaga primećena i da li je bilo skorašnjih radova u stanu."),
          cls="sec")
    + sec(price_table("Cena detekcije curenja vode",
                      [("Jedna jasno ograničena zona u stanu", "5.000–12.000"),
                       ("Više prostorija ili složen razvod", "10.000–18.000"),
                       ("Ukopani dvorišni vod", "10.000–25.000"),
                       ("Detekcija termovizijskom kamerom", "od 5.000"),
                       ("Detekcija geofonom i akustičnom opremom", "od 7.000"),
                       ("Veći poslovni ili zajednički sistem", "po proceni")],
                      intro="Cena zavisi od veličine prostora, broja grana instalacije i od toga da li je cev u zidu, podu ili zemlji.",
                      note_up="Debeo estrih, nepoznata trasa cevi, nedostupni ventili i potreba da se kombinuje više metoda merenja.",
                      note_in="Dolazak, merenje odgovarajućom opremom, obeležavanje mesta i usmeni nalaz sa predlogom sanacije.",
                      caption="Okvirne cene detekcije curenja vode"),
          cls="sec sec-alt", sid="cene")
    + sec(works("Detekcije sa terena",
                [("termovizijski snimak zida", "Vračar · februar 2026",
                  "Vlažan zid bez vidljivog curenja",
                  "Termovizija je pokazala tačku na toploj cevi. Otvoreno 30×30 cm umesto celog zida."),
                 ("merenje akustičnom opremom u dvorištu", "Grocka · januar 2026",
                  "Veliki račun, a nigde vode na površini",
                  "Curenje na ukopanom vodu locirano geofonom, kopano je na dva kvadrata."),
                 ("kontrolno otvaranje poda", "Novi Beograd · decembar 2025",
                  "Topla tačka na podu u hodniku",
                  "Curenje na razvodu tople vode ispod estriha, sanacija bez rušenja celog poda.")]),
          cls="sec")
    + sec(faq_block(p["faq"], "Česta pitanja o detekciji curenja"), cls="sec sec-alt")
    + sec(related(p, [("blog/kako-prepoznati-curenje-vode", "Kako prepoznati curenje"),
                      ("detekcija-curenja-vode-bez-razbijanja", "Bez razbijanja"),
                      ("detekcija-curenja-vode-u-zemlji", "Curenje u zemlji"),
                      ("detekcija-geofonom-i-termovizijom", "Geofon i termovizija")])
          + "\n" + chips("Detekcija po opštinama", OPSTINE_CHIPS, p,
                         last=("lokacije", "Sve lokacije →")),
          cls="sec")
)
PAGES.append(p)


# ============================================================ BEZ RAZBIJANJA
p = {
    "slug": "detekcija-curenja-vode-bez-razbijanja",
    "title": "Detekcija curenja vode bez razbijanja | od 5.000 RSD",
    "desc": "Lociramo curenje vode bez nepotrebnog razbijanja zidova, pločica i poda. Termovizija, akustika i merenje pritiska. Beograd, okvirno od 5.000 RSD.",
    "h1": "Detekcija curenja vode bez razbijanja",
    "crumbs": [H, ("detekcija-curenja-vode-beograd", "Detekcija curenja vode"),
               ("detekcija-curenja-vode-bez-razbijanja", "Bez razbijanja")],
    "schema": "service",
    "service_type": "Detekcija curenja vode bez razbijanja",
    "offer": (5000, 15000),
}
p["faq"] = [
    ("Znači li „bez razbijanja“ da se neće ništa otvarati?",
     "Znači da se ne otvara da bi se tražilo. Kada se mesto locira, otvara se samo tu, i to onoliko koliko je potrebno da se dođe do cevi — najčešće je to površina veličine jedne do dve pločice."),
    ("Da li je moguće da se ništa ne nađe?",
     "Retko, ali je moguće kod vrlo male količine vode ili kada curenje nije stalno nego se javlja povremeno. U tom slučaju predlažemo kontrolno merenje posle nekoliko dana ili drugu metodu."),
    ("Koliko se čeka nalaz?",
     "Nalaz dobijate odmah, na licu mesta. Majstor obeleži mesto, objasni šta je pronašao i kaže koliko bi koštala sanacija."),
    ("Radite li i sanaciju posle detekcije?",
     "Radimo. Ako se složite sa cenom, popravka može da se uradi odmah ili u terminu koji vam odgovara."),
]
p["body"] = (
    hero(p,
         "Prvo se traži, pa se otvara",
         "Detekcija curenja vode bez razbijanja",
         "Umesto da se obija po vlažnoj fleci, mesto curenja se prvo locira opremom. Tako se otvara jedna do dve pločice, a ne pola kupatila.",
         ["Merenje pritiska i odvajanje deonica",
          "Termovizijska i akustična provera",
          "Obeležavanje mesta pre otvaranja",
          "Nalaz i cena sanacije odmah"])
    + sec(prose("Šta znači pregled bez razbijanja",
                ["Pristup je jednostavan: ne otvara se ništa dok se ne zna gde je cev oštećena. Prvo se proverava da li uopšte ima curenja na instalaciji pod pritiskom, zatim se zatvaranjem ventila sužava deo mreže na kome je problem, pa se tek onda meri na površini.",
                 "Termovizija pokazuje temperaturne razlike i korisna je kod tople vode i podnog grejanja. Akustična oprema registruje zvuk vode koja izlazi iz cevi i koristi se i na hladnoj vodi. U praksi se metode kombinuju, jer svaka ima slučajeve u kojima je slabija.",
                 "Rezultat je obeleženo mesto i kratak nalaz: koja instalacija propušta, koliko je mesto duboko i šta je potrebno za popravku. Sa tim nalazom možete da odlučite da li sanaciju radimo mi, ili vam je potreban samo podatak — na primer da biste ga pokazali upravniku zgrade ili osiguranju."]),
          cls="sec")
    + sec(price_table("Cena pregleda",
                      [("Jedna prostorija ili ograničena zona", "5.000–12.000"),
                       ("Više prostorija ili složen razvod", "10.000–18.000"),
                       ("Kontrolno merenje posle sanacije", "po dogovoru"),
                       ("Sanacija pronađenog curenja", "po proceni na licu mesta")],
                      note_up="Nepoznata trasa cevi, nedostupni ventili, debeo estrih i povremeno curenje koje se ne javlja u trenutku merenja.",
                      note_in="Dolazak, merenje, obeležavanje mesta i usmeni nalaz sa predlogom daljih koraka."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"]), cls="sec")
    + sec(related(p, [("detekcija-curenja-vode-beograd", "Detekcija curenja vode"),
                      ("detekcija-geofonom-i-termovizijom", "Geofon i termovizija"),
                      ("detekcija-curenja-vode-u-zemlji", "Curenje u zemlji"),
                      ("vodovodne-instalacije-i-popravke", "Sanacija curenja")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ U ZEMLJI
p = {
    "slug": "detekcija-curenja-vode-u-zemlji",
    "title": "Detekcija curenja vode u zemlji Beograd — 10.000–25.000 RSD",
    "desc": "Lociranje curenja na ukopanim vodovima u dvorištu i na priključku, geofonom i akustičnom opremom. Kopa se samo na obeleženom mestu.",
    "h1": "Detekcija curenja vode u zemlji",
    "crumbs": [H, ("detekcija-curenja-vode-beograd", "Detekcija curenja vode"),
               ("detekcija-curenja-vode-u-zemlji", "Curenje u zemlji")],
    "schema": "service",
    "service_type": "Detekcija curenja vode u zemlji",
    "offer": (10000, 25000),
}
p["faq"] = [
    ("Kako znam da curi ukopana cev, a ne nešto u kući?",
     "Zatvorite glavni ventil na ulazu u objekat i pogledajte vodomer. Ako se i dalje okreće, curenje je na delu između vodomera i objekta, dakle u zemlji."),
    ("Mora li se kopati po celom dvorištu?",
     "Ne. Cilj detekcije je da se mesto suzi na jedan do dva kvadrata, pa se kopa samo tu. Bez merenja se najčešće kopa duž cele trase, što je i skuplje i sporije."),
    ("Radi li akustična oprema i na plastičnim cevima?",
     "Radi, ali teže nego na metalnim, jer plastika slabije prenosi zvuk. Kod plastičnih i okiten cevi obično se kombinuju metode i merenje traje duže."),
    ("Šta ako je cev ispod betona ili ploče?",
     "I to se radi, samo je zahtevnije. Tada se više oslanjamo na merenje pritiska po deonicama i na akustiku, a otvaranje se planira tako da se ošteti što manja površina."),
]
p["body"] = (
    hero(p,
         "Kopa se samo na obeleženom mestu",
         "Detekcija curenja vode u zemlji",
         "Veliki račun za vodu, blato u dvorištu kada nema kiše ili pad pritiska bez vidljivog razloga. Ukopani vod se proverava akustikom i merenjem po deonicama.",
         ["Geofon i akustična oprema",
          "Merenje po deonicama i provera vodomera",
          "Obeleženo mesto pre kopanja",
          "Radi se i na plastičnim i na metalnim cevima"])
    + sec(prose("Kako se traži curenje pod zemljom",
                ["Prvi korak je potvrda da curenje uopšte postoji na ukopanom delu. To se proverava vodomerom i zatvaranjem ventila na ulazu u objekat: ako brojilo radi i kada je sve u kući zatvoreno, problem je spolja.",
                 "Zatim se trasa deli na deonice i meri se gde pritisak pada. Na sumnjivom delu se radi akustično merenje — voda koja izlazi iz cevi pod pritiskom pravi karakterističan šum koji se čuje na površini, a geofon ga pojačava i pomaže da se mesto suzi.",
                 "Na kraju se mesto obeležava i tek onda se kopa. Razlika u praksi je velika: bez merenja se najčešće otvara ceo rov duž trase, a sa merenjem jedan do dva kvadrata. Kod starih dvorišnih instalacija vredi istovremeno proceniti i stanje ostatka voda, da se isti posao ne ponavlja posle godinu dana."]),
          cls="sec")
    + sec(price_table("Cena detekcije u zemlji",
                      [("Ukopani dvorišni vod", "10.000–25.000"),
                       ("Priključak do vodomernog šahta", "od 10.000"),
                       ("Curenje ispod betona ili ploče", "po proceni"),
                       ("Sanacija pronađenog mesta", "po proceni na licu mesta")],
                      note_up="Nepoznata trasa, velika dubina, plastične cevi koje slabo prenose zvuk i rad po lošem vremenu.",
                      note_in="Dolazak, provera vodomera i pritiska, akustično merenje i obeležavanje mesta za kopanje."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"]), cls="sec")
    + sec(related(p, [("detekcija-curenja-vode-beograd", "Detekcija curenja vode"),
                      ("detekcija-geofonom-i-termovizijom", "Geofon i termovizija"),
                      ("detekcija-curenja-vode-bez-razbijanja", "Bez razbijanja"),
                      ("vodovodne-instalacije-i-popravke", "Zamena cevi")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ GEOFON I TERMOVIZIJA
p = {
    "slug": "detekcija-geofonom-i-termovizijom",
    "title": "Detekcija curenja geofonom i termovizijom — Beograd",
    "desc": "Kada se koristi geofon, kada termovizijska kamera i zašto se metode kombinuju. Profesionalna dijagnostika curenja vode u Beogradu.",
    "h1": "Detekcija curenja geofonom i termovizijskom kamerom",
    "crumbs": [H, ("detekcija-curenja-vode-beograd", "Detekcija curenja vode"),
               ("detekcija-geofonom-i-termovizijom", "Geofon i termovizija")],
    "schema": "service",
    "service_type": "Detekcija curenja geofonom i termovizijom",
    "offer": (5000, 18000),
}
p["faq"] = [
    ("Koja metoda je bolja?",
     "Nijedna sama po sebi. Termovizija je jaka kod tople vode i podnog grejanja, akustika kod instalacija pod pritiskom i ukopanih vodova. U praksi se kombinuju, jer se tako isključuju lažni nalazi."),
    ("Radi li termovizija na hladnoj vodi?",
     "Radi posredno. Kamera ne vidi cev nego temperaturnu razliku na površini — kod hladne vode razlika je manja, pa se pouzdanost smanjuje i oslanjamo se više na akustiku i merenje pritiska."),
    ("Može li termovizija da vidi kroz zid?",
     "Ne. Ona prikazuje temperaturu površine, a zaključak o cevi ispod izvodi se iz rasporeda toplih i hladnih zona. Zato je važno iskustvo u tumačenju snimka, a ne samo posedovanje kamere."),
    ("Dobijam li snimak?",
     "Snimke i fotografije sa merenja možemo da vam prosledimo, što je korisno kada nalaz treba pokazati upravniku zgrade, komšiji ili osiguranju."),
]
p["body"] = (
    hero(p,
         "Oprema i metode",
         "Detekcija geofonom i termovizijskom kamerom",
         "Dve različite metode za dva različita tipa problema. Ovde objašnjavamo kada se koja koristi i zašto se najpouzdaniji nalaz dobija kombinacijom.",
         ["Akustično merenje i geofon",
          "Termovizijska kamera",
          "Merenje pritiska po deonicama",
          "Snimak i nalaz na zahtev"])
    + sec(prose("Akustična detekcija i geofon",
                ["Voda koja izlazi iz cevi pod pritiskom pravi šum. Taj šum se širi kroz cev i kroz materijal oko nje, a na površini je pretih da bi se čuo golim uhom. Geofon i akustična oprema ga pojačavaju i filtriraju, pa se poređenjem jačine na više tačaka mesto postepeno sužava.",
                 "Metoda najbolje radi na instalacijama pod pritiskom i na metalnim cevima, koje dobro prenose zvuk. Kod plastičnih i okiten cevi signal je slabiji, pa merenje traje duže i obavezno se kombinuje sa proverom pritiska po deonicama.",
                 "Akustika je glavna metoda kod ukopanih dvorišnih vodova, jer tamo termovizija najčešće nema šta da pokaže."]),
          cls="sec")
    + sec(prose("Termovizijska kamera",
                ["Termovizija prikazuje temperaturu površine. Kod curenja na toploj vodi ili na cevima grejanja, topla voda zagreva materijal oko cevi i na snimku se vidi karakteristična topla zona — često mnogo jasnije nego što se vidi vlaga golim okom.",
                 "Ograničenje je u tome što kamera ne gleda kroz zid. Ona pokazuje posledicu na površini, pa je tumačenje snimka posao koji traži iskustvo: topla zona može poticati i od ispravne cevi grejanja, a hladna fleka od vlage koja isparava.",
                 "Zato se termovizija koristi kao deo postupka, a ne kao jedini dokaz. Nalaz se potvrđuje akustikom ili merenjem pritiska pre nego što se bilo šta otvori."],
                h2_id="termovizija"),
          cls="sec sec-alt")
    + sec(price_table("Cena po metodi",
                      [("Detekcija termovizijskom kamerom", "od 5.000"),
                       ("Detekcija geofonom i akustičnom opremom", "od 7.000"),
                       ("Kombinovana dijagnostika, jedna zona", "5.000–12.000"),
                       ("Kombinovana dijagnostika, složen razvod", "10.000–18.000")],
                      note_up="Veliki objekti, nepoznata trasa instalacije i potreba za ponovljenim merenjem kod povremenog curenja.",
                      note_in="Dolazak, merenje, obeležavanje mesta i usmeni nalaz sa objašnjenjem."),
          cls="sec", sid="cene")
    + sec(faq_block(p["faq"]), cls="sec sec-alt")
    + sec(related(p, [("detekcija-curenja-vode-beograd", "Detekcija curenja vode"),
                      ("detekcija-curenja-vode-u-zemlji", "Curenje u zemlji"),
                      ("detekcija-curenja-vode-bez-razbijanja", "Bez razbijanja"),
                      ("snimanje-kanalizacije-kamerom", "Snimanje kamerom")]),
          cls="sec")
)
PAGES.append(p)


# ============================================================ SNIMANJE KAMEROM
p = {
    "slug": "snimanje-kanalizacije-kamerom",
    "title": "Snimanje kanalizacije kamerom Beograd — 6.000–8.000 RSD",
    "desc": "Inspekcija kanalizacionih cevi kamerom u Beogradu: uzrok ponovljenih zapušenja, oštećenja, nagib i stanje cevi pre kupovine ili renoviranja.",
    "h1": "Snimanje kanalizacije kamerom",
    "crumbs": [H, ("snimanje-kanalizacije-kamerom", "Snimanje kanalizacije kamerom")],
    "schema": "service",
    "service_type": "Snimanje kanalizacije inspekcijskom kamerom",
    "offer": (6000, 8000),
}
p["faq"] = [
    ("Kada ima smisla snimanje kamerom?",
     "Kada se isto mesto zapuši više puta, kada se posle odgušenja problem brzo vrati, pre kupovine ili renoviranja objekta i kada iz kanalizacije stalno ide miris bez jasnog razloga."),
    ("Šta sve kamera može da pokaže?",
     "Naslage i stepen suženja cevi, propale i razdvojene spojeve, pukotine, ulegnuća, pogrešan nagib, prodor korena drveta i predmete u cevi."),
    ("Dobijam li snimak?",
     "Da, snimak vam prosleđujemo. Koristan je i kada treba da dokažete stanje instalacije upravniku zgrade, prodavcu stana ili izvođaču radova."),
    ("Da li se cev prvo mora očistiti?",
     "Najčešće da. Kroz zapušenu cev kamera ne vidi ništa, pa se prvo radi odgušenje, a zatim pregled. Zato se te dve usluge često rade u istom izlasku."),
]
p["body"] = (
    hero(p,
         "Vidi se uzrok, ne samo posledica",
         "Snimanje kanalizacije kamerom u Beogradu",
         "Kada se isti odvod zapuši po treći put, nema smisla ponovo plaćati čišćenje. Inspekcijska kamera pokazuje zašto se to dešava i šta treba popraviti.",
         ["Pregled unutrašnjih i dostupnih spoljnih cevi",
          "Lociranje oštećenja i začepljenja",
          "Snimak ostaje kod vas",
          "Korisno i pre kupovine ili renoviranja"])
    + sec(brief([('Šta je', 'Pregled unutrašnjosti kanalizacione cevi inspekcijskom kamerom.'), ('Kada ima smisla', 'Ponovljena zapušenja, miris bez uzroka, pre kupovine stana i pre renoviranja kupatila.'), ('Cena', '6.000–8.000 RSD. Ako cev prvo mora da se očisti, odgušenje se dogovara posebno.'), ('Šta pokazuje', 'Naslage i stepen suženja, propale spojeve, pukotine, ulegnuća, pogrešan nagib i prodor korena.'), ('Dobijate', 'Snimak pregleda i objašnjenje nalaza.')]), cls="sec")
    + sec(prose("Šta pregled može da otkrije",
                ["Najčešći nalaz su naslage koje su sa godinama suzile presek cevi. U takvoj cevi svaka sitnica pravi čep, pa se zapušenje vraća uprkos redovnom čišćenju. Kamera pokazuje koliki je stvarni presek i da li je cev uopšte isplativo dalje čistiti.",
                 "Drugi čest nalaz je mehaničko oštećenje: razdvojen ili propali spoj, pukotina, ulegnuće zbog sleganja tla ili pogrešno izveden nagib. To se čišćenjem ne rešava — potrebna je popravka ili zamena dela voda, a pregled pokazuje koliki je taj deo.",
                 "Kod kuća sa dvorištem redovno se javlja i prodor korena drveta kroz spoj. Koren raste kroz cev i radi kao sito koje zadržava sve što prođe, pa se zapušenje ponavlja u sve kraćim razmacima."]),
          cls="sec")
    + sec(cards("Kada se najčešće poziva pregled",
                [("", "Ponovljena zapušenja",
                  "Isti odvod se zapušava više puta u kratkom periodu, a čišćenje daje kratkotrajan efekat.", ""),
                 ("", "Pre kupovine stana ili kuće",
                  "Provera stanja kanalizacije pre nego što se potpiše ugovor i preuzme problem.", ""),
                 ("", "Pre renoviranja kupatila",
                  "Da se ne postavi nova keramika preko instalacije koju treba menjati.", ""),
                 ("", "Neprijatan miris bez uzroka",
                  "Miris iz slivnika ili odvoda koji ne nestaje posle čišćenja sifona.", ""),
                 ("", "Posle izlivanja",
                  "Utvrđivanje da li je izlivanje posledica začepljenja ili oštećenja cevi.", ""),
                 ("", "Spor rad uprkos čišćenju",
                  "Voda otiče sporo i kada je vod nedavno očišćen.", "")],
                page=p),
          cls="sec sec-alt")
    + sec(price_table("Cena snimanja kamerom",
                      [("Snimanje kanalizacije kamerom", "6.000–8.000"),
                       ("Snimanje uz odgušenje u istom izlasku", "po dogovoru"),
                       ("Pregled spoljne kanalizacije i šahtova", "po proceni"),
                       ("Snimanje vodovodnih cevi", "od 6.000")],
                      note_up="Nepristupačna revizija, potreba da se vod prvo očisti i veća dužina trase.",
                      note_in="Dolazak, pregled dostupnih cevi kamerom, objašnjenje nalaza i snimak."),
          cls="sec", sid="cene")
    + sec(faq_block(p["faq"]), cls="sec sec-alt")
    + sec(related(p, [("radovi", "Primeri sa terena"),
                      ("blog/zasto-se-kanalizacija-stalno-zapusava", "Zašto se vraća"),
                      ("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije"),
                      ("masinsko-odgusenje-kanalizacije", "Mašinsko odgušenje")]),
          cls="sec")
)
PAGES.append(p)


# ============================================================ HITNE
p = {
    "slug": "hitne-intervencije-beograd",
    "title": "Vodoinstalater — hitne intervencije 0–24 | od 4.000 RSD",
    "desc": "Vodoinstalater za hitne intervencije u Beogradu, 0–24: pukla cev, izlivanje vode, ventil koji ne zatvara, izlivanje kanalizacije. Pozovite [TELEFON].",
    "h1": "Vodoinstalater — hitne intervencije u Beogradu",
    "crumbs": [H, ("hitne-intervencije-beograd", "Hitne intervencije")],
    "schema": "service",
    "service_type": "Vodoinstalater hitne intervencije",
    "offer": (4000, 20000),
}
p["faq"] = [
    ("Za koliko stižete?",
     "Zavisi od dela grada, doba dana i broja ekipa koje su trenutno na terenu. Kada pozovete, kažemo realno vreme za tu konkretnu situaciju. Ne obećavamo rok koji ne možemo da ispunimo."),
    ("Šta da uradim dok čekam majstora?",
     "Zatvorite glavni ventil za vodu u stanu ili u hodniku zgrade. Ako voda curi blizu instalacija, isključite struju u tom delu stana. Sklonite stvari sa poda i obavestite komšije ispod ako postoji rizik od prokišnjavanja."),
    ("Koliko košta hitan izlazak?",
     "Izlazak za hitnu intervenciju kreće od 4.000 dinara, a konačna cena zavisi od toga šta je potrebno uraditi. Za intervencije noću, vikendom i praznikom važi ista cena kao i radnim danom — bez doplate za hitnost i bez doplate za neradne dane."),
    ("Radite li u zgradama, lokalima i poslovnim prostorima?",
     "Radimo. Za stambene zajednice i firme izdajemo račun na pravno lice, a po potrebi i predračun."),
    ("Ne mogu da nađem glavni ventil — šta onda?",
     "Pozovite nas i opišite stan. Kroz razgovor najčešće možemo da navedemo gde se ventil obično nalazi kod tog tipa objekta. Ako ne može da se zatvori, to je razlog više da izađemo odmah."),
]
p["body"] = (
    hero(p,
         "Dežurni majstor 0–24",
         "Vodoinstalater — hitne intervencije u Beogradu",
         "Pukla cev, voda se izliva, ventil ne zatvara ili se kanalizacija vraća u stan. Zovite odmah — kažemo šta da uradite do našeg dolaska i kada realno možemo da stignemo.",
         ["Dežurstvo 0–24, i vikendom i praznikom",
          "Realno vreme dolaska, bez praznih obećanja",
          "Stanovi, kuće, lokali i stambene zajednice",
          "Račun i garancija, moguće i preko računa"],
         pre_note="<strong>Pre svega:</strong> ako voda ne može da se zaustavi, zatvorite glavni ventil i isključite struju u delu stana gde se voda izliva.")
    + sec(brief([('Kada zvati', 'Pukla cev, izlivanje vode, ventil koji ne zatvara, kanalizacija koja se vraća u stan.'), ('Dostupnost', '0–24, svih sedam dana, i vikendom i praznikom.'), ('Vreme dolaska', 'Kažemo realan termin za vašu situaciju pri pozivu. Ne obećavamo rok unapred.'), ('Cena', 'Hitan izlazak i intervencija od 4.000 RSD. Noću, vikendom i praznikom ista cena, bez doplate.'), ('Prvo uradite', 'Zatvorite glavni ventil i isključite struju u delu stana gde se voda izliva.')]), cls="sec")
    + sec(cards("Zbog čega nas najčešće zovu hitno",
                [("popravka-pukle-cevi", "Pukla vodovodna cev",
                  "Cev u zidu, podu ili iza ugradnih elemenata, sa vidljivim izlivanjem vode.", "od 4.000 RSD"),
                 ("", "Ventil ne zatvara",
                  "Zaporni, ugaoni ili glavni ventil koji je zapekao ili propušta i ne može da se zatvori.", "od 2.400 RSD"),
                 ("", "Izlivanje kanalizacije",
                  "Voda se vraća kroz slivnik, šolju ili kadu, najčešće zbog zapušene vertikale.", "od 3.500 RSD"),
                 ("", "Poplava u stanu ili podrumu",
                  "Zaustavljanje dotoka, ispumpavanje i sanacija uzroka.", "po proceni"),
                 ("", "Curenje iz bojlera",
                  "Bojler kaplje ili curi na spoju, sa rizikom od kontakta vode i struje.", "od 3.000 RSD"),
                 ("", "Curenje kod vodomera",
                  "Propuštanje na priključku i u vodomernom šahtu.", "po proceni")],
                page=p),
          cls="sec sec-alt")
    + sec(prose("Šta možete da uradite do dolaska majstora",
                ["<strong>Zatvorite dotok vode.</strong> Glavni ventil je najčešće u kupatilu iza revizionog otvora, u kuhinjskom elementu ispod sudopere ili u hodniku zgrade kod vodomera. Ako postoji samo ventil na celom stanu, zatvorite njega.",
                 "<strong>Isključite struju u ugroženom delu.</strong> Ako voda curi blizu utičnica, bojlera ili razvodne kutije, isključite odgovarajući osigurač. Ne dirajte uređaje koji stoje u vodi.",
                 "<strong>Smanjite štetu.</strong> Sklonite stvari sa poda, podignite tepihe i stavite sud ispod mesta gde kaplje. Ako postoji rizik da voda prođe kod komšija ispod, javite im odmah — to skraćuje i njihovu i vašu štetu.",
                 "<strong>Ne improvizujte popravku pod pritiskom.</strong> Zatezanje spoja ili stavljanje obujmice na cev pod punim pritiskom često pogorša pukotinu. Bolje je zatvoriti vodu i sačekati."]),
          cls="sec")
    + sec(price_table("Okvirne cene hitnih intervencija",
                      [("Hitan izlazak i intervencija", "od 4.000"),
                       ("Zamena ventila", "2.400–4.000"),
                       ("Sanacija pukle cevi", "po proceni"),
                       ("Hitno odgušenje kanalizacije", "od 3.500"),
                       ("Odgušenje vertikale", "6.000–8.000"),
                       ("Ispumpavanje vode iz podruma", "po proceni")],
                      intro="Za intervencije noću, vikendom i praznikom važi ista cena kao i radnim danom — bez doplate za hitnost i bez doplate za neradne dane.",
                      note_up="Teško dostupna instalacija i obim štete koji traži više od jedne intervencije.",
                      note_in="Dolazak, zaustavljanje dotoka, utvrđivanje uzroka i dogovor o sanaciji pre početka rada."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja o hitnim intervencijama"), cls="sec")
    + sec(related(p, [("popravka-pukle-cevi", "Pukla cev"),
                      ("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije"),
                      ("detekcija-curenja-vode-beograd", "Detekcija curenja"),
                      ("bojler-curi", "Bojler curi")])
          + "\n" + chips("Hitne intervencije po opštinama", OPSTINE_CHIPS, p,
                         last=("lokacije", "Sve lokacije →")),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ GEBERIT
p = {
    "slug": "servis-ugradnih-vodokotlica-geberit",
    "title": "Ugradni vodokotlić — servis u zidu, Beograd | 2.500–5.000",
    "desc": "Servis ugradnog i nadgradnog vodokotlića: zamena plovka i zvona, ulivni i ispusni ventil, aktivaciona tipka. Radimo kroz revizioni otvor. Beograd, od 2.500 RSD.",
    "h1": "Ugradni vodokotlić — servis mehanizma u zidu",
    "crumbs": [H, ("servis-ugradnih-vodokotlica-geberit", "Vodokotlići")],
    "schema": "service",
    "service_type": "Servis ugradnih vodokotlića",
    "offer": (2500, 5000),
}
p["faq"] = [
    ("Mora li da se obija zid?",
     "U najvećem broju slučajeva ne. Skoro svi ugradni sistemi imaju revizioni otvor iza aktivacione tipke, a kroz njega se dolazi do ulivnog i ispusnog ventila i do većine delova mehanizma."),
    ("Voda stalno curi u šolju — šta je uzrok?",
     "Najčešće ispusni ventil, odnosno zvono, koje više ne zaptiva. Ređe je uzrok plovak koji ne zatvara dotok, pa voda stalno prelazi preko preliva. Oba se rešavaju kroz revizioni otvor."),
    ("Vodokotlić se sporo puni ili se uopšte ne puni.",
     "Obično je u pitanju ulivni ventil ili filter na njemu, zapušen kamencem i nečistoćom. Ponekad je kriv i zatvoren ili zapekao ugaoni ventil ispred kotlića."),
    ("Je li Geberit posebna vrsta vodokotlića?",
     "Nije, Geberit je marka. Kod nas se odomaćila toliko da se tako zove svaki ugradni vodokotlić, ali to je ime proizvođača — koji pravi i ugradne i nadgradne sisteme. Vrste su dve: ugradni, sa mehanizmom u zidu, i nadgradni, vidljivi. Radimo obe."),
    ("Koji se delovi najčešće menjaju?",
     "Plovak i zvono. Plovak reguliše dotok vode u kotlić, zvono je ispusni mehanizam koji pušta vodu u šolju. Kod velike većine kvarova problem je u jednom od ta dva dela i oba se menjaju kroz revizioni otvor."),
    ("Radite li sa svim proizvođačima?",
     "Radimo sa uobičajenim ugradnim sistemima na našem tržištu, u skladu sa dostupnošću rezervnih delova. Ako je reč o retkom modelu, prvo proveravamo da li se deo može nabaviti."),
    ("Koliko traje popravka?",
     "Zamena plovka ili zvona najčešće traje do sat vremena. Ako je potrebno nabaviti specifičan deo, radi se u dva dolaska."),
]
p["body"] = (
    hero(p,
         "Radimo kroz revizioni otvor",
         "Ugradni vodokotlić — servis mehanizma u zidu",
         "Voda stalno otiče u šolju, kotlić se sporo puni ili tipka ne radi. U devet od deset slučajeva menja se plovak ili zvono, i to kroz revizioni otvor — bez obijanja pločica.",
         ["Plovak i zvono — najčešće zamene",
          "Radimo i ugradne i nadgradne vodokotliće",
          "Popravka tipke i mehanizma za ispiranje",
          "2.500–5.000 RSD za standardnu intervenciju"])
    + sec(prose("Ugradni, nadgradni i Geberit — šta je šta",
                ["Ljudi ovo često pomešaju, pa se i na telefonu izgubi vreme. <strong>Ugradni vodokotlić</strong> je onaj koji ne vidite: mehanizam je u zidu, u metalnom nosaču iza obloge, a spolja je samo aktivaciona tipka. <strong>Nadgradni</strong> je klasičan, vidljiv kotlić iznad ili uz šolju. To su dve različite vrste i serviser im prilazi potpuno drugačije.",
                 "<strong>Geberit nije vrsta vodokotlića nego marka.</strong> Kod nas se toliko odomaćila da se rečju „geberit“ često naziva svaki ugradni vodokotlić, ali Geberit pravi i ugradne i nadgradne sisteme, a pored njega na tržištu postoji još nekoliko proizvođača. Zato kada nam kažete da se „pokvario geberit“, pitamo da li je kotlić u zidu ili vidljiv — od toga zavisi šta nosimo sa sobom.",
                 "Radimo oba tipa. Ako niste sigurni koji imate, pošaljite fotografiju tipke ili kotlića i reći ćemo vam."]),
          cls="sec")
    + sec(prose("Zašto je ugradni poseban posao",
                ["Ugradni vodokotlić nije isto što i nadgradni. Mehanizam je u zidu, pristup je samo kroz revizioni otvor, a delovi se razlikuju od proizvođača do proizvođača. Zato se dešava da opšti majstor ili ne uzme posao ili nepotrebno predloži obijanje.",
                 "U praksi se skoro sve rešava kroz otvor iza tipke: zamena plovka, zamena zvona odnosno ispusnog mehanizma, zamena zaptivki i gumica, podešavanje nivoa vode i popravka same aktivacione tipke. Obijanje dolazi u obzir samo kada je oštećen deo nosača ili cev iza njega.",
                 "Pre izlaska je korisno da nam pošaljete fotografiju tipke. Po njoj se često prepoznaje sistem i unapred se zna koji delovi mogu da zatrebaju, pa se posao završava u jednom dolasku."]),
          cls="sec")
    + sec(cards("Šta najčešće radimo",
                [("", "Zamena plovka",
                  "Kada vodokotlić ne zatvara dotok ili se puni presporo.", "od 2.500 RSD"),
                 ("", "Zamena zvona i ispusnog mehanizma",
                  "Kada voda neprestano otiče u WC šolju.", "od 3.000 RSD"),
                 ("", "Zamena ulivnog ventila",
                  "Zapušen ili neispravan ventil koji ne propušta vodu u kotlić.", "od 3.000 RSD"),
                 ("", "Zamena zaptivki i gumica",
                  "Sitna curenja na spojevima unutar mehanizma.", "od 2.500 RSD"),
                 ("", "Popravka aktivacione tipke",
                  "Tipka koja je upala, zaglavila se ili ne pokreće ispiranje.", "od 2.500 RSD"),
                 ("", "Podešavanje nivoa vode",
                  "Prevelika ili premala količina vode po ispiranju.", "od 2.000 RSD"),
                 ("", "Servis nadgradnog vodokotlića",
                  "Klasičan, vidljiv kotlić: plovak, zvono, zaptivke i dotok. Jeftinije i brže nego ugradni.", "od 2.000 RSD"),
                 ("", "Zamena nadgradnog vodokotlića",
                  "Kada je kotlić napukao ili su delovi dotrajali toliko da se popravka ne isplati.", "od 3.000 RSD")],
                intro="Plovak i zvono su dva dela koja se menjaju najčešće — kod većine kvarova problem je u jednom od njih. Delovi se naplaćuju posebno i cenu kažemo pre ugradnje.",
                page=p),
          cls="sec sec-alt")
    + sec(price_table("Cena servisa vodokotlića",
                      [("Dijagnostika i podešavanje mehanizma", "od 2.000"),
                       ("Zamena plovka", "od 2.500"),
                       ("Zamena zvona i ispusnog mehanizma", "od 3.000"),
                       ("Zamena ulivnog ventila", "od 3.000"),
                       ("Popravka ili zamena aktivacione tipke", "od 2.500"),
                       ("Kompletan servis mehanizma", "3.500–5.000"),
                       ("Servis nadgradnog vodokotlića", "od 2.000"),
                       ("Zamena nadgradnog vodokotlića", "od 3.000")],
                      note_up="Redak model kod koga se deo teško nabavlja i nepostojeći ili zazidan revizioni otvor.",
                      note_in="Dolazak, dijagnostika, rad na mehanizmu i provera ispiranja posle popravke. Delovi se naplaćuju posebno."),
          cls="sec", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja o ugradnim vodokotlićima"), cls="sec sec-alt")
    + sec(related(p, [("odgusenje-wc-solje-beograd", "Odgušenje WC šolje"),
                      ("sanitarije-i-kupatila", "Sanitarije i kupatila"),
                      ("vodovodne-instalacije-i-popravke", "Zamena ventila"),
                      ("hitne-intervencije-beograd", "Hitne intervencije")]),
          cls="sec")
)
PAGES.append(p)
