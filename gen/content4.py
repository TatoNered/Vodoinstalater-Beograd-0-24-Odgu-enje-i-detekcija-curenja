# -*- coding: utf-8 -*-
"""Страницы, добавленные по данным Google Trends (октябрь 2026):
pukla cev, кластер бойлеров, renoviranje kupatila."""

from blocks import (hero, sec, prose, cards, steps, price_table, faq_block,
                    works, chips, related, brief)
from content1 import H, OPSTINE_CHIPS

PAGES = []
U = ("vodoinstalaterske-usluge", "Usluge")


# ============================================================ PUKLA CEV
p = {
    "slug": "popravka-pukle-cevi",
    "title": "Pukla cev — hitna popravka u Beogradu 0–24 | od 4.000 RSD",
    "desc": "Pukla cev u stanu, zidu, podu ili dvorištu: hitan izlazak 0–24, zaustavljanje vode i sanacija. Beograd, okvirna cena pre početka rada.",
    "h1": "Pukla cev — hitna popravka u Beogradu",
    "crumbs": [H, ("hitne-intervencije-beograd", "Hitne intervencije"),
               ("popravka-pukle-cevi", "Pukla cev")],
    "schema": "service",
    "service_type": "Popravka pukle cevi",
    "offer": (4000, 25000),
}
p["faq"] = [
    ("Šta prvo da uradim kada pukne cev?",
     "Zatvorite glavni ventil za vodu u stanu ili u hodniku zgrade. Ako voda curi blizu utičnica, bojlera ili razvodne kutije, isključite odgovarajući osigurač. Zatim sklonite stvari sa poda i obavestite komšije ispod — to im daje nekoliko minuta da se zaštite."),
    ("Mora li da se razbija zid?",
     "Ako se mesto pucanja vidi, otvara se samo tu. Ako cev curi u zidu ili podu, a mesto nije očigledno, prvo radimo detekciju i tek onda otvaramo — tako se obija jedna do dve pločice umesto cele prostorije."),
    ("Može li cev da se zakrpi ili mora zamena?",
     "Zavisi od materijala i stanja instalacije. Lokalno oštećenje na zdravoj cevi se sanira. Ako je cev stara i iznutra zarasla, krpljenje jednog mesta najčešće znači da će za mesec-dva pući drugo, pa predlažemo zamenu deonice."),
    ("Za koliko stižete?",
     "Zavisi od dela grada, doba dana i broja ekipa na terenu. Kada pozovete, kažemo realno vreme za tu konkretnu situaciju — ne obećavamo rok koji ne možemo da ispunimo."),
    ("Koliko košta popravka pukle cevi?",
     "Hitan izlazak i intervencija kreću od 4.000 dinara. Konačna cena zavisi od toga gde je cev, koliko treba otvarati i da li se menja deonica. Iznos kažemo na licu mesta pre nego što počnemo."),
    ("Da li je pucanje cevi zimi češće?",
     "Jeste, kod nezaštićenih instalacija u dvorištu, podrumu i na spoljnim zidovima. Voda pri smrzavanju širi se i kida cev, a pukotina se otkrije tek kada se odledi i voda krene."),
]
p["body"] = (
    hero(p,
         "Hitan izlazak 0–24",
         "Pukla cev — hitna popravka u Beogradu",
         "Voda ide, a ne znate odakle i kako da je zaustavite. Zovite odmah — kroz razgovor kažemo šta da uradite do dolaska i kada realno možemo da stignemo.",
         ["Dežurstvo 0–24, i vikendom i praznikom",
          "Zaustavljanje vode, pa utvrđivanje uzroka",
          "Sanacija ili zamena deonice, po dogovoru",
          "Račun i pisana garancija na rad"],
         pre_note="<strong>Pre svega:</strong> zatvorite glavni ventil i isključite struju u delu stana gde se voda izliva. Tek onda zovite.")
    + sec(brief([('Prvo uradite', 'Zatvorite glavni ventil, isključite struju u ugroženom delu, obavestite komšije ispod.'), ('Dostupnost', 'Hitan izlazak 0–24, svih sedam dana.'), ('Cena', 'Izlazak i intervencija od 4.000 RSD. Zamena deonice cevi od 6.000. Zamena ventila 2.400–4.000.'), ('Ako se mesto ne vidi', 'Radi se detekcija, od 5.000 RSD — pa se otvara tačno tu, a ne po vlažnoj fleci.'), ('Uključeno', 'Dolazak, zaustavljanje vode, utvrđivanje uzroka i dogovor o ceni pre početka rada.')]), cls="sec")
    + sec(steps("Dok čekate majstora",
                [("Zatvorite dotok", "Glavni ventil je najčešće u kupatilu iza revizionog otvora, u elementu ispod sudopere ili u hodniku zgrade kod vodomera."),
                 ("Isključite struju u ugroženom delu", "Ako je voda blizu utičnica ili bojlera, isključite osigurač. Ne dirajte uređaje koji stoje u vodi."),
                 ("Obavestite komšije ispod", "Nekoliko minuta ranije upozorenje im omogući da sklone stvari i smanji ukupnu štetu."),
                 ("Fotografišite pre čišćenja", "Snimci i vreme nastanka su ono što traži osiguranje i, ako do toga dođe, druga strana.")],
                intro="Prvi potez je uvek zaustavljanje vode, ne traženje uzroka."),
          cls="sec")
    + sec(cards("Gde cevi najčešće pucaju",
                [("", "Cev u zidu",
                  "Vertikalni razvod i spojevi iza pločica. Najčešće posle bušenja zida ili na dotrajalom spoju.", "po proceni"),
                 ("", "Cev u podu i estrihu",
                  "Razvod u podu i podno grejanje — mesto se prvo locira, pa se otvara tačno tu.", "po proceni"),
                 ("", "Pukla cev u dvorištu",
                  "Ukopani vod i priključak do vodomera, često posle mraza ili sleganja tla.", "po proceni"),
                 ("", "Cev u podrumu i na tavanu",
                  "Nezaštićene instalacije koje zimi prve stradaju od smrzavanja.", "po proceni"),
                 ("", "Spoj kod ventila i vodomera",
                  "Propuštanje na navoju i holenderu — najčešće se rešava zamenom spoja.", "od 2.400 RSD"),
                 ("", "Cev iza ugradnih elemenata",
                  "Iza kuhinjskih elemenata, kade i ugradnog vodokotlića, gde se curenje dugo ne vidi.", "po proceni")],
                page=p),
          cls="sec sec-alt")
    + sec(prose("Zašto se ne krpi na brzinu",
                ["Obujmica na cev pod punim pritiskom je rešenje za sat vremena, ne za godinu. Kod starih pocinkovanih instalacija zatezanje spoja često pretvori kapanje u mlaz, jer materijal oko navoja više ne drži.",
                 "Zato prvo gledamo stanje cele grane, a ne samo mesta koje je puklo. Ako je ostatak razvoda zdrav, menja se oštećena deonica i posao je gotov. Ako je cev iznutra zarasla i tanka, kažemo to odmah — u takvoj instalaciji svaka popravka pomera problem nekoliko metara dalje.",
                 "Ako se mesto pucanja ne vidi, a voda se pojavljuje na zidu ili u plafonu, radi se <a href=\"../detekcija-curenja-vode-beograd/\">detekcija</a>. Otvaranje po vlažnoj fleci je najskuplja greška: voda putuje niz cev i izlazi tamo gde joj je najlakše, a ne tamo gde cev propušta."]),
          cls="sec")
    + sec(price_table("Okvirne cene",
                      [("Hitan izlazak i intervencija", "od 4.000"),
                       ("Sanacija spoja koji propušta", "od 3.500"),
                       ("Zamena deonice vodovodne cevi", "od 6.000"),
                       ("Zamena ventila", "2.400–4.000"),
                       ("Detekcija, kada mesto nije vidljivo", "od 5.000"),
                       ("Pukla cev u dvorištu, sa zemljanim radom", "po proceni")],
                      intro="Za intervencije noću, vikendom i praznikom važi ista cena kao i radnim danom — bez doplate za hitnost i bez doplate za neradne dane.",
                      note_up="Cev u podu ili pod betonom, nepoznata trasa i obim štete koji traži više od jedne intervencije.",
                      note_in="Dolazak, zaustavljanje vode, utvrđivanje uzroka i dogovor o ceni pre početka rada."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja — pukla cev"), cls="sec")
    + sec(related(p, [("blog/pukla-cev-sta-prvo-uraditi", "Prvih pet minuta"),
                      ("hitne-intervencije-beograd", "Hitne intervencije"),
                      ("vodovodne-instalacije-i-popravke", "Zamena cevi i ventila"),
                      ("cenovnik", "Cenovnik")])
          + "\n" + chips("Izlazimo na celu teritoriju Beograda", OPSTINE_CHIPS, p,
                         last=("lokacije", "Sve lokacije →")),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ ZAMENA BOJLERA
p = {
    "slug": "zamena-bojlera",
    "title": "Zamena bojlera Beograd — montaža i demontaža | od 5.000 RSD",
    "desc": "Zamena bojlera u Beogradu: demontaža starog, montaža novog, povezivanje i provera ventila. Savet oko zapremine i tipa pre kupovine.",
    "h1": "Zamena bojlera u Beogradu",
    "crumbs": [H, U, ("servis-bojlera", "Bojleri"), ("zamena-bojlera", "Zamena bojlera")],
    "schema": "service",
    "service_type": "Zamena bojlera",
    "offer": (5000, 12000),
}
p["faq"] = [
    ("Kada se bojler menja, a kada popravlja?",
     "Ako je probio kazan, popravka nema smisla — bojler se menja. Curenje na ventilu, priključku ili zaptivci, pregoreo grejač i neispravan termostat se popravljaju i to je znatno jeftinije."),
    ("Koju zapreminu da uzmem?",
     "Za jednu do dve osobe obično je dovoljno 50–80 litara, za porodicu od tri do četiri 80 litara, a za veće domaćinstvo ili kupatilo sa kadom 100 litara i više. Na izbor utiče i mesto ugradnje, jer veći bojler traži jači nosač i više prostora."),
    ("Kupujete li vi bojler ili ja?",
     "Kako vam odgovara. Većina ljudi sama bira i kupuje, a mi radimo zamenu. Ako hoćete, pre kupovine možemo da kažemo koja zapremina i tip odgovaraju prostoru i postojećem priključku."),
    ("Koliko traje zamena?",
     "Standardna zamena na istom mestu traje obično jedan do dva sata. Duže je ako se menja pozicija, ako nosač ne odgovara novom modelu ili ako su priključci zapekli."),
    ("Šta se radi sa starim bojlerom?",
     "Demontiramo ga i, ako tražite, odnosimo. Ta stavka se dogovara posebno."),
]
p["body"] = (
    hero(p,
         "Demontaža, montaža, provera",
         "Zamena bojlera u Beogradu",
         "Bojler je probio kazan ili je jednostavno dotrajao. Skidamo stari, postavljamo novi, povezujemo i obavezno proveravamo sigurnosni ventil — jer upravo on najčešće i ubije sledeći bojler.",
         ["Demontaža starog i montaža novog",
          "Provera nosača i priključaka",
          "Novi sigurnosni ventil po potrebi",
          "Savet oko zapremine pre kupovine"])
    + sec(prose("Šta radimo pri zameni",
                ["Prvo pražnjenje i demontaža starog bojlera, pa provera nosača u zidu — kod većih zapremina to nije formalnost, jer pun bojler od sto litara teži preko sto kilograma.",
                 "Zatim montaža novog, povezivanje na toplu i hladnu vodu i ugradnja ispravnog sigurnosnog ventila. Ventil ispušta višak pritiska pri zagrevanju i kada zapekne, pritisak u kazanu raste — to je najčešći uzrok curenja i probijanja. Stari ventil se ne prenosi na novi bojler.",
                 "Na kraju punjenje, provera na curenje i praćenje prvog zagrevanja. Ako je električni priključak dotrajao ili nije odgovarajući, kažemo to pre nego što uključimo."]),
          cls="sec")
    + sec(steps('Kako ide zamena',
                [('Pražnjenje i demontaža starog', 'Voda se isušti, bojler skine i, ako tražite, odnese.'), ('Provera nosača i priključaka', 'Gleda se da li nosač u zidu odgovara težini novog uređaja i u kakvom su stanju priključci.'), ('Montaža i nov sigurnosni ventil', 'Novi bojler se postavlja i povezuje, sa novim ventilom — stari se ne prenosi, jer je on najčešći uzrok sledećeg kvara.'), ('Punjenje i prvo zagrevanje', 'Proveravamo curenje na spojevima i pratimo prvo zagrevanje. Ako električni priključak nije odgovarajući, kažemo to pre uključivanja.')],
                intro='Pun bojler od sto litara teži preko sto kilograma — nosač nije formalnost.'),
          cls="sec")
    + sec(price_table("Cena zamene bojlera",
                      [("Montaža novog bojlera", "od 5.000"),
                       ("Demontaža starog bojlera", "od 2.500"),
                       ("Zamena bojlera, kompletno", "od 7.000"),
                       ("Zamena sigurnosnog ventila", "od 2.500"),
                       ("Izrada novog priključka ili pomeranje pozicije", "po proceni"),
                       ("Odvoz starog bojlera", "po dogovoru")],
                      intro="Cene se odnose na rad. Bojler i materijal se naplaćuju posebno.",
                      note_up="Veća zapremina, zapekli priključci, nepristupačno mesto i potreba da se radi novi nosač.",
                      note_in="Dolazak, demontaža, montaža, povezivanje i provera posle punjenja."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja — zamena bojlera"), cls="sec")
    + sec(related(p, [("servis-bojlera", "Servis bojlera"),
                      ("bojler-curi", "Bojler curi"),
                      ("vodovodne-instalacije-i-popravke", "Instalacije i popravke"),
                      ("cenovnik", "Cenovnik")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ BOJLER CURI
p = {
    "slug": "bojler-curi",
    "title": "Bojler curi — uzroci i popravka, Beograd | od 2.500 RSD",
    "desc": "Bojler curi odozdo, sa ventila ili na priključku: šta je uzrok, šta se popravlja, a kada je kazan probio i bojler mora da se menja.",
    "h1": "Bojler curi — šta je uzrok i šta se radi",
    "crumbs": [H, U, ("servis-bojlera", "Bojleri"), ("bojler-curi", "Bojler curi")],
    "schema": "service",
    "service_type": "Popravka bojlera koji curi",
    "offer": (2500, 10000),
}
p["faq"] = [
    ("Bojler kaplje sa ventila dok greje — je li to kvar?",
     "Ne nužno. Sigurnosni ventil pri zagrevanju ispušta višak pritiska i par kapi je normalno. Problem je ako curi stalno, i kada bojler ne greje — tada ventil ne zaptiva i menja se."),
    ("Curi odozdo, ispod poklopca — šta je to?",
     "Najčešće zaptivka prirubnice ili sam grejač. To se popravlja: bojler se prazni, otvara i zaptivka ili grejač se menja. Ako voda izlazi iz samog kazana, a ne sa spoja, kazan je probio."),
    ("Kako da znam da je kazan probio?",
     "Voda curi stalno, ne sa spoja nego iz tela bojlera, i količina raste kako se greje. Na takvom bojleru popravka ne postoji — kazan se ne vari i ne krpi, bojler se menja."),
    ("Mogu li da isključim bojler i ostavim ga tako?",
     "Isključite struju i zatvorite dovod vode — to zaustavlja štetu. Ali ako curi, voda u kazanu i dalje ima pritisak iz instalacije, pa to nije trajno rešenje nego način da sačekate majstora bez poplave."),
    ("Zašto bojleri probiju?",
     "Najčešće zbog kamenca i potrošene magnezijumske anode. Anoda je žrtvovani deo koji štiti kazan od korozije; kada se istroši, korozija ide na kazan. Zato se servis radi na dve do tri godine, a ne kada bojler već curi."),
]
p["body"] = (
    hero(p,
         "Prvo uzrok, pa odluka",
         "Bojler curi — šta je uzrok i šta se radi",
         "Voda ispod bojlera ne znači automatski da je gotov. U najvećem broju slučajeva curi ventil, priključak ili zaptivka — a to su jeftine popravke.",
         ["Utvrđujemo odakle tačno curi",
          "Zamena ventila, zaptivki i grejača",
          "Iskreno kažemo kada popravka nema smisla",
          "Hitan izlazak kada voda ne može da se zaustavi"],
         pre_note="<strong>Odmah:</strong> isključite bojler sa struje i zatvorite dovod vode. Ne dirajte uređaj dok stoji u vodi.")
    + sec(cards("Odakle najčešće curi",
                [("", "Sigurnosni ventil",
                  "Par kapi pri zagrevanju je normalno. Stalno curenje znači da ventil ne zaptiva.", "od 2.500 RSD"),
                 ("", "Zaptivka prirubnice",
                  "Voda ispod poklopca, pojačava se kada bojler greje. Rešava se zamenom zaptivke.", "od 3.000 RSD"),
                 ("", "Grejač",
                  "Curenje oko grejača ili pregoreo grejač uz vlagu — menja se zajedno sa zaptivkom.", "od 4.000 RSD"),
                 ("", "Priključci tople i hladne",
                  "Navoji i holenderi koji su popustili ili zarđali.", "od 2.500 RSD"),
                 ("", "Probijen kazan",
                  "Voda izlazi iz tela bojlera. Popravka ne postoji — bojler se menja.", "zamena"),
                 ("", "Kondenz, a ne curenje",
                  "Kod hladne prostorije ponekad je u pitanju kondenzacija, a ne kvar. I to proveravamo.", "—")],
                intro="Prvo gledamo mesto, pa tek onda govorimo o ceni — razlika između ventila i probijenog kazana je razlika između 2.500 dinara i novog bojlera.",
                page=p),
          cls="sec sec-alt")
    + sec(prose("Zašto bojleri počnu da cure",
                ["Skoro svako curenje bojlera ima jedan od dva uzroka, i oba se godinama pripremaju. Prvi je <strong>kamenac</strong>: taloži se na grejaču i po dnu kazana, grejač se pregreva, a naslaga mehanički oštećuje emajl iznutra. Drugi je <strong>potrošena magnezijumska anoda</strong> — to je žrtvovani deo koji na sebe prima koroziju umesto kazana. Kada se istroši, korozija kreće na sam kazan.",
                 "Treći, ređi, ali najbrži put do kvara je <strong>sigurnosni ventil koji je zapekao</strong>. Taj ventil pri zagrevanju ispušta višak pritiska; kada prestane da radi, pritisak u kazanu raste svaki put kada bojler greje. To probija i potpuno zdrav bojler.",
                 "Zato servis na dve do tri godine nije prodaja usluge nego računica: zamena anode i ventila košta nekoliko hiljada dinara, a nov bojler sa montažom — višestruko više. Ako vam bojler već curi, prvo gledamo odakle, jer od toga zavisi da li je u pitanju jeftina popravka ili zamena."]),
          cls="sec")
    + sec(steps('Kako utvrđujemo odakle curi',
                [('Isključenje i pregled spolja', 'Bojler se isključi sa struje, zatvori dotok i posmatra odakle voda zaista izlazi — sa ventila, sa spoja ili iz tela.'), ('Provera sigurnosnog ventila', 'Par kapi pri zagrevanju je normalno. Stalno curenje znači da ventil ne zaptiva, i to je najjeftiniji kvar u ovoj grupi.'), ('Otvaranje i pregled prirubnice', 'Ako voda izlazi ispod poklopca, menja se zaptivka ili grejač. Radi se na licu mesta.'), ('Iskrena procena kada ne vredi', 'Ako voda izlazi iz samog kazana, popravka ne postoji — kazan se ne vari. Tada odmah kažemo da je u pitanju zamena.')],
                intro='Razlika između ventila i probijenog kazana je razlika između 2.500 dinara i novog bojlera.'),
          cls="sec")
    + sec(price_table("Okvirne cene",
                      [("Dijagnostika i utvrđivanje mesta curenja", "od 2.000"),
                       ("Zamena sigurnosnog ventila", "od 2.500"),
                       ("Zamena zaptivke prirubnice", "od 3.000"),
                       ("Zamena grejača", "od 4.000"),
                       ("Sanacija priključaka", "od 2.500"),
                       ("Servis sa čišćenjem kamenca", "3.000–6.000"),
                       ("Zamena bojlera, kada je kazan probio", "od 7.000")],
                      note_up="Nepristupačno mesto i zapekli priključci.",
                      note_in="Dolazak, pražnjenje, utvrđivanje uzroka i provera posle popravke. Delovi se naplaćuju posebno."),
          cls="sec", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja — bojler curi"), cls="sec sec-alt")
    + sec(related(p, [("servis-bojlera", "Servis bojlera"),
                      ("zamena-bojlera", "Zamena bojlera"),
                      ("hitne-intervencije-beograd", "Hitne intervencije"),
                      ("popravka-pukle-cevi", "Pukla cev")]),
          cls="sec")
)
PAGES.append(p)


# ============================================================ RENOVIRANJE KUPATILA
p = {
    "slug": "renoviranje-kupatila",
    "title": "Renoviranje kupatila Beograd — cena radova i rokovi",
    "desc": "Renoviranje kupatila u Beogradu: cena vodoinstalaterskog dela, šta ulazi u posao, koliko traje i u kom redosledu se radi sa keramičarem.",
    "h1": "Renoviranje kupatila — vodoinstalaterski radovi i cena",
    "crumbs": [H, U, ("sanitarije-i-kupatila", "Sanitarije i kupatila"),
               ("renoviranje-kupatila", "Renoviranje kupatila")],
    "schema": "service",
    "service_type": "Renoviranje kupatila — vodoinstalaterski radovi",
    "offer": (20000, 120000),
}
p["faq"] = [
    ("Koliko košta renoviranje kupatila?",
     "Vodoinstalaterski deo kod standardnog kupatila u stanu kreće se okvirno od 20.000 do 60.000 dinara, u zavisnosti od broja tačaka, da li se pomera odvod i da li se menja kompletan razvod. Keramika, materijal i sanitarija se računaju posebno. Tačnu cifru dajemo posle izlaska i merenja, u pisanoj ponudi."),
    ("Šta tačno ulazi u vodoinstalaterski deo?",
     "Demontaža stare sanitarije, novi razvod tople i hladne vode, odvodi, priprema za ugradni vodokotlić ili tuš kabinu, proba pod pritiskom pre keramike i montaža sanitarije posle keramike."),
    ("Koliko traje?",
     "Vodoinstalaterski deo kod standardnog kupatila je obično dva do tri radna dana, podeljeno na dve faze: razvod pre keramike i montaža posle nje. Ukupno renoviranje traje duže, jer između faza radi keramičar i treba vreme da se sve osuši."),
    ("Može li da se pomeri WC šolja ili kada?",
     "Često može, ali to zavisi od položaja vertikale i od toga koliko ima pada za odvod. Na izlasku merimo i kažemo odmah šta je izvodljivo, a šta bi tražilo podizanje poda ili zahvat na zajedničkoj instalaciji."),
    ("Radite li i keramiku?",
     "Radimo vodoinstalaterski deo. Za keramiku, molerske i elektro radove sarađujemo sa majstorima sa kojima redovno radimo, pa možemo da uskladimo redosled i da vi imate jedan kontakt."),
    ("Kada se plaća?",
     "Po dogovorenim fazama, uz račun. Za veće radove dajemo pisanu ponudu sa popisom stavki pre početka, da ne bude iznenađenja na kraju."),
]
p["body"] = (
    hero(p,
         "Pisana ponuda pre početka",
         "Renoviranje kupatila — vodoinstalaterski radovi i cena",
         "Razvod, odvodi i sanitarija za novo kupatilo. Pre početka dobijate popis radova i cenu po stavkama — a ne okvirnu cifru koja raste u hodu.",
         ["Pisana ponuda sa popisom stavki",
          "Proba pod pritiskom pre keramike",
          "Usklađujemo redosled sa keramičarem",
          "Vodoinstalaterski deo od 20.000 RSD"])
    + sec(brief([('Šta ulazi', 'Demontaža stare sanitarije, nov razvod vode i odvoda, proba pod pritiskom i montaža sanitarije posle keramike.'), ('Cena', 'Vodoinstalaterski deo standardnog kupatila 20.000–60.000 RSD. Keramika, sanitarija i materijal se računaju posebno.'), ('Koliko traje', 'Vodoinstalaterski deo obično dva do tri radna dana, u dve faze.'), ('Pre početka', 'Izlazak, merenje i pisana ponuda sa cenama po stavkama.'), ('Keramika', 'Radimo vodoinstalaterski deo i usklađujemo redosled sa keramičarem.')]), cls="sec")
    + sec(price_table("Cena vodoinstalaterskih radova",
                      [("Kompletan razvod u standardnom kupatilu", "20.000–60.000"),
                       ("Razvod vodovoda (topla i hladna)", "od 12.000"),
                       ("Nov odvod i priprema za tuš kabinu", "od 8.000"),
                       ("Priprema i ugradnja nosača za ugradni vodokotlić", "od 10.000"),
                       ("Pomeranje odvoda WC šolje", "po proceni"),
                       ("Demontaža stare sanitarije", "od 4.000"),
                       ("Montaža sanitarije posle keramike", "od 12.000"),
                       ("Veće kupatilo ili kuća sa dva čvora", "po ponudi")],
                      intro="Cene se odnose na rad i na vodoinstalaterski deo posla. Keramika, sanitarija i materijal se računaju posebno.",
                      note_up="Pomeranje vertikale i odvoda, stari objekat sa nepoznatom trasom instalacije, dva sanitarna čvora i netipične dimenzije.",
                      note_in="Izlazak i merenje, pisana ponuda, demontaža, razvod, proba pod pritiskom i montaža sanitarije."),
          cls="sec", sid="cene")
    + sec(steps("Kako ide posao",
                [("Izlazak i merenje", "Gledamo postojeći razvod, položaj vertikale i šta je moguće bez velikih zahvata. Besplatno i bez obaveze."),
                 ("Pisana ponuda", "Popis radova sa cenama po stavkama, rok i redosled. Tek posle vaše saglasnosti počinjemo."),
                 ("Demontaža i razvod", "Skidanje stare sanitarije, novi razvod vodovoda i odvoda, priprema za ugradne elemente."),
                 ("Proba pod pritiskom", "Instalacija se proverava pre nego što dođe keramičar. Greška otkrivena posle keramike košta višestruko."),
                 ("Montaža posle keramike", "Sanitarija, baterije, sifoni i vodokotlić se montiraju na gotovu keramiku i sve se proverava.")],
                intro="Redosled nije formalnost — na njemu se najčešće i gubi novac u renoviranju."),
          cls="sec sec-alt")
    + sec(prose("Na čemu se u renoviranju najčešće gubi novac",
                ["<strong>Razvod se radi na brzinu, pre keramike.</strong> Ako se instalacija ne proveri pod pritiskom, a greška se pojavi posle postavljanja pločica, obija se nova keramika. To je najskuplja stavka koja se lako izbegava.",
                 "<strong>Nova instalacija se veže na staru vertikalu.</strong> Čest slučaj u starim zgradama na Vračaru i u Starom gradu: razvod u stanu je nov i uredan, ali zajednički vod nije menjan decenijama. Problem onda nastaje na spoju, i to posle renoviranja.",
                 "<strong>Sanitarija se kupuje pre merenja.</strong> Razmak rupa, tip odvoda i dubina ugradnog nosača se razlikuju. Pet minuta provere pre kupovine štedi vraćanje robe i izgubljenu nedelju.",
                 "<strong>Faze se ne usklade.</strong> Kada keramičar dođe pre nego što je razvod gotov, ili sanitarija stigne posle njegovog odlaska, posao stoji. Zato redosled dogovaramo unapred, zajedno sa vama."]),
          cls="sec")
    + sec(faq_block(p["faq"], "Česta pitanja — renoviranje kupatila"), cls="sec sec-alt")
    + sec(related(p, [("sanitarije-i-kupatila", "Montaža sanitarije"),
                      ("servis-ugradnih-vodokotlica-geberit", "Ugradni vodokotlići"),
                      ("vodovodne-instalacije-i-popravke", "Zamena cevi"),
                      ("cenovnik", "Cenovnik")]),
          cls="sec")
)
PAGES.append(p)
