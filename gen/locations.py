# -*- coding: utf-8 -*-
"""Lokacijske stranice: hub + stranica po beogradskoj opštini."""

from blocks import hero, sec, prose, cards, price_table, faq_block, chips, related
from content1 import H

PAGES = []

# ime, slug, lokativ, naselja, karakter izgradnje, tipični problemi, susedi
OPSTINE = [
    dict(
        ime="Novi Beograd", slug="novi-beograd", profil="blok", lok="na Novom Beogradu",
        naselja="Blokovi 19–70, Bežanijska kosa, Fontana, Ledine, Studentski grad, Belville, Savada",
        karakter=(
            "Novi Beograd je grad vertikala. Blokovska izgradnja od šezdesetih do osamdesetih znači "
            "dugačke zajedničke vertikale na koje je vezano i po deset stanova, pa se zapušenje retko "
            "tiče samo jednog domaćinstva — ako se voda vraća u prizemlju, uzrok je skoro uvek niže od "
            "stana koji je prijavio problem."),
        karakter2=(
            "Uz to postoji i druga, sasvim drugačija grupa objekata: novogradnja iz poslednjih dvadeset "
            "godina, sa ugradnim vodokotlićima, ravnim odvodima u tuš kabinama i razvodom u podu. Tamo "
            "se najčešće ne traži odgušenje nego servis mehanizma u zidu i detekcija curenja ispod estriha."),
        problemi=[
            ("Zapušena vertikala u bloku", "Voda se vraća u nižim stanovima, a čep je u zajedničkom vodu — rešava se sa revizije, ne iz stana."),
            ("Ugradni vodokotlići u novogradnji", "Mehanizam u zidu, servis kroz revizioni otvor bez obijanja pločica."),
            ("Curenje u podu i estrihu", "Razvod u podu kod novijih stanova — termovizija i akustika umesto nasumičnog otvaranja."),
        ],
        susedi=["zemun", "cukarica", "surcin"],
        extra_faq=[
            ("Radite li u blokovima na Novom Beogradu?",
             "Radimo u svim blokovima. U blokovskoj izgradnji najčešći posao je zajednička vertikala, a tu je bitno da se odmah utvrdi da li je čep u stanu ili u zajedničkom vodu — od toga zavisi i ko snosi trošak."),
            ("Ko plaća odgušenje vertikale u bloku?",
             "Vertikala je zajednički deo zgrade, pa trošak po pravilu ide na stambenu zajednicu. Zato ako se voda vraća i kod komšija, odmah obavestite upravnika — mi izdajemo račun i na stambenu zajednicu."),
            ("Radite li u novogradnji u Belvilu i na Savadi?",
             "Radimo. U novijim stanovima najčešći pozivi su servis ugradnog vodokotlića i curenje u podu, gde se radi detekcija umesto otvaranja estriha."),
        ],
        extra=[
            ("Blokovi: zašto problem retko počinje u vašem stanu",
             ["Na jednu fekalnu vertikalu u bloku vezano je i po deset stanova. Kada se u njoj nakupe naslage, prvi znak dobijaju najniži stanovi — voda se vraća kroz slivnik u kupatilu ili kroz kadu, iako u tom stanu niko ništa nije bacio u odvod.",
              "Zbog toga u blokovima prvo pitamo da li se isto dešava kod komšija i da li je problem u jednom odvodu ili u više njih. Ako je vertikala, intervencija se radi sa revizije u podrumu ili na međuspratu, a ne iz stana — i to je posao za stambenu zajednicu, ne za pojedinca.",
              "Posle odgušenja vertikale ima smisla uraditi i <a href=\"../../snimanje-kanalizacije-kamerom/\">pregled kamerom</a>. U zgradama iz sedamdesetih presek je često toliko sužen naslagama da se čep vraća za nekoliko meseci, a snimak je jedini način da se to pokaže upravniku crno na belo."]),
            ("Novogradnja: ugradni sistemi i curenje u podu",
             ["Belvil, Savada i noviji objekti oko Arene su druga priča. Tamo nema starih vertikala, ali ima ugradnih vodokotlića, ravnih tuš odvoda i razvoda u podu — a to su kvarovi koji se ne vide dok ne postanu skupi.",
              "Ugradni mehanizam servisiramo kroz revizioni otvor, bez obijanja pločica. Curenje u podu se prvo locira termovizijom i akustikom, pa se otvara jedna do dve pločice umesto cele prostorije. U stanu sa skupom obradom ta razlika je ceo smisao poziva."]),
        ],
    ),
    dict(
        ime="Zemun", slug="zemun", profil="mes",
        stizemo='Zemun je blizu, ali je razvučen: od Gardoša do Batajnice i Zemun Polja ima dvadesetak minuta razlike. Zato vreme kažemo za vašu adresu, a ne za opštinu.', priprema='Ako ste u starom delu, korisno je da znate da li je instalacija menjana i kada. U Batajnici i Zemun Polju pitamo da li je objekat na gradskoj kanalizaciji ili na jami.', lok="u Zemunu",
        naselja="Gornji grad, Donji grad, Gardoš, Novi Zemun, Altina, Batajnica, Zemun Polje, Galenika",
        karakter=(
            "Zemun je dve priče u jednoj opštini. Stari deo oko Gardoša i Donjeg grada ima kuće sa "
            "instalacijama koje su dograđivane u više navrata — pocinkovane cevi, improvizovani priključci "
            "i dvorišna kanalizacija koja nije uvek na mestu gde se očekuje."),
        karakter2=(
            "Batajnica, Altina i Zemun Polje su, nasuprot tome, pretežno individualna izgradnja sa dvorišnim "
            "vodovima i septičkim jamama u delovima bez priključka. Tu su česti pozivi za curenje na ukopanom "
            "vodu i za odgušenje spoljne kanalizacije, a ne za sifon u kuhinji."),
        problemi=[
            ("Stare pocinkovane instalacije", "Zarasle cevi, slab pritisak i curenje koje se javlja na novom mestu posle svake popravke."),
            ("Dvorišna kanalizacija i šahtovi", "Odgušenje spoljnog voda i revizionih šahtova kod kuća."),
            ("Curenje na ukopanom vodu", "Veliki račun bez vidljive vode — lociranje akustičnom opremom pre kopanja."),
        ],
        susedi=["novi-beograd", "surcin", "cukarica"],
    ),
    dict(
        ime="Voždovac", slug="vozdovac", profil="mes",
        stizemo='Donji Voždovac je blizu centra i ekipe su tu češće. Prema Kumodražu, Jajincima i Ripnju put je duži i to kažemo unapred, bez zaokruživanja naniže.', priprema='Zbog nagiba terena ovde često nije kriv odvod nego njegov pad. Ako voda sporo otiče i posle čišćenja, recite nam to odmah — drugačije pristupamo.', lok="na Voždovcu",
        naselja="Autokomanda, Dušanovac, Konjarnik, Banjica, Medaković, Braće Jerković, Kumodraž, Jajinci, Ripanj",
        karakter=(
            "Voždovac se penje uzbrdo i to se vidi na instalacijama. Donji deo prema Autokomandi i Dušanovcu "
            "je stara gradnja sa zajedničkim vertikalama, a prema Banjici i Medakoviću preovlađuju blokovi iz "
            "sedamdesetih i osamdesetih sa dugim horizontalnim razvodima u podrumima."),
        karakter2=(
            "Više prema Kumodražu, Jajincima i Ripnju prelazi se na individualnu izgradnju sa dvorištima, gde "
            "su u igri spoljna kanalizacija, septičke jame i vodovi koji prolaze ispod betoniranih prilaza. "
            "Zbog nagiba terena ovde se češće nego drugde javljaju problemi sa nagibom odvoda i sa vraćanjem vode."),
        problemi=[
            ("Zapušenje u podrumskom razvodu", "Dugi horizontalni vodovi u blokovima — mašinsko odgušenje sa revizije."),
            ("Spoljna kanalizacija kod kuća", "Vodovi ispod prilaza i dvorišta, sa pregledom kamerom kad se problem ponavlja."),
            ("Pogrešan nagib odvoda", "Voda sporo otiče i posle čišćenja — utvrđuje se snimanjem, ne ponovnim čišćenjem."),
        ],
        susedi=["zvezdara", "rakovica", "vracar"],
    ),
    dict(
        ime="Zvezdara", slug="zvezdara", profil="mes",
        stizemo='Oko Vukovog spomenika i Đerma ekipe su najčešće u blizini. Za Mirijevo i Mokre Lugove vreme zavisi od saobraćaja i kažemo ga tek kada vidimo gde je ekipa.', priprema='U starim zgradama ovde se u jednoj vertikali sretnu dva-tri materijala. Ako znate šta je i kada menjano u vašem stanu, to je podatak koji skraćuje posao.', lok="na Zvezdari",
        naselja="Cvetkova pijaca, Đeram, Vukov spomenik, Lion, Mirijevo, Veliki Mokri Lug, Mali Mokri Lug, Zvezdarska šuma",
        karakter=(
            "Zvezdara ima izrazito mešovit fond. Oko Vukovog spomenika i Đerma su zgrade iz prve polovine "
            "dvadesetog veka sa instalacijama koje su menjane delimično, pa se u istoj vertikali sreću dva "
            "ili tri različita materijala — a spojevi među njima su najčešće mesto curenja."),
        karakter2=(
            "Mirijevo i Mokri Lugovi su druga priča: brza individualna i polukolektivna izgradnja, često sa "
            "instalacijama izvedenim bez projekta. Tu se najviše radi na odvodima sa nedovoljnim nagibom i na "
            "priključcima koji su rađeni naknadno, kako se objekat dograđivao."),
        problemi=[
            ("Spojevi različitih materijala", "Curenje na prelazu sa stare na novu cev — detekcija pre otvaranja zida."),
            ("Odvodi bez pravilnog nagiba", "Ponovljena zapušenja u objektima građenim u fazama."),
            ("Zapušenje vertikale u starim zgradama", "Zajednički vod sa naslagama — mašinsko čišćenje i pregled kamerom."),
        ],
        susedi=["palilula", "vozdovac", "stari-grad"],
    ),
    dict(
        ime="Palilula", slug="palilula", profil="mes",
        stizemo='Gradski deo je blizu, prekodunavska naselja su posebna priča — most i gužva menjaju računicu. Zato za Borču, Krnjaču i Kotež kažemo realno vreme, a ne prosek.', priprema='U prekodunavskim naseljima je kota niska i vodostaj visok. Pre poziva pogledajte da li se voda vraća samo kod vas ili i kod komšija — u nizini je to najčešće zajednički vod.', lok="na Paliluli",
        naselja="Karaburma, Hadžipopovac, Profesorska kolonija, Bogoslovija, Krnjača, Borča, Ovča, Kotež, Padinska skela",
        karakter=(
            "Palilula je najveća beogradska opština i deli se Dunavom na dva potpuno različita dela. Na gradskoj "
            "strani, od Karaburme do Bogoslovije, radi se o zgradama sa zajedničkim vertikalama i o starijim "
            "kućama u kolonijama, gde su instalacije stare po nekoliko decenija."),
        karakter2=(
            "Preko Dunava — Krnjača, Borča, Kotež, Ovča — teren je nizak i vodostaj visok. To menja sve: podrumi "
            "i prizemlja su osetljivi na uspon vode, kanalizacija se teže prazni, a curenja na ukopanim vodovima "
            "se dugo ne primete, jer se voda gubi u vlažnom tlu. Za ovaj deo opštine planiramo intervenciju drugačije."),
        problemi=[
            ("Vraćanje vode u prizemlja i podrume", "Niska kota i visok vodostaj u prekodunavskim naseljima."),
            ("Zapušenje spoljne kanalizacije", "Dvorišni vodovi i šahtovi u Borči, Kotežu i Krnjači."),
            ("Skrivena curenja u vlažnom tlu", "Ukopani vodovi gde nema vidljivog traga — akustično merenje."),
        ],
        susedi=["zvezdara", "stari-grad", "grocka"],
    ),
    dict(
        ime="Čukarica", slug="cukarica", profil="mes",
        stizemo='Banovo brdo, Cerak i Vidikovac su blizu i pokriveni dobro. Za Sremčicu, Umku i Ostružnicu put je duži i to se odmah kaže, pre izlaska.', priprema='U blokovima proverite da li je problem samo u vašem stanu. Kod kuća prema Savi korisno je da znate gde je dvorišna revizija i dokle ide vaš priključak.', lok="na Čukarici",
        naselja="Banovo brdo, Žarkovo, Cerak, Vidikovac, Julino brdo, Košutnjak, Sremčica, Umka, Ostružnica",
        karakter=(
            "Banovo brdo, Cerak i Vidikovac su planski građena naselja iz sedamdesetih i osamdesetih, sa "
            "tipskim razvodom i zajedničkim vertikalama. Problemi su predvidivi: naslage u vertikalama posle "
            "četrdeset godina rada i ventili koji su zapekli od stajanja."),
        karakter2=(
            "Žarkovo, Sremčica, Umka i Ostružnica su pretežno individualna izgradnja, mestimično na kosom terenu "
            "i uz Savu. Tu dolaze dvorišni vodovi, septičke jame u delovima bez priključka i curenja na spoljnim "
            "instalacijama koja se otkrivaju tek kada stigne račun za vodu."),
        problemi=[
            ("Naslage u starim vertikalama", "Suženi presek u blokovima sa Banovog brda i Ceraka."),
            ("Zapekli ventili", "Ugaoni i zaporni ventili koji ne zatvaraju — čest uzrok hitnog poziva."),
            ("Dvorišni vodovi i septičke jame", "Odgušenje i detekcija na individualnim objektima."),
        ],
        susedi=["rakovica", "novi-beograd", "savski-venac"],
    ),
    dict(
        ime="Rakovica", slug="rakovica", profil="blok",
        stizemo='Rakovica je gusto naseljena i ekipe su tu često. Teren je brdovit, pa adresu i sprat tražimo odmah — na Miljakovcu i Labudovom brdu to nije formalnost.', priprema='Ako se isti odvod zapušava više puta, recite koliko puta i kada. Na dugim razvodima sa lomovima čep najčešće nije tamo gde se pojavio problem.', lok="u Rakovici",
        naselja="Kanarevo brdo, Petlovo brdo, Miljakovac, Labudovo brdo, Resnik, Skojevsko naselje, Vidikovac",
        karakter=(
            "Rakovica je gusto naseljena opština sa velikim udelom stanova iz sedamdesetih i osamdesetih. "
            "Miljakovac, Kanarevo i Labudovo brdo su naselja gde se u istoj zgradi godinama rešavaju iste stvari: "
            "vertikale sa naslagama, stari ventili i vodokotlići koji neprekidno propuštaju."),
        karakter2=(
            "Teren je izrazito brdovit, pa su razvodi dugi i sa više lomova nego u ravnim delovima grada. To znači "
            "da se čep često ne nalazi u stanu koji ga prijavljuje, nego dalje niz trasu — zbog čega se ovde "
            "pregled kamerom isplati češće nego ponovljeno čišćenje istog odvoda."),
        problemi=[
            ("Ponovljena zapušenja u istom stanu", "Uzrok je dalje niz trasu — utvrđuje se snimanjem kamerom."),
            ("Stari ugradni i nadgradni vodokotlići", "Stalno propuštanje vode u šolju i visok račun."),
            ("Curenje u zidu u stanovima iz osamdesetih", "Dotrajali spojevi — detekcija pre obijanja pločica."),
        ],
        susedi=["cukarica", "vozdovac", "barajevo"],
    ),
    dict(
        ime="Vračar", slug="vracar", profil="stari",
        stizemo='Vračar je mali i ekipe su najčešće u blizini. Najveća nepoznanica nije razdaljina nego parkiranje — zato umesto okruglog broja kažemo realan termin.', priprema='Ako je kupatilo skoro renovirano, recite to odmah. Problem je tada najčešće na spoju novog razvoda i stare zajedničke vertikale, a ne u onome što se vidi.', lok="na Vračaru",
        naselja="Crveni krst, Neimar, Kalenić, Slavija, Cvetni trg, Hram Svetog Save",
        karakter=(
            "Vračar je najgušća opština u zemlji i gotovo sav fond je stara gradnja — zgrade iz tridesetih, "
            "pedesetih i šezdesetih, sa instalacijama koje su menjane po stanovima, a ne po vertikalama. "
            "Posledica je da se u jednoj vertikali nalaze cevi iz tri različite decenije."),
        karakter2=(
            "Druga specifičnost su renovirana kupatila u starim stanovima. Novi razvod je najčešće izveden "
            "solidno, ali je vezan na stari zajednički vod koji nije menjan, pa problem nastaje na spoju — i "
            "tu je detekcija važnija nego bilo gde, jer se obija skupo sređena keramika."),
        problemi=[
            ("Voda curi kod komšije ispod", "Najčešći poziv na Vračaru. Merimo i dajemo nalaz koji možete pokazati komšiji i upravniku."),
            ("Renovirano kupatilo na staroj vertikali", "Problem na spoju novog i starog razvoda."),
            ("Zapušenje zajedničkog voda", "Vertikale sa decenijskim naslagama u zgradama iz sredine veka."),
        ],
        susedi=["stari-grad", "savski-venac", "zvezdara"],
    ),
    dict(
        ime="Stari grad", slug="stari-grad", profil="stari",
        stizemo='Centar je blizu, ali prilaz i parkiranje umeju da pojedu više vremena nego sama vožnja. Kažemo realno vreme kada vidimo gde je ekipa, ne pre toga.', priprema='Za lokale radimo i van najprometnijeg dela dana. Ako ste ugostitelj, recite kada vam najmanje smeta — najčešće možemo da se prilagodimo.', lok="u Starom gradu",
        naselja="Dorćol, Skadarlija, Knez Mihailova, Kosančićev venac, Kalemegdan, Jevremovac",
        karakter=(
            "Stari grad ima najstariji fond u Beogradu. Zgrade sa Dorćola i oko Skadarlije često imaju originalne "
            "trase instalacija iz prve polovine dvadesetog veka, sa naknadnim zahvatima koji nisu dokumentovani. "
            "Pre bilo kakvog otvaranja zida ovde se isplati prvo izmeriti, jer se iza maltera retko nalazi ono što se očekuje."),
        karakter2=(
            "Veliki deo prizemlja čine lokali — kafići, restorani i prodavnice. Njihovi kuhinjski odvodi i sanitarni "
            "čvorovi vezani su na iste stare vertikale kao i stanovi iznad, pa se zapušenja i izlivanja ovde rešavaju "
            "brzo i, kad god je moguće, van najprometnijeg dela dana."),
        problemi=[
            ("Nepoznate trase u starim zgradama", "Instalacija se locira merenjem, ne po crtežu kojeg nema."),
            ("Kuhinjski odvodi lokala", "Masnoća u zajedničkoj vertikali — planska odgušenja za ugostitelje."),
            ("Izlivanje u prizemlju i podrumu", "Zapušenje zajedničkog voda ispod nivoa lokala."),
        ],
        susedi=["vracar", "palilula", "savski-venac"],
    ),
    dict(
        ime="Savski venac", slug="savski-venac", profil="stari",
        stizemo='Savski venac je blizu centra i pokriven dobro. Za objekte sa kontrolom ulaza i rampom recite to pri pozivu, da ekipa ne čeka pred kapijom.', priprema='U objektu sa skupom završnom obradom ne otvaramo ništa dok se mesto ne locira. Ako postoji projekat instalacija, pripremite ga — ubrzava merenje.', lok="na Savskom vencu",
        naselja="Senjak, Dedinje, Topčider, Savamala, Beograd na vodi, Prokop, Klinički centar",
        karakter=(
            "Savski venac spaja stare vile na Senjaku i Dedinju sa novom izgradnjom u Savamali i priobalju. "
            "U vilama su u pitanju velike instalacije sa dugim razvodima, često sa dvorišnim vodovima i bazenskom "
            "ili zalivnom instalacijom koja komplikuje traženje curenja."),
        karakter2=(
            "U novoj izgradnji dominiraju ugradni sistemi, skriveni razvodi i završne obrade koje je skupo dirati. "
            "Zato se ovde radi prvenstveno dijagnostika: termovizija, akustika i pregled kamerom, pa tek onda zahvat — "
            "i to na najmanjoj mogućoj površini."),
        problemi=[
            ("Curenje u objektu sa skupom obradom", "Prvo lociranje, pa otvaranje tačno na mestu."),
            ("Dugi razvodi i dvorišne instalacije", "Zalivni sistemi i spoljni vodovi na većim parcelama."),
            ("Ugradni sistemi u novogradnji", "Servis mehanizma kroz reviziju, bez obijanja."),
        ],
        susedi=["vracar", "cukarica", "stari-grad"],
    ),
    dict(
        ime="Surčin", slug="surcin", profil="kuce",
        stizemo='Surčin je blizu, ali su parcele velike i adrese raštrkane po naseljima. Zato pri pozivu tražimo tačnu adresu i orijentir — na Bečmenu i Petrovčiću navigacija ume da promaši.', priprema='Pre dolaska je korisno da znate gde je vodomerni šaht i dokle ide vaš priključak. Kod dugih dvorišnih vodova to je prvo mesto gde merimo.', lok="u Surčinu",
        naselja="Surčin, Dobanovci, Bečmen, Petrovčić, Jakovo, Boljevci, Progar",
        karakter=(
            "Surčin je pretežno individualna izgradnja sa dvorištima i velikim parcelama. Vodovodni priključci su "
            "dugački, često prolaze ispod prilaza i dvorišta, a dobar deo objekata nije priključen na gradsku "
            "kanalizaciju nego koristi septičke jame."),
        karakter2=(
            "Zbog toga se ovde najviše radi na spoljnim instalacijama: odgušenje dvorišne kanalizacije i šahtova, "
            "detekcija curenja na ukopanim vodovima i sanacija priključaka. Zemljani radovi su deo posla, pa je "
            "tačno lociranje pre kopanja ovde direktna ušteda."),
        problemi=[
            ("Curenje na dugom dvorišnom priključku", "Lociranje geofonom umesto kopanja duž cele trase."),
            ("Zapušenje spoljne kanalizacije", "Dvorišni vodovi, šahtovi i veza sa septičkom jamom."),
            ("Instalacije u poslovnim objektima", "Skladišta i hale u zoni oko aerodroma."),
        ],
        susedi=["zemun", "novi-beograd", "obrenovac"],
    ),
    dict(
        ime="Grocka", slug="grocka", profil="kuce",
        stizemo='Kaluđerica i Leštane su blizu, Ritopek i Begaljica znatno dalje — pa se i vreme razlikuje. Kažemo realan termin za vašu adresu, ne prosek za opštinu.', priprema='Na kosom terenu prema Dunavu trase retko idu pravo. Ako znate da je nešto dograđivano ili betonirano preko cevi, recite odmah — to najviše skraćuje traženje.', lok="u Grockoj",
        naselja="Grocka, Kaluđerica, Vinča, Ritopek, Boleč, Leštane, Zaklopača, Begaljica",
        karakter=(
            "Grocka, a pre svega Kaluđerica, Leštane i Vinča, nastala je brzom individualnom izgradnjom, velikim "
            "delom bez planske infrastrukture. Instalacije su rađene u fazama, kako se kuća dograđivala, pa trase "
            "često nisu poznate ni samim vlasnicima."),
        karakter2=(
            "Teren je kosi i spušta se ka Dunavu, što utiče i na nagib odvoda i na vodostaj u nižim delovima. "
            "U praksi to znači dosta posla sa spoljnom kanalizacijom, septičkim jamama i sa vodovima koji su "
            "prošli ispod naknadno betoniranih površina."),
        problemi=[
            ("Nepoznate trase instalacija", "Objekti dograđivani u fazama — lociranje pre svakog zahvata."),
            ("Septičke jame i spoljna kanalizacija", "Odgušenje i pregled veza između objekta i jame."),
            ("Vodovi ispod betoniranih površina", "Detekcija pre otvaranja prilaza i staza."),
        ],
        susedi=["palilula", "vozdovac", "mladenovac"],
    ),
    dict(
        ime="Obrenovac", slug="obrenovac", profil="kuce",
        stizemo='Obrenovac je dalje od centra, pa planirane radove dogovaramo za termin unapred. Hitne pozive primamo u svako doba i odmah kažemo za koliko realno možemo da budemo tamo.', priprema='Zbog visokog nivoa podzemnih voda curenje se ovde dugo ne primeti — tlo je i inače vlažno. Zato je provera vodomera pre poziva ovde korisnija nego bilo gde.', lok="u Obrenovcu",
        naselja="Obrenovac, Barič, Zvečka, Mislođin, Urovci, Veliko Polje, Skela",
        karakter=(
            "Obrenovac je nizijska opština uz Savu i Kolubaru, sa visokim nivoom podzemnih voda u većem delu "
            "godine. To utiče i na podrume i na ukopane instalacije: curenje se teško primeti, jer se voda gubi "
            "u već vlažnom tlu, a kanalizacija se u nižim delovima sporije prazni."),
        karakter2=(
            "Fond čine pretežno porodične kuće sa dvorištima i deo kolektivnog stanovanja u centru. Za kuće se "
            "najviše traži odgušenje spoljne kanalizacije i rad na priključcima, a za stanove u centru uobičajene "
            "intervencije na vertikalama i sanitariji."),
        problemi=[
            ("Visok nivo podzemnih voda", "Curenje bez vidljivog traga — merenje umesto pretpostavke."),
            ("Spoljna kanalizacija kod kuća", "Dvorišni vodovi i šahtovi, sa pregledom kamerom po potrebi."),
            ("Podrumske instalacije", "Vlaga i instalacije u objektima sa niskom kotom."),
        ],
        susedi=["surcin", "barajevo", "cukarica"],
    ),
    dict(
        ime="Barajevo", slug="barajevo", profil="kuce",
        stizemo='Barajevo je prigradska opština sa raštrkanim naseljima, pa izlazak planiramo unapred. Za hitne situacije javite se odmah i recite tačnu adresu, ne samo naselje.', priprema='Pošto je dolazak duži, pre izlaska detaljnije pitamo o problemu — da ekipa ponese pravi alat i delove i da se posao završi u jednom dolasku, a ne u dva.', lok="u Barajevu",
        naselja="Barajevo, Veliki Borak, Meljak, Vranić, Lisović, Baćevac, Arnajevo",
        karakter=(
            "Barajevo je prigradska opština sa pretežno individualnom izgradnjom i velikim parcelama. Objekti su "
            "različite starosti, instalacije su često izvođene sopstvenim snagama, a priključci na vodovod znaju "
            "biti dugi i nepravilno trasirani."),
        karakter2=(
            "Deo naselja koristi septičke jame, pa su česti pozivi za odgušenje veze između objekta i jame i za "
            "sanaciju ulegnutih deonica. Zbog udaljenosti od centra, izlaske planiramo tako da se u jednom dolasku "
            "uradi sve što je moguće — zato pre dolaska detaljnije pitamo o problemu."),
        problemi=[
            ("Dugi i netrasirani priključci", "Lociranje curenja na ukopanom vodu pre kopanja."),
            ("Septičke jame i veze ka objektu", "Odgušenje i provera ulegnutih deonica."),
            ("Instalacije rađene bez projekta", "Pregled stanja i plan sanacije umesto krpljenja."),
        ],
        susedi=["rakovica", "obrenovac", "lazarevac"],
    ),
    dict(
        ime="Lazarevac", slug="lazarevac", profil="kuce",
        stizemo='Lazarevac je najudaljeniji deo grada, pa planirane izlaske dogovaramo za konkretan dan i termin. Kod hitnih poziva odmah kažemo iskreno koliko nam treba.', priprema='Zbog udaljenosti na telefonu uzimamo više podataka nego inače: tip objekta, šta je već pokušano i da li postoji pristupna revizija. Tako se posao završava iz prve.', lok="u Lazarevcu",
        naselja="Lazarevac, Vreoci, Veliki Crljeni, Rudovci, Stepojevac, Junkovac",
        karakter=(
            "Lazarevac je najudaljenija velika beogradska opština, sa centrom koji ima kolektivno stanovanje i "
            "okolinom u kojoj dominiraju porodične kuće. U naseljima uz rudarski basen deo objekata je star i "
            "instalacije su menjane parcijalno."),
        karakter2=(
            "Za ovu opštinu izlaske planiramo unapred, osim kod hitnih situacija. Zato na telefonu uzimamo više "
            "podataka nego inače — tip objekta, šta je već pokušano i da li postoji pristupna revizija — da bi se "
            "posao završio u jednom dolasku."),
        problemi=[
            ("Parcijalno menjane instalacije", "Spojevi starog i novog razvoda kao mesto curenja."),
            ("Odgušenje kod porodičnih kuća", "Spoljni vodovi, šahtovi i veze sa jamom."),
            ("Planirani radovi u centru", "Intervencije na vertikalama i sanitariji u kolektivnom stanovanju."),
        ],
        susedi=["barajevo", "obrenovac", "sopot"],
    ),
    dict(
        ime="Mladenovac", slug="mladenovac", profil="kuce",
        stizemo='Za Mladenovac i okolna sela izlazak planiramo unapred. Hitne pozive primamo uvek, ali ne obećavamo rok koji na toj udaljenosti ne možemo da ispunimo.', priprema='Ako ste u nekom od okolnih sela, recite da li je objekat na gradskoj kanalizaciji ili na jami i da li postoji bunar. To menja i pristup i opremu koju nosimo.', lok="u Mladenovcu",
        naselja="Mladenovac, Selo Mladenovac, Amerić, Velika Ivanča, Koraćica, Mala Vrbica",
        karakter=(
            "Mladenovac ima gradsko jezgro sa zgradama i široku okolinu sa porodičnim kućama. U gradskom delu "
            "posao je uobičajen za kolektivno stanovanje — vertikale, sanitarija, bojleri — dok se u okolnim "
            "selima radi pretežno na spoljnim instalacijama i bunarskim sistemima."),
        karakter2=(
            "Zbog udaljenosti izlazak planiramo unapred i pre dolaska uzimamo detaljan opis, kako bi se u jednom "
            "dolasku poneo pravi alat i rezervni delovi koji bi mogli da zatrebaju."),
        problemi=[
            ("Spoljne i dvorišne instalacije", "Odgušenje i detekcija na porodičnim objektima."),
            ("Vertikale u gradskom jezgru", "Zajednički vodovi sa naslagama u starijim zgradama."),
            ("Bojleri i sanitarija", "Servis i zamena, sa delovima poneseni unapred."),
        ],
        susedi=["sopot", "grocka", "vozdovac"],
    ),
    dict(
        ime="Sopot", slug="sopot", profil="kuce",
        stizemo='Sopot je najmanja i jedna od udaljenijih opština, pa se izlazak dogovara unapred. Za hitne slučajeve javite se odmah — recićemo realno kada možemo da stignemo.', priprema='Kod seoskih domaćinstava najviše vremena troši traženje trase. Ako postoji bilo kakav crtež ili se sećate gde se kopalo, to je najkorisniji podatak koji možete da date.', lok="u Sopotu",
        naselja="Sopot, Ralja, Mali Požarevac, Drlupa, Nemenikuće, Babe",
        karakter=(
            "Sopot je najmanja beogradska opština po broju stanovnika, sa pretežno seoskim i prigradskim "
            "domaćinstvima. Objekti su uglavnom porodične kuće sa dvorištima, a deo naselja nije priključen na "
            "gradsku kanalizaciju."),
        karakter2=(
            "Posao je zato pretežno na spoljnim instalacijama: dvorišni vodovi, septičke jame, priključci i "
            "sanacija ulegnutih deonica. Izlazak se planira unapred, a za hitne situacije se javite odmah i "
            "recićemo realno kada možemo da stignemo."),
        problemi=[
            ("Dvorišni vodovi i jame", "Odgušenje i provera veze objekat–jama."),
            ("Curenje na ukopanom priključku", "Akustično merenje pre kopanja po dvorištu."),
            ("Instalacije u starijim kućama", "Zamena dotrajalih deonica i ventila."),
        ],
        susedi=["mladenovac", "lazarevac", "grocka"],
    ),
]

