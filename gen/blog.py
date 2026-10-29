# -*- coding: utf-8 -*-
"""Saveti: hub + informativni tekstovi koji hvataju pitanja pre poziva."""

import prices
from blocks import hero, sec, prose, cards, steps, faq_block, related
from content1 import H

PAGES = []
B = ("blog", "Saveti")

ARTICLES = []


def article(slug, title, desc, h1, pill, lead, ticks, body, faq, published, teaser):
    p = {
        "slug": "blog/%s" % slug,
        "title": title,
        "desc": desc,
        "h1": h1,
        "crumbs": [H, B, ("blog/%s" % slug, h1)],
        "schema": "article",
        "published": published,
        "faq": faq,
    }
    MES = ("januara februara marta aprila maja juna jula avgusta "
           "septembra oktobra novembra decembra").split()
    g, m, d = published.split("-")
    datum = "%d. %s %s." % (int(d), MES[int(m) - 1], g)
    p["body"] = (
        hero(p, "%s · objavljeno %s" % (pill, datum), h1, lead, ticks, with_form=False)
        + body(p)
        + sec(faq_block(faq), cls="sec sec-alt")
        + sec(prose("Ko piše ove tekstove",
                    ["Tekst je napisao majstor koji i izlazi na teren — vodoinstalater sa "
                     "[ISKUSTVO] iskustva u zanatu, koji u Beogradu i prigradskim opštinama "
                     "radi odgušenja, detekciju curenja i hitne intervencije. Primeri u tekstu "
                     "su sa stvarnih izlazaka, a ne prepisani sa drugih sajtova.",
                     "Ako vam nešto iz teksta nije jasno ili situacija ne liči ni na jedan opisan "
                     "slučaj — pozovite <a href=\"../../kontakt/\">[TELEFON]</a> i opišite šta se "
                     "dešava. Odgovor na telefonu je besplatan i ne obavezuje vas ni na šta."]),
              cls="sec")
        + sec(related(p, [("odgusenje-kanalizacije-beograd", "Odgušenje"),
                          ("detekcija-curenja-vode-beograd", "Detekcija curenja"),
                          ("hitne-intervencije-beograd", "Hitne intervencije"),
                          ("cenovnik", "Cenovnik")]),
              cls="sec")
    )
    PAGES.append(p)
    ARTICLES.append((p["slug"], h1, teaser))


