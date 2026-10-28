# -*- coding: utf-8 -*-
"""Услуги, добавленные по правкам клиента (28 октября 2026):
лавабо, када и туш-кабина, замена кранов и вентилей, замена труб."""

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
    "offer": (3000, 3500),
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
    "offer": (3000, 4500),
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
    "offer": (2400, 6000),
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
    "offer": (6000, 60000),
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