BY_SLUG = {o["slug"]: o for o in OPSTINE}

# Заполняется из блока NASELJA ниже, но нужен уже в цикле по общинам.
NASELJA_PO_OPSTINI = {}
HUB_CHIPS = [("lokacije/vodoinstalater-%s" % o["slug"], o["ime"]) for o in OPSTINE]


CARD_SETS = {
    "blok": ("Šta najviše radimo u zgradama ovde", [
        ("odgusenje-kanalizacije-beograd", "Odgušenje vertikale",
         "Zajednički vod na koji je vezano više stanova. Radi se sa revizije, ne iz stana, i trošak ide na stambenu zajednicu.", "6.000–8.000 RSD"),
        ("servis-ugradnih-vodokotlica-geberit", "Ugradni vodokotlić",
         "Mehanizam u zidu — plovak, zvono i tipka. Servis kroz revizioni otvor, bez obijanja pločica.", "2.500–5.000 RSD"),
        ("hitne-intervencije-beograd", "Hitne intervencije 0–24",
         "Pukla cev, ventil koji ne zatvara i izlivanje koje ugrožava stanove ispod.", "od 4.000 RSD"),
        ("detekcija-curenja-vode-beograd", "Curenje između stanova",
         "Merenje kada se ne zna da li voda dolazi od komšije, iz vertikale ili iz vašeg razvoda.", "od 5.000 RSD")]),
    "stari": ("Šta najviše radimo u starim zgradama ovde", [
        ("detekcija-curenja-vode-bez-razbijanja", "Detekcija bez razbijanja",
         "U stanu sa sređenom keramikom mesto se prvo locira, pa se otvara jedna do dve pločice.", "5.000–12.000 RSD"),
        ("vodovodne-instalacije-i-popravke", "Zamena starih cevi",
         "Pocinkovane instalacije koje su iznutra zarasle: slab pritisak i novo curenje posle svake popravke.", "od 6.000 RSD"),
        ("odgusenje-kanalizacije-beograd", "Odgušenje vertikale",
         "Zajednički vodovi sa decenijskim naslagama, često zajedno sa lokalima u prizemlju.", "6.000–8.000 RSD"),
        ("renoviranje-kupatila", "Renoviranje kupatila",
         "Nov razvod u starom stanu, sa proverom spoja na zajedničku vertikalu.", "od 20.000 RSD")]),
    "kuce": ("Šta najviše radimo kod kuća ovde", [
        ("odgusenje-kanalizacije-beograd", "Spoljna kanalizacija i šahtovi",
         "Dvorišni vodovi, revizioni šahtovi i veza objekta sa jamom ili priključkom.", "od 8.000 RSD"),
        ("detekcija-curenja-vode-u-zemlji", "Curenje na ukopanom vodu",
         "Veliki račun bez vidljive vode. Mesto se locira geofonom, pa se kopa jedan do dva kvadrata.", "10.000–25.000 RSD"),
        ("hitne-intervencije-beograd", "Hitne intervencije 0–24",
         "Pukla cev, izlivanje i kvarovi koji ne mogu da čekaju planirani izlazak.", "od 4.000 RSD"),
        ("servis-bojlera", "Servis bojlera",
         "Kamenac, grejač, termostat i sigurnosni ventil — često u istom izlasku sa drugim poslom.", "od 3.000 RSD")]),
    "mes": ("Šta najviše radimo na ovoj lokaciji", [
        ("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije",
         "Sudopera, WC šolja, kada, slivnik, vertikala i spoljni vod.", "od 3.000 RSD"),
        ("detekcija-curenja-vode-beograd", "Detekcija curenja vode",
         "Lociranje mesta curenja pre nego što se bilo šta obija.", "od 5.000 RSD"),
        ("snimanje-kanalizacije-kamerom", "Snimanje kamerom",
         "Kada se isti odvod zapuši po treći put — pokazuje uzrok, a ne posledicu.", "6.000–8.000 RSD"),
        ("hitne-intervencije-beograd", "Hitne intervencije 0–24",
         "Pukla cev, izlivanje, ventil koji ne zatvara.", "od 4.000 RSD")]),
}