# ------------------------------------------------------------ 1
article(
    "zapusena-sudopera-sta-raditi",
    "Zapušena sudopera — šta uraditi pre poziva majstoru",
    "Šta zaista pomaže kod zapušene sudopere, šta samo pogorša stvar i kada ima smisla zvati vodoinstalatera. Praktično uputstvo korak po korak.",
    "Zapušena sudopera: šta uraditi pre nego što pozovete majstora",
    "Savet · 4 minuta čitanja",
    "Pola kuhinjskih zapušenja rešava se za petnaest minuta, bez alata i bez majstora. Druga polovina ne može i tu je važno znati kada prestati sa pokušajima.",
    ["Šta pomaže, a šta pogoršava",
     "Zašto hemija nije prvo rešenje",
     "Kada je u pitanju sifon, a kada vertikala",
     "Kako sprečiti da se ponovi"],
    lambda p: (
        sec(prose("Prvo proverite da li je problem samo kod vas",
                  ["Pre bilo čega, pustite vodu u drugim odvodima — u kupatilu, u kadi, u WC šolji. Ako sporo otiče samo sudopera, problem je skoro sigurno u sifonu ili u kratkoj deonici iza njega i verovatno možete sami.",
                   "Ako sporo otiče i negde drugde, ili se voda vraća kroz slivnik u kupatilu, onda je čep dalje — u zajedničkoj vertikali ili u horizontalnom vodu. Tu kućna sredstva nemaju efekta i jedino što ćete postići je da napunite vodom nešto što i tako ne otiče.",
                   "I treći znak: ako se kod komšija ispod ili iznad dešava isto, javite upravniku. Zajednička vertikala nije stvar jednog stana, ni tehnički ni po tome ko snosi trošak."]),
            cls="sec")
        + sec(steps("Šta možete da pokušate sami",
                    [("Vruća voda i deterdžent", "Litar vruće (ne ključale) vode sa sredstvom za sudove, u dva-tri navrata. Najbolje radi kod svežeg čepa od masnoće."),
                     ("Soda bikarbona i sirće", "Kašika sode u odvod, pa pola šolje sirćeta, pa posle petnaest minuta vruća voda. Ne pravi čudo, ali razgrađuje mekše naslage."),
                     ("Pumpica (putce)", "Napunite sudoperu sa malo vode, zatvorite preliv krpom i pumpajte sa nekoliko kratkih poteza. Zatvoren preliv je ono što najčešće fali."),
                     ("Čišćenje sifona", "Stavite lavor ispod, odvrnite sifon rukom, izvadite sadržaj i isperite. Kod većine kuhinjskih zapušenja čep je upravo tu.")],
                    intro="Redosled nije slučajan — ide se od najblažeg ka najdirektnijem."),
              cls="sec sec-alt")
        + sec(prose("Šta ne treba raditi",
                    ["<strong>Ne sipajte jaku hemiju u potpuno zapušen odvod.</strong> Ako voda uopšte ne prolazi, sredstvo ostaje da stoji u cevi. Ne rastvori čep, a kada majstor dođe i otvori sifon, iz njega izlazi agresivna tečnost. Hemija eventualno ima smisla kao preventiva, kada voda još otiče.",
                     "<strong>Ne kombinujte različita sredstva.</strong> Mešanje hemije na bazi kiseline i one na bazi baze daje reakciju i isparenja u zatvorenoj kuhinji.",
                     "<strong>Ne gurajte žicu nasumično.</strong> Improvizovana sajla ume da probije stariju plastičnu cev ili da probuši koleno, i tada od zapušenja dobijate curenje u plafonu komšije ispod.",
                     "<strong>Ne rasklapajte ono što ne znate da vratite.</strong> Ako sifon ne može rukom, nemojte ključem na silu — plastični navoj puca lako."]),
              cls="sec")
        + sec(prose("Kada pozvati majstora",
                    ["Kada voda uopšte ne prolazi posle čišćenja sifona. Kada se problem vratio u roku od nekoliko nedelja. Kada se voda vraća i u drugim odvodima ili kroz slivnik. I kada čujete grgljanje u drugim odvodima dok pušta voda — to znači da je čep dalje niz trasu.",
                     "Ako se isti odvod zapušava treći ili četvrti put, čišćenje više nije rešenje nego odlaganje. Tada ima smisla <a href=\"../../snimanje-kanalizacije-kamerom/\">snimanje kamerom</a>, jer se najčešće ispostavi da je cev suzila od naslaga ili da postoji oštećenje na spoju.",
                     "Okvirna cena <a href=\"../../odgusenje-sudopere-beograd/\">odgušenja sudopere</a> kreće se od 3.000 do 3.500 dinara, a mašinsko odgušenje od 3.500. Pun cenovnik je na <a href=\"../../cenovnik/\">stranici sa cenama</a>."]),
              cls="sec sec-alt")
        + sec(prose("Kako sprečiti sledeće zapušenje",
                    ["Masnoća je uzrok skoro svakog kuhinjskog čepa. Ne sipa se u sudoperu dok je tečna — hladi se u cevi i hvata ostatke hrane. Bolje je prebrisati tiganj papirnom salvetom pre pranja.",
                     "Rešetka na odvodu zaustavlja ostatke hrane i košta koliko i jedna kafa. Jednom nedeljno pustite litar vruće vode sa deterdžentom kroz odvod — to je dovoljno da se sveže naslage ne stegnu.",
                     "Za kafiće i restorane ovo nije dovoljno: tamo se isplati plansko čišćenje odvoda u dogovorenim razmacima, jer se trošak zatvorene kuhinje meri u satima, a ne u ceni intervencije."]),
              cls="sec")
    ),
    [("Pomaže li soda bikarbona zaista?",
      "Kod svežih i mekših naslaga od masnoće pomaže. Kod stvrdnutog čepa ili kod zapušenja dalje niz cev nema efekta — tada samo gubite vreme."),
     ("Da li je hemija za odgušenje opasna za cevi?",
      "Jaka sredstva na bazi kiseline mogu da oštete starije plastične i gumene delove, pre svega zaptivke u sifonu. Povremena upotreba kao preventiva je u redu, redovna nije."),
     ("Koliko košta odgušenje sudopere u Beogradu?",
      "Okvirno 3.000–3.500 dinara za standardnu intervenciju. Ako je potrebna mašina, od 3.500. Tačna cena se kaže na licu mesta pre početka rada."),
     ("Ko plaća odgušenje vertikale u zgradi?",
      "Vertikala je zajednički deo zgrade, pa je trošak po pravilu na stambenoj zajednici. Odluku donosi upravnik — zato ga odmah obavestite ako sumnjate na zajednički vod.")],
    "2026-01-18",
    "Pola kuhinjskih zapušenja rešava se bez majstora. Šta pomaže, šta pogorša stvar i kada prestati sa pokušajima.",
)


