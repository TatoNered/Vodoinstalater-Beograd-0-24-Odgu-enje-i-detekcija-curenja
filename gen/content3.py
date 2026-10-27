# -*- coding: utf-8 -*-
"""Sadržaj: popravke, sanitarije, bojleri, hub usluga, cenovnik, firme, o nama, utisci, kontakt."""

from render import SITE, SVG_PHONE, SVG_TICK, depth_prefix
from blocks import (hero, sec, prose, cards, steps, price_table, faq_block,
                    works, chips, related, brief)
from content1 import H, OPSTINE_CHIPS

PAGES = []


# ============================================================ INSTALACIJE I POPRAVKE
p = {
    "slug": "vodovodne-instalacije-i-popravke",
    "title": "Vodovodne instalacije i popravke — Beograd | od 2.400 RSD",
    "desc": "Zamena ventila, popravka i zamena vodovodnih cevi, sanacija curenja, povezivanje mašina i česmi. Vodoinstalater u Beogradu, cena pre početka rada.",
    "h1": "Vodovodne instalacije i popravke",
    "crumbs": [H, ("vodoinstalaterske-usluge", "Usluge"),
               ("vodovodne-instalacije-i-popravke", "Instalacije i popravke")],
    "schema": "service",
    "service_type": "Vodovodne instalacije i popravke",
    "offer": (2400, 30000),
}
p["faq"] = [
    ("Da li menjate samo deo instalacije ili mora cela?",
     "Zavisi od stanja. Ako je ostatak razvoda u redu, menja se samo oštećena deonica. Kod starih pocinkovanih cevi koje su iznutra zarasle često je isplativije zameniti celu granu nego svakih nekoliko meseci krpiti novo mesto."),
    ("Koliko traje zamena vodovodnih cevi u kupatilu?",
     "Obično jedan do dva radna dana za razvod, u zavisnosti od toga koliko tačaka ima i da li se radi u zidu. Keramika i završni radovi se rade posle i ne ulaze u taj rok."),
    ("Radite li sa PPR, bakarnim i višeslojnim cevima?",
     "Radimo sa materijalima koji su uobičajeni na našem tržištu i biramo ih prema postojećoj instalaciji i nameni. Ako postoji razlog da se materijal promeni, objasnimo zašto pre nego što počnemo."),
    ("Dajete li garanciju na rad?",
     "Dajemo pisanu garanciju na izvedeni rad. Na ugrađeni materijal važi garancija proizvođača."),
]
p["body"] = (
    hero(p,
         "Popravke i zamena instalacije",
         "Vodovodne instalacije i popravke",
         "Od zamene jednog ventila do kompletnog razvoda u kupatilu. Pre početka kažemo šta je potrebno, koliko košta i koliko traje.",
         ["Zamena ventila, slavina i priključaka",
          "Popravka i zamena cevi",
          "Sanacija curenja posle detekcije",
          "Račun i pisana garancija na rad"])
    + sec(cards("Šta radimo",
                [("", "Zamena ventila",
                  "Ugaoni, zaporni i glavni ventili koji propuštaju, kapaju ili su zapekli.", "2.400–4.000 RSD"),
                 ("", "Zamena slavine",
                  "Kuhinjska, lavabo i tuš baterija, sa proverom priključaka i zaptivki.", "od 2.500 RSD"),
                 ("", "Popravka pukle cevi",
                  "Sanacija oštećene deonice u zidu, podu ili na vidnom delu razvoda.", "po proceni"),
                 ("", "Zamena vodovodnih cevi",
                  "Deonica ili kompletan razvod kod stare, zarasle i korodirane instalacije.", "od 12.000 RSD"),
                 ("", "Nove instalacije u kupatilu",
                  "Razvod tople i hladne vode i odvoda za novo ili renovirano kupatilo.", "po projektu"),
                 ("", "Povezivanje uređaja",
                  "Veš i sudo mašina, bojler, frižider sa vodom i spoljna česma.", "od 2.500 RSD")],
                intro="Materijal se naplaćuje posebno i cenu kažemo pre nabavke.",
                page=p),
          cls="sec")
    + sec(prose("Kada se isplati popravka, a kada zamena",
                ["Popravka ima smisla kada je instalacija u dobrom stanju, a oštećenje lokalno — pukao spoj, propao ventil, mehaničko oštećenje posle bušenja zida. Tada se menja samo taj deo i posao je gotov istog dana.",
                 "Zamena se isplati kada je cev stara i iznutra zarasla. Kod pocinkovanih instalacija iz starijih zgrada presek se sa godinama smanji toliko da pritisak opadne, voda bude rđava, a svaka intervencija otvori novo slabo mesto nekoliko metara dalje. U tom slučaju je jeftinije zameniti granu odjednom nego plaćati niz popravki.",
                 "Odluku ne donosimo umesto vas. Kažemo šta smo zatekli, koliko bi koštala popravka, koliko zamena i koliko realno može da izdrži postojeća instalacija — pa birate. Ako se curenje ne vidi, prvo radimo <a href=\"../detekcija-curenja-vode-beograd/\">detekciju</a>, da se ne otvara nasumično."]),
          cls="sec sec-alt")
    + sec(price_table("Okvirne cene",
                      [("Zamena ugaonog ili zapornog ventila", "2.400–4.000"),
                       ("Zamena baterije (slavine)", "od 2.500"),
                       ("Povezivanje veš ili sudo mašine", "od 2.500"),
                       ("Sanacija curenja na spoju", "od 3.500"),
                       ("Zamena deonice vodovodne cevi", "od 6.000"),
                       ("Razvod vodovoda u kupatilu", "od 12.000"),
                       ("Spoljna česma i dvorišni priključak", "po proceni")],
                      note_up="Rad u zidu i podu, teško dostupna instalacija, nestandardni delovi i rad van radnog vremena.",
                      note_in="Dolazak, utvrđivanje stanja, rad i provera pod pritiskom posle popravke. Materijal se naplaćuje posebno."),
          cls="sec", sid="cene")
    + sec(faq_block(p["faq"]), cls="sec sec-alt")
    + sec(related(p, [("detekcija-curenja-vode-beograd", "Detekcija curenja"),
                      ("sanitarije-i-kupatila", "Sanitarije i kupatila"),
                      ("servis-bojlera", "Servis bojlera"),
                      ("hitne-intervencije-beograd", "Hitne intervencije")]),
          cls="sec")
)
PAGES.append(p)