STIZEMO = {
    "blok": "U gusto naseljenim delovima ekipe su češće u blizini, pa je izlazak najčešće brži. Ali tačno vreme zavisi od toga koliko je intervencija u toku — kada pozovete, kažemo realan termin za tu situaciju, a ne okrugao broj.",
    "stari": "U centru je najveća nepoznanica parkiranje i prilaz, posebno u špicu. Zbog toga ne obećavamo rok unapred nego kažemo realno vreme kada vidimo gde je ekipa.",
    "kuce": "Ovo je udaljeniji deo grada, pa planirane izlaske dogovaramo unapred. Za hitne situacije javite se odmah — kažemo iskreno za koliko možemo da budemo tamo, bez obećanja koje ne možemo da ispunimo.",
    "mes": "Zavisi od trenutnog rasporeda ekipa i doba dana. Kada pozovete, kažemo realno vreme za tu situaciju — ne obećavamo rok koji ne možemo da ispunimo.",
}

PRIPREMA = {
    "blok": "Ako ste u zgradi, pre poziva proverite da li se isto dešava kod komšija iznad i ispod i recite nam sprat. Time se odmah zna da li je čep u vašem odvodu ili u zajedničkoj vertikali — a od toga zavisi i ko snosi trošak.",
    "stari": "U starim zgradama trasa instalacije retko odgovara očekivanom. Ako znate da je nešto menjano u stanu ili ako je skoro bilo radova, recite nam — to najviše skraćuje traženje.",
    "kuce": "Kod kuća je korisno da unapred znate gde je vodomerni šaht i gde je revizija na spoljnoj kanalizaciji. Ako postoji septička jama, recite kada je poslednji put pražnjena.",
    "mes": "Pre poziva pogledajte da li sporo otiče samo jedan odvod ili više njih. To je podatak po kome se odmah vidi da li je problem lokalan ili na zajedničkom vodu.",
}