# ------------------------------------------------------------ 2
article(
    "kako-prepoznati-curenje-vode",
    "Kako prepoznati curenje vode u stanu — pet znakova",
    "Veliki račun, vlažan zid, buđ ili vodomer koji radi kada je sve zatvoreno. Pet pouzdanih znakova curenja i kako ga sami proveriti.",
    "Kako prepoznati curenje vode u stanu",
    "Savet · 5 minuta čitanja",
    "Curenje retko počne kao poplava. Najčešće se mesecima gubi voda koju plaćate, a prvi vidljivi znak dođe kada je šteta već napravljena.",
    ["Test vodomerom za pet minuta",
     "Pet znakova koje ne treba ignorisati",
     "Zašto fleka nije mesto curenja",
     "Šta uraditi pre nego što nekog zovete"],
    lambda p: (
        sec(prose("Najpouzdaniji test traje pet minuta",
                  ["Zatvorite sve slavine i isključite sve što troši vodu — veš mašinu, sudo mašinu, bojler ako se puni. Zatim pogledajte vodomer i zapamtite stanje, ili fotografišite brojčanik.",
                   "Sačekajte petnaest do trideset minuta bez trošenja vode i pogledajte ponovo. Ako se brojčanik pomerio, negde curi. Mnogi vodomeri imaju i mali crveni točkić koji registruje i vrlo mali protok — ako se on okreće, imate odgovor odmah.",
                   "Sledeći korak sužava zonu: zatvorite glavni ventil na ulazu u stan i ponovite proveru. Ako se vodomer i dalje pomera, curenje je pre stana — na priključku ili u zajedničkom delu. Ako stane, curenje je unutar stana."]),
            cls="sec")
        + sec(cards("Pet znakova curenja",
                    [("", "Račun veći bez promene navika",
                      "Najčešći prvi signal. Skok potrošnje bez objašnjenja znači da voda negde odlazi.", ""),
                     ("", "Vlažan zid, mrlja ili buđ",
                      "Posebno ako se vraća posle krečenja ili se širi sporo i stalno.", ""),
                     ("", "Topla tačka na podu",
                      "Kod curenja na toploj vodi ili podnom grejanju pod zna da bude primetno topliji na jednom mestu.", ""),
                     ("", "Pad pritiska",
                      "Slabiji mlaz nego ranije, naročito kada se istovremeno koristi više tačaka.", ""),
                     ("", "Zvuk vode kada je sve zatvoreno",
                      "Tiho šuštanje u zidu noću, kada je stan tih, čest je znak curenja pod pritiskom.", ""),
                     ("", "Miris vlage i hladan zid",
                      "Prostorija koja se teško zagreva i miriše na vlagu i kada je provetrena.", "")],
                    page=p),
              cls="sec sec-alt")
        + sec(prose("Zašto se ne otvara tamo gde je fleka",
                    ["Ovo je najskuplja greška u celoj priči. Voda ne izlazi tamo gde cev propušta — putuje niz cev, ispod estriha i kroz spojeve, i pojavi se tamo gde joj je najlakše. Mrlja u kupatilu može biti posledica curenja u hodniku.",
                     "Zbog toga se prvo meri. <a href=\"../../detekcija-curenja-vode-beograd/\">Detekcija curenja</a> koristi merenje pritiska po deonicama, termovizijsku kameru i akustičnu opremu da suzi zonu na metar ili manje. Tek onda se otvara, i to tačno tu.",
                     "Razlika u praksi: otvaranje po fleci znači obijenu prostoriju i neizvestan rezultat; otvaranje po nalazu znači jednu do dve pločice."]),
              cls="sec")
        + sec(prose("Šta uraditi pre nego što nekog zovete",
                    ["<strong>Uradite test vodomerom</strong> i zapišite rezultat. To je prvi podatak koji će vam svako tražiti.",
                     "<strong>Zabeležite kada se pojavilo</strong> i da li se pogoršava. Curenje koje raste i ono koje stoji isto ponašaju se različito.",
                     "<strong>Setite se skorašnjih radova.</strong> Bušenje zida, montaža police, postavljanje klime ili renoviranje kupatila su česti uzroci oštećenja cevi — i podatak koji odmah sužava traženje.",
                     "<strong>Fotografišite mrlju i okolinu.</strong> Fotografija često dovoljno govori da se telefonom kaže realan raspon cene i koja metoda dolazi u obzir."]),
              cls="sec sec-alt")
    ),
    [("Vodomer se okreće, a ništa ne curi vidljivo — šta sad?",
      "To je tipična slika skrivenog curenja u zidu, podu ili na ukopanom vodu. Sledeći korak je detekcija, jer bez merenja nema načina da se pogodi mesto."),
     ("Koliko košta detekcija curenja?",
      "Za jednu jasno ograničenu zonu okvirno 5.000–12.000 dinara, za složeniji razvod 10.000–18.000, a za ukopane dvorišne vodove 10.000–25.000."),
     ("Da li osiguranje pokriva štetu od curenja?",
      "Zavisi od polise i od toga šta je uzrok. Za prijavu je obično potreban nalaz o uzroku, pa je korisno da tražite pisani nalaz i fotografije sa merenja."),
     ("Curi mi od komšije iznad — šta mogu da uradim?",
      "Prvo obavestite komšiju i upravnika. Nezavisno merenje pomaže da se utvrdi odakle voda dolazi, a nalaz može da posluži kao osnova za dogovor o popravci i šteti.")],
    "2026-02-02",
    "Veliki račun, vlažan zid ili vodomer koji radi kada je sve zatvoreno — pet znakova i test koji traje pet minuta.",
)


