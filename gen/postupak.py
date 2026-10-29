# -*- coding: utf-8 -*-
"""Блок «Postupak rada» для страниц услуг.

Клиент просил, чтобы на каждой главной услуге было ясно описано, как именно
идёт работа. Порядок у каждой услуги свой — это не один шаблон с подменой слов.
"""

POSTUPAK = {
 "odgusenje-kanalizacije-beograd": (
  "Kako izgleda intervencija, korak po korak",
  "Redosled je uvek isti: prvo se utvrdi gde je čep, pa se bira metoda. Obrnuto se gubi vreme i novac.",
  [("Razgovor i okvirna cena",
    "Pitamo koji odvod ne radi, da li se voda vraća, da li je isto kod komšija i kada je počelo. Na osnovu toga kažemo šta je verovatan uzrok i u kom je rasponu cena."),
   ("Utvrđivanje gde je čep",
    "Na licu mesta puštamo vodu u više odvoda. Ako stoji samo jedan — problem je lokalan. Ako stoje svi ili se voda vraća kroz slivnik — čep je u zajedničkom vodu i radi se sa revizije."),
   ("Izbor metode",
    "Sajla za meke čepove i kraće trase, mašina sa odgovarajućom glavom za tvrdu naslagu i duže vodove. Metodu biramo prema nalazu, ne prema tome šta je nama brže."),
   ("Čišćenje i provera protoka",
    "Posle čišćenja puštamo vodu nekoliko minuta i gledamo kako otiče. Prostor zaštitimo pre rada i očistimo posle njega."),
   ("Šta dalje, ako se ponavlja",
    "Ako je to treći put na istom mestu, ne predlažemo još jedno čišćenje nego pregled kamerom — uzrok je tada u samoj cevi.")]),

 "odgusenje-wc-solje-beograd": (
  "Kako radimo",
  "Skidanje šolje je poslednja opcija, ne prva.",
  [("Provera šta je u pitanju",
    "Pitamo da li voda stoji u šolji, da li se vraća i da li je nešto upalo. Od toga zavisi da li se radi sajlom ili se mora do odvoda."),
   ("Rad kroz šolju",
    "Specijalna sajla za WC šolju prolazi kroz sifon bez oštećenja keramike. Ovim se rešava većina slučajeva."),
   ("Mašina, kada je čep dalje",
    "Ako je zapušenje iza šolje, u horizontalnom vodu ili vertikali, radi se mašinom sa najbližeg revizionog otvora."),
   ("Skidanje šolje — samo ako treba",
    "Kod predmeta koji ne može da se izvuče drugačije. To uvek kažemo i dogovorimo pre nego što počnemo, zajedno sa cenom.")]),

 "odgusenje-kade-i-tus-kabine": (
  "Kako radimo",
  "Kada ostaje na mestu — radi se kroz odvod, preliv ili rešetku slivnika.",
  [("Provera obima",
    "Puštamo vodu u lavabou i šolji. Ako i tamo stoji, čep nije u kadi nego na zajedničkom odvodu kupatila."),
   ("Čišćenje sifona i odvoda",
    "Kod kade kroz odvod i preliv, kod tuš-kabine kroz rešetku. Kosa i sapunska naslaga se izvlače, ne guraju dalje."),
   ("Tanja sajla za linijske kanalice",
    "Ravne tuš-kanalice imaju plitak sifon i duži put do odvoda, pa traže drugu opremu nego klasična kada."),
   ("Provera pada",
    "Ako voda i posle čišćenja stoji oko slivnika, merimo pad. To je drugi problem i rešava se prepravkom, a ne ponovnim čišćenjem.")]),

 "masinsko-odgusenje-kanalizacije": (
  "Kako radimo mašinom",
  "Mašina nije univerzalno rešenje — pogrešna glava u staroj cevi pravi štetu.",
  [("Procena cevi pre rada",
    "Gledamo materijal i starost instalacije. U staroj i tankoj cevi ne ide svaka glava i ne ide puna snaga."),
   ("Izbor glave i debljine sajle",
    "Za masnoću jedna glava, za koren druga, za naslagu kamenca treća. Debljina sajle bira se prema prečniku voda."),
   ("Prolaz do čepa i razbijanje",
    "Sajla se uvodi sa najbližeg revizionog otvora i vodi do mesta zastoja. Radi se postepeno, dok vod ne prođe celom dužinom."),
   ("Ispiranje i kontrola",
    "Posle proboja vod se ispira da naslaga ode dalje, a ne da se zaustavi nekoliko metara niže. Na zahtev radimo i kontrolni pregled kamerom.")]),

 "detekcija-curenja-vode-bez-razbijanja": (
  "Kako izgleda merenje",
  "Ništa se ne otvara dok se mesto ne obeleži.",
  [("Provera da curenje uopšte postoji",
    "Zatvaramo sve potrošače i gledamo vodomer. Ako se brojilo pomera, instalacija pod pritiskom negde propušta."),
   ("Suženje zone zatvaranjem ventila",
    "Mreža se deli na deonice. Zatvaranjem po redu utvrđujemo na kojoj grani pada pritisak."),
   ("Merenje na površini",
    "Termovizija za toplu vodu i podno grejanje, akustika za instalacije pod pritiskom. Metode se kombinuju da se isključi lažan nalaz."),
   ("Obeležavanje i nalaz",
    "Mesto se obeleži na zidu ili podu, uz objašnjenje šta je uzrok i koliko bi koštala sanacija. Otvara se tek posle toga.")]),

 "detekcija-curenja-vode-u-zemlji": (
  "Kako tražimo ukopano curenje",
  "Cilj je da se kopa jedan do dva kvadrata umesto celog rova.",
  [("Potvrda da je curenje spolja",
    "Zatvaramo glavni ventil na ulazu u objekat. Ako vodomer i dalje radi, gubitak je na ukopanom delu."),
   ("Deljenje trase na deonice",
    "Merimo pritisak po delovima da bismo suzili dužinu koju treba oslušnuti."),
   ("Akustično merenje i geofon",
    "Voda koja izlazi pod pritiskom pravi šum. Poređenjem jačine na više tačaka mesto se postepeno sužava."),
   ("Obeležavanje mesta za kopanje",
    "Tačka se obeleži na terenu. Tek tada se kopa — i samo tu.")]),

 "detekcija-geofonom-i-termovizijom": (
  "Kako biramo metodu",
  "Nijedna metoda sama po sebi nije dovoljna; nalaz se uvek potvrđuje drugom.",
  [("Šta je instalacija i šta curi",
    "Topla ili hladna voda, u zidu, podu ili zemlji. Od toga zavisi koja oprema uopšte ima smisla."),
   ("Termovizija kod tople vode",
    "Kamera pokazuje temperaturnu razliku na površini. Jaka je kod tople vode i podnog grejanja, slabija kod hladne."),
   ("Akustika i geofon kod pritiska",
    "Zvuk vode koja izlazi iz cevi. Radi i na hladnoj vodi i na ukopanim vodovima, gde termovizija nema šta da pokaže."),
   ("Unakrsna provera pre otvaranja",
    "Nalaz jedne metode potvrđujemo drugom ili merenjem pritiska. Topla zona može biti i ispravna cev grejanja — zato se ne otvara na osnovu jedne slike.")]),

 "snimanje-kanalizacije-kamerom": (
  "Kako ide pregled",
  "Kamera pokazuje uzrok, ali tek kada kroz cev ima šta da se vidi.",
  [("Priprema voda",
    "Kroz potpuno zapušenu cev kamera ne vidi ništa. Ako je vod začepljen, prvo se radi odgušenje, pa pregled — najčešće u istom izlasku."),
   ("Uvođenje kamere sa revizije",
    "Sonda ide kroz reviziju ili kroz odvod, u zavisnosti od toga šta je dostupno. Dubina se prati po dužini kabla."),
   ("Pregled i obeležavanje nalaza",
    "Na snimku se vidi stepen suženja, propali spojevi, pukotine, ulegnuća i prodor korena. Mesto nalaza se beleži po rastojanju od ulaza."),
   ("Objašnjenje i snimak",
    "Prolazimo kroz snimak zajedno sa vama i kažemo šta je opravdan sledeći korak. Snimak ostaje kod vas.")]),

 "hitne-intervencije-beograd": (
  "Kako ide hitan poziv",
  "Prvo zaustavljanje vode, pa traženje uzroka. Nikad obrnuto.",
  [("Razgovor dok ste još na vezi",
    "Pitamo šta curi i odakle, i vodimo vas kroz zatvaranje glavnog ventila i isključivanje struje u ugroženom delu. To radimo pre nego što uopšte krenemo."),
   ("Realan termin, ne okrugao broj",
    "Kažemo koliko nam stvarno treba za tu adresu i to doba dana. Radije ćemo reći dva sata i doći, nego pola sata i ne doći."),
   ("Zaustavljanje i procena na licu mesta",
    "Prvo se zaustavlja dotok, pa se utvrđuje uzrok. Tek onda govorimo o ceni — i počinjemo kada se složite."),
   ("Sanacija i dogovor o trajnom rešenju",
    "Hitna intervencija rešava ono što gori. Ako instalacija traži veći zahvat, to planiramo posebno, u mirnom terminu.")]),

 "servis-bojlera": (
  "Kako izgleda servis",
  "Servis nije samo skidanje kamenca — anoda i sigurnosni ventil su ono što produžava vek bojlera.",
  [("Pražnjenje i otvaranje",
    "Voda se isušti, bojler se otvori i izvadi grejač. Prostor ispod se zaštiti pre toga."),
   ("Čišćenje kamenca i provera grejača",
    "Sa grejača i iz kazana se uklanja naslaga, pa se meri ispravnost grejača i termostata."),
   ("Magnezijumska anoda",
    "Anoda je žrtvovani deo koji štiti kazan od korozije i troši se. Ako je potrošena, menja se — to je ono što odlaže kupovinu novog bojlera."),
   ("Sigurnosni ventil i kontrola",
    "Ventil se proverava i po potrebi menja, bojler se puni i prati se prvo zagrevanje pre nego što odemo.")]),

 "zamena-bojlera": (
  "Kako ide zamena",
  "Pun bojler od sto litara teži preko sto kilograma — nosač nije formalnost.",
  [("Pražnjenje i demontaža starog",
    "Voda se isušti, bojler skine i, ako tražite, odnese."),
   ("Provera nosača i priključaka",
    "Gleda se da li nosač u zidu odgovara težini novog uređaja i u kakvom su stanju priključci."),
   ("Montaža i nov sigurnosni ventil",
    "Novi bojler se postavlja i povezuje, sa novim ventilom — stari se ne prenosi, jer je on najčešći uzrok sledećeg kvara."),
   ("Punjenje i prvo zagrevanje",
    "Proveravamo curenje na spojevima i pratimo prvo zagrevanje. Ako električni priključak nije odgovarajući, kažemo to pre uključivanja.")]),

 "bojler-curi": (
  "Kako utvrđujemo odakle curi",
  "Razlika između ventila i probijenog kazana je razlika između 2.500 dinara i novog bojlera.",
  [("Isključenje i pregled spolja",
    "Bojler se isključi sa struje, zatvori dotok i posmatra odakle voda zaista izlazi — sa ventila, sa spoja ili iz tela."),
   ("Provera sigurnosnog ventila",
    "Par kapi pri zagrevanju je normalno. Stalno curenje znači da ventil ne zaptiva, i to je najjeftiniji kvar u ovoj grupi."),
   ("Otvaranje i pregled prirubnice",
    "Ako voda izlazi ispod poklopca, menja se zaptivka ili grejač. Radi se na licu mesta."),
   ("Iskrena procena kada ne vredi",
    "Ako voda izlazi iz samog kazana, popravka ne postoji — kazan se ne vari. Tada odmah kažemo da je u pitanju zamena.")]),

 "servis-vodokotlica-beograd": (
  "Kako radimo kroz revizioni otvor",
  "Fotografija tipke pre dolaska često odlučuje hoće li posao biti gotov iz prve.",
  [("Prepoznavanje sistema",
    "Po tipki se vidi proizvođač i generacija mehanizma. Ako nam pošaljete fotografiju unapred, ponesemo odgovarajuće delove."),
   ("Skidanje tipke i pregled",
    "Tipka se skida, kroz otvor se vidi plovak, zvono i ulivni ventil. Zid se ne dira."),
   ("Zamena dela koji je otkazao",
    "Najčešće plovak ili zvono. Delovi se menjaju kroz isti otvor, bez obijanja pločica."),
   ("Podešavanje i probno ispiranje",
    "Nivo vode se podesi, ispiranje se proveri nekoliko puta i tek onda vraćamo tipku.")]),

 "vodovodne-instalacije-i-popravke": (
  "Kako pristupamo poslu",
  "Prvo stanje cele grane, pa odluka — popravka ili zamena.",
  [("Pregled i procena stanja",
    "Gledamo materijal, starost i pritisak. Jedno oštećenje na zdravoj instalaciji je drugi posao nego isto oštećenje na zarasloj cevi."),
   ("Jasna ponuda pre rada",
    "Kažemo koliko košta popravka, koliko zamena i koliko realno može da izdrži postojeća instalacija. Odluku donosite vi."),
   ("Rad sa zatvorenom vodom",
    "Dogovaramo termin tako da voda bude zatvorena što kraće, a u zgradama se po potrebi javlja upravniku unapred."),
   ("Proba pod pritiskom",
    "Posle svakog zahvata instalacija se proverava pod pritiskom — pre nego što se bilo šta zatvori ili obloži.")]),

 "zamena-slavina-i-ventila": (
  "Kako ide zamena",
  "Najkraći posao u ponudi — ali sa dva mesta na kojima se najčešće greši.",
  [("Provera šta se stvarno kvari",
    "Kod slavine koja kaplje gleda se da li je dovoljna zaptivka ili kartuša, ili je baterija za zamenu."),
   ("Zatvaranje vode na pravom mestu",
    "Za većinu zamena dovoljan je ventil u stanu. Ako je zapekao, to je prvo što menjamo — i o tome vas obavestimo."),
   ("Demontaža bez lomljenja priključka",
    "Zarđali navoj se oslobađa postepeno. Sila na staroj cevi pravi veći kvar od onog zbog kog smo došli."),
   ("Ugradnja i provera pod pritiskom",
    "Novi deo se ugradi, voda pusti i spoj proveri. Ne odlazimo dok spoj ne odstoji pod punim pritiskom.")]),

 "popravka-i-zamena-vodovodnih-cevi": (
  "Kako odlučujemo i kako radimo",
  "Najskuplja greška je zameniti deonicu u instalaciji koju je trebalo menjati celu.",
  [("Procena stanja instalacije",
    "Merimo pritisak, gledamo materijal i pitamo koliko je puta puklo do sada. Tri podatka koja odlučuju popravka ili zamena."),
   ("Lociranje, ako mesto nije vidljivo",
    "Kod curenja u zidu ili podu prvo radimo detekciju. Otvaranje po vlažnoj fleci je najskuplji način traženja."),
   ("Ponuda po fazama",
    "Kažemo koja grana je najkritičnija i šta može da sačeka. Često je najpametnije raditi po fazama, a ne sve odjednom."),
   ("Zamena i obavezna proba",
    "Deonica se menja, instalacija proverava pod pritiskom i tek onda se zatvara zid ili pod.")]),

 "za-firme": (
  "Kako izgleda saradnja",
  "Za lokal nije bitna samo cena intervencije nego i to koliko sati kuhinja ne radi.",
  [("Obilazak i procena objekta",
    "Gledamo instalacije, dostupnost revizija i gde su uska grla. Za ugostitelje to je skoro uvek kuhinjski odvod i mastolov."),
   ("Plan održavanja i cene",
    "Pišemo predlog: koliko puta godišnje, šta ulazi i po kojoj ceni. Cenovnik intervencija fiksira se ugovorom, bez pregovaranja u hitnoj situaciji."),
   ("Rad van najprometnijeg dela dana",
    "Planska odgušenja radimo rano ujutru, kasno uveče ili neradnim danom — da lokal ne gubi promet."),
   ("Izveštaj i račun",
    "Posle svakog izlaska dobijate specifikaciju radova uz račun, po objektu i datumu — spremno za knjigovodstvo.")]),
}
