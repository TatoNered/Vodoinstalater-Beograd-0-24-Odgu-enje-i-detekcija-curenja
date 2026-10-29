# -*- coding: utf-8 -*-
"""Sadržaj: početna i klaster odgušenja."""

from render import SITE, depth_prefix
import prices
from blocks import (hero, sec, prose, cards, steps, price_table, faq_block,
                    works, chips, related, brief)
from render import quote_form

H = ("", "Početna")

OPSTINE_CHIPS = [
    ("lokacije/vodoinstalater-novi-beograd", "Novi Beograd"),
    ("lokacije/vodoinstalater-zemun", "Zemun"),
    ("lokacije/vodoinstalater-vozdovac", "Voždovac"),
    ("lokacije/vodoinstalater-zvezdara", "Zvezdara"),
    ("lokacije/vodoinstalater-palilula", "Palilula"),
    ("lokacije/vodoinstalater-cukarica", "Čukarica"),
    ("lokacije/vodoinstalater-rakovica", "Rakovica"),
    ("lokacije/vodoinstalater-vracar", "Vračar"),
    ("lokacije/vodoinstalater-stari-grad", "Stari grad"),
]

# Naselja sa svojom stranom. Ranije je na njih vodilo po 3–4 linka ukupno,
# pa stoje i u nizu lokacija na glavnim stranama usluga.
NASELJA_CHIPS = [
    ("lokacije/vodoinstalater-altina", "Altina"),
    ("lokacije/vodoinstalater-batajnica", "Batajnica"),
    ("lokacije/vodoinstalater-medakovic", "Medaković"),
    ("lokacije/vodoinstalater-banjica", "Banjica"),
    ("lokacije/vodoinstalater-vidikovac", "Vidikovac"),
    ("lokacije/vodoinstalater-miljakovac", "Miljakovac"),
    ("lokacije/vodoinstalater-zarkovo", "Žarkovo"),
    ("lokacije/vodoinstalater-banovo-brdo", "Banovo brdo"),
]

# Opštine + naselja u jednom nizu — za strane usluga.
SVE_CHIPS = OPSTINE_CHIPS + NASELJA_CHIPS

PAGES = []