# ------------------------------------------------------------ 3
article(
    "zasto-se-kanalizacija-stalno-zapusava",
    "Zašto se kanalizacija stalno zapušava — pet uzroka",
    "Ako se isti odvod zapušava treći put, uzrok nije u onome što ste bacili u njega. Pet pravih razloga i kako se svaki od njih utvrđuje.",
    "Zašto se kanalizacija stalno zapušava",
    "Savet · 5 minuta čitanja",
    "Jedno zapušenje je nezgoda. Treće na istom mestu u godinu dana je simptom — i tada ponovno čišćenje znači samo da ćete isti račun platiti još nekoliko puta.",
    ["Pet stvarnih uzroka ponavljanja",
     "Kada čišćenje gubi smisao",
     "Šta pokazuje pregled kamerom",
     "Šta se isplati uraditi odmah"],
    lambda p: (
        sec(cards("Pet razloga zašto se vraća",
                  [("", "Naslage su suzile cev",
                    "Posle decenija rada presek se smanji toliko da i sitnica pravi čep. Čišćenje vraća protok na kratko.", ""),
                   ("", "Pogrešan nagib odvoda",
                    "Premali ili obrnut pad znači da voda ne nosi sadržaj sa sobom. Čest kod objekata građenih u fazama.", ""),
                   ("", "Propao ili razdvojen spoj",
                    "Na mestu spoja se zadržava sve što prođe. Čišćenjem se oslobodi, pa se za mesec dana ponovi.", ""),
                   ("", "Ulegnuće cevi",
                    "Sleganje tla napravi udubljenje u kome voda stoji. Taloži se mulj i čep nastaje uvek na istom mestu.", ""),
                   ("", "Koren drveta",
                    "Kod kuća sa dvorištem koren ulazi kroz spoj i radi kao sito. Vraća se dok se ne sanira spoj.", ""),
                   ("", "Pogrešna upotreba",
                    "Vlažne maramice, mast i higijenski otpad. Jedini uzrok sa ove liste koji se rešava navikama.", "")],
                  page=p),
            cls="sec")
        + sec(prose("Kada čišćenje prestaje da bude rešenje",
                    ["Pravilo je jednostavno: ako se isti odvod zapušio tri puta u godinu dana, problem nije u sadržaju nego u cevi. Svako sledeće čišćenje tada kupuje nekoliko nedelja mira po punoj ceni.",
                     "U tom trenutku se isplati <a href=\"../../snimanje-kanalizacije-kamerom/\">pregled kamerom</a>. Košta otprilike kao dva odgušenja, a daje odgovor koji odgušenje ne može da da: koliki je stvarni presek, gde je oštećenje i da li uopšte ima smisla dalje čistiti.",
                     "Nalaz najčešće vodi u jednu od tri odluke — sanirati jedan spoj, zameniti kratku deonicu, ili prihvatiti da je cev dotrajala i planirati zamenu. Sve tri su jeftinije od serije intervencija bez kraja."]),
              cls="sec sec-alt")
        + sec(steps("Šta uraditi po redu",
                    [("Zapišite istoriju", "Kada se zapušilo, koliko puta, koji odvod i šta je rađeno. To je podatak koji usmerava traženje."),
                     ("Proverite da li je zajednički vod", "Ako se dešava i kod komšija ili se voda vraća kroz slivnik, u pitanju je vertikala i upravnik mora da zna."),
                     ("Uradite pregled kamerom", "Posle trećeg zapušenja ovo je jeftinija opcija od četvrtog čišćenja."),
                     ("Sanirajte uzrok, ne posledicu", "Spoj, deonica ili nagib — zahvat je najčešće manji nego što ljudi očekuju.")]),
              cls="sec")
    ),
    [("Koliko često je normalno čistiti kanalizaciju?",
      "U domaćinstvu — po potrebi, i to retko ako je instalacija zdrava. U ugostiteljstvu je planska pročistka u dogovorenim razmacima normalna praksa, jer je masnoća stalan priliv."),
     ("Koliko košta snimanje kanalizacije kamerom?",
      "Okvirno 6.000–8.000 dinara. Ako cev prvo mora da se očisti da bi se išta videlo, odgušenje se radi u istom izlasku i dogovara posebno."),
     ("Pomaže li hemija protiv ponovljenih zapušenja?",
      "Ne, ako je uzrok mehanički — suženje, ulegnuće, propao spoj ili koren. Hemija eventualno usporava stvaranje naslaga, ali ne menja geometriju cevi."),
     ("Ko snosi trošak kada je u pitanju vertikala?",
      "Zajednički vodovi su deo zgrade i trošak po pravilu ide na stambenu zajednicu. Za to je potrebno da upravnik bude uključen od početka.")],
    "2026-02-20",
    "Treće zapušenje na istom mestu nije nezgoda. Pet pravih uzroka i trenutak kada čišćenje prestaje da se isplati.",
)