CARD4 = {'surcin': ('vodovodne-instalacije-i-popravke', 'Priključci i spoljne česme', 'Dugi dvorišni priključci, zamena dotrajalih deonica i spoljna česma na parceli.', 'od 2.400 RSD'), 'grocka': ('snimanje-kanalizacije-kamerom', 'Snimanje kamerom', 'Kod objekata građenih u fazama pregled pokazuje gde je nagib pogrešan ili cev ulegla.', '6.000–8.000 RSD'), 'obrenovac': ('detekcija-curenja-vode-bez-razbijanja', 'Detekcija bez razbijanja', 'U vlažnom tlu i podrumima vlaga ne znači i mesto curenja — prvo se meri, pa se otvara.', '5.000–12.000 RSD'), 'barajevo': ('servis-bojlera', 'Servis bojlera', 'Kamenac, grejač i sigurnosni ventil — po mogućstvu u istom izlasku sa drugim poslom.', 'od 3.000 RSD'), 'lazarevac': ('renoviranje-kupatila', 'Renoviranje kupatila', 'Planirani radovi sa pisanom ponudom i dogovorenim terminima, bez improvizacije.', 'od 20.000 RSD'), 'mladenovac': ('vodovodne-instalacije-i-popravke', 'Zamena cevi i ventila', 'Parcijalno menjane instalacije u starijim kućama i spojevi starog i novog razvoda.', 'od 2.400 RSD'), 'sopot': ('popravka-pukle-cevi', 'Pukla cev', 'Zimi najčešći poziv kod nezaštićenih dvorišnih i podrumskih instalacija.', 'od 4.000 RSD'), 'zemun': ('detekcija-curenja-vode-u-zemlji', 'Curenje u zemlji', 'Dvorišni vodovi u Batajnici, Altini i Zemun Polju — lociranje pre kopanja.', '10.000–25.000 RSD'), 'vozdovac': ('snimanje-kanalizacije-kamerom', 'Snimanje kamerom', 'Na kosom terenu pokazuje pogrešan pad odvoda, koji se čišćenjem ne rešava.', '6.000–8.000 RSD'), 'zvezdara': ('vodovodne-instalacije-i-popravke', 'Spojevi starog i novog', 'Curenje na prelazu sa stare na novu cev — najčešće mesto kvara u ovim zgradama.', 'od 2.400 RSD'), 'palilula': ('hitne-intervencije-beograd', 'Izlivanje u prizemlju', 'Niska kota i visok vodostaj: voda se vraća kroz slivnik u podrumima i prizemljima.', 'od 4.000 RSD'), 'cukarica': ('vodovodne-instalacije-i-popravke', 'Zapekli ventili', 'Ugaoni i zaporni ventili koji ne zatvaraju — čest uzrok hitnog poziva u blokovima.', '2.400–4.000 RSD'), 'vracar': ('servis-ugradnih-vodokotlica-geberit', 'Ugradni vodokotlić', 'U renoviranim kupatilima mehanizam se servisira kroz reviziju, bez diranja keramike.', '2.500–5.000 RSD'), 'stari-grad': ('za-firme', 'Lokali i ugostitelji', 'Kuhinjski odvodi i sanitarni čvorovi lokala, sa planskim čišćenjem van špica.', 'po ugovoru'), 'savski-venac': ('detekcija-geofonom-i-termovizijom', 'Geofon i termovizija', 'Dugi razvodi i dvorišne instalacije na većim parcelama — merenje umesto otvaranja.', 'od 5.000 RSD'), 'rakovica': ('snimanje-kanalizacije-kamerom', 'Snimanje kamerom', 'Kada se isti stan zapušava po treći put, uzrok je dalje niz trasu.', '6.000–8.000 RSD')}