# ============================================================ POČETNA
p = {
    "slug": "",
    "title": "Vodoinstalater Beograd 0–24 | Odgušenje i detekcija curenja",
    "desc": "Vodoinstalater u Beogradu za odgušenje kanalizacije, detekciju curenja vode i hitne intervencije 0–24. Cena se dogovara pre početka rada. Pozovite [TELEFON].",
    "h1": "Vodoinstalater Beograd — odgušenje, detekcija curenja i hitne intervencije",
    "crumbs": [H],
    "schema": "home",
}
p["faq"] = [
    ("Koliko brzo možete da izađete?",
     "Zavisi od dela grada i od toga koliko ekipa je trenutno na terenu. Kada pozovete, kažemo realno vreme za tu situaciju — ne obećavamo rok koji ne možemo da ispunimo."),
    ("Da li se dolazak naplaćuje posebno?",
     "Ne, ako radimo intervenciju. Ako posle pregleda odustanete od posla, naplaćuje se izlazak i dijagnostika, i taj iznos vam kažemo unapred."),
    ("Kada saznajem cenu?",
     "Okvirni raspon dobijate telefonom, na osnovu opisa ili fotografije. Tačan iznos kažemo na licu mesta, pre nego što počnemo. Posle toga se cena ne menja."),
    ("Radite li noću, vikendom i praznicima?",
     "Da, dežurni majstor je dostupan 0–24, svih sedam dana. Za intervencije noću, vikendom i praznikom važi ista cena kao i radnim danom — bez doplate za hitnost i bez doplate za neradne dane."),
    ("Izdajete li račun i garanciju?",
     "Da. Izdajemo račun i pisanu garanciju na izvedeni rad. Radimo i sa pravnim licima, po predračunu i uplati na račun."),
    ("Radite li za firme i stambene zajednice?",
     "Radimo. Kafići, restorani, lokali, poslovni prostori i stambene zajednice — po pozivu ili po ugovoru o redovnom održavanju."),
]
p["body"] = (
    hero(p,
         "Dežurni majstor dostupan 0–24",
         "Vodoinstalater Beograd — odgušenje, detekcija curenja i hitne intervencije",
         "Kažete šta se dešava, dobijate okvirnu cenu pre nego što izađemo. Radimo za domaćinstva, lokale i stambene zajednice, uz račun i garanciju.",
         ["Cena dogovorena pre početka rada",
          "Račun i pisana garancija",
          "Profesionalna oprema za dijagnostiku",
          "Radimo i preko računa, za pravna lica"],
         with_form=False)
    # Klijent je tražio da usluge i cene budu jasno izdvojene. Zato idu
    # odmah posle prvog ekrana, a forma za upit posle njih — na telefonu je
    # blok sa cenama ranije počinjao posle 2.300 px skrolovanja.
    + sec(cards("Dve usluge po kojima nas najčešće zovu",
                [("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije i odvoda",
                  "Sudopera, WC šolja, kada, tuš kabina, podni slivnik, vertikala i zajednička kanalizacija u zgradi. Mašinski, sajlom ili pod pritiskom.",
                  "od 3.000 RSD"),
                 ("detekcija-curenja-vode-beograd", "Detekcija curenja vode bez nepotrebnog razbijanja",
                  "Termovizijska kamera, geofon i akustična oprema. Lociramo mesto curenja pre nego što se išta obija.",
                  "od 5.000 RSD")],
                intro="Na ove dve grupe otpada najveći deo poziva, pa im je na sajtu posvećeno najviše prostora.",
                cls="g2", page=p),
          cls="sec")
    + sec(cards("Ostale vodoinstalaterske usluge",
                [("snimanje-kanalizacije-kamerom", "Snimanje kanalizacije kamerom",
                  "Inspekcija cevi kada se isto mesto zapuši više puta ili pre kupovine i renoviranja objekta.", "6.000–8.000 RSD"),
                 ("hitne-intervencije-beograd", "Hitne intervencije 0–24",
                  "Pukla cev, izlivanje vode, ventil koji ne zatvara, poplava u stanu ili podrumu.", "od 4.000 RSD"),
                 ("servis-vodokotlica-beograd", "Vodokotlići — ugradni i nadgradni",
                  "Servis mehanizma u zidu kroz revizioni otvor: plovak, zvono, ulivni i ispusni ventil.", "2.000–5.000 RSD"),
                 ("vodovodne-instalacije-i-popravke", "Vodovodne instalacije i popravke",
                  "Zamena ventila, slavina, creva i sifona, sanacija pukle cevi, nove instalacije i adaptacije.", "od 2.400 RSD"),
                 ("servis-bojlera", "Servis i zamena bojlera",
                  "Grejač, termostat, sigurnosni ventil, kamenac, curenje i montaža novog uređaja.", "3.000–6.000 RSD"),
                 ("sanitarije-i-kupatila", "Montaža i zamena sanitarija",
                  "Montaža i zamena WC šolje, lavaboa, sudopere, tuš kabine i kade, do kompletne adaptacije.", "od 2.500 RSD"),
                 ("popravka-pukle-cevi", "Pukla cev",
                  "Hitna popravka kada voda ide i ne može da se zaustavi — u zidu, podu ili u dvorištu.", "od 4.000 RSD"),
                 ("bojler-curi", "Bojler curi",
                  "Ventil, zaptivka, grejač ili probijen kazan. Prvo utvrđujemo uzrok, pa govorimo o ceni.", "od 2.500 RSD"),
                 ("renoviranje-kupatila", "Renoviranje kupatila",
                  "Vodoinstalaterski deo adaptacije: razvod, odvodi i sanitarija, uz pisanu ponudu pre početka.", "od 20.000 RSD")],
                intro="Svaka usluga ima svoju stranicu sa objašnjenjem postupka i okvirnim cenama.",
                page=p)
          + '\n    <p class="intro" style="margin:18px 0 0">Cene su okvirne i služe za orijentaciju. '
            'Tačan iznos saopštavamo pre početka rada. Ceo pregled je na stranici '
            '<a href="cenovnik/">Cenovnik vodoinstalaterskih usluga</a>.</p>',
          cls="sec")
    + sec(quote_form(p, "Procena pre dolaska",
                     "Opišite kvar ili pošaljite fotografiju — javljamo okvirnu cenu i kada možemo "
                     "da izađemo. Raspitivanje ne obavezuje ni na šta."),
          cls="sec sec-alt")
    + sec(steps("Kako izgleda saradnja",
                [("Opišete problem",
                  "Telefonom, porukom na Viberu ili fotografijom. Tri podatka su dovoljna: šta se dešava, od kada i o kakvom je objektu reč."),
                 ("Dobijate okvirnu cenu",
                  "Na osnovu opisa javljamo raspon i kažemo kada realno možemo da izađemo."),
                 ("Potvrda na licu mesta",
                  "Majstor pregleda instalaciju i saopštava tačan iznos. Rad počinje tek kada se složite."),
                 ("Rad, provera i garancija",
                  "Posle intervencije proveravamo protok, čistimo za sobom i izdajemo račun sa garancijom.")],
                intro="Raspitivanje je besplatno i ne obavezuje vas ni na šta."),
          cls="sec")
    + sec(brief([('Šta radimo', 'Odgušenje kanalizacije, detekcija curenja vode, hitne intervencije i vodoinstalaterski radovi.'), ('Gde', 'Beograd i prigradske opštine, bez razlike u ceni.'), ('Kada', 'Dežurstvo 0–24, svih sedam dana, i praznikom.'), ('Cena', 'Okvir telefonom, tačan iznos pre početka rada. Odgušenje od 3.000, detekcija od 5.000, popravka pukle cevi od 4.000 RSD.'), ('Dokument', 'Račun za svaki posao i pisana garancija na rad. Za pravna lica — preko računa.')]), cls="sec")
    + sec(works("Naši radovi sa terena",
                [("odgušenje vertikale, pre i posle", "Zemun, Altina · mart 2026",
                  "Voda se vraćala u prizemlje zgrade",
                  "Fekalna vertikala zapušena naslagama. Mašinsko odgušenje i kontrola kamerom posle intervencije."),
                 ("termovizijski snimak vlažnog zida", "Vračar · februar 2026",
                  "Vlažan zid bez vidljivog curenja",
                  "Termovizija je pokazala tačku na toploj cevi. Otvorena je površina 30×30 cm umesto celog zida."),
                 ("ugradni vodokotlić, revizioni otvor", "Novi Beograd, Blok 45 · januar 2026",
                  "Ugradni vodokotlić nije punio vodu",
                  "Zamena ulaznog ventila kroz revizioni otvor, bez obijanja pločica.")],
                intro="Fotografije su sa stvarnih intervencija. Adresu ne objavljujemo, samo naselje i mesec."),
          cls="sec sec-alt")
    + sec('<p class="intro" style="margin:0"><a href="radovi/"><strong>Pogledajte još radova sa terena →</strong></a></p>', cls="sec")
    + sec('    <h2>Ocene na Google profilu</h2>\n'
          '    <p class="intro">Najpouzdaniji utisak o majstoru su ocene ljudi koji su ga već zvali. '
          'Naše ocene i komentare možete pročitati na <a href="[GOOGLE PROFIL URL]" rel="noopener">'
          'Google poslovnom profilu</a>, a izbor stoji i na stranici '
          '<a href="recenzije/">utisci klijenata</a>.</p>\n'
          '    <p class="intro" style="margin-top:10px">Ne objavljujemo izmišljene recenzije i ne '
          'navodimo ocene koje se ne mogu proveriti. Ako ste radili sa nama, ocena na Google profilu '
          'nam najviše znači — i ona koja nam kaže šta da popravimo.</p>',
          cls="sec sec-alt")
    + sec(cards("Zašto nas ljudi preporučuju",
                [("", "Cena se dogovara pre rada",
                  "Okvir dobijate telefonom, tačan iznos pre početka. Posle toga se ne menja, a ako se obim posla promeni — zaustavljamo se i dogovaramo.", ""),
                 ("", "Realno vreme, ne obećanje",
                  "Kažemo kada stvarno možemo da stignemo za tu situaciju. Radije ćemo reći dva sata i doći, nego trideset minuta i ne doći.", ""),
                 ("", "Račun i pisana garancija",
                  "Registrovana firma, račun za svaki posao i garancija na rad u pisanoj formi — ne na reč.", ""),
                 ("", "Dijagnostika pre rušenja",
                  "Kamera i oprema za detekciju. Prvo se vidi uzrok, pa se otvara tačno tu — a ne po vlažnoj fleci.", ""),
                 ("blog/kako-izabrati-vodoinstalatera", "Kako izabrati majstora",
                  "Četiri pitanja koja vredi postaviti na telefonu — i znaci da nešto nije u redu.", "Pročitajte →"),
                 ("recenzije", "Utisci klijenata",
                  "Prave ocene sa realnih izlazaka. Bez naručenih recenzija.", "Pogledajte →")],
                intro="Najčešći razlog zbog kog nas zovu drugi put ili preporuče nekome — ne cena, nego to što nema iznenađenja.",
                page=p),
          cls="sec")
    + sec(chips("Radimo u celom Beogradu", SVE_CHIPS, p,
                intro="Na stranici svake opštine piše šta se u tom delu grada najčešće kvari i koje usluge tamo najviše radimo.",
                last=("lokacije", "Sve opštine i naselja →")),
          cls="sec")
    + sec(prose("Zašto je važno reagovati na vreme",
                ["Zapušenje i curenje retko nastaju preko noći. Pre potpunog začepljenja voda nedeljama otiče sporije, u cevima se čuje klokotanje, a iz slivnika se oseti miris. Što duže traje, naslaga je tvrđa i za uklanjanje je potrebno više vremena i jača oprema — pa je i intervencija skuplja.",
                 "Isto važi i za curenje. Vlažna fleka na zidu znači da voda negde izlazi već neko vreme. Osim računa za vodu, dugotrajno vlaženje oštećuje malter, pločice i susedne prostorije, a kod curenja na toploj vodi i greje konstrukciju oko cevi.",
                 "Zato prvo radimo dijagnostiku, pa tek onda popravku. Kamerom i termovizijom se utvrđuje gde je stvarni uzrok, umesto da se nagađa i obija na više mesta."]),
          cls="sec sec-alt")
    + sec(faq_block(p["faq"]), cls="sec")
)
PAGES.append(p)