# ------------------------------------------------------------ 4
article(
    "pukla-cev-sta-prvo-uraditi",
    "Pukla cev u stanu — šta uraditi u prvih pet minuta",
    "Redosled poteza kada voda ide, a majstor još nije stigao: gde je glavni ventil, šta sa strujom i kako smanjiti štetu kod komšija.",
    "Pukla cev u stanu: šta uraditi u prvih pet minuta",
    "Hitno · 3 minuta čitanja",
    "Kod izlivanja vode najveći deo štete nastane u prvih petnaest minuta. Ovih nekoliko poteza vredi znati pre nego što zatrebaju.",
    ["Gde je glavni ventil",
     "Kada i zašto isključiti struju",
     "Šta reći komšijama i upravniku",
     "Šta ne pokušavati sami"],
    lambda p: (
        sec(steps("Redosled poteza",
                  [("Zatvorite vodu", "Glavni ventil je najčešće u kupatilu iza revizionog otvora, u kuhinjskom elementu ispod sudopere ili u hodniku zgrade kod vodomera. Ako postoji samo ventil na celom stanu, zatvorite njega."),
                   ("Isključite struju u ugroženom delu", "Ako voda je blizu utičnica, bojlera ili razvodne kutije, isključite odgovarajući osigurač. Ne dirajte uređaje koji stoje u vodi."),
                   ("Obavestite komšije ispod", "Nekoliko minuta ranije upozorenje im omogući da sklone stvari. To direktno smanjuje i njihovu i vašu štetu."),
                   ("Smanjite štetu u stanu", "Sklonite stvari sa poda, podignite tepihe, stavite sud ispod mesta gde kaplje i fotografišite stanje pre nego što počnete da čistite."),
                   ("Pozovite majstora i recite konkretno", "Šta curi, odakle, da li ste uspeli da zatvorite vodu i na kom ste spratu. Na osnovu toga se procenjuje koliko je hitno i šta se nosi.")],
                  intro="Prvi potez je uvek zaustavljanje dotoka, ne traženje uzroka."),
            cls="sec")
        + sec(prose("Gde je glavni ventil — proverite danas, ne kad zatreba",
                    ["U većini beogradskih stanova ventil za stan je u kupatilu, iza revizionog otvora kod vodokotlića ili ispod kade. U starijim zgradama zna biti u hodniku, u zajedničkoj niši kod vodomera, a u kuhinjama se često nalazi dodatni ventil u elementu ispod sudopere.",
                     "Nađite ga sada, dok je mirno, i proverite da li se uopšte okreće. Ventili koji godinama stoje otvoreni zapeknu, i to se otkrije baš u trenutku kada treba da se zatvore. Ako ne ide rukom, ne lomite ga na silu — bolje ga zameniti u redovnom terminu nego u poplavi.",
                     "Ako živite u zgradi, vredi znati i gde je ventil za vertikalu i ko ima ključ od prostorije u kojoj se nalazi."]),
              cls="sec sec-alt")
        + sec(prose("Šta ne pokušavati",
                    ["<strong>Ne zatežite spoj koji curi dok je instalacija pod pritiskom.</strong> Kod starih cevi zatezanje često pretvori kapanje u mlaz.",
                     "<strong>Ne stavljajte improvizovane obujmice na pukotinu pod punim pritiskom.</strong> Ako već morate, prvo zatvorite vodu.",
                     "<strong>Ne uključujte bojler koji je ostao bez vode.</strong> Grejač u praznom kazanu pregori za nekoliko minuta.",
                     "<strong>Ne čekajte da „prestane samo“.</strong> Voda koja je ušla u pod i zidove pravi štetu i posle toga, i to je ono što na kraju košta više od same popravke."]),
              cls="sec")
    ),
    [("Ne mogu da nađem glavni ventil — šta onda?",
      "Pozovite i opišite stan i tip zgrade; kroz razgovor se najčešće može navesti gde se ventil obično nalazi. Ako ne može da se zatvori, to je razlog više da se izađe odmah."),
     ("Koliko košta hitna intervencija?",
      "Popravka pukle cevi kreće od 4.000 dinara. Za intervencije noću, vikendom i praznikom važi ista cena kao i radnim danom — bez doplate za hitnost i bez doplate za neradne dane."),
     ("Treba li zvati upravnika?",
      "Da, ako je u pitanju zajednički deo instalacije ili ako je voda prošla kod drugih stanara. Upravnik mora da zna i zbog evidencije štete."),
     ("Da li da fotografišem štetu?",
      "Obavezno, pre čišćenja. Fotografije i vreme nastanka su ono što traži i osiguranje i, ako do toga dođe, druga strana u sporu.")],
    "2026-03-05",
    "Najveći deo štete nastane u prvih petnaest minuta. Redosled poteza koji vredi znati unapred.",
)