def _usluge_cards_naselje(page, prof, card4):
    h2, items = CARD_SETS[prof]
    return cards("Usluge koje radimo ovde", items[:3] + [card4], page=page)


def _usluge_cards(page, prof, slug):
    h2, items = CARD_SETS[prof]
    if slug in CARD4:
        items = items[:3] + [CARD4[slug]]
    return cards(h2, items, page=page)


# ============================================================ NASELJA
# Клиент отдельно просил страницы по наcельям. Содержание у каждой своё —
# по типу застройки и по тому, что там реально ломается.
NASELJA = [
    dict(
        ime="Altina", slug="altina", lok="na Altini", opstina="zemun", profil="mes",
        opis="Altina, Plavi horizonti i okolne ulice",
        karakter=(
            "Altina je nastala brzo i u fazama. Veliki deo kuća dograđivan je kako je ko stizao, "
            "često bez projekta, pa se u jednom objektu nađu dve ili tri generacije instalacija — "
            "stariji pocinkovani razvod do jednog dela kuće i novije cevi do onoga što je dozidano kasnije."),
        karakter2=(
            "Posledica se vidi na spojevima. Tamo gde se stari i novi materijal sreću najčešće i procuri, "
            "a pošto su te veze obično u zidu ili ispod naknadno betoniranog poda, mesto se ne vidi. "
            "Zato ovde pre otvaranja gotovo uvek prvo merimo."),
        problemi=[
            ("Curenje na spoju starog i novog", "Objekti dograđivani u fazama — mesto se locira, pa se otvara tačno tu."),
            ("Slab pritisak u višim delovima", "Zarasle pocinkovane cevi i dugi priključci sa ulice."),
            ("Dvorišna kanalizacija", "Vodovi i šahtovi na parceli, kod dela objekata i veza sa jamom."),
        ],
        stizemo=("Altina je blizu i ekipe su tu često, ali su ulice slabo označene. Recite nam broj i orijentir — "
                 "navigacija ovde ume da promaši, a to je izgubljenih petnaest minuta."),
        priprema=("Korisno je da unapred znate da li je deo kuće dograđivan i kada. Kod curenja koje se ne vidi "
                  "to je najkorisniji podatak koji možete da nam date."),
        card4=("detekcija-curenja-vode-bez-razbijanja", "Detekcija bez razbijanja",
               "Spojevi u zidu i pod naknadno betoniranim podom — prvo merimo, pa otvaramo.", "5.000–12.000 RSD"),
    ),
    dict(
        ime="Batajnica", slug="batajnica", lok="u Batajnici", opstina="zemun", profil="kuce",
        opis="Batajnica, Crvenka, Šangaj i okolne ulice",
        karakter=(
            "Batajnica je velika i razvučena, i po instalacijama se deli na dva dela. Stariji deo naselja "
            "ima kuće sa dvorišnim vodovima i priključcima koji znaju biti dugački po dvadeset i više metara, "
            "često postavljenim pre nego što je ulica dobila kanalizaciju."),
        karakter2=(
            "Noviji deo je drugačiji: tu su objekti podignuti odjednom i instalacije su uredne, ali su "
            "priključci na gradsku mrežu mestimično improvizovani, jer se mreža širila sporije od gradnje. "
            "U delovima bez priključka i dalje se radi sa septičkim jamama."),
        problemi=[
            ("Curenje na dugom priključku", "Dvadeset i više metara ukopanog voda — geofon umesto kopanja duž cele trase."),
            ("Spoljna kanalizacija i jame", "Odgušenje dvorišnog voda i veze objekta sa jamom."),
            ("Zimsko pucanje cevi", "Nezaštićene instalacije u dvorištu i neukopanim delovima."),
        ],
        stizemo=("Batajnica je udaljenija od centra Zemuna i velika je, pa se vreme razlikuje od ulice do ulice. "
                 "Planirane radove dogovaramo za termin, a kod hitnih odmah kažemo realno koliko nam treba."),
        priprema=("Pre dolaska je dobro da znate gde je vodomerni šaht i dokle ide vaš priključak. Ako imate "
                  "septičku jamu, recite kada je poslednji put pražnjena."),
        card4=("detekcija-curenja-vode-u-zemlji", "Curenje u zemlji",
               "Dugi ukopani priključci — mesto se obeleži, pa se kopa jedan do dva kvadrata.", "10.000–25.000 RSD"),
    ),
    dict(
        ime="Medaković", slug="medakovic", lok="na Medakoviću", opstina="vozdovac", profil="blok",
        opis="Medaković I, II i III",
        karakter=(
            "Medaković je građen u tri faze na padini, i to se oseti na kanalizaciji. Zgrade su iz "
            "sedamdesetih i osamdesetih, sa zajedničkim vertikalama na koje je vezano više stanova, "
            "a zbog nagiba terena horizontalni razvodi u podrumima su duži nego u ravnim delovima grada."),
        karakter2=(
            "Zato se čep ovde retko nalazi tamo gde je prijavljen. Stan u prizemlju dobije vodu u slivnik, "
            "a uzrok je u vertikali ili u podrumskom vodu nekoliko desetina metara dalje. Prvo pitanje koje "
            "postavljamo jeste da li se isto dešava i kod komšija."),
        problemi=[
            ("Zapušena vertikala", "Zajednički vod sa naslagama — radi se sa revizije, trošak ide na stambenu zajednicu."),
            ("Dugi podrumski razvod", "Zbog nagiba trase su duže, pa je čep često daleko od mesta prijave."),
            ("Vraćanje vode u prizemlja", "Niži stanovi prvi osete problem u zajedničkom vodu."),
        ],
        priprema=("Pre poziva proverite da li se isto dešava kod komšija iznad i ispod i recite nam sprat. "
                  "Od toga zavisi i odakle se radi i ko snosi trošak."),
        card4=("snimanje-kanalizacije-kamerom", "Snimanje kamerom",
               "Kada se vertikala zapuši po treći put, pregled pokazuje koliko je presek stvarno sužen.", "6.000–8.000 RSD"),
    ),
    dict(
        ime="Banjica", slug="banjica", lok="na Banjici", opstina="vozdovac", profil="blok",
        opis="Banjica, Banjički venac i okolne stambene celine",
        karakter=(
            "Banjica je planski građeno naselje i instalacije su tipske — što posao čini predvidivim. "
            "Zgrade su uglavnom iz sedamdesetih, vertikale su posle pola veka rada sužene naslagama, "
            "a ugaoni i zaporni ventili u stanovima su dobrim delom originalni."),
        karakter2=(
            "Upravo ti ventili su ovde najčešći razlog za hitan poziv. Ventil koji pedeset godina stoji "
            "otvoren zapekne, pa kada pukne crevo do mašine nema čime da se zatvori voda. Zamena u mirnom "
            "terminu košta nekoliko hiljada dinara, a u panici — mnogo više, uz štetu kod komšija."),
        problemi=[
            ("Zapekli ventili u stanu", "Originalni ventili iz sedamdesetih koji više ne zatvaraju."),
            ("Naslage u vertikalama", "Pola veka rada bez zamene zajedničkog voda."),
            ("Curenje u podu i podrumskim prostorijama", "Tipski razvod, pa se mesto brzo locira merenjem."),
        ],
        priprema=("Ako zovete zbog curenja, prvo probajte da zatvorite ventil u stanu. Ako ne ide — recite "
                  "nam to odmah, jer tada ekipa nosi i rezervni ventil."),
        card4=("zamena-slavina-i-ventila", "Zamena ventila",
               "Zapekao ventil je ovde najčešći uzrok hitnog poziva. Jeftinije unapred nego u poplavi.", "2.400–4.000 RSD"),
    ),
    dict(
        ime="Vidikovac", slug="vidikovac", lok="na Vidikovcu", opstina="rakovica", profil="blok",
        opis="Vidikovac, Vidikovački venac i okolne ulice",
        karakter=(
            "Vidikovac je visoko i to definiše većinu poziva. Pritisak u gornjim spratovima je osetno slabiji "
            "nego u nižim delovima grada, pa svako dodatno suženje u cevi — kamenac, zapušen filter, "
            "poluzatvoren ventil — odmah postane primetno."),
        karakter2=(
            "Druga posledica visine i nagiba su dugi razvodi. Horizontalne trase u podrumima su duže od "
            "uobičajenih, a kod kanalizacije to znači da se naslage talože postepeno po celoj dužini, a ne "
            "na jednom mestu. Čišćenje jedne tačke zato daje kratkotrajan efekat."),
        problemi=[
            ("Slab pritisak na višim spratovima", "Proveravamo da li je uzrok zarasla cev, filter ili ventil, a ne mreža."),
            ("Ponovljena zapušenja", "Naslage po celoj dužini duge trase — čišćenje jedne tačke drži kratko."),
            ("Vertikale u blokovima", "Zajednički vodovi iz sedamdesetih i osamdesetih."),
        ],
        priprema=("Ako je problem slab pritisak, proverite da li je slab na svim slavinama ili samo na jednoj. "
                  "To odmah razdvaja kvar u stanu od problema na zajedničkoj instalaciji."),
        card4=("popravka-i-zamena-vodovodnih-cevi", "Slab pritisak i zamena cevi",
               "Na visini se svako suženje oseti. Utvrđujemo da li je kriva cev, filter ili ventil.", "od 3.000 RSD"),
    ),
    dict(
        ime="Miljakovac", slug="miljakovac", lok="na Miljakovcu", opstina="rakovica", profil="blok",
        opis="Miljakovac I, II i III",
        karakter=(
            "Miljakovac je mešavina blokova i individualne gradnje na strmom terenu. U zgradama su "
            "zajedničke vertikale iz sedamdesetih i osamdesetih, a razvodi imaju više lomova nego obično, "
            "jer su trase morale da prate pad."),
        karakter2=(
            "Svaki lom na trasi je mesto gde se nešto zadržava. Zbog toga se ovde češće nego drugde dešava "
            "da se isti stan zapušava po treći i četvrti put, iako je svaki put očišćen — uzrok nije u stanu "
            "nego dalje niz vod. Posle trećeg puta ne čistimo ponovo, nego snimamo."),
        problemi=[
            ("Ponovljeno zapušenje istog stana", "Uzrok je dalje niz trasu, na nekom od lomova."),
            ("Vertikale sa naslagama", "Zgrade iz sedamdesetih i osamdesetih, bez zamene zajedničkog voda."),
            ("Mešovita zona kuća i zgrada", "Kod kuća dvorišni vodovi, kod zgrada zajednički — pristup je različit."),
        ],
        priprema=("Recite nam koliko puta se isti odvod zapušio i kada. Ako je to treći put u godinu dana, "
                  "na izlasku odmah predlažemo pregled kamerom umesto još jednog čišćenja."),
        card4=("masinsko-odgusenje-kanalizacije", "Mašinsko odgušenje",
               "Duge trase sa lomovima traže mašinu i odgovarajuću glavu, ne sajlu iz prodavnice.", "od 3.500 RSD"),
    ),
    dict(
        ime="Žarkovo", slug="zarkovo", lok="u Žarkovu", opstina="cukarica", profil="mes",
        opis="Žarkovo, Julino brdo, Golf naselje i okolne ulice",
        karakter=(
            "Žarkovo je staro selo koje je grad progutao, i to se vidi na instalacijama. Na starom jezgru "
            "su kuće sa dvorišnim vodovima, a između njih su kasnije gusto ubačene nove zgrade — često "
            "priključene na infrastrukturu koja je pravljena za znatno manji broj domaćinstava."),
        karakter2=(
            "Zbog toga se ovde sreću problemi koji inače ne idu zajedno: u istoj ulici jedan objekat ima "
            "zapušen dvorišni vod, a susedna zgrada preopterećen priključak na gradsku kanalizaciju. "
            "Na telefonu zato pitamo i tip objekta, ne samo adresu."),
        problemi=[
            ("Preopterećen priključak", "Nove zgrade na staroj mreži — vraćanje vode u nižim etažama."),
            ("Dvorišni vodovi kod kuća", "Staro jezgro naselja, sa šahtovima i vezama na gradsku mrežu."),
            ("Curenje na starim instalacijama", "Pocinkovane cevi u kućama koje nisu menjane decenijama."),
        ],
        priprema=("Recite nam da li je objekat kuća ili zgrada i kada je građen. U Žarkovu se u istoj ulici "
                  "sreću dva potpuno različita tipa instalacije."),
        card4=("odgusenje-kanalizacije-beograd", "Odgušenje kanalizacije",
               "I dvorišni vodovi kod kuća i zajednički vodovi u novim zgradama.", "od 3.000 RSD"),
    ),
    dict(
        ime="Banovo brdo", slug="banovo-brdo", lok="na Banovom brdu", opstina="cukarica", profil="blok",
        opis="Banovo brdo, Ada Ciganlija, Žarkovačka i okolne ulice",
        karakter=(
            "Banovo brdo je sređeno i planski građeno naselje, sa zgradama iz sedamdesetih i osamdesetih i "
            "nešto starijih kuća i vila. Pristup je dobar, parkiranje uglavnom rešivo, pa je i izlazak ovde "
            "jednostavniji nego u gušćim delovima grada."),
        karakter2=(
            "Po instalacijama je tipična priča zrelog naselja: vertikale rade pedesetak godina i presek im "
            "je sužen naslagama, a u stanovima je dosta kupatila renovirano pojedinačno. Nov razvod u stanu "
            "zato često završava na staroj zajedničkoj vertikali — i problem nastane upravo na tom spoju."),
        problemi=[
            ("Nov razvod na staroj vertikali", "Renovirano kupatilo spojeno na zajednički vod koji nije menjan."),
            ("Naslage u vertikalama", "Pola veka rada bez zamene zajedničkog voda."),
            ("Curenje u renoviranom kupatilu", "Skupa keramika — prvo merimo, pa otvaramo jednu do dve pločice."),
        ],
        priprema=("Ako je kupatilo renovirano u poslednjih nekoliko godina, recite nam to odmah. Problem je "
                  "tada najčešće na spoju sa zajedničkom vertikalom, a ne u onome što se vidi."),
        card4=("detekcija-curenja-vode-bez-razbijanja", "Detekcija bez razbijanja",
               "U sređenom kupatilu mesto se prvo locira, pa se otvara jedna do dve pločice.", "5.000–12.000 RSD"),
    ),
]