# ============================================================ ODGUŠENJE — HUB
p = {
    "slug": "odgusenje-kanalizacije-beograd",
    "title": "Odgušenje kanalizacije Beograd — cena od 3.000 RSD | 0–24",
    "desc": "Odgušenje i otpušavanje kanalizacije u Beogradu: sudopera, WC šolja, kada, slivnik, vertikala. Mašinski ili pod pritiskom. Cena pre početka rada.",
    "h1": "Odgušenje kanalizacije u Beogradu",
    "crumbs": [H, ("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije")],
    "schema": "service",
    "service_type": "Odgušenje kanalizacije",
    "cene": ("odgusenje_sudopere", "odgusenje_wc", "odgusenje_kade", "odgusenje_slivnika", "masinsko_odgusenje", "odgusenje_vertikale", "odgusenje_spoljne", "odgusenje_pritisak"),
}
p["faq"] = [
    ("Koliko traje odgušenje?",
     "Standardno zapušenje u stanu rešava se najčešće za 30 do 90 minuta. Vertikala u zgradi i spoljni vodovi traju duže, ponekad i nekoliko sati."),
    ("Da li se lome pločice?",
     "Ne. Radimo kroz postojeće otvore — sifon, reviziju ili samu šolju. Obijanje dolazi u obzir samo ako je cev pukla, i o tome se prvo dogovaramo s vama."),
    ("Ko plaća odgušenje vertikale u zgradi?",
     "Vertikala je zajednička instalacija, pa trošak najčešće ide preko upravnika i stambene zajednice. Izdajemo račun na stambenu zajednicu ili na firmu."),
    ("Pomaže li hemija iz prodavnice?",
     "Kod blagog usporenja ponekad pomogne. Kod potpunog začepljenja ne rešava uzrok, a kod starih livenih cevi može da ubrza propadanje materijala."),
    ("Dajete li garanciju na odgušenje?",
     "Da, na izvedeni rad. Ako se isto mesto ponovo zapuši u garantnom roku, izlazimo bez dodatne naplate."),
    ("Radite li odgušenje u lokalima i restoranima?",
     "Radimo. Za ugostiteljske objekte radimo i preventivno čišćenje masnih vodova po dogovorenom rasporedu, da se zastoj ne desi u toku smene."),
]
p["body"] = (
    hero(p,
         "Odgušenja radimo 0–24",
         "Odgušenje kanalizacije u Beogradu",
         "Voda sporo otiče, vraća se u kadu ili se iz slivnika oseća miris — to je zapušenje koje neće proći samo od sebe. Dolazimo sa mašinom i kamerom i rešavamo uzrok, ne samo posledicu.",
         ["Sajla, visoki pritisak i inspekcijska kamera",
          "Cena potvrđena pre početka rada",
          "Stanovi, kuće, lokali i zgrade",
          "Račun i garancija na izvedeni rad"])
    + sec(brief([('Šta je', 'Mehaničko čišćenje zapušenog odvoda ili kanalizacionog voda, bez hemije i bez rušenja.'), ('Cena', 'Sudopera, šolja i kada 3.000–3.500 RSD. Mašinsko od 3.500. Vertikala u zgradi 6.000–8.000. Spoljna kanalizacija od 8.000.'), ('Koliko traje', 'Standardno zapušenje u stanu najčešće 30–60 minuta. Vertikala i spoljni vod duže.'), ('Uključeno', 'Dolazak, utvrđivanje uzroka, čišćenje, provera protoka i čišćenje za sobom.'), ('Kada ne pomaže', 'Ako se isti odvod zapuši treći put, uzrok je u cevi — tada se radi pregled kamerom.')]), cls="sec")
    + sec(prose("Kada je vreme da pozovete majstora",
                ["Zapušenje se skoro uvek najavi. Prvo voda otiče sporije nego ranije, pa se javi klokotanje u cevima kada pustite sudoperu ili pustite vodu u kadi. Zatim se pojavi neprijatan miris iz slivnika, a na kraju voda prestane da otiče ili počne da se vraća na drugom mestu u stanu.",
                 "Povratak vode na drugom mestu je važan znak: on znači da zapušenje nije u sifonu nego niže u sistemu, najčešće u horizontalnom vodu ili u vertikali. Tada kućna hemija i vakuum pumpa ne pomažu, a dalje puštanje vode samo povećava rizik od izlivanja.",
                 "Ako se isti odvod zapuši više puta u kratkom roku, problem najverovatnije nije u načinu korišćenja nego u samoj cevi — propali spoj, ulegnuće, naslage ili koren drveta kod spoljnih vodova. U tom slučaju ima smisla uraditi <a href=\"../snimanje-kanalizacije-kamerom/\">snimanje kanalizacije kamerom</a> i videti uzrok, umesto da se čisti svaka tri meseca."]),
          cls="sec")
    + sec(cards("Šta sve odgušujemo",
                [("odgusenje-sudopere-beograd", "Odgušenje sudopere",
                  "Kuhinjski odvod zapušen masnoćom i ostacima hrane. Najčešći poziv koji dobijamo.", "3.000–3.500 RSD"),
                 ("odgusenje-wc-solje-beograd", "Odgušenje WC šolje",
                  "Šolja, monoblok i odvod iza njih. Radimo bez skidanja šolje kada je to moguće.", "3.000–3.500 RSD"),
                 ("masinsko-odgusenje-kanalizacije", "Mašinsko odgušenje kanalizacije",
                  "Sajla na elektropogon za dublja i tvrđa zapušenja u horizontalnim vodovima.", "3.500–7.000 RSD"),
                 ("odgusenje-kade-i-tus-kabine", "Odgušenje kade i tuš-kabine",
                  "Odvod zapušen kosom i sapunom, sa čišćenjem sifona. Bez skidanja kade.", "3.000–3.500 RSD"),
                 ("odgusenje-lavaboa", "Odgušenje lavaboa",
                  "Sifon i odvod lavaboa u kupatilu — kosa slepljena sapunom.", "3.000–3.500 RSD"),
                 ("", "Odgušenje podnog slivnika",
                  "Slivnik u kupatilu, podrumu ili garaži, često pun mulja i sitnog otpada.", "od 3.000 RSD"),
                 ("", "Odgušenje vertikale",
                  "Zajednička vertikala u zgradi, sajlom ili pod pritiskom. Račun na stambenu zajednicu.", "6.000–8.000 RSD"),
                 ("", "Odgušenje spoljne kanalizacije",
                  "Dvorišni vodovi, šahte i vod do gradske kanalizacije ili septičke jame.", "od 10.000 RSD"),
                 ("", "Preventivno čišćenje cevi",
                  "Redovno održavanje za lokale, restorane i zgrade, po dogovorenom rasporedu.", "po dogovoru")],
                intro="Pokrivamo i unutrašnju i spoljnu kanalizaciju, u stanovima, kućama, lokalima i poslovnim objektima.",
                page=p),
          cls="sec sec-alt")
    + sec(cards("Tri metode i kada koju koristimo",
                [("", "Sajla na elektropogon",
                  "Mehanički probija zapušenje i skida naslagu sa zida cevi. Za sudopere, WC šolje, kade i kraće horizontalne vodove.", "3.500–7.000 RSD"),
                 ("", "Voda pod visokim pritiskom",
                  "Ispira masnoću i mulj po celom preseku cevi. Za vertikale, duže vodove i zapušenja koja se ponavljaju.", "od 10.000 RSD"),
                 ("", "Inspekcijska kamera",
                  "Kada treba videti uzrok: propali spoj, koren drveta, ulegnuta cev. Snimak ostaje kod vas.", "6.000–8.000 RSD")],
                intro="Metodu biramo prema tome gde je zapušenje i od čega je nastalo. Pogrešno izabrana metoda ili ne reši problem ili optereti staru cev.",
                page=p),
          cls="sec")
    + sec(steps('Kako izgleda intervencija, korak po korak',
                [('Razgovor i okvirna cena', 'Pitamo koji odvod ne radi, da li se voda vraća, da li je isto kod komšija i kada je počelo. Na osnovu toga kažemo šta je verovatan uzrok i u kom je rasponu cena.'), ('Utvrđivanje gde je čep', 'Na licu mesta puštamo vodu u više odvoda. Ako stoji samo jedan — problem je lokalan. Ako stoje svi ili se voda vraća kroz slivnik — čep je u zajedničkom vodu i radi se sa revizije.'), ('Izbor metode', 'Sajla za meke čepove i kraće trase, mašina sa odgovarajućom glavom za tvrdu naslagu i duže vodove. Metodu biramo prema nalazu, ne prema tome šta je nama brže.'), ('Čišćenje i provera protoka', 'Posle čišćenja puštamo vodu nekoliko minuta i gledamo kako otiče. Prostor zaštitimo pre rada i očistimo posle njega.'), ('Šta dalje, ako se ponavlja', 'Ako je to treći put na istom mestu, ne predlažemo još jedno čišćenje nego pregled kamerom — uzrok je tada u samoj cevi.')],
                intro='Redosled je uvek isti: prvo se utvrdi gde je čep, pa se bira metoda. Obrnuto se gubi vreme i novac.'),
          cls="sec")
    + sec(price_table("Cenovnik odgušenja",
                      [("Odgušenje WC šolje", "3.000–3.500"),
                       ("Odgušenje sudopere", "3.000–3.500"),
                       ("Odgušenje kade ili tuš kabine", "3.000–3.500"),
                       ("Odgušenje lavaboa i umivaonika", "3.000–3.500"),
                       ("Odgušenje podnog slivnika", "od 3.000"),
                       ("Mašinsko odgušenje kanalizacije", "3.500–7.000"),
                       ("Odgušenje vertikale sajlom", "6.000–8.000"),
                       ("Odgušenje pod visokim pritiskom", "od 10.000"),
                       ("Vod do gradske kanalizacije ili septičke jame", "od 10.000"),
                       ("Snimanje kanalizacije kamerom", "6.000–8.000")],
                      intro="Rasponi važe za teritoriju Beograda. Tačan iznos kažemo na licu mesta, pre nego što počnemo, i posle toga se ne menja.",
                      note_up="Nedostupna revizija, zapušenje dublje od desetak metara, tvrde naslage koje traže kombinaciju metoda, kao i izlazak noću ili praznikom.",
                      note_in="Dolazak i pregled instalacije kada radimo intervenciju, odgušenje odgovarajućom metodom, provera protoka posle rada i čišćenje prostora.",
                      caption="Okvirne cene odgušenja po vrsti intervencije"),
          cls="sec sec-alt", sid="cene")
    + sec(works("Odgušenja sa terena",
                [("mašina za odgušenje na terenu", "Zemun, Altina · mart 2026",
                  "Dvorišni vod zapušen posle kiše",
                  "Blato i lišće u slivniku, voda se vraćala u garažu. Ispiranje pod pritiskom."),
                 ("snimak cevi kamerom pre intervencije", "Galenika · februar 2026",
                  "Vertikala u zgradi, četiri stana",
                  "Naslage masti kroz ceo presek. Mašinsko odgušenje i kontrola kamerom."),
                 ("kuhinjski odvod posle čišćenja", "Vračar · februar 2026",
                  "Sudopera se punila svakog jutra",
                  "Naslaga masnoće u horizontalnom vodu iza sifona, čišćenje sajlom.")]),
          cls="sec")
    + sec(faq_block(p["faq"], "Česta pitanja o odgušenju"), cls="sec sec-alt")
    + sec(related(p, [("odgusenje-lavaboa", "Odgušenje lavaboa"),
                      ("odgusenje-kade-i-tus-kabine", "Kada i tuš-kabina"),
                      ("odgusenje-sudopere-beograd", "Odgušenje sudopere"),
                      ("odgusenje-wc-solje-beograd", "Odgušenje WC šolje"),
                      ("masinsko-odgusenje-kanalizacije", "Mašinsko odgušenje"),
                      ("snimanje-kanalizacije-kamerom", "Snimanje kamerom")])
          + "\n" + chips("Odgušenje po opštinama i naseljima", SVE_CHIPS, p,
                         last=("lokacije", "Sve lokacije →")),
          cls="sec")
)
PAGES.append(p)