# ------------------------------------------------------------ 5
article(
    "kako-izabrati-vodoinstalatera",
    "Kako izabrati vodoinstalatera u Beogradu — na šta paziti",
    "Šta pitati pre nego što majstor izađe, koji su znaci da nešto nije u redu i kako da izbegnete cenu koja naraste tek kad je posao gotov.",
    "Kako izabrati vodoinstalatera u Beogradu",
    "Savet · 4 minuta čitanja",
    "Santehničara se najčešće traži u panici, kad voda već ide — a to je najgori trenutak za biranje. Nekoliko pitanja na telefonu odvaja ozbiljnog majstora od onog kod koga cena naraste tek na kraju.",
    ["Četiri pitanja pre izlaska",
     "Znaci da nešto nije u redu",
     "Zašto cena mora da se kaže pre rada",
     "Šta tražiti posle posla"],
    lambda p: (
        sec(steps("Četiri pitanja koja vredi postaviti na telefonu",
                  [("Koliko okvirno košta?", "Ozbiljan majstor će na osnovu opisa dati raspon. Neće dati tačan iznos naslepo — to niko pošten ne može — ali će reći okvir. Odgovor „videćemo na licu mesta“ bez ikakvog broja je loš znak."),
                   ("Da li se izlazak naplaćuje ako odustanem?", "Treba da znate unapred. Normalna praksa je da se izlazak ne naplaćuje ako se radi intervencija, a da se naplaćuje dijagnostika ako posle pregleda odustanete — ali to mora da se kaže pre, ne posle."),
                   ("Izdajete li račun?", "Račun znači da firma postoji, da je registrovana i da imate čime da dokažete posao ako nešto krene po zlu. Bez računa nemate ni garanciju, ni osnov za reklamaciju."),
                   ("Dajete li garanciju i na šta tačno?", "Garancija na rad i garancija na ugrađeni materijal nisu isto. Pitajte koliko traje i šta pokriva, i tražite da piše na računu.")],
                  intro="Traje dva minuta i štedi najviše."),
            cls="sec")
        + sec(cards("Znaci da nešto nije u redu",
                    [("", "Cena se saznaje tek na kraju",
                      "Ako majstor počne rad bez dogovorene cene, iznos na kraju je njegova odluka, ne vaša.", ""),
                     ("", "Obećava tačno vreme dolaska",
                      "„Za trideset minuta“ zvuči dobro, ali niko ne zna stanje saobraćaja i koliko traje prethodna intervencija. Realan odgovor je pošteniji od brzog.", ""),
                     ("", "Odmah predlaže da se obija",
                      "Kod skrivenog curenja prvo se meri, pa se otvara. Obijanje po vlažnoj fleci je najskuplji način da se traži cev.", ""),
                     ("", "Nema račun ni firmu",
                      "Bez računa nema garancije. Kod veće štete to je razlika između reklamacije i izgubljenog novca.", ""),
                     ("", "Predlaže zamenu svega odmah",
                      "Ponekad je zamena stvarno jedino rešenje — ali to treba da bude objašnjeno, sa razlogom, a ne postavljeno kao jedina opcija.", ""),
                     ("", "Ne želi da pokaže šta je uradio",
                      "Posle posla je normalno da vam majstor pokaže šta je zatekao i šta je zamenio, i da ostavi stare delove ako tražite.", "")],
                    page=p),
              cls="sec sec-alt")
        + sec(prose("Zašto je cena pre rada ključna",
                    ["Vodoinstalaterski posao ima jednu neprijatnu osobinu: kada majstor već stoji u vašem kupatilu, a voda je zatvorena, pregovaračka pozicija više nije vaša. Zato se cena dogovara dok ste još u poziciji da kažete ne.",
                     "Ispravan redosled je jednostavan: opis telefonom i okvirni raspon, zatim pregled na licu mesta, zatim tačan iznos, i tek onda rad. Ako se tokom posla otkrije nešto što menja obim — recimo oštećena cev ispod čepa — normalno je da se majstor zaustavi, objasni i dogovori dalje, a ne da razliku saopšti na kraju.",
                     "Pitajte i da li se rad noću, vikendom i praznikom dodatno naplaćuje. Kod većine firmi se naplaćuje — kod nas ne, ali to je podatak koji treba da čujete pre izlaska, a ne posle posla."]),
              cls="sec")
        + sec(prose("Šta tražiti posle posla",
                    ["<strong>Račun sa popisom.</strong> Ne samo ukupan iznos, nego šta je rađeno i koji su delovi ugrađeni.",
                     "<strong>Garanciju u pisanoj formi.</strong> Usmena garancija ne postoji kada zatreba.",
                     "<strong>Objašnjenje uzroka.</strong> Dobar majstor će reći ne samo šta je popravio, nego i zašto se pokvarilo i šta da radite da se ne ponovi.",
                     "<strong>Snimak ili fotografije</strong>, ako je rađena dijagnostika kamerom ili detekcija. To je vaš dokument, koristan i kod upravnika i kod osiguranja."]),
              cls="sec sec-alt")
    ),
    [("Koliko košta izlazak vodoinstalatera u Beogradu?",
      "Zavisi od firme i od toga da li se radi intervencija. Kod nas se izlazak ne naplaćuje posebno ako radimo posao; ako posle pregleda odustanete, naplaćuje se izlazak i dijagnostika, i taj iznos kažemo unapred."),
     ("Kako da proverim da je firma registrovana?",
      "Tražite PIB i matični broj — oni se mogu proveriti u registru APR-a. Ozbiljna firma ih ima na sajtu i na računu."),
     ("Da li je skuplji majstor nužno bolji?",
      "Ne. Ali majstor koji unapred objasni cenu, rok i obim posla je po pravilu pouzdaniji od onog koji daje najnižu cifru na telefonu, a na licu mesta nađe razlog da je podigne."),
     ("Šta ako nisam zadovoljan urađenim poslom?",
      "Javite odmah, dok je situacija sveža. Sa računom i pisanom garancijom imate osnov za reklamaciju, i korektna firma će izaći ponovo bez dodatne naplate ako je propust njen.")],
    "2026-03-20",
    "Četiri pitanja na telefonu koja odvajaju ozbiljnog majstora od onog kod koga cena naraste na kraju.",
)


