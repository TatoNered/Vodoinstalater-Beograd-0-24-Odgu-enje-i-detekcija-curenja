# -*- coding: utf-8 -*-
"""Услуги, добавленные по правкам клиента (28 октября 2026):
лавабо, када и туш-кабина, замена кранов и вентилей, замена труб."""

import prices
from blocks import (hero, sec, prose, cards, steps, price_table, faq_block,
                    works, chips, related, brief)
from content1 import H, OPSTINE_CHIPS

PAGES = []
U = ("vodoinstalaterske-usluge", "Usluge")
ODG = ("odgusenje-kanalizacije-beograd", "Odgušenje")
INST = ("vodovodne-instalacije-i-popravke", "Instalacije i popravke")


# ============================================================ LAVABO
p = {
    "slug": "odgusenje-lavaboa",
    "title": "Odgušenje lavaboa Beograd — 3.000–3.500 RSD | 0–24",
    "desc": "Zapušen lavabo u kupatilu: voda sporo otiče ili stoji. Čistimo sifon i odvod, mašinski ako treba. Beograd, 3.000–3.500 RSD, dolazak 0–24.",
    "h1": "Odgušenje lavaboa u Beogradu",
    "crumbs": [H, ODG, ("odgusenje-lavaboa", "Odgušenje lavaboa")],
    "schema": "service",
    "service_type": "Odgušenje lavaboa",
    "cene": ("odgusenje_lavaboa",),
}
p["faq"] = [
    ("Zašto se lavabo zapušava kad u njega ne ide hrana?",
     "Zbog kose i sapuna. Kosa se zakači za sifon i za neravnine u cevi, a sapun i gel prave masnu prevlaku koja je lepi u čvrstu grudvu. Zato se lavabo u kupatilu zapušava polako, mesecima, i to bez ikakvog vidljivog razloga."),
    ("Mogu li sam da očistim sifon ispod lavaboa?",
     "Najčešće možete. Stavite lavor ispod, odvrnite čašicu sifona rukom, izvadite sadržaj i isperite. Ako posle toga voda i dalje stoji, čep je dalje u odvodu i tu treba mašina."),
    ("Pomaže li hemija?",
     "Kod sveže naslage može, ali ne sipajte je u lavabo koji uopšte ne propušta vodu — ostane da stoji u cevi, ne rastvori čep, a majstor posle otvara sifon pun agresivne tečnosti."),
    ("Voda sporo otiče i kod lavaboa i kod kade — šta to znači?",
     "Da čep nije u sifonu nego dalje, na zajedničkom odvodu kupatila ili na vertikali. Tada se radi sa drugog mesta i cena je drugačija, pa nam to recite odmah na telefonu."),
    ("Koliko traje intervencija?",
     "Kada je u pitanju sifon ili kratka deonica — obično pola sata. Ako treba mašina i duža trasa, do sat vremena."),
]
p["body"] = (
    hero(p,
         "Najčešće kosa i sapun",
         "Odgušenje lavaboa u Beogradu",
         "Voda u lavabou stoji ili otiče presporo. U kupatilu je uzrok skoro uvek isti — kosa slepljena sapunom u sifonu ili odmah iza njega.",
         ["3.000–3.500 RSD za standardnu intervenciju",
          "Dolazak 0–24, i vikendom i praznikom",
          "Mašina kada sifon nije kriv",
          "Čistimo za sobom i proveravamo protok"])
    + sec(brief([
        ("Cena", "3.000–3.500 RSD. Ako treba mašina i duža trasa — od 3.500."),
        ("Koliko traje", "Sifon — oko pola sata. Sa mašinom — do sat vremena."),
        ("Uzrok u 9 od 10 slučajeva", "Kosa i sapunska naslaga u sifonu ili neposredno iza njega."),
        ("Šta uraditi pre poziva", "Proverite da li sporo otiče i kada ili tuš. Ako da, problem nije u lavabou."),
        ("Uključeno", "Dolazak, čišćenje, provera protoka i čišćenje za sobom."),
    ]), cls="sec")
    + sec(prose("Zašto baš lavabo",
                ["Kuhinjska sudopera se zapuši od masnoće, a lavabo od kose. Svaka opran glava ostavi nešto dlaka, one se zakače za unutrašnjost sifona, a sapun, šampon i gel za tuširanje ih oblepe masnim slojem. Za nekoliko meseci nastane grudva koja propušta vodu sve sporije.",
                 "Zato se lavabo retko zapuši naglo. Prvo voda otiče malo sporije, pa još sporije, pa jednog jutra ostane da stoji. Ako reagujete u toj prvoj fazi, često je dovoljno odvrnuti sifon i isprati ga.",
                 "Drugi, ređi uzrok je nakupljeni kamenac, naročito kod starih metalnih odvoda. Tu čišćenje pomaže kratko i vredi razmisliti o zameni te deonice."]),
          cls="sec sec-alt")
    + sec(steps("Kako radimo",
                [("Proveravamo gde je čep", "Puštamo vodu u kadi i tušu da vidimo da li stoji samo lavabo ili ceo odvod kupatila."),
                 ("Otvaramo i čistimo sifon", "Najčešći nalaz. Sifon se rastavlja, čisti i vraća sa proverom zaptivanja."),
                 ("Mašina, ako treba dalje", "Kada je čep iza sifona, ide sajla odgovarajuće debljine za odvod lavaboa."),
                 ("Provera i čišćenje", "Puštamo vodu nekoliko minuta i gledamo da nema curenja na spojevima.")]),
          cls="sec")
    + sec(price_table("Cena odgušenja lavaboa",
                      [("Čišćenje sifona i odvoda lavaboa", "3.000–3.500"),
                       ("Mašinsko odgušenje, duža trasa", "od 3.500"),
                       ("Zamena sifona", "od 2.500"),
                       ("Odgušenje celog odvoda kupatila", "od 3.500"),
                       ("Odgušenje vertikale, ako je čep u zajedničkom vodu", "6.000–8.000")],
                      intro="Cene se odnose na rad. Sifon i materijal, ako se menjaju, naplaćuju se posebno.",
                      note_up="Nepristupačan sifon iza ugradnog ormarića i čep dalje od nekoliko metara.",
                      note_in="Dolazak, utvrđivanje gde je čep, čišćenje, provera protoka i čišćenje za sobom."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja — zapušen lavabo"), cls="sec")
    + sec(related(p, [("odgusenje-sudopere-beograd", "Odgušenje sudopere"),
                      ("odgusenje-kade-i-tus-kabine", "Kada i tuš-kabina"),
                      ("masinsko-odgusenje-kanalizacije", "Mašinsko odgušenje"),
                      ("cenovnik", "Cenovnik")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ KADA I TUŠ
p = {
    "slug": "odgusenje-kade-i-tus-kabine",
    "title": "Odgušenje kade i tuš-kabine Beograd — 3.000–3.500 RSD",
    "desc": "Voda stoji u kadi ili tuš-kabini i sporo otiče. Čistimo sifon, tuš-kanalicu i odvod, mašinski kada treba. Beograd, 0–24, od 3.000 RSD.",
    "h1": "Odgušenje kade i tuš-kabine",
    "crumbs": [H, ODG, ("odgusenje-kade-i-tus-kabine", "Kada i tuš-kabina")],
    "schema": "service",
    "service_type": "Odgušenje kade i tuš-kabine",
    "cene": ("odgusenje_kade",),
}
p["faq"] = [
    ("Voda u tuš-kabini stoji oko slivnika — zašto?",
     "Dva razloga. Ili je slivnik zapušen kosom i sapunom, ili je kada postavljena bez dovoljnog pada pa voda nema kuda. Prvo se rešava čišćenjem, drugo samo prepravkom — i to vam kažemo pošteno na licu mesta."),
    ("Da li se kada mora skidati?",
     "Skoro nikada. Kod kade se radi kroz sam odvod i kroz preliv, a kod tuš-kabine kroz rešetku slivnika. Skidanje dolazi u obzir samo kada je sifon ispod kade pukao ili potpuno nedostupan."),
    ("Ima li razlike između obične i ravne tuš-kanalice?",
     "Ima. Ravne linijske kanalice imaju plitak sifon i duži put do odvoda, pa se brže zapušavaju i traže tanju sajlu. Kažite nam koji tip imate, poneseme odgovarajući alat."),
    ("Osetio se smrad iz odvoda kade — je li to isto zapušenje?",
     "Često jeste: naslaga u sifonu zadržava vodu i počinje da miriše. Ali miris može značiti i da je sifon presušio ili da je loše zaptiven, pa to proveravamo pre nego što bilo šta čistimo."),
]
p["body"] = (
    hero(p,
         "Bez skidanja kade",
         "Odgušenje kade i tuš-kabine",
         "Voda u kadi stoji, tuš-kabina se puni dok se tuširate ili se iz odvoda oseti miris. Radimo kroz odvod i preliv — kada ostaje na mestu.",
         ["3.000–3.500 RSD za standardnu intervenciju",
          "Kada, tuš-kabina i ravna tuš-kanalica",
          "Bez demontaže u najvećem broju slučajeva",
          "Dolazak 0–24, i vikendom"])
    + sec(brief([
        ("Cena", "3.000–3.500 RSD. Ravna tuš-kanalica i duža trasa — od 3.500."),
        ("Koliko traje", "Najčešće 30–45 minuta."),
        ("Uzrok", "Kosa i sapunska naslaga u sifonu, ređe nedovoljan pad odvoda."),
        ("Demontaža", "Nije potrebna; radi se kroz odvod, preliv ili rešetku slivnika."),
        ("Ako se vrati brzo", "Znak da pad odvoda nije dobar — tada ne čistimo ponovo nego merimo."),
    ]), cls="sec")
    + sec(cards("Šta tačno odgušujemo",
                [("", "Kada",
                  "Klasična kada sa sifonom i prelivom. Radi se kroz odvod, bez skidanja.", "3.000–3.500 RSD"),
                 ("", "Tuš-kabina sa tuš-kadom",
                  "Plitak sifon ispod kade, čest zastoj od kose.", "3.000–3.500 RSD"),
                 ("", "Ravna tuš-kanalica",
                  "Linijski slivnik u podu. Plići sifon i duža trasa, treba tanja sajla.", "od 3.500 RSD"),
                 ("", "Podni slivnik u kupatilu",
                  "Slivnik u koji se vraća voda iz drugih odvoda.", "od 3.000 RSD"),
                 ("", "Ceo odvod kupatila",
                  "Kada sporo otiče na više mesta odjednom — čep je na zajedničkoj deonici.", "od 3.500 RSD"),
                 ("", "Miris iz odvoda",
                  "Proveravamo naslagu, zaptivanje i da li je sifon presušio.", "po proceni")],
                page=p),
          cls="sec sec-alt")
    + sec(prose("Kada čišćenje ne pomaže",
                ["Ako se kada ili tuš-kabina zapuši ponovo u roku od nekoliko nedelja, problem najčešće nije u količini kose nego u padu odvoda. Kod tuš-kabina postavljenih na gotov pod i kod linijskih kanalica ugrađenih bez dovoljnog nagiba voda ne nosi sa sobom ništa — i svaka sitnica se zadržava na istom mestu.",
                 "To se ne rešava ponovnim čišćenjem. Potrebno je izmeriti pad i, ako je premali, prepraviti deonicu. Kažemo vam to iskreno, iako je drugi dolazak za čišćenje za nas jednostavniji posao.",
                 "Isto važi i za miris: ako se vraća i posle čišćenja, obično je u pitanju zaptivanje ili presušen sifon, a ne naslaga."]),
          cls="sec")
    + sec(steps('Kako radimo',
                [('Provera obima', 'Puštamo vodu u lavabou i šolji. Ako i tamo stoji, čep nije u kadi nego na zajedničkom odvodu kupatila.'), ('Čišćenje sifona i odvoda', 'Kod kade kroz odvod i preliv, kod tuš-kabine kroz rešetku. Kosa i sapunska naslaga se izvlače, ne guraju dalje.'), ('Tanja sajla za linijske kanalice', 'Ravne tuš-kanalice imaju plitak sifon i duži put do odvoda, pa traže drugu opremu nego klasična kada.'), ('Provera pada', 'Ako voda i posle čišćenja stoji oko slivnika, merimo pad. To je drugi problem i rešava se prepravkom, a ne ponovnim čišćenjem.')],
                intro='Kada ostaje na mestu — radi se kroz odvod, preliv ili rešetku slivnika.'),
          cls="sec")
    + sec(price_table("Cena odgušenja kade i tuš-kabine",
                      [("Odgušenje kade", "3.000–3.500"),
                       ("Odgušenje tuš-kabine", "3.000–3.500"),
                       ("Odgušenje ravne tuš-kanalice", "od 3.500"),
                       ("Odgušenje podnog slivnika", "od 3.000"),
                       ("Odgušenje celog odvoda kupatila", "od 3.500"),
                       ("Zamena sifona kade ili tuš-kade", "od 2.500")],
                      note_up="Nedostupan sifon ispod kade, ugrađena maska bez revizionog otvora i ponovljeno zapušenje zbog lošeg pada.",
                      note_in="Dolazak, čišćenje, provera protoka i čišćenje za sobom."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja — kada i tuš"), cls="sec")
    + sec(related(p, [("odgusenje-lavaboa", "Odgušenje lavaboa"),
                      ("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije"),
                      ("sanitarije-i-kupatila", "Montaža sanitarije"),
                      ("renoviranje-kupatila", "Renoviranje kupatila")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ SLAVINE I VENTILI
p = {
    "slug": "zamena-slavina-i-ventila",
    "title": "Zamena slavina i ventila Beograd — od 2.400 RSD",
    "desc": "Slavina kaplje, ventil ne zatvara ili je zapekao. Zamena baterija, ugaonih i zapornih ventila u Beogradu. Od 2.400 RSD, dolazak 0–24.",
    "h1": "Zamena slavina i ventila",
    "crumbs": [H, INST, ("zamena-slavina-i-ventila", "Slavine i ventili")],
    "schema": "service",
    "service_type": "Zamena slavina i ventila",
    "cene": ("zamena_ugaonog", "zamena_baterije"),
}
p["faq"] = [
    ("Slavina kaplje — menja se cela ili samo zaptivka?",
     "Kod starijih slavina sa gumicom često je dovoljna zamena zaptivke. Kod jednoručnih baterija kaplje kada otkaže keramička kartuša; kartuša se menja ako se za taj model može nabaviti, a ako ne — menja se baterija."),
    ("Zašto se ventil zapeče?",
     "Zato što godinama stoji u istom položaju. Kamenac i korozija spoje vreteno sa telom ventila i on prosto ne može da se okrene. Najgore je što se to otkrije baš onda kada vodu hitno treba zatvoriti."),
    ("Da li treba zatvarati vodu u celoj zgradi?",
     "Za zamenu baterije i ugaonog ventila obično ne — dovoljan je ventil u stanu. Zatvaranje vertikale je potrebno samo kada se menja sam stanski ventil ili nešto pre njega, i to se dogovara sa upravnikom unapred."),
    ("Kupujem li ja slavinu?",
     "Kako vam odgovara. Većina ljudi sama bira izgled, a mi radimo montažu. Ako hoćete, pre kupovine recite nam gde ide i poslaćemo vam na šta da obratite pažnju — razmak priključaka ume da iznenadi."),
    ("Koliko traje zamena?",
     "Baterija ili ugaoni ventil — pola sata do sat. Ako je priključak zarđao i mora da se seče, duže, i to kažemo pre nego što počnemo."),
]
p["body"] = (
    hero(p,
         "Najbrža intervencija u ponudi",
         "Zamena slavina i ventila",
         "Slavina kaplje, baterija se klima ili ventil ne zatvara. Sitan posao koji se obično završi za pola sata — ali koji odlaže se dok ne postane poplava.",
         ["Od 2.400 RSD za zamenu ventila",
          "Baterije, ugaoni i zaporni ventili",
          "Donosimo delove ili ugrađujemo vaše",
          "Dolazak 0–24, i vikendom"])
    + sec(brief([
        ("Cena", "Zamena ventila 2.400–4.000 RSD. Zamena baterije od 2.500. Zamena creva od 2.000."),
        ("Koliko traje", "Standardna zamena — 30 do 60 minuta."),
        ("Materijal", "Možete kupiti sami ili donosimo mi; cenu delova kažemo unapred."),
        ("Voda", "Za većinu zamena dovoljno je zatvoriti ventil u stanu."),
        ("Garancija", "Pisana garancija na rad, na deo garancija proizvođača."),
    ]), cls="sec")
    + sec(cards("Šta menjamo",
                [("", "Kuhinjska baterija",
                  "Jednoručna ili sa dve ručke, sa izvlačivim tušem ili bez.", "od 2.500 RSD"),
                 ("", "Baterija za lavabo",
                  "Stojeća ili zidna, sa zamenom ugaonih ventila po potrebi.", "od 2.500 RSD"),
                 ("", "Baterija za kadu i tuš",
                  "Zidna baterija, tuš-set i preusmerivač.", "od 2.500 RSD"),
                 ("", "Ugaoni ventil",
                  "Mali ventil ispod lavaboa, uz šolju ili iza mašine. Najčešći kvar u stanu.", "2.400–3.500 RSD"),
                 ("", "Zaporni ventil u stanu",
                  "Glavni ventil kojim zatvarate vodu. Ako je zapekao, menja se pre nego što zatreba.", "od 3.500 RSD"),
                 ("", "Fleksibilna creva",
                  "Creva do baterije, mašine i vodokotlića — tipično mesto iznenadnog pucanja.", "od 2.000 RSD")],
                intro="Delovi se naplaćuju posebno. Ako kupujete sami, recite nam model pre nego što naručite.",
                page=p),
          cls="sec sec-alt")
    + sec(prose("Ventil koji ne zatvara je hitniji nego što izgleda",
                ["Dok sve radi, zaporni ventil u stanu niko ne dira. Problem je u tome što ventil koji godinama stoji otvoren postepeno zapeče — kamenac i korozija spoje vreteno sa telom i ručica prosto ne može da se okrene.",
                 "Otkriva se to u najgorem mogućem trenutku: pukne crevo do mašine, voda ide po stanu, čovek trči da zatvori ventil, a ventil ne ide. Odatle do poplave kod komšije ispod prođe nekoliko minuta.",
                 "Zato predlažemo jednostavnu proveru: jednom godišnje zatvorite i otvorite glavni ventil u stanu. Ako ide teško ili škripi — zamenite ga u mirnom terminu, za 3.500 dinara, umesto u panici po ceni hitne intervencije i sa štetom u stanu ispod."]),
          cls="sec")
    + sec(steps('Kako ide zamena',
                [('Provera šta se stvarno kvari', 'Kod slavine koja kaplje gleda se da li je dovoljna zaptivka ili kartuša, ili je baterija za zamenu.'), ('Zatvaranje vode na pravom mestu', 'Za većinu zamena dovoljan je ventil u stanu. Ako je zapekao, to je prvo što menjamo — i o tome vas obavestimo.'), ('Demontaža bez lomljenja priključka', 'Zarđali navoj se oslobađa postepeno. Sila na staroj cevi pravi veći kvar od onog zbog kog smo došli.'), ('Ugradnja i provera pod pritiskom', 'Novi deo se ugradi, voda pusti i spoj proveri. Ne odlazimo dok spoj ne odstoji pod punim pritiskom.')],
                intro='Najkraći posao u ponudi — ali sa dva mesta na kojima se najčešće greši.'),
          cls="sec")
    + sec(price_table("Cena zamene",
                      [("Zamena ugaonog ventila", "2.400–3.500"),
                       ("Zamena zapornog ventila u stanu", "od 3.500"),
                       ("Zamena baterije (slavine)", "od 2.500"),
                       ("Zamena kartuše u jednoručnoj bateriji", "od 2.200"),
                       ("Zamena zaptivki u staroj slavini", "od 2.000"),
                       ("Zamena fleksibilnog creva", "od 2.000"),
                       ("Zamena više komada u istom izlasku", "po dogovoru, povoljnije")],
                      intro="Cene se odnose na rad. Slavine, ventili i creva naplaćuju se posebno.",
                      note_up="Zarđao priključak koji mora da se seče, zazidan ventil i rad u nepristupačnom prostoru.",
                      note_in="Dolazak, demontaža starog, ugradnja novog i provera na curenje pod pritiskom."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja — slavine i ventili"), cls="sec")
    + sec(related(p, [("vodovodne-instalacije-i-popravke", "Instalacije i popravke"),
                      ("popravka-i-zamena-vodovodnih-cevi", "Zamena cevi"),
                      ("sanitarije-i-kupatila", "Sanitarije i kupatila"),
                      ("hitne-intervencije-beograd", "Hitne intervencije")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ CEVI
p = {
    "slug": "popravka-i-zamena-vodovodnih-cevi",
    "title": "Popravka i zamena vodovodnih cevi Beograd — od 6.000 RSD",
    "desc": "Stare pocinkovane cevi, slab pritisak, curenje na spoju. Zamena deonice ili kompletnog razvoda u Beogradu. Od 6.000 RSD, procena pre rada.",
    "h1": "Popravka i zamena vodovodnih cevi",
    "crumbs": [H, INST, ("popravka-i-zamena-vodovodnih-cevi", "Vodovodne cevi")],
    "schema": "service",
    "service_type": "Popravka i zamena vodovodnih cevi",
    "cene": ("zamena_deonice",),
}
p["faq"] = [
    ("Kako znam da je vreme za zamenu, a ne za popravku?",
     "Po tome koliko se često kvari. Jedno oštećenje na zdravoj instalaciji se popravlja. Ako vam je u poslednjih godinu dana puklo na dva mesta, ako je pritisak osetno slabiji nego ranije i ako je voda posle pauze rđava — cev je iznutra zarasla i krpljenje samo pomera problem nekoliko metara dalje."),
    ("Mora li se razbijati zid?",
     "Tamo gde cev prolazi kroz zid — da, ali samo na toj trasi. Ako se ne zna gde tačno curi, prvo radimo detekciju pa otvaramo na jednom mestu umesto da tražimo nasumično."),
    ("Koliko traje zamena razvoda u kupatilu?",
     "Vodoinstalaterski deo obično jedan do dva radna dana, u zavisnosti od broja tačaka. Keramika i završni radovi idu posle i ne ulaze u taj rok."),
    ("Koje cevi ugrađujete?",
     "Materijal biramo prema postojećoj instalaciji i nameni, iz onoga što je uobičajeno na našem tržištu. Ako ima razloga da se materijal promeni, objasnimo zašto pre nego što počnemo."),
    ("Može li da se radi po fazama?",
     "Može i često je tako najpametnije: prvo grana koja pravi probleme, ostalo kada vam odgovara. Na izlasku kažemo koja deonica je najkritičnija."),
]
p["body"] = (
    hero(p,
         "Prvo procena, pa odluka",
         "Popravka i zamena vodovodnih cevi",
         "Slab pritisak, rđava voda posle pauze ili pukotina koja se vraća na novom mestu. Kažemo šta je realno stanje instalacije i da li se isplati krpiti ili menjati.",
         ["Zamena deonice od 6.000 RSD",
          "Razvod u kupatilu od 12.000 RSD",
          "Detekcija pre otvaranja zida",
          "Može i po fazama, po dogovoru"])
    + sec(brief([
        ("Cena", "Sanacija spoja od 3.500 RSD. Zamena deonice od 6.000. Razvod u kupatilu od 12.000."),
        ("Koliko traje", "Deonica — isti dan. Razvod u kupatilu — jedan do dva radna dana."),
        ("Kada popravka", "Lokalno oštećenje na instalaciji koja je inače u dobrom stanju."),
        ("Kada zamena", "Stare pocinkovane cevi: slab pritisak, rđava voda, pucanje na novim mestima."),
        ("Pre otvaranja zida", "Ako mesto nije vidljivo — detekcija od 5.000 RSD, pa se otvara tačno tu."),
    ]), cls="sec")
    + sec(prose("Tri znaka da instalacija više nije za krpljenje",
                ["<strong>Pritisak je pao.</strong> Pocinkovana cev zarasta iznutra — naslage sužavaju presek dok mlaz ne postane upola slabiji nego ranije. To se ne vraća čišćenjem, jer problem nije prolaznost nego sam materijal.",
                 "<strong>Voda je rđava posle pauze.</strong> Ako posle vikenda ili odmora iz slavine prvo ide braonkasta voda, to je rđa sa unutrašnjeg zida cevi. Zdrava instalacija to ne radi.",
                 "<strong>Puca na novim mestima.</strong> Najjasniji znak. Kada se posle svake popravke za koji mesec pojavi curenje nekoliko metara dalje, plaćate niz intervencija umesto jedne zamene — i svaki put iznova obijanje i krečenje."]),
          cls="sec sec-alt")
    + sec(cards("Šta radimo",
                [("", "Sanacija spoja koji propušta",
                  "Najjeftiniji zahvat, kada je ostatak grane u dobrom stanju.", "od 3.500 RSD"),
                 ("", "Zamena deonice cevi",
                  "Oštećeni deo se seče i menja, sa proverom pod pritiskom.", "od 6.000 RSD"),
                 ("", "Zamena grane u stanu",
                  "Kompletna grana do kupatila ili kuhinje kod zarasle instalacije.", "po proceni"),
                 ("", "Razvod vodovoda u kupatilu",
                  "Nov razvod tople i hladne vode, uz renoviranje.", "od 12.000 RSD"),
                 ("", "Cevi u dvorištu i priključak",
                  "Ukopani vod do vodomera, sa zemljanim radom.", "po proceni"),
                 ("", "Slab pritisak vode",
                  "Utvrđujemo da li je uzrok zarasla cev, zapušen filter ili ventil.", "od 3.000 RSD")],
                page=p),
          cls="sec")
    + sec(steps('Kako odlučujemo i kako radimo',
                [('Procena stanja instalacije', 'Merimo pritisak, gledamo materijal i pitamo koliko je puta puklo do sada. Tri podatka koja odlučuju popravka ili zamena.'), ('Lociranje, ako mesto nije vidljivo', 'Kod curenja u zidu ili podu prvo radimo detekciju. Otvaranje po vlažnoj fleci je najskuplji način traženja.'), ('Ponuda po fazama', 'Kažemo koja grana je najkritičnija i šta može da sačeka. Često je najpametnije raditi po fazama, a ne sve odjednom.'), ('Zamena i obavezna proba', 'Deonica se menja, instalacija proverava pod pritiskom i tek onda se zatvara zid ili pod.')],
                intro='Najskuplja greška je zameniti deonicu u instalaciji koju je trebalo menjati celu.'),
          cls="sec")
    + sec(price_table("Okvirne cene",
                      [("Sanacija curenja na spoju", "od 3.500"),
                       ("Zamena deonice vodovodne cevi", "od 6.000"),
                       ("Razvod vodovoda u kupatilu", "od 12.000"),
                       ("Zamena grane do kuhinje ili kupatila", "po proceni"),
                       ("Detekcija, kada mesto curenja nije vidljivo", "od 5.000"),
                       ("Provera uzroka slabog pritiska", "od 3.000"),
                       ("Ukopani dvorišni vod", "po proceni")],
                      intro="Cene se odnose na rad. Cevi, fitinzi i ostali materijal naplaćuju se posebno, po nabavnoj ceni.",
                      note_up="Rad u zidu i podu, nepoznata trasa, zazidani spojevi i objekat u kome voda ne može dugo da stoji zatvorena.",
                      note_in="Dolazak, procena stanja instalacije, rad i obavezna proba pod pritiskom posle zahvata."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja — vodovodne cevi"), cls="sec")
    + sec(related(p, [("popravka-pukle-cevi", "Pukla cev — hitno"),
                      ("detekcija-curenja-vode-beograd", "Detekcija curenja"),
                      ("zamena-slavina-i-ventila", "Slavine i ventili"),
                      ("renoviranje-kupatila", "Renoviranje kupatila")])
          + "\n" + chips("Radimo u celom Beogradu", OPSTINE_CHIPS, p,
                         last=("lokacije", "Sve lokacije →")),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ CURENJE OD KOMŠIJE
# Klijent je ovo dao kao zasebnu uslugu (pravka br. 3): „Curenje vode od
# komšije“, „Voda curi kod komšije ispod“, „Vlaga na plafonu“.
p = {
    "slug": "curenje-vode-od-komsije",
    "title": "Curenje vode od komšije — utvrđivanje odakle curi",
    "desc": "Vlaga na plafonu ili voda curi kod komšije ispod? Merenjem utvrđujemo da li curi vaša instalacija, zajednička vertikala ili susedni stan. Beograd, 5.000–12.000 RSD, 0–24.",
    "h1": "Curenje vode od komšije — kako se utvrđuje odakle curi",
    "crumbs": [H, ("detekcija-curenja-vode-beograd", "Detekcija curenja vode"),
               ("curenje-vode-od-komsije", "Curenje od komšije")],
    "schema": "service",
    "service_type": "Utvrđivanje izvora curenja vode između stanova",
    "cene": ("curenje_od_komsije",),
}
p["faq"] = [
    ("Komšija kaže da mu voda curi od mene, a ja u stanu ne vidim ništa. Šta sada?",
     "To je najčešći slučaj i zato se ne počinje razbijanjem. Prvo se proverava da li vaša "
     "instalacija uopšte propušta: voda se zatvori na ventilu u stanu i meri se da li pritisak "
     "pada. Ako ne pada, vaše cevi ne cure i izvor je negde drugde — u vertikali, u odvodu ili u "
     "trećem stanu. Nalaz dobijate napisan."),
    ("Ko plaća popravku ako curi zajednička vertikala?",
     "Zajednička instalacija je trošak stambene zajednice, a ne pojedinog stana. Granica je obično "
     "prvi ventil u stanu: od njega ka stanu je vaše, od njega ka vertikali zajedničko. Zato je "
     "važno da se pre popravke zapiše šta je tačno curelo — bez toga se trošak najčešće prebaci na "
     "onoga kod koga se voda videla."),
    ("Mora li da se razbija kupatilo u stanu iznad?",
     "Ne odmah. Mesto se prvo locira merenjem — termovizijom, akustično i proverom pritiska po "
     "deonicama. Kada se zna gde curi, otvara se jedno do dva mesta, a ne ceo zid ili pod."),
    ("Da li izlazite kada se komšija ne javlja ili ne pušta u stan?",
     "Izlazimo. Dobar deo merenja može da se radi iz stana u kojem se vlaga vidi i sa zajedničkih "
     "delova — iz hodnika, sa vertikale i iz šahta. To ne zamenjuje pregled iznad, ali najčešće "
     "pokazuje da li je izvor u vertikali ili u stanu."),
    ("Dobijam li nešto napisano, za osiguranje ili za stambenu zajednicu?",
     "Dobijate. Nalaz sadržava šta je merenjem utvrđeno, gde je mesto curenja i šta sanacija "
     "obuhvata. Fotografije i termovizijski snimak idu uz nalaz na vaš zahtev."),
    ("Koliko traje i koliko košta?",
     "Pregled jedne ograničene zone obično traje sat do dva. Cena je %s RSD za jednu zonu; kada "
     "treba merenje u dva stana i na vertikali, obim je veći i cenu kažemo pre izlaska."
     % prices.c("curenje_od_komsije")),
]
p["body"] = (
    hero(p,
         "Prvo merimo, pa otvaramo",
         "Curenje vode od komšije — kako se utvrđuje odakle curi",
         "Vlaga na plafonu, mrlja koja se širi ili komšija koji kaže da mu voda curi odozgo. "
         "Mesto gde se voda vidi skoro nikada nije mesto gde cev propušta — zato se prvo meri.",
         ["Utvrđujemo čija instalacija curi",
          "%s RSD za jednu ograničenu zonu" % prices.c("curenje_od_komsije"),
          "Nalaz u pisanom obliku",
          "Izlazak 0–24, i vikendom i praznikom"])
    + sec(brief([
        ("Šta je", "Merenje kojim se utvrđuje da li curi vaša instalacija, zajednička vertikala "
                   "ili susedni stan — pre nego što se bilo šta obija."),
        ("Cena", "%s RSD za jednu ograničenu zonu. Za merenje u dva stana i na vertikali obim je "
                 "veći i cenu kažemo pre izlaska." % prices.c("curenje_od_komsije")),
        ("Koliko traje", "Jedna zona obično sat do dva."),
        ("Rezultat", "Obeleženo mesto, pisani nalaz šta je utvrđeno i cena sanacije."),
        ("Izlazak", prices.IZLAZAK_KRATKO),
        ("Noć, vikend, praznik", "Ista cena kao radnim danom."),
    ]), cls="sec")
    + sec(prose("Vlaga na plafonu, a voda curi kod komšije ispod — zašto se ne razbija odmah",
                ["Voda ne ide najkraćim putem nego putem najmanjeg otpora. Iz mesta gde cev "
                 "propušta ona se razlije po betonskoj ploči, pa krene duž cevi ili između slojeva "
                 "poda i izbije tamo gde nađe prvi prolaz — pukotinu u ploči, prodor instalacije, "
                 "spoj dve ploče. Zato je mrlja na plafonu često metar ili dva od stvarnog mesta "
                 "curenja, a ponekad i u drugoj prostoriji.",
                 "Iz toga nastaje tipičan spor između suseda: kod jednog se voda vidi, drugi "
                 "ništa ne primećuje i ne priznaje, a treći, čija vertikala zapravo propušta, nije "
                 "ni uključen u razgovor. Kupatilo iznad se razbije, cevi se pokažu suhe, "
                 "a pare odu i na razbijanje i na vraćanje keramike.",
                 "Merenje to rešava pre štete. Termovizijska kamera pokazuje gde je temperaturna "
                 "razlika na zidu i plafonu, akustično merenje i geofon gde se voda kreće pod "
                 "pritiskom, a provera pritiska po deonicama odgovara na glavno pitanje: propušta "
                 "li uopšte instalacija u tom stanu. Tek kada se zna odakle curi, otvara se — i to "
                 "jedno do dva mesta."]),
          cls="sec sec-alt")
    + sec(cards("Tri situacije zbog kojih nas zovu",
                [("", "Vlaga na plafonu",
                  "Mrlja na plafonu kupatila ili hodnika koja se širi, boja koja se ljušti, "
                  "ponekad kapanje. Izvor je najčešće u podu stana iznad ili u vertikali koja "
                  "prolazi kroz oba stana.",
                  "%s RSD" % prices.c("curenje_od_komsije")),
                 ("", "Voda curi kod komšije ispod",
                  "Komšija zvoni i kaže da mu curi odozgo, a u vašem stanu nema nikakvog znaka. "
                  "Prvo merimo da li vaša instalacija drži pritisak — i to je obično odgovor.",
                  "%s RSD" % prices.c("curenje_od_komsije")),
                 ("", "Curenje u zajedničkoj vertikali",
                  "Vlaga se javlja u više stanova jedan iznad drugog, uglavnom oko sanitarnog "
                  "čvora. Trošak u tom slučaju ide na stambenu zajednicu, a ne na jedan stan.",
                  "%s RSD" % prices.c("curenje_u_zidu"))],
                intro="U svim trima situacijama posao je isti po redosledu: najpre se utvrdi čija "
                      "je instalacija, pa onda gde je mesto.",
                page=p),
          cls="sec")
    + sec(steps("Kako ide posao",
                [("Razgovor i prve provere telefonom",
                  "Pitamo gde je vlaga, od kada je, da li se menja posle tuširanja ili ispiranja i "
                  "koji je sprat. Već to sužava krug — vlaga koja raste samo posle kupanja i vlaga "
                  "koja je stalna nisu isti kvar."),
                 ("Provera da li instalacija drži pritisak",
                  "Voda se zatvori na ventilu u stanu i gleda se da li pritisak pada. Ako ne pada, "
                  "vodovod u tom stanu ne curi i dalje se traži u odvodu ili u vertikali."),
                 ("Merenje instrumentima",
                  "Termovizija na zidu i plafonu, akustično merenje i geofon na razvodu. Zona se "
                  "sužava sa cele prostorije na konkretno mesto."),
                 ("Otvaranje jednog mesta i nalaz",
                  "Otvara se tamo gde merenje pokazuje. Dobijate pisani nalaz šta je utvrđeno, "
                  "čija je instalacija i koliko sanacija košta."),
                 ("Sanacija, kada se dogovori",
                  "Popravka se dogovara posebno, posle nalaza — i cena se kaže pre početka rada.")],
                intro="Redosled je isti i kada u stanu iznad niko ne otvara vrata: tada se meri iz "
                      "stana u kojem je vlaga i sa zajedničkih delova."),
          cls="sec sec-alt")
    + sec(price_table("Cena utvrđivanja curenja između stanova",
                      prices.tabela(("curenje_od_komsije", "Merenje u jednom stanu, jedna zona"),
                                    ("detekcija_vise", "Merenje u dva stana i na vertikali"),
                                    "curenje_u_zidu", "curenje_ispod_poda",
                                    "detekcija_termo", "detekcija_geofon",
                                    "sanacija_curenja"),
                      intro="Cene se odnose na rad. Pisani nalaz ulazi u cenu merenja. "
                            "Izlazak se ne naplaćuje kada radimo intervenciju; ako posle pregleda "
                            "odustanete od posla, naplaćuje se izlazak i pregled, a iznos vam "
                            "kažemo unapred, na telefonu.",
                      note_up="Nedostupan razvod, merenje u više stanova u istom izlasku i "
                              "slučajevi u kojima se ne može ući u stan iznad.",
                      note_in="Dolazak, merenje instrumentima, obeležavanje mesta, pisani nalaz i "
                              "procena cene sanacije."),
          cls="sec", sid="cene")
    + sec(prose("Čije je i ko plaća",
                ["Granica između vašeg i zajedničkog je najčešće prvi ventil u stanu. Sve od tog "
                 "ventila ka stanu je instalacija stana; sve od njega ka vertikali, kao i sama "
                 "vertikala i odvodna cev kroz koju prolaze stanovi, pripada zajedničkoj "
                 "instalaciji i trošak ide na stambenu zajednicu.",
                 "Zato ima smisla da se pre popravke zapiše šta je tačno curelo. Kada popravka "
                 "prođe bez nalaza, trošak po pravilu padne na onoga kod koga se voda videla — "
                 "a to je, kao što smo pisali, najčešće onaj koji nije ni bio uzrok.",
                 "Mi ne presuđujemo ni jednoj strani i ne izlazimo kao sudski veštak. Dajemo nalaz "
                 "merenja: šta je izmereno, gde je mesto i šta sanacija obuhvata. Sa tim se dalje "
                 "razgovara sa komšijom, upravnikom ili osiguranjem."]),
          cls="sec sec-alt")
    + sec(faq_block(p["faq"], "Česta pitanja — curenje od komšije"), cls="sec")
    + sec(chips("Izlazimo u sve beogradske opštine", OPSTINE_CHIPS, p,
                intro="Dežurstvo 0–24 na celom području Beograda, sa istom cenom u svim delovima grada.",
                last=("lokacije", "Sve lokacije")),
          cls="sec sec-alt")
    + sec(related(p, [("detekcija-curenja-vode-beograd", "Detekcija curenja vode"),
                      ("detekcija-curenja-vode-bez-razbijanja", "Bez razbijanja"),
                      ("detekcija-geofonom-i-termovizijom", "Geofon i termovizija"),
                      ("hitne-intervencije-beograd", "Hitne intervencije")]),
          cls="sec")
)
PAGES.append(p)