NASELJA_CHIPS = [("lokacije/vodoinstalater-%s" % n["slug"], n["ime"]) for n in NASELJA]

for _n in NASELJA:
    NASELJA_PO_OPSTINI.setdefault(_n["opstina"], []).append(_n)

for n in NASELJA:
    slug = "lokacije/vodoinstalater-%s" % n["slug"]
    ime, lok = n["ime"], n["lok"]
    rod = BY_SLUG[n["opstina"]]
    prof = n["profil"]
    p = {
        "slug": slug,
        "title": "Vodoinstalater %s — odgušenje i hitne intervencije" % ime,
        "desc": ("Vodoinstalater %s: odgušenje kanalizacije, detekcija curenja vode i hitne "
                 "intervencije 0–24. Ista cena kao u ostatku Beograda, račun i garancija." % ime),
        "h1": "Vodoinstalater %s" % ime,
        "crumbs": [H, ("lokacije", "Lokacije"),
                   ("lokacije/vodoinstalater-%s" % rod["slug"], rod["ime"]), (slug, ime)],
        "schema": "service",
        "service_type": "Vodoinstalaterske usluge",
        "area": ime,
        "offer": (3000, 25000),
    }
    p["faq"] = [
        ("Izlazite li %s?" % lok,
         "Izlazimo. %s je deo opštine %s, koju pokrivamo u celini. %s"
         % (ime, rod["ime"], n.get("stizemo", STIZEMO[prof]))),
        ("Da li je cena %s drugačija?" % lok,
         "Nije. Cenovnik je isti za celo područje Beograda. Na cenu utiče vrsta i težina intervencije, "
         "a ne deo grada."),
        ("Šta ovde najčešće radite?",
         "Najviše poziva dobijamo zbog ovoga: %s." % ", ".join(t.lower() for t, _ in n["problemi"])),
        ("Radite li %s noću i vikendom?" % lok,
         "Radimo, dežurstvo je 0–24 svih sedam dana. Za intervencije noću, vikendom i praznikom važi "
         "ista cena kao i radnim danom — bez doplate."),
    ]
    p["body"] = (
        hero(p,
             "Deo opštine %s" % rod["ime"],
             "Vodoinstalater %s" % ime,
             "Odgušenje, detekcija curenja i hitne intervencije %s. Opišite problem telefonom i dobijate "
             "okvirnu cenu pre nego što iko izađe." % lok,
             ["Dežurstvo 0–24, bez doplate za vikend",
              "Ista cena kao u ostatku Beograda",
              "Oprema za dijagnostiku, ne samo za čišćenje",
              "Račun i pisana garancija"])
        + sec(prose("Kakve instalacije zatičemo %s" % lok, [n["karakter"], n["karakter2"]])
              + '\n    <p class="intro" style="margin-top:18px"><strong>Pokrivamo:</strong> %s.</p>' % n["opis"],
              cls="sec")
        + sec(cards("Zbog čega nas najčešće zovu %s" % lok,
                    [("", t, d, "") for t, d in n["problemi"]], page=p),
              cls="sec sec-alt")
        + sec(_usluge_cards_naselje(p, prof, n["card4"]), cls="sec")
        + sec(prose("Cena i dogovor",
                    [n.get("priprema", PRIPREMA[prof]),
                     "Cenovnik je isti za celo područje Beograda. Okvirni raspon dobijate telefonom na "
                     "osnovu opisa, tačan iznos kažemo na licu mesta pre nego što počnemo, i posle toga "
                     "se ne menja. Pun pregled cena je na stranici "
                     "<a href=\"../../cenovnik/\">Cenovnik vodoinstalaterskih usluga</a>."]),
              cls="sec sec-alt", sid="cene")
        + sec(faq_block(p["faq"], "Česta pitanja — %s" % ime), cls="sec")
        + sec(related(p, [("lokacije/vodoinstalater-%s" % rod["slug"], "Cela opština %s" % rod["ime"])]
                      + [("lokacije/vodoinstalater-%s" % m["slug"], m["ime"])
                         for m in NASELJA if m["opstina"] == n["opstina"] and m["slug"] != n["slug"]]
                      + [("lokacije", "Sve lokacije")],
                      h2="U blizini"),
              cls="sec sec-alt")
    )
    PAGES.append(p)