# ============================================================ HUB
p = {
    "slug": "blog",
    "title": "Saveti vodoinstalatera — Beograd | [NAZIV FIRME]",
    "desc": "Praktični saveti o zapušenjima, curenju vode i hitnim situacijama: šta možete sami, šta ne treba pokušavati i kada ima smisla zvati majstora.",
    "h1": "Saveti vodoinstalatera",
    "crumbs": [H, B],
    "schema": "page",
}
p["body"] = (
    hero(p,
         "Iz prakse, bez prodaje",
         "Saveti vodoinstalatera",
         "Tekstovi o stvarima koje najčešće objašnjavamo telefonom. Ako nešto možete sami, ovde piše kako — i gde je granica posle koje je bolje pozvati.",
         ["Šta možete sami, korak po korak",
          "Šta pogoršava situaciju",
          "Kada pozvati majstora",
          "Okvirne cene u tekstovima"],
         with_form=False)
    + sec(prose("Zašto ovo pišemo",
                ["Veliki deo poziva počinje istim pitanjima: da li mogu sam, šta da uradim dok čekam, koliko bi to otprilike koštalo. Umesto da to objašnjavamo iznova svakom ko pozove, napisali smo ovde — detaljnije nego što staje u jedan telefonski razgovor.",
                 "Tekstovi su iz prakse i pisani su pošteno. Gde posao možete da uradite sami, tako i piše, zajedno sa uputstvom. Gde ne možete, objašnjeno je zašto i šta se dešava ako se ipak pokuša — jer improvizovana popravka pod pritiskom ume da košta više od intervencije.",
                 "Ako vam je situacija hitna, nemojte čitati — <a href=\"../kontakt/\">pozovite</a>. Tekstovi su za trenutak kada imate vremena da razmislite."]),
          cls="sec")
    + sec(cards("Tekstovi", [(s, t, d, "") for s, t, d in ARTICLES], page=p, cls="g2"),
          cls="sec sec-alt")
    + sec(related(p, [("vodoinstalaterske-usluge", "Sve usluge"),
                      ("cenovnik", "Cenovnik"),
                      ("hitne-intervencije-beograd", "Hitne intervencije"),
                      ("kontakt", "Kontakt")]),
          cls="sec sec-alt")
)
PAGES.append(p)