# ============================================================ SANITARIJE
p = {
    "slug": "sanitarije-i-kupatila",
    "title": "Montaža sanitarija i opremanje kupatila — Beograd",
    "desc": "Montaža WC šolje, lavaboa, kade, tuš kabine i baterija, zamena sifona i povezivanje mašina. Vodoinstalater u Beogradu, cena pre početka rada.",
    "h1": "Sanitarije i kupatila",
    "crumbs": [H, ("vodoinstalaterske-usluge", "Usluge"),
               ("sanitarije-i-kupatila", "Sanitarije i kupatila")],
    "schema": "service",
    "service_type": "Montaža sanitarija",
    "offer": (2500, 20000),
}
p["faq"] = [
    ("Da li nabavljate sanitariju ili je kupujem sam?",
     "Kako vam odgovara. Većina ljudi sama bira sanitariju, a mi radimo montažu. Ako želite, možemo da preporučimo šta se u praksi pokazalo kao izdržljivo i da pomognemo oko dimenzija pre kupovine."),
    ("Može li se WC šolja zameniti bez obijanja pločica?",
     "Najčešće može, ako su odvod i razmak rupa kompatibilni sa novim modelom. Kada se menja tip šolje — na primer podna u konzolnu — obijanje je neizbežno, jer se menja i nosač i odvod."),
    ("Radite li i keramiku?",
     "Radimo vodoinstalaterski deo: instalacije, odvode i montažu sanitarije. Za keramiku i molerske radove sarađujemo sa majstorima sa kojima redovno radimo, pa možemo da uskladimo redosled."),
    ("Koliko traje opremanje kupatila?",
     "Vodoinstalaterski deo kod standardnog kupatila obično traje dva do tri dana, podeljeno na fazu razvoda pre keramike i fazu montaže sanitarije posle nje."),
]
p["body"] = (
    hero(p,
         "Montaža i zamena sanitarije",
         "Sanitarije i kupatila",
         "Montaža nove sanitarije, zamena dotrajale i vodoinstalaterski deo renoviranja kupatila — od razvoda do poslednje zaptivke.",
         ["WC šolja, lavabo, kada i tuš kabina",
          "Baterije, sifoni i odvodi",
          "Razvod za renovirano kupatilo",
          "Usklađujemo se sa keramičarem"])
    + sec(cards("Najčešći poslovi",
                [("", "Montaža WC šolje",
                  "Podna i konzolna šolja, sa povezivanjem na odvod i vodokotlić.", "od 3.500 RSD"),
                 ("", "Montaža lavaboa",
                  "Lavabo sa sifonom i baterijom, nadgradni i ugradni modeli.", "od 3.000 RSD"),
                 ("", "Montaža kade ili tuš kabine",
                  "Postavljanje, povezivanje odvoda i provera zaptivanja.", "od 6.000 RSD"),
                 ("", "Zamena baterije",
                  "Kuhinjska, lavabo, tuš i kada baterija.", "od 2.500 RSD"),
                 ("", "Zamena sifona",
                  "Sifon sudopere, lavaboa, kade i tuš kade.", "od 2.500 RSD"),
                 ("", "Povezivanje mašina",
                  "Veš i sudo mašina, sa ventilom i odvodom.", "od 2.500 RSD")],
                page=p),
          cls="sec sec-alt")
    + sec(steps("Kako ide renoviranje kupatila",
                [("Izlazak i merenje", "Gledamo postojeći razvod, položaj odvoda i šta je moguće bez pomeranja vertikale."),
                 ("Ponuda i dogovor", "Dobijate popis radova i cenu pre početka, sa redosledom i trajanjem."),
                 ("Razvod pre keramike", "Vodovod i odvodi se izvode i proveravaju pod pritiskom pre nego što dođe keramičar."),
                 ("Montaža posle keramike", "Sanitarija, baterije i sifoni se montiraju na gotovu keramiku i sve se proverava.")],
                intro="Ovaj redosled je bitan: greška u fazi razvoda se posle keramike skupo ispravlja."),
          cls="sec")
    + sec(price_table("Okvirne cene montaže",
                      [("Montaža WC šolje", "od 3.500"),
                       ("Montaža lavaboa sa sifonom", "od 3.000"),
                       ("Montaža kade ili tuš kabine", "od 6.000"),
                       ("Zamena baterije", "od 2.500"),
                       ("Zamena sifona", "od 2.500"),
                       ("Vodoinstalaterski deo renoviranja kupatila", "od 20.000")],
                      note_up="Pomeranje odvoda i vertikale, netipične dimenzije i rad u objektu bez funkcionalne instalacije.",
                      note_in="Dolazak, montaža, povezivanje i provera na curenje. Sanitarija i materijal se naplaćuju posebno."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"]), cls="sec")
    + sec(related(p, [("renoviranje-kupatila", "Renoviranje kupatila"),
                      ("servis-ugradnih-vodokotlica-geberit", "Ugradni vodokotlići"),
                      ("vodovodne-instalacije-i-popravke", "Instalacije i popravke"),
                      ("servis-bojlera", "Servis bojlera")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ BOJLERI
p = {
    "slug": "servis-bojlera",
    "title": "Servis bojlera Beograd — kamenac, grejač, ventil | od 3.000",
    "desc": "Servis bojlera u Beogradu: čišćenje kamenca, zamena grejača, termostata, magnezijumske anode i sigurnosnog ventila. Cena se kaže pre početka rada.",
    "h1": "Servis bojlera u Beogradu",
    "crumbs": [H, ("vodoinstalaterske-usluge", "Usluge"), ("servis-bojlera", "Servis bojlera")],
    "schema": "service",
    "service_type": "Servis bojlera",
    "offer": (3000, 12000),
}
p["faq"] = [
    ("Koliko često treba servisirati bojler?",
     "Orijentaciono na dve do tri godine, a u delovima grada sa tvrđom vodom i češće. Redovno čišćenje kamenca produžava vek grejača i smanjuje potrošnju struje."),
    ("Bojler curi — može li da se popravi?",
     "Zavisi odakle curi. Curenje na ventilu, priključku ili zaptivci se popravlja. Ako je probio sam kazan, popravka nema smisla i bojler se menja."),
    ("Zašto voda nije dovoljno topla?",
     "Najčešće zbog kamenca na grejaču ili zbog neispravnog termostata. Oba se utvrđuju otvaranjem i proverom, i to je deo servisa."),
    ("Da li menjate bojler koji sam već kupio?",
     "Menjamo. Skidamo stari, postavljamo novi, povezujemo i proveravamo ventil i priključke. Ako bojler tek kupujete, možemo da kažemo koja zapremina i tip odgovaraju prostoru."),
]
p["body"] = (
    hero(p,
         "Servis na dve do tri godine",
         "Servis bojlera u Beogradu",
         "Voda nije dovoljno topla, bojler kaplje ili je grejač pregoreo. Servis bojlera znači otvaranje, čišćenje kamenca, proveru anode i zamenu dela koji je otkazao.",
         ["Čišćenje kamenca i servis grejača",
          "Zamena grejača, termostata i anode",
          "Zamena sigurnosnog ventila",
          "Montaža novog bojlera"])
    + sec(brief([('Šta obuhvata', 'Pražnjenje, čišćenje kamenca, provera grejača, termostata, magnezijumske anode i sigurnosnog ventila.'), ('Cena', 'Servis sa čišćenjem kamenca 3.000–6.000 RSD. Zamena grejača od 4.000. Zamena ventila od 2.500.'), ('Koliko često', 'Orijentaciono na dve do tri godine, češće tamo gde je voda tvrđa.'), ('Koliko traje', 'Standardan servis najčešće jedan do dva sata.'), ('Kada ne vredi', 'Ako je kazan probio, servis nema smisla — bojler se menja.')]), cls="sec")
    + sec(prose("Šta obuhvata servis",
                ["Servis počinje pražnjenjem i otvaranjem bojlera. Sa grejača i iz kazana se uklanja kamenac, proverava se stanje magnezijumske anode — ona štiti kazan od korozije i troši se — i meri se ispravnost grejača i termostata.",
                 "Poseban deo je sigurnosni ventil. On ispušta višak pritiska pri zagrevanju i kada zapekne, pritisak u kazanu raste. To je najčešći uzrok curenja i oštećenja bojlera, a ventil je jedan od jeftinijih delova.",
                 "Posle sklapanja bojler se puni, proverava se na curenje i prati prvo zagrevanje. Ako se pokaže da je kazan probio, kažemo to odmah — u tom slučaju servis nema smisla i preporučujemo zamenu."]),
          cls="sec")
    + sec(price_table("Cena servisa bojlera",
                      [("Servis i čišćenje kamenca", "3.000–6.000"),
                       ("Zamena grejača", "od 4.000"),
                       ("Zamena termostata", "od 3.500"),
                       ("Zamena magnezijumske anode", "od 3.000"),
                       ("Zamena sigurnosnog ventila", "od 2.500"),
                       ("Montaža novog bojlera", "od 5.000"),
                       ("Demontaža starog bojlera", "od 2.500")],
                      note_up="Teško dostupan bojler, zapekli priključci, veća zapremina i rad van radnog vremena.",
                      note_in="Dolazak, pražnjenje, servis, provera ventila i kontrola posle punjenja. Delovi se naplaćuju posebno."),
          cls="sec sec-alt", sid="cene")
    + sec(faq_block(p["faq"]), cls="sec")
    + sec(cards("Pojedinačno po problemu",
                [("bojler-curi", "Bojler curi",
                  "Voda ispod bojlera, sa ventila ili iz kazana — šta se popravlja, a kada je gotov.", "od 2.500 RSD"),
                 ("zamena-bojlera", "Zamena bojlera",
                  "Demontaža starog, montaža novog, nov sigurnosni ventil i provera nosača.", "od 5.000 RSD"),
                 ("", "Zamena grejača i termostata",
                  "Voda se ne greje ili bojler iskače — najčešći kvar posle kamenca.", "od 3.500 RSD")],
                page=p),
          cls="sec")
    + sec(related(p, [("bojler-curi", "Bojler curi"),
                      ("zamena-bojlera", "Zamena bojlera"),
                      ("vodovodne-instalacije-i-popravke", "Instalacije i popravke"),
                      ("cenovnik", "Cenovnik")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ HUB USLUGA
p = {
    "slug": "vodoinstalaterske-usluge",
    "title": "Vodoinstalaterske usluge u Beogradu — spisak i cene",
    "desc": "Sve vodoinstalaterske usluge na jednom mestu: odgušenje, detekcija curenja, snimanje kamerom, hitne intervencije, bojleri, sanitarije i instalacije.",
    "h1": "Vodoinstalaterske usluge u Beogradu",
    "crumbs": [H, ("vodoinstalaterske-usluge", "Usluge")],
    "schema": "page",
}
p["faq"] = [
    ("Kako da znam koja usluga mi treba?",
     "Ne morate da znate. Opišite šta se dešava telefonom ili pošaljite fotografiju — na osnovu toga kažemo šta je verovatan uzrok, koja intervencija je potrebna i u kom je rasponu cena."),
    ("Radite li i poslove koji nisu na spisku?",
     "Radimo i druge vodoinstalaterske poslove. Ako nešto nije u našem domenu, kažemo to odmah umesto da uzmemo posao koji ne možemo da uradimo kako treba."),
]
p["body"] = (
    hero(p,
         "Sve usluge na jednom mestu",
         "Vodoinstalaterske usluge u Beogradu",
         "Odgušenje, dijagnostika, hitne intervencije i redovni vodoinstalaterski radovi — za stanove, kuće, lokale i stambene zajednice.",
         ["Dežurstvo 0–24, i vikendom",
          "Cena dogovorena pre početka rada",
          "Račun i pisana garancija",
          "Rad sa pravnim licima, preko računa"],
         with_form=False)
    + sec(cards("Odgušenje i kanalizacija",
                [("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije",
                  "Svi odvodi u stanu i kući, vertikala i zajednička kanalizacija u zgradi.", "od 3.000 RSD"),
                 ("odgusenje-sudopere-beograd", "Odgušenje sudopere",
                  "Kuhinjski odvod zapušen masnoćom i ostacima hrane.", "3.000–3.500 RSD"),
                 ("odgusenje-wc-solje-beograd", "Odgušenje WC šolje",
                  "Zapušena šolja, voda koja se vraća ili sporo otiče.", "3.000–3.500 RSD"),
                 ("masinsko-odgusenje-kanalizacije", "Mašinsko odgušenje",
                  "Mašina sa sajlom za tvrdokorne čepove i duže trase.", "od 3.500 RSD"),
                 ("snimanje-kanalizacije-kamerom", "Snimanje kamerom",
                  "Utvrđivanje uzroka ponovljenih zapušenja i stanja cevi.", "6.000–8.000 RSD"),
                 ("popravka-pukle-cevi", "Pukla cev",
                  "Hitna popravka kada voda ide, a ne može da se zaustavi.", "od 4.000 RSD")],
                page=p),
          cls="sec")
    + sec(cards("Voda, curenja i dijagnostika",
                [("detekcija-curenja-vode-beograd", "Detekcija curenja vode",
                  "Lociranje mesta curenja pre nego što se bilo šta obija.", "od 5.000 RSD"),
                 ("detekcija-curenja-vode-bez-razbijanja", "Detekcija bez razbijanja",
                  "Termovizija i akustika umesto nasumičnog otvaranja.", "5.000–12.000 RSD"),
                 ("detekcija-curenja-vode-u-zemlji", "Curenje u zemlji",
                  "Dvorišni i ukopani vodovi, priključak do vodomera.", "10.000–25.000 RSD"),
                 ("detekcija-geofonom-i-termovizijom", "Geofon i termovizija",
                  "Metode i oprema koju koristimo i kada koja ima smisla.", "od 5.000 RSD"),
                 ("vodovodne-instalacije-i-popravke", "Instalacije i popravke",
                  "Ventili, cevi, sanacija curenja i novi razvod.", "od 2.400 RSD"),
                 ("hitne-intervencije-beograd", "Hitne intervencije 0–24",
                  "Pukla cev, poplava, ventil koji ne zatvara.", "od 4.000 RSD")],
                page=p),
          cls="sec sec-alt")
    + sec(cards("Uređaji i sanitarije",
                [("servis-bojlera", "Servis i zamena bojlera",
                  "Kamenac, grejač, termostat, anoda i sigurnosni ventil.", "od 3.000 RSD"),
                 ("servis-ugradnih-vodokotlica-geberit", "Ugradni vodokotlići",
                  "Servis mehanizma kroz revizioni otvor, bez obijanja.", "2.500–5.000 RSD"),
                 ("bojler-curi", "Bojler curi",
                  "Ventil, zaptivka ili probijen kazan — prvo uzrok, pa odluka.", "od 2.500 RSD"),
                 ("renoviranje-kupatila", "Renoviranje kupatila",
                  "Razvod, odvodi i sanitarija, sa pisanom ponudom pre početka.", "od 20.000 RSD"),
                 ("sanitarije-i-kupatila", "Sanitarije i kupatila",
                  "Montaža šolje, lavaboa, kade, baterija i sifona.", "od 2.500 RSD"),
                 ("za-firme", "Usluge za firme",
                  "Lokali, kafići, restorani, poslovni prostori i stambene zajednice.", "po ugovoru"),
                 ("cenovnik", "Ceo cenovnik",
                  "Okvirne cene svih usluga na jednom mestu.", ""),
                 ("kontakt", "Procena pre dolaska",
                  "Pošaljite opis ili fotografiju i dobijate okvirnu cenu.", "")],
                page=p),
          cls="sec")
    + sec(faq_block(p["faq"]), cls="sec sec-alt")
    + sec(prose("Kako da znate šta vam treba",
                ["Ne morate da pogodite uslugu. Opišite šta se dešava — koji odvod, da li se voda vraća, kada je počelo, da li je isto kod komšija — i na osnovu toga kažemo šta je verovatan uzrok i u kom je rasponu cena.",
                 "Ako hoćete prvo da pročitate, u <a href=\"../blog/\">savetima</a> stoji šta možete sami kod <a href=\"../blog/zapusena-sudopera-sta-raditi/\">zapušene sudopere</a>, kako se <a href=\"../blog/kako-prepoznati-curenje-vode/\">prepoznaje curenje vode</a> i šta uraditi u prvih pet minuta kada <a href=\"../blog/pukla-cev-sta-prvo-uraditi/\">pukne cev</a>."]),
          cls="sec")
    + sec(chips("Radimo u svim beogradskim opštinama", OPSTINE_CHIPS, p,
                last=("lokacije", "Sve lokacije →")),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ CENOVNIK
p = {
    "slug": "cenovnik",
    "title": "Cenovnik vodoinstalaterskih usluga — Beograd [GODINA]",
    "desc": "Okvirne cene odgušenja, detekcije curenja, snimanja kamerom, servisa bojlera i montaže sanitarije u Beogradu. Tačna cena se dogovara pre početka rada.",
    "h1": "Cenovnik vodoinstalaterskih usluga",
    "crumbs": [H, ("cenovnik", "Cenovnik")],
    "schema": "page",
}
p["faq"] = [
    ("Zašto su cene date u rasponu, a ne fiksno?",
     "Zato što se iste intervencije razlikuju po težini. Zapušen sifon i zapušena vertikala su oba „odgušenje“, ali to nije isti posao. Raspon pokazuje realan okvir, a tačan iznos dobijate na licu mesta pre nego što počnemo."),
    ("Da li se dolazak naplaćuje?",
     "Ako radimo intervenciju, ne naplaćuje se posebno. Ako posle pregleda odustanete od posla, naplaćuje se izlazak i dijagnostika, i taj iznos vam kažemo unapred, telefonom."),
    ("Može li cena da se promeni tokom rada?",
     "Dogovorena cena se ne menja. Ako se tokom rada otkrije nešto što menja obim posla — na primer oštećena cev ispod čepa — zaustavljamo se, objasnimo šta je nađeno i dogovaramo dalje pre nego što nastavimo."),
    ("Kako se tarifira rad noću, vikendom i praznikom?",
     "Drugačije nego u redovnom terminu. Razliku kažemo pre izlaska, a ne posle obavljenog posla."),
    ("Izdajete li račun i radite li sa firmama?",
     "Izdajemo račun za svaki posao. Za pravna lica radimo preko računa, po predračunu ili po ugovoru o održavanju."),
    ("Da li cene uključuju materijal?",
     "Ne. Cene se odnose na rad. Materijal i rezervni delovi se naplaćuju posebno i cenu kažemo pre nabavke."),
]
p["body"] = (
    hero(p,
         "Okvirne cene, bez skrivenih stavki",
         "Cenovnik vodoinstalaterskih usluga u Beogradu",
         "Cene ispod su okviri za tipične situacije. Tačan iznos kažemo na licu mesta pre nego što počnemo rad — i posle toga se ne menja.",
         ["Okvirni raspon dobijate telefonom",
          "Tačna cena pre početka rada",
          "Račun za svaki posao",
          "Za firme — preko računa"],
         pre_note="Cenovnik je informativan i važi za područje Beograda. Materijal i rezervni delovi se naplaćuju posebno. <strong>Ažurirano: [MESEC GODINA]</strong>.")
    + sec(brief([('Odgušenje', 'Sudopera, šolja, kada 3.000–3.500 RSD. Mašinsko od 3.500. Vertikala 6.000–8.000.'), ('Dijagnostika', 'Snimanje kamerom 6.000–8.000 RSD. Detekcija curenja od 5.000.'), ('Hitno', 'Izlazak i intervencija od 4.000 RSD. Rad noću i praznikom tarifira se drugačije.'), ('Popravke', 'Zamena ventila 2.400–4.000 RSD. Servis bojlera 3.000–6.000. Ugradni vodokotlić 2.500–5.000.'), ('Kako se plaća', 'Račun za svaki posao. Pravna lica — preko računa, po predračunu ili ugovoru.'), ('Važno', 'Cene su za rad. Materijal se naplaćuje posebno. Tačan iznos se kaže pre početka i posle se ne menja.')]), cls="sec")
    + sec(price_table("Odgušenje i kanalizacija",
                      [("Odgušenje sudopere", "3.000–3.500"),
                       ("Odgušenje WC šolje", "3.000–3.500"),
                       ("Odgušenje kade ili tuš kabine", "3.000–3.500"),
                       ("Odgušenje podnog slivnika", "od 3.000"),
                       ("Mašinsko odgušenje", "od 3.500"),
                       ("Odgušenje vertikale u zgradi", "6.000–8.000"),
                       ("Odgušenje spoljne kanalizacije i šahtova", "od 8.000"),
                       ("Odgušenje pod pritiskom", "od 10.000"),
                       ("Snimanje kanalizacije kamerom", "6.000–8.000")]),
          cls="sec", sid="odgusenje")
    + sec(price_table("Detekcija curenja vode",
                      [("Detekcija, jedna ograničena zona", "5.000–12.000"),
                       ("Detekcija, više prostorija ili složen razvod", "10.000–18.000"),
                       ("Detekcija termovizijskom kamerom", "od 5.000"),
                       ("Detekcija geofonom i akustičnom opremom", "od 7.000"),
                       ("Detekcija curenja u zemlji", "10.000–25.000"),
                       ("Sanacija pronađenog curenja", "po proceni")]),
          cls="sec sec-alt", sid="detekcija")
    + sec(price_table("Popravke, bojleri i sanitarija",
                      [("Zamena ugaonog ili zapornog ventila", "2.400–4.000"),
                       ("Zamena baterije (slavine)", "od 2.500"),
                       ("Zamena sifona", "od 2.500"),
                       ("Povezivanje veš ili sudo mašine", "od 2.500"),
                       ("Servis ugradnog vodokotlića", "2.500–5.000"),
                       ("Servis bojlera i čišćenje kamenca", "3.000–6.000"),
                       ("Zamena grejača u bojleru", "od 4.000"),
                       ("Montaža novog bojlera", "od 5.000"),
                       ("Montaža WC šolje", "od 3.500"),
                       ("Montaža lavaboa", "od 3.000"),
                       ("Montaža kade ili tuš kabine", "od 6.000"),
                       ("Zamena deonice vodovodne cevi", "od 6.000"),
                       ("Razvod vodovoda u kupatilu", "od 12.000"),
                       ("Renoviranje kupatila, vodoinstalaterski deo", "20.000–60.000")]),
          cls="sec", sid="popravke")
    + sec(price_table("Hitne intervencije",
                      [("Hitan izlazak i intervencija", "od 4.000"),
                       ("Hitno odgušenje", "od 3.500"),
                       ("Popravka pukle cevi", "od 4.000"),
                       ("Zamena deonice vodovodne cevi", "od 6.000"),
                       ("Ispumpavanje vode iz podruma", "po proceni")],
                      intro="Rad noću, vikendom i praznikom tarifira se drugačije. Razliku kažemo pre izlaska.",
                      note_up="Rad van radnog vremena, nedostupna instalacija, veća dužina trase i obim štete koji traži više od jedne intervencije.",
                      note_in="Dolazak, utvrđivanje uzroka, dogovor o ceni pre rada, izvođenje, provera i čišćenje za sobom."),
          cls="sec sec-alt", sid="hitno")
    + sec(prose("Kako formiramo cenu",
                ["Prvo opis. Kada pozovete, pitamo nekoliko konkretnih stvari: koji odvod, da li se voda vraća, da li problem postoji i kod komšija, kada je počelo. Na osnovu toga dajemo okvirni raspon — ne zato što je to konačno, nego da biste znali sa čim računate pre nego što iko izađe.",
                 "Zatim pregled. Na licu mesta se vidi prava slika: dostupnost revizije, dužina trase, stanje instalacije. Tada kažemo tačan iznos i tek posle vaše saglasnosti počinjemo rad.",
                 "I na kraju račun. Za fizička lica izdajemo račun za izvedeni posao, za pravna lica radimo preko računa, po predračunu ili po ugovoru o redovnom održavanju. Na rad dajemo pisanu garanciju."]),
          cls="sec")
    + sec(faq_block(p["faq"], "Česta pitanja o cenama"), cls="sec sec-alt")
    + sec(related(p, [("blog/kako-izabrati-vodoinstalatera", "Kako izabrati majstora"),
                      ("radovi", "Naši radovi"),
                      ("za-firme", "Za firme"),
                      ("kontakt", "Procena pre dolaska")]),
          cls="sec")
)
PAGES.append(p)


# ============================================================ ZA FIRME
p = {
    "slug": "za-firme",
    "title": "Vodoinstalater za firme, lokale i restorane — Beograd",
    "desc": "Vodoinstalaterske usluge za kafiće, restorane, lokale, poslovne prostore i stambene zajednice u Beogradu. Preko računa, po pozivu ili po ugovoru.",
    "h1": "Vodoinstalater za firme i poslovne prostore",
    "crumbs": [H, ("za-firme", "Za firme")],
    "schema": "page",
}
p["faq"] = [
    ("Izdajete li račun i radite li preko računa?",
     "Da. Radimo sa pravnim licima, izdajemo predračun i račun i plaćanje ide na tekući račun. Na zahtev dostavljamo i specifikaciju radova za knjigovodstvo."),
    ("Šta obuhvata ugovor o redovnom održavanju?",
     "Dogovoreni broj preventivnih izlazaka godišnje, prioritet u javljanju kod kvara i unapred poznate cene intervencija. Obim se piše prema objektu — nije isto kafić sa jednim šankom i restoran sa kuhinjom."),
    ("Možete li da radite van radnog vremena lokala?",
     "Možemo i najčešće tako i radimo. Rano ujutru, kasno uveče ili neradnim danom — da intervencija ne zatvara lokal u najprometnijem delu dana."),
    ("Radite li za stambene zajednice?",
     "Radimo. Zajednička kanalizacija, vertikale, podrumske instalacije i hitne intervencije, sa računom na stambenu zajednicu i izveštajem koji upravnik može da priloži."),
    ("Da li dajete ponudu unapred?",
     "Za planirane radove dajemo pisanu ponudu sa popisom i cenama. Za intervencije po pozivu dajemo okvirni raspon telefonom, a tačan iznos pre početka rada."),
]
p["body"] = (
    hero(p,
         "Radimo preko računa",
         "Vodoinstalater za firme, lokale i stambene zajednice",
         "Kafići, restorani, poslovni prostori, agencije za izdavanje i stambene zajednice. Predračun, račun i mogućnost ugovora o redovnom održavanju.",
         ["Predračun i račun na pravno lice",
          "Rad van radnog vremena lokala",
          "Ugovor o redovnom održavanju",
          "Jedan kontakt za sve objekte"])
    + sec(cards("Sa kim radimo",
                [("", "Kafići i restorani",
                  "Kuhinjski odvodi, mastolovi, šank i sanitarni čvor — tamo gde zapušenje znači zatvoren lokal.", ""),
                 ("", "Poslovni prostori i kancelarije",
                  "Sanitarni čvorovi, čajne kuhinje i instalacije u zakupljenom prostoru.", ""),
                 ("", "Stambene zajednice",
                  "Vertikale, zajednička kanalizacija, podrumske instalacije i hitne intervencije.", ""),
                 ("", "Agencije i izdavaoci stanova",
                  "Više stanova, jedan kontakt i jedan račun, sa izveštajem po adresi.", ""),
                 ("", "Hoteli i apartmani",
                  "Intervencije usklađene sa prijavom gostiju i preventivni pregledi van sezone.", ""),
                 ("", "Prodavnice i tržni prostori",
                  "Sanitarni deo, odvodi i instalacije u zakupljenom prostoru.", "")],
                page=p),
          cls="sec sec-alt")
    + sec(prose("Preventivno održavanje se isplati",
                ["U ugostiteljstvu se kuhinjski odvod ne zapuši odjednom. Masnoća se taloži mesecima, protok se smanjuje, a čep nastane u najgorem mogućem trenutku — u subotu uveče, kada je lokal pun. Trošak tada nije intervencija, nego sat i po zatvorene kuhinje.",
                 "Zato za lokale radimo planska odgušenja u dogovorenim razmacima: odvodi se čiste pre nego što se zapuše, u terminu koji vi birate. Isto važi za sanitarne čvorove u poslovnim prostorima i za vertikale u zgradama, gde se zapušenje retko tiče samo jednog stana.",
                 "Uz to idu i preventivni pregledi: stanje odvoda, ventila i priključaka, sa kratkim izveštajem šta je u redu, šta treba pratiti i šta bi trebalo zameniti u narednom periodu. Taj izveštaj je koristan i kod zakupa, jer jasno pokazuje u kakvom je stanju instalacija preuzeta."]),
          cls="sec")
    + sec(cards("Šta radimo po ugovoru",
                [("", "Planirana odgušenja",
                  "Čišćenje kuhinjskih i sanitarnih odvoda u dogovorenim razmacima.", ""),
                 ("", "Preventivni pregledi",
                  "Provera odvoda, ventila i priključaka, sa kratkim pisanim izveštajem.", ""),
                 ("", "Prioritet kod kvara",
                  "Ugovorni objekti imaju prednost pri rasporedu ekipa.", ""),
                 ("", "Unapred poznate cene",
                  "Cenovnik intervencija fiksiran ugovorom, bez pregovaranja u hitnoj situaciji.", ""),
                 ("", "Snimanje kamerom",
                  "Periodična provera stanja kanalizacije na objektima sa ponovljenim problemima.", ""),
                 ("", "Izveštaj za knjigovodstvo",
                  "Specifikacija radova uz račun, po objektu i po datumu.", "")],
                page=p),
          cls="sec sec-alt")
    + sec(faq_block(p["faq"], "Česta pitanja — saradnja sa firmama"), cls="sec")
    + sec(related(p, [("cenovnik", "Cenovnik"),
                      ("odgusenje-kanalizacije-beograd", "Odgušenje"),
                      ("snimanje-kanalizacije-kamerom", "Snimanje kamerom"),
                      ("kontakt", "Kontakt")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ O NAMA
p = {
    "slug": "o-nama",
    "title": "O nama — vodoinstalaterska služba u Beogradu | [NAZIV FIRME]",
    "desc": "Ko smo, kako radimo i zašto cenu dogovaramo pre početka posla. Registrovana vodoinstalaterska služba u Beogradu, sa računom i garancijom na rad.",
    "h1": "O nama",
    "crumbs": [H, ("o-nama", "O nama")],
    "schema": "page",
}
p["faq"] = [
    ("Da li ste registrovana firma?",
     "Jesmo, registrovani smo u APR-u. Izdajemo račun za svaki posao i radimo sa pravnim licima preko računa."),
    ("Ko odgovara na telefon?",
     "Pozive prima neko iz firme ko poznaje posao, a ne služba za zakazivanje. Zato kroz razgovor može odmah da se proceni o čemu je reč i da se kaže okvirna cena."),
    ("Imate li garanciju na rad?",
     "Dajemo pisanu garanciju na izvedeni rad. Na ugrađeni materijal važi garancija proizvođača."),
]
p["body"] = (
    hero(p,
         "Registrovana služba, rad sa računom",
         "O nama",
         "Vodoinstalaterska služba iz Beograda. Radimo za domaćinstva, lokale i stambene zajednice, sa dežurstvom 0–24 i cenom koja se dogovara pre početka posla.",
         ["Registrovani u APR-u",
          "Račun za svaki posao",
          "Pisana garancija na rad",
          "Oprema za dijagnostiku, ne samo za čišćenje"],
         with_form=False)
    + sec(prose("Kako radimo",
                ["Posao počinje razgovorom, ne izlaskom. Kada pozovete, pitamo nekoliko konkretnih stvari i na osnovu odgovora kažemo šta je verovatan uzrok i u kom je rasponu cena. Ako je nešto što možete sami da rešite za pet minuta, reći ćemo vam i to.",
                 "Na licu mesta prvo utvrđujemo uzrok, pa tek onda radimo. Tačna cena se kaže pre početka i posle se ne menja. Ako se tokom rada pojavi nešto što menja obim posla, zaustavljamo se i dogovaramo, umesto da se razlika pojavi na kraju.",
                 "Imamo opremu za dijagnostiku — inspekcijsku kameru, termovizijsku kameru i opremu za detekciju curenja — i to je razlika u odnosu na rad „na slepo“. Umesto da se obija po vlažnoj fleci ili da se isti odvod čisti svaka tri meseca, prvo se vidi šta je uzrok."]),
          cls="sec")
    + sec(cards("Na šta se obavezujemo",
                [("", "Cena pre rada",
                  "Dogovorena cena se ne menja posle posla. Nema stavki koje se pojave na kraju.", ""),
                 ("", "Realan rok, ne obećanje",
                  "Kažemo kada realno možemo da stignemo za tu situaciju, umesto roka koji ne možemo uvek da ispunimo.", ""),
                 ("", "Račun i garancija",
                  "Račun za svaki posao i pisana garancija na izvedeni rad.", ""),
                 ("", "Čisto za sobom",
                  "Zaštita poda i okolnog prostora i čišćenje posle intervencije.", ""),
                 ("", "Bez nepotrebnih radova",
                  "Ako popravka ima smisla, nećemo predložiti zamenu. Ako nema, reći ćemo i zašto.", ""),
                 ("", "Rad i sa pravnim licima",
                  "Predračun, račun i mogućnost ugovora o redovnom održavanju.", "")],
                page=p),
          cls="sec sec-alt")
    + sec(brief([
        ("Ko smo", "[NAZIV FIRME], vodoinstalaterska služba registrovana u APR-u. PIB [PIB], matični broj [MB]."),
        ("Od kada", "Radimo od [GODINA]. godine na području Beograda."),
        ("Ko se javlja", "Na pozive se javlja [IME VLASNIKA], vlasnik — ne služba za zakazivanje."),
        ("Radno vreme", "Dežurstvo 0–24, svih sedam dana, i praznikom."),
        ("Baza", "[ADRESA], Beograd. Magacin i baza ekipa; rad je terenski."),
        ("Dokumenti", "Račun za svaki posao, pisana garancija na rad, rad sa pravnim licima preko računa."),
    ]), cls="sec sec-alt")
    + sec(prose("Ko vam se javlja kada pozovete",
                ["Na telefon se javlja [IME VLASNIKA], vlasnik firme i vodoinstalater — ne operater koji samo upisuje adresu. To je razlika koja se čuje u prvom minutu razgovora: umesto „poslaćemo nekoga“ dobijate konkretna pitanja i, na osnovu odgovora, procenu šta je verovatan uzrok i u kom je rasponu cena.",
                 "Praktična korist od toga je i da vam neko kaže kada <em>ne</em> treba da zovete majstora. Deo zapušenja u kuhinji rešava se čišćenjem sifona za petnaest minuta, i to ćemo vam reći, iako bi nam bilo isplativije da izađemo.",
                 "Posao radi ekipa, ali odgovornost za dogovorenu cenu i za rok ostaje na jednom čoveku, i on je dostupan i posle posla — zbog toga <a href=\"../garancija/\">garancija</a> ovde znači nešto konkretno, a ne rečenicu na sajtu."]),
          cls="sec")
    + sec(prose("Oprema kojom radimo",
                ["<strong>Mašine za odgušenje</strong> — za odvode u stanu i za duže trase i vertikale, sa različitim glavama prema vrsti čepa.",
                 "<strong>Inspekcijska kamera</strong> — za pregled kanalizacije i utvrđivanje uzroka ponovljenih zapušenja, sa snimkom koji ostaje kod vas.",
                 "<strong>Termovizijska kamera</strong> — za lociranje curenja na toploj vodi i na instalacijama grejanja, bez otvaranja zidova.",
                 "<strong>Oprema za detekciju curenja</strong> — akustično merenje i geofon za instalacije pod pritiskom i za ukopane vodove."]),
          cls="sec")
    + sec(faq_block(p["faq"]), cls="sec sec-alt")
    + sec(related(p, [("radovi", "Naši radovi"),
                      ("garancija", "Garancija i reklamacije"),
                      ("recenzije", "Utisci klijenata"),
                      ("cenovnik", "Cenovnik")]),
          cls="sec")
)
PAGES.append(p)


# ============================================================ RECENZIJE
p = {
    "slug": "recenzije",
    "title": "Utisci klijenata — vodoinstalater Beograd | [NAZIV FIRME]",
    "desc": "Šta kažu klijenti o našem radu: odgušenja, detekcija curenja i hitne intervencije u Beogradu. Utisci sa realnih izlazaka.",
    "h1": "Utisci klijenata",
    "crumbs": [H, ("recenzije", "Utisci klijenata")],
    "schema": "page",
    "robots": "noindex,follow",
}
p["body"] = (
    hero(p,
         "Reč klijenata",
         "Utisci klijenata",
         "Na ovoj strani skupljamo utiske sa realnih izlazaka. Ako ste radili sa nama, zahvalni smo na svakoj oceni — i na onoj koja nam kaže šta da popravimo.",
         ["Utisci sa realnih intervencija",
          "Ocene i na Google profilu",
          "Odgovaramo i na kritike",
          "Bez naručenih recenzija"],
         with_form=False)
    + sec(prose("Napomena pre objave",
                ["Ova strana je pripremljena za prave utiske klijenata. Dok se ne prikupe prve ocene, ovde stoji objašnjenje umesto izmišljenih recenzija — jer recenzija koja nije prava ne vredi ništa, ni vama ni nama.",
                 "Kada budete zadovoljni poslom, ocena na Google profilu nam najviše znači. Ako nešto nije bilo kako treba, javite nam direktno — bolje je da to rešimo nego da ostane neizgovoreno.",
                 "<strong>Napomena za vlasnika sajta:</strong> ovde se ubacuju pravi utisci sa imenom, delom grada i vrstom intervencije, i po potrebi dodaje <em>Review</em> i <em>AggregateRating</em> šema. Do tada strana stoji na <em>noindex</em>."]),
          cls="sec")
    + sec(related(p, [("o-nama", "O nama"),
                      ("vodoinstalaterske-usluge", "Sve usluge"),
                      ("cenovnik", "Cenovnik"),
                      ("kontakt", "Kontakt")]),
          cls="sec sec-alt")
)
PAGES.append(p)


# ============================================================ KONTAKT
p = {
    "slug": "kontakt",
    "title": "Kontakt — vodoinstalater Beograd 0–24 | [TELEFON]",
    "desc": "Pozovite [TELEFON] ili pošaljite opis i fotografiju kvara. Vodoinstalater u Beogradu, dežurstvo 0–24, procena pre dolaska.",
    "h1": "Kontakt",
    "crumbs": [H, ("kontakt", "Kontakt")],
    "schema": "page",
}
p["faq"] = [
    ("Kako najbrže da dobijem procenu?",
     "Pozovite i opišite šta se dešava, ili pošaljite fotografiju kroz formu ili na Viber. Fotografija je često dovoljna da se vidi o kom je tipu instalacije reč i da se kaže realan raspon cene."),
    ("Radite li vikendom i praznicima?",
     "Radimo, dežurni majstor je dostupan 0–24 svih sedam dana. Rad van radnog vremena se tarifira drugačije i to kažemo pre izlaska."),
    ("Dolazite li i van Beograda?",
     "Pokrivamo područje Beograda sa prigradskim opštinama. Za lokacije van tog područja pitajte — reći ćemo odmah da li možemo da izađemo."),
]
p["body"] = (
    hero(p,
         "Dostupni 0–24",
         "Kontakt",
         "Najbrže je telefonom. Ako vam je lakše, pošaljite opis i fotografiju kvara — javljamo se sa okvirnom cenom i terminom.",
         ["Telefon 0–24, svih sedam dana",
          "Viber i e-mail za fotografije",
          "Okvirna cena pre izlaska",
          "Rad sa fizičkim i pravnim licima"])
    + sec(f"""    <h2>Podaci za kontakt</h2>
    <div class="grid g3">
      <div class="card"><h3>Telefon</h3><p><a href="tel:{SITE['phone_href']}">{SITE['phone_display']}</a><br>Dostupno 0–24, svih sedam dana.</p></div>
      <div class="card"><h3>E-mail</h3><p><a href="mailto:{SITE['email']}">{SITE['email']}</a><br>Za ponude, predračune i fotografije kvara.</p></div>
      <div class="card"><h3>Adresa</h3><p>{SITE['address']}<br>Magacin i baza ekipa. Rad je terenski.</p></div>
      <div class="card"><h3>Radno vreme</h3><p>Redovne intervencije: svakog dana.<br>Hitne intervencije: 0–24, i vikendom i praznikom.</p></div>
      <div class="card"><h3>Područje rada</h3><p>Beograd sa prigradskim opštinama.<br><a href="../lokacije/">Spisak lokacija</a></p></div>
      <div class="card"><h3>Podaci firme</h3><p>{SITE['name']}<br>PIB: {SITE['pib']} · Matični broj: {SITE['mb']}</p></div>
    </div>""", cls="sec sec-alt")
    + sec(prose("Šta da napišete kada se javljate",
                ["<strong>Šta se dešava.</strong> Na primer: voda u sudoperi ne otiče, vraća se kroz slivnik u kupatilu, mokar zid u hodniku, bojler kaplje.",
                 "<strong>Gde.</strong> Deo grada i tip objekta — stan u zgradi, kuća, lokal. Za zgradu je korisno da kažete i sprat.",
                 "<strong>Od kada.</strong> Da li je počelo iznenada ili se pogoršavalo, i da li je neko već pokušavao da popravi.",
                 "<strong>Fotografija.</strong> Slika odvoda, mesta curenja ili tipke vodokotlića često skrati razgovor i omogući precizniju procenu."]),
          cls="sec")
    + sec(faq_block(p["faq"]), cls="sec sec-alt")
    + sec(chips("Lokacije koje pokrivamo", OPSTINE_CHIPS, p,
                last=("lokacije", "Sve lokacije →")),
          cls="sec")
)
PAGES.append(p)