for o in OPSTINE:
    slug = "lokacije/vodoinstalater-%s" % o["slug"]
    ime, lok = o["ime"], o["lok"]
    p = {
        "slug": slug,
        "title": next(t for t in (
            "Vodoinstalater %s — odgušenje i hitne intervencije 0–24" % ime,
            "Vodoinstalater %s — odgušenje i hitne intervencije" % ime,
            "Vodoinstalater %s — hitne intervencije 0–24" % ime,
        ) if len(t) <= 60),
        "desc": ("Vodoinstalater %s: odgušenje kanalizacije, detekcija curenja vode i hitne "
                 "intervencije 0–24. Okvirna cena pre izlaska, račun i garancija." % ime),
        "h1": "Vodoinstalater %s" % ime,
        "crumbs": [H, ("lokacije", "Lokacije"), (slug, ime)],
        "schema": "service",
        "service_type": "Vodoinstalaterske usluge",
        "area": ime,
        "offer": (3000, 25000),
    }
    prof = o["profil"]
    extra_faq = o.get("extra_faq", [])
    p["faq"] = [
        ("Za koliko stižete %s?" % lok, o.get("stizemo", STIZEMO[prof])),
        ("Da li je cena %s drugačija nego u centru?" % lok,
         "Nije. Cenovnik je isti za celo područje Beograda. Na cenu utiče vrsta i težina intervencije, "
         "a ne deo grada."),
        ("Koja naselja pokrivate u ovoj opštini?",
         "Izlazimo na celu opštinu: %s i okolna naselja." % o["naselja"]),
        ("Radite li %s i vikendom i noću?" % lok,
         "Radimo, dežurstvo je 0–24 svih sedam dana. Za intervencije noću, vikendom i praznikom "
         "važi ista cena kao i radnim danom — bez doplate za hitnost i bez doplate za neradne dane."),
    ] + extra_faq
    p["body"] = (
        hero(p,
             "Izlazimo na celu opštinu",
             "Vodoinstalater %s" % ime,
             "Odgušenje, detekcija curenja i hitne intervencije %s. Opišite problem telefonom i dobijate "
             "okvirnu cenu pre nego što iko izađe." % lok,
             ["Dežurstvo 0–24, i vikendom",
              "Ista cena kao u ostatku Beograda",
              "Oprema za dijagnostiku, ne samo za čišćenje",
              "Račun i pisana garancija"])
        + sec(prose("Kakve instalacije zatičemo %s" % lok, [o["karakter"], o["karakter2"]])
              + '\n    <p class="intro" style="margin-top:18px"><strong>Naselja koja pokrivamo:</strong> %s.</p>' % o["naselja"],
              cls="sec")
        + sec(cards("Zbog čega nas najčešće zovu %s" % lok,
                    [("", t, d, "") for t, d in o["problemi"]],
                    page=p),
              cls="sec sec-alt")
        + "".join(sec(prose(h, paras), cls="sec sec-alt" if i % 2 else "sec")
                  for i, (h, paras) in enumerate(o.get("extra", [])))
        + sec(_usluge_cards(p, prof, o["slug"]), cls="sec")
        + sec(prose("Cena i dogovor",
                    [o.get("priprema", PRIPREMA[prof]),
                     "Cenovnik je isti za celo područje Beograda — udaljenost ne menja cenu intervencije. "
                     "Okvirni raspon dobijate telefonom na osnovu opisa, tačan iznos kažemo na licu mesta "
                     "pre nego što počnemo, i posle toga se ne menja. Pun pregled cena je na stranici "
                     "<a href=\"../../cenovnik/\">Cenovnik vodoinstalaterskih usluga</a>."]),
              cls="sec sec-alt", sid="cene")
        + sec(faq_block(p["faq"], "Česta pitanja — %s" % ime), cls="sec")
        + ("" if not NASELJA_PO_OPSTINI.get(o["slug"]) else
           sec(cards("Naselja u opštini %s" % ime,
                     [("lokacije/vodoinstalater-%s" % m["slug"], "Vodoinstalater %s" % m["ime"],
                       m["opis"], "") for m in NASELJA_PO_OPSTINI[o["slug"]]],
                     intro="Za ova naselja postoji zasebna strana sa onim što tamo najčešće zatičemo.",
                     page=p, cls="g2"),
               cls="sec"))
        + sec(related(p, [("lokacije/vodoinstalater-%s" % s, BY_SLUG[s]["ime"]) for s in o["susedi"]]
                      + [("lokacije", "Sve lokacije")],
                      h2="Susedne opštine"),
              cls="sec sec-alt")
    )
    PAGES.append(p)