# ============================================================ SUDOPERA
p = {
    "slug": "odgusenje-sudopere-beograd",
    "title": "Odgušenje sudopere Beograd — cena 3.000–3.500 RSD",
    "desc": "Otpušavanje sudopere u Beogradu: zapušen kuhinjski odvod, sifon i horizontalni vod. Dolazimo sa mašinom, cena se zna pre početka rada.",
    "h1": "Odgušenje sudopere u Beogradu",
    "crumbs": [H, ("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije"),
               ("odgusenje-sudopere-beograd", "Odgušenje sudopere")],
    "schema": "service",
    "service_type": "Odgušenje sudopere",
    "cene": ("odgusenje_sudopere",),
}
p["faq"] = [
    ("Zašto se sudopera stalno zapušava?",
     "Najčešće zbog masnoće. Ona se u cevi hladi, lepi za zidove i vremenom sužava presek, pa se za nju hvataju ostaci hrane i talog od deterdženta. Ako se to ponavlja, vredi proveriti i nagib cevi i stanje horizontalnog voda."),
    ("Može li da se reši hemijom iz prodavnice?",
     "Kod blagog usporenja ponekad pomaže. Kada voda uopšte ne otiče, hemija najčešće samo stoji u cevi i ne rastvara stvrdnutu naslagu, a kod starih cevi može da napravi dodatnu štetu."),
    ("Treba li da se skida sifon?",
     "Ne uvek. Ako je zapušenje u sifonu, čistimo ga i vraćamo nazad. Ako je dublje u zidu, idemo sajlom kroz odvod, bez demontaže kuhinjskog elementa."),
    ("Šta ako je zapušena i sudopera i WC šolja?",
     "To obično znači da zapušenje nije u pojedinačnom odvodu nego niže, u vertikali ili horizontalnom vodu. Tada je potrebno odgušenje vertikale, a ne čišćenje pojedinačnog sifona."),
]
p["body"] = (
    hero(p,
         "Najčešći poziv koji dobijamo",
         "Odgušenje sudopere u Beogradu",
         "Voda u sudoperi stoji, sporo otiče ili se vraća nazad. Najčešći uzrok je naslaga masnoće u odvodu iza sifona. Rešavamo mašinski, bez demontaže kuhinje.",
         ["Dolazimo sa sajlom na elektropogon",
          "Bez obijanja i bez rušenja elemenata",
          "Cena 3.000–3.500 RSD za standardno zapušenje",
          "Račun i garancija"])
    + sec(prose("Kako prepoznati gde je zapušenje",
                ["Ako voda otiče sporo samo u sudoperi, a ostali odvodi u stanu rade normalno, zapušenje je skoro sigurno u sifonu ili u kratkom vodu odmah iza njega. To je najlakši slučaj i najčešće se rešava za pola sata.",
                 "Ako se uz sudoperu usporio i odvod u kupatilu, ili se voda pri puštanju sudopere pojavljuje u podnom slivniku, zapušenje je dublje — u horizontalnom vodu ili u zajedničkoj vertikali. Tada čišćenje sifona ne pomaže i potrebno je <a href=\"../masinsko-odgusenje-kanalizacije/\">mašinsko odgušenje</a>.",
                 "Treći slučaj je sudopera koja se zapuši svakih nekoliko meseci. Tu obično nije reč o lošoj navici nego o samoj cevi: premali nagib, propali spoj ili stara cev sa hrapavim zidovima za koje se naslaga hvata brže. U takvoj situaciji predlažemo pregled kamerom pre nego što se ponovo plaća čišćenje."]),
          cls="sec")
    + sec(steps("Kako izgleda intervencija",
                [("Pregled i procena", "Majstor proverava sifon, odvod i ostale tačke u stanu da utvrdi dokle seže zapušenje."),
                 ("Dogovor o ceni", "Saopštavamo tačan iznos pre nego što se bilo šta otvara."),
                 ("Čišćenje odvoda", "Sifon se rastavlja i pere ili se ide sajlom kroz odvod, u zavisnosti od nalaza."),
                 ("Provera i čišćenje", "Puštamo vodu i proveravamo protok, a radno mesto ostavljamo uredno.")]),
          cls="sec sec-alt")
    + sec(price_table("Cena odgušenja sudopere",
                      [("Odgušenje sudopere — standardno zapušenje", "3.000–3.500"),
                       ("Čišćenje i zamena sifona", "od 2.500"),
                       ("Mašinsko odgušenje kuhinjskog voda", "3.500–7.000"),
                       ("Odgušenje kuhinjske vertikale", "6.000–8.000"),
                       ("Snimanje odvoda kamerom", "6.000–8.000")],
                      note_up="Teško dostupan sifon iza ugradnih elemenata i zapušenje dublje od nekoliko metara.",
                      note_in="Dolazak i pregled, čišćenje odgovarajućom metodom, provera protoka i uredno radno mesto."),
          cls="sec", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja o zapušenoj sudoperi"), cls="sec sec-alt")
    + sec(related(p, [("odgusenje-lavaboa", "Odgušenje lavaboa"),
                      ("odgusenje-kade-i-tus-kabine", "Odgušenje kade i tuš kabine"),
                      ("odgusenje-wc-solje-beograd", "Odgušenje WC šolje"),
                      ("snimanje-kanalizacije-kamerom", "Snimanje kamerom")]),
          cls="sec")
)
PAGES.append(p)


# ============================================================ WC ŠOLJA
p = {
    "slug": "odgusenje-wc-solje-beograd",
    "title": "Odgušenje WC šolje Beograd — cena 3.000–3.500 RSD | 0–24",
    "desc": "Otpušavanje WC šolje u Beogradu bez skidanja šolje kad god je moguće. Dežurni majstor 0–24, cena poznata pre početka rada.",
    "h1": "Odgušenje WC šolje u Beogradu",
    "crumbs": [H, ("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije"),
               ("odgusenje-wc-solje-beograd", "Odgušenje WC šolje")],
    "schema": "service",
    "service_type": "Odgušenje WC šolje",
    "cene": ("odgusenje_wc",),
}
p["faq"] = [
    ("Da li morate da skidate šolju?",
     "U većini slučajeva ne. Prvo se ide sajlom kroz samu šolju. Skidanje dolazi u obzir samo kada je u odvodu predmet koji ne može da se izvuče drugačije, i o tome vas pitamo pre nego što počnemo."),
    ("Šta najčešće zapuši WC šolju?",
     "Vlažne maramice, higijenski ulošci, krpe i veće količine toalet-papira. Vlažne maramice su najčešći uzrok, jer se ne razgrađuju u vodi, nego se skupljaju u čvor na prvom suženju."),
    ("Voda se diže i polako otiče — je li hitno?",
     "Nije još uvek, ali nemojte dalje puštati vodu i nemojte koristiti vakuum pumpu na silu. Ako se nivo diže pri svakom ispiranju, zapušenje raste i izlivanje je pitanje vremena."),
    ("Zapušena je i šolja i kada — šta to znači?",
     "Da je problem niže u sistemu, u horizontalnom vodu ili vertikali. Tada se ne čisti pojedinačni odvod nego vertikala, a to je drugačija intervencija i druga cena."),
]
p["body"] = (
    hero(p,
         "Dežurni majstor 0–24",
         "Odgušenje WC šolje u Beogradu",
         "Voda se diže pri ispiranju ili uopšte ne otiče. Dolazimo sa opremom za odgušenje i rešavamo problem kroz samu šolju, bez demontaže kad god je to moguće.",
         ["Bez skidanja šolje u većini slučajeva",
          "Radimo i noću, vikendom i praznikom",
          "Cena 3.000–3.500 RSD za standardno zapušenje",
          "Čisto radno mesto posle intervencije"])
    + sec(prose("Šta uraditi pre nego što stignemo",
                ["Prestanite da puštate vodu. Svako novo ispiranje podiže nivo i povećava rizik da se voda prelije na pod, a to od sitnog problema pravi veliku štetu, naročito u stanu iznad prizemlja.",
                 "Ne sipajte hemiju za odgušenje u šolju u kojoj već stoji voda. Ona neće stići do zapušenja, a majstor posle radi u agresivnoj tečnosti koja može da prska.",
                 "Ako imate vakuum pumpu, probajte je najviše nekoliko puta i bez velike sile. Kada je u odvodu maramica ili krpa, pumpa je samo gura dublje i otežava vađenje."]),
          cls="sec")
    + sec(cards("Šta tačno radimo",
                [("", "Odgušenje šolje sajlom",
                  "Sajla se uvodi kroz šolju i probija zapušenje u kolenu ili prvom delu odvoda.", "3.000–3.500 RSD"),
                 ("", "Odgušenje monobloka",
                  "Kada je zapušen ugradni ili nadgradni monoblok zajedno sa šoljom.", "od 3.000 RSD"),
                 ("", "Demontaža i vraćanje šolje",
                  "Samo kada je predmet u odvodu i ne može da se izvuče na drugi način.", "po proceni")],
                page=p),
          cls="sec sec-alt")
    + sec(steps('Kako radimo',
                [('Provera šta je u pitanju', 'Pitamo da li voda stoji u šolji, da li se vraća i da li je nešto upalo. Od toga zavisi da li se radi sajlom ili se mora do odvoda.'), ('Rad kroz šolju', 'Specijalna sajla za WC šolju prolazi kroz sifon bez oštećenja keramike. Ovim se rešava većina slučajeva.'), ('Mašina, kada je čep dalje', 'Ako je zapušenje iza šolje, u horizontalnom vodu ili vertikali, radi se mašinom sa najbližeg revizionog otvora.'), ('Skidanje šolje — samo ako treba', 'Kod predmeta koji ne može da se izvuče drugačije. To uvek kažemo i dogovorimo pre nego što počnemo, zajedno sa cenom.')],
                intro='Skidanje šolje je poslednja opcija, ne prva.'),
          cls="sec")
    + sec(price_table("Cena odgušenja WC šolje",
                      [("Odgušenje WC šolje", "3.000–3.500"),
                       ("Odgušenje monobloka", "od 3.000"),
                       ("Mašinsko odgušenje odvoda iza šolje", "3.500–7.000"),
                       ("Odgušenje fekalne vertikale", "6.000–8.000"),
                       ("Hitna intervencija, u svako doba", "od 4.000")],
                      note_up="Predmet u odvodu koji traži demontažu šolje, zapušenje u vertikali i noćni ili praznični izlazak.",
                      note_in="Dolazak i pregled, odgušenje, provera ispiranja i čišćenje prostora posle rada."),
          cls="sec", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja o zapušenoj WC šolji"), cls="sec sec-alt")
    + sec(related(p, [("servis-vodokotlica-beograd", "Vodokotlići — ugradni i nadgradni"),
                      ("odgusenje-kade-i-tus-kabine", "Odgušenje kade i tuš kabine"),
                      ("masinsko-odgusenje-kanalizacije", "Mašinsko odgušenje"),
                      ("hitne-intervencije-beograd", "Hitne intervencije")]),
          cls="sec")
)
PAGES.append(p)


# ============================================================ MAŠINSKO
p = {
    "slug": "masinsko-odgusenje-kanalizacije",
    "title": "Mašinsko odgušenje kanalizacije Beograd — 3.500–7.000 RSD",
    "desc": "Mašinsko odgušenje kanalizacije u Beogradu sajlom na elektropogon. Za tvrda zapušenja, vertikale i duže vodove. Cena se dogovara pre rada.",
    "h1": "Mašinsko odgušenje kanalizacije",
    "crumbs": [H, ("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije"),
               ("masinsko-odgusenje-kanalizacije", "Mašinsko odgušenje")],
    "schema": "service",
    "service_type": "Mašinsko odgušenje kanalizacije",
    "cene": ("masinsko_odgusenje",),
}
p["faq"] = [
    ("Po čemu se mašinsko odgušenje razlikuje od ručnog?",
     "Ručna sajla probija zapušenje i vraća protok, ali ostavlja naslagu na zidovima cevi. Sajla na elektropogon sa odgovarajućom glavom struže naslagu i vraća cevi pun presek, pa se zapušenje ne vraća tako brzo."),
    ("Može li mašina da ošteti staru cev?",
     "Kod ispravno izabrane glave i brzine ne može. Zato pre rada proveravamo materijal i stanje cevi — kod starih livenih i azbestnih vodova koristimo blaži pristup ili predlažemo ispiranje pod pritiskom."),
    ("Kada je potreban visoki pritisak umesto sajle?",
     "Kada je zapušenje od masnoće i mulja po celoj dužini voda, a ne jedan čep. Visoki pritisak ispira ceo presek i koristi se kod vertikala, dužih horizontalnih vodova i spoljne kanalizacije."),
    ("Da li posle odgušenja proveravate rezultat?",
     "Da. Puštamo vodu i pratimo protok, a kod ponovljenih zapušenja predlažemo i kontrolu kamerom da se vidi da li je uzrok uklonjen ili postoji oštećenje cevi."),
]
p["body"] = (
    hero(p,
         "Oprema za tvrda zapušenja",
         "Mašinsko odgušenje kanalizacije u Beogradu",
         "Kada sajla iz kućne radinosti i hemija ne pomažu, potrebna je mašina. Sajla na elektropogon skida naslagu sa zidova cevi i vraća pun presek, a ne samo probija prolaz.",
         ["Sajla na elektropogon sa izmenjivim glavama",
          "Opcija ispiranja pod visokim pritiskom",
          "Kontrola rezultata posle intervencije",
          "Radimo u stanovima, kućama, lokalima i zgradama"])
    + sec(prose("Kada ima smisla mašinsko odgušenje",
                ["Mašina je potrebna kada zapušenje nije u sifonu nego dublje u instalaciji, kada je naslaga stvrdnuta i kada se isto mesto zapušava više puta. To su situacije u kojima probijanje prolaza traje kratko, a problem se vrati za nekoliko nedelja.",
                 "Najčešći slučajevi su kuhinjski vodovi sa naslagom masnoće, fekalne vertikale u starijim zgradama i horizontalni vodovi u podrumima. Kod njih je cilj da se vrati pun presek cevi, jer samo tako prestaje ciklus ponovnog zapušavanja.",
                 "Ako se posle mašinskog čišćenja problem i dalje vraća, uzrok je najčešće mehanički: ulegnuta cev, propali spoj, koren drveta ili pogrešan nagib. To se ne rešava čišćenjem nego popravkom, a vidi se <a href=\"../snimanje-kanalizacije-kamerom/\">pregledom kamerom</a>."]),
          cls="sec")
    + sec(cards("Metode koje koristimo",
                [("", "Sajla na elektropogon",
                  "Osnovna metoda za unutrašnje vodove. Glava se bira prema prečniku cevi i vrsti naslage.", "3.500–7.000 RSD"),
                 ("", "Ispiranje pod visokim pritiskom",
                  "Za masnoću i mulj po celoj dužini voda, vertikale i spoljnu kanalizaciju.", "od 10.000 RSD"),
                 ("", "Kontrola kamerom",
                  "Posle čišćenja ili kod ponovljenih zapušenja, da se utvrdi stvarni uzrok.", "6.000–8.000 RSD")],
                page=p),
          cls="sec sec-alt")
    + sec(steps('Kako radimo mašinom',
                [('Procena cevi pre rada', 'Gledamo materijal i starost instalacije. U staroj i tankoj cevi ne ide svaka glava i ne ide puna snaga.'), ('Izbor glave i debljine sajle', 'Za masnoću jedna glava, za koren druga, za naslagu kamenca treća. Debljina sajle bira se prema prečniku voda.'), ('Prolaz do čepa i razbijanje', 'Sajla se uvodi sa najbližeg revizionog otvora i vodi do mesta zastoja. Radi se postepeno, dok vod ne prođe celom dužinom.'), ('Ispiranje i kontrola', 'Posle proboja vod se ispira da naslaga ode dalje, a ne da se zaustavi nekoliko metara niže. Na zahtev radimo i kontrolni pregled kamerom.')],
                intro='Mašina nije univerzalno rešenje — pogrešna glava u staroj cevi pravi štetu.'),
          cls="sec")
    + sec(price_table("Cena mašinskog odgušenja",
                      [("Mašinsko odgušenje kanalizacije", "3.500–7.000"),
                       ("Mašinsko odgušenje sudopere", "od 3.500"),
                       ("Mašinsko odgušenje WC šolje", "od 3.500"),
                       ("Odgušenje vertikale sajlom na elektropogon", "6.000–8.000"),
                       ("Odgušenje pod visokim pritiskom", "od 10.000"),
                       ("Vod do gradske kanalizacije ili septičke jame", "od 10.000")],
                      note_up="Dužina voda preko desetak metara, nepristupačna revizija i kombinacija više metoda.",
                      note_in="Dolazak, pregled instalacije, odgušenje mašinom, provera protoka i čišćenje radnog mesta."),
          cls="sec", sid="cene")
    + sec(faq_block(p["faq"], "Česta pitanja o mašinskom odgušenju"), cls="sec sec-alt")
    + sec(related(p, [("snimanje-kanalizacije-kamerom", "Snimanje kamerom"),
                      ("odgusenje-lavaboa", "Odgušenje lavaboa"),
                      ("odgusenje-sudopere-beograd", "Odgušenje sudopere"),
                      ("hitne-intervencije-beograd", "Hitne intervencije")]),
          cls="sec")
)
PAGES.append(p)