# ============================================================ HUB LOKACIJA
p = {
    "slug": "lokacije",
    "title": "Vodoinstalater po opštinama Beograda — spisak lokacija",
    "desc": "Izlazimo na sve beogradske opštine: Novi Beograd, Zemun, Voždovac, Zvezdara, Palilula, Čukarica, Rakovica, Vračar, Stari grad i prigradske opštine.",
    "h1": "Gde radimo — beogradske opštine",
    "crumbs": [H, ("lokacije", "Lokacije")],
    "schema": "page",
}
p["faq"] = [
    ("Izlazite li na sve beogradske opštine?",
     "Izlazimo na celo područje grada Beograda, uključujući i prigradske opštine. Za udaljenije opštine "
     "izlazak se planira unapred, osim kod hitnih situacija."),
    ("Da li se cena razlikuje po opštinama?",
     "Ne. Cenovnik je isti za celo područje. Na cenu utiče vrsta i težina intervencije, a ne udaljenost."),
    ("Radite li van Beograda?",
     "Osnovno područje rada je Beograd sa prigradskim opštinama. Za lokacije van tog područja pitajte — "
     "odmah ćemo reći da li možemo da izađemo."),
]
p["body"] = (
    hero(p,
         "Celo područje Beograda",
         "Gde radimo — beogradske opštine",
         "Izlazimo na sve gradske i prigradske opštine. Za svaku opštinu postoji strana sa tipičnim problemima "
         "koje tamo najčešće zatičemo.",
         ["Sve gradske i prigradske opštine",
          "Isti cenovnik na celom području",
          "Dežurstvo 0–24",
          "Okvirna cena pre izlaska"],
         with_form=False)
    + sec(prose("Kako radimo po opštinama",
                ["Beograd nije jedan grad u smislu instalacija, nego nekoliko različitih. U blokovima Novog Beograda problem je skoro uvek zajednička vertikala; na Vračaru i u Starom gradu — stare zgrade u kojima su cevi menjane po stanovima, pa se u jednoj vertikali nađu tri različita materijala; u Surčinu, Grockoj i Barajevu — dvorišni vodovi, septičke jame i zemljani radovi.",
                 "Zato za svaku opštinu postoji zasebna strana sa onim što tamo zaista zatičemo. To nije ukras: ekipa koja zna da ide u Kaluđericu ponese drugu opremu nego ekipa koja ide u Belvil.",
                 "Cenovnik je isti za celo područje. Udaljenost ne menja cenu intervencije — za udaljenije opštine samo planiramo izlazak unapred, osim kada je hitno."]),
          cls="sec")
    + sec(cards("Gradske opštine",
                [("lokacije/vodoinstalater-%s" % o["slug"], "Vodoinstalater %s" % o["ime"],
                  o["naselja"], "")
                 for o in OPSTINE[:10]],
                page=p),
          cls="sec sec-alt")
    + sec(cards("Prigradske opštine",
                [("lokacije/vodoinstalater-%s" % o["slug"], "Vodoinstalater %s" % o["ime"],
                  o["naselja"], "")
                 for o in OPSTINE[10:]],
                page=p),
          cls="sec")
    + sec(cards("Naselja sa zasebnom stranom",
                [("lokacije/vodoinstalater-%s" % n["slug"], "Vodoinstalater %s" % n["ime"],
                  "%s · opština %s" % (n["opis"], BY_SLUG[n["opstina"]]["ime"]), "")
                 for n in NASELJA],
                intro="Za ova naselja smo napisali posebne strane, jer se po tipu gradnje i po tome šta "
                      "se u njima kvari dovoljno razlikuju od ostatka svoje opštine.",
                page=p, cls="g2"),
          cls="sec sec-alt")
    + sec(faq_block(p["faq"]), cls="sec")
    + sec(related(p, [("vodoinstalaterske-usluge", "Sve usluge"),
                      ("cenovnik", "Cenovnik"),
                      ("hitne-intervencije-beograd", "Hitne intervencije"),
                      ("kontakt", "Kontakt")]),
          cls="sec sec-alt")
)
PAGES.append(p)
