# -*- coding: utf-8 -*-
"""Lokacijske stranice: hub + stranica po beogradskoj opštini."""

import prices
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
        stizemo='Banovo brdo, Cerak i Julino brdo su blizu i pokriveni dobro. Za Sremčicu, Umku i Ostružnicu put je duži i to se odmah kaže, pre izlaska.', priprema='U blokovima proverite da li je problem samo u vašem stanu. Kod kuća prema Savi korisno je da znate gde je dvorišna revizija i dokle ide vaš priključak.', lok="na Čukarici",
        naselja="Banovo brdo, Žarkovo, Cerak, Julino brdo, Košutnjak, Sremčica, Umka, Ostružnica",
        karakter=(
            "Banovo brdo, Cerak i Julino brdo su planski građena naselja iz sedamdesetih i osamdesetih, sa "
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
        ("servis-vodokotlica-beograd", "Ugradni vodokotlić",
         "Mehanizam u zidu — plovak, zvono i tipka. Servis kroz revizioni otvor, bez obijanja pločica.", "2.000–5.000 RSD"),
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


CARD4 = {'surcin': ('vodovodne-instalacije-i-popravke', 'Priključci i spoljne česme', 'Dugi dvorišni priključci, zamena dotrajalih deonica i spoljna česma na parceli.', 'od 2.400 RSD'), 'grocka': ('snimanje-kanalizacije-kamerom', 'Snimanje kamerom', 'Kod objekata građenih u fazama pregled pokazuje gde je nagib pogrešan ili cev ulegla.', '6.000–8.000 RSD'), 'obrenovac': ('detekcija-curenja-vode-bez-razbijanja', 'Detekcija bez razbijanja', 'U vlažnom tlu i podrumima vlaga ne znači i mesto curenja — prvo se meri, pa se otvara.', '5.000–12.000 RSD'), 'barajevo': ('servis-bojlera', 'Servis bojlera', 'Kamenac, grejač i sigurnosni ventil — po mogućstvu u istom izlasku sa drugim poslom.', 'od 3.000 RSD'), 'lazarevac': ('renoviranje-kupatila', 'Renoviranje kupatila', 'Planirani radovi sa pisanom ponudom i dogovorenim terminima, bez improvizacije.', 'od 20.000 RSD'), 'mladenovac': ('vodovodne-instalacije-i-popravke', 'Zamena cevi i ventila', 'Parcijalno menjane instalacije u starijim kućama i spojevi starog i novog razvoda.', 'od 2.400 RSD'), 'sopot': ('popravka-pukle-cevi', 'Pukla cev', 'Zimi najčešći poziv kod nezaštićenih dvorišnih i podrumskih instalacija.', 'od 4.000 RSD'), 'zemun': ('detekcija-curenja-vode-u-zemlji', 'Curenje u zemlji', 'Dvorišni vodovi u Batajnici, Altini i Zemun Polju — lociranje pre kopanja.', '10.000–25.000 RSD'), 'vozdovac': ('snimanje-kanalizacije-kamerom', 'Snimanje kamerom', 'Na kosom terenu pokazuje pogrešan pad odvoda, koji se čišćenjem ne rešava.', '6.000–8.000 RSD'), 'zvezdara': ('vodovodne-instalacije-i-popravke', 'Spojevi starog i novog', 'Curenje na prelazu sa stare na novu cev — najčešće mesto kvara u ovim zgradama.', 'od 2.400 RSD'), 'palilula': ('hitne-intervencije-beograd', 'Izlivanje u prizemlju', 'Niska kota i visok vodostaj: voda se vraća kroz slivnik u podrumima i prizemljima.', 'od 4.000 RSD'), 'cukarica': ('vodovodne-instalacije-i-popravke', 'Zapekli ventili', 'Ugaoni i zaporni ventili koji ne zatvaraju — čest uzrok hitnog poziva u blokovima.', '2.400–4.000 RSD'), 'vracar': ('servis-vodokotlica-beograd', 'Ugradni vodokotlić', 'U renoviranim kupatilima mehanizam se servisira kroz reviziju, bez diranja keramike.', '2.000–5.000 RSD'), 'stari-grad': ('za-firme', 'Lokali i ugostitelji', 'Kuhinjski odvodi i sanitarni čvorovi lokala, sa planskim čišćenjem van špica.', 'po ugovoru'), 'savski-venac': ('detekcija-geofonom-i-termovizijom', 'Geofon i termovizija', 'Dugi razvodi i dvorišne instalacije na većim parcelama — merenje umesto otvaranja.', 'od 5.000 RSD'), 'rakovica': ('snimanje-kanalizacije-kamerom', 'Snimanje kamerom', 'Kada se isti stan zapušava po treći put, uzrok je dalje niz trasu.', '6.000–8.000 RSD')}


def _usluge_cards_naselje(page, prof, card4, h2=None):
    _h2, items = CARD_SETS[prof]
    return cards(h2 or "Usluge koje radimo ovde", items[:3] + [card4], page=page)


def _usluge_cards(page, prof, slug, h2=None):
    _h2, items = CARD_SETS[prof]
    if slug in CARD4:
        items = items[:3] + [CARD4[slug]]
    return cards(h2 or _h2, items, page=page)
# ============================================ DOPUNA PO OPŠTINAMA
# Klijent je tražio da tekstovi po lokacijama ne budu isti sa zamenjenim
# imenom opštine. Svaka opština zato ima odeljak i pitanje kojih nema nigde
# drugde na sajtu — ono što se tu zaista razlikuje u poslu.
OPSTINE_EXTRA = {
 "zemun": dict(
   extra=[("Pocinkovana cev koja je iznutra zarasla",
     ["U starom delu Zemuna veliki broj zgrada i kuća još ima originalni pocinkovani "
      "razvod. Takva cev se ne troši spolja nego iznutra: kamenac i korozija se "
      "naslažu po zidu i presek se godinama sužava, nekada do polovine. Spolja cev "
      "izgleda ispravno.",
      "Odatle dolaze dva tipična poziva. Prvi je slab pritisak koji se ne vraća ni "
      "posle zamene perlatora i creva — jer uzrok nije u armaturi. Drugi je curenje "
      "koje se pojavi odmah posle neke popravke: kada se na zaraslu cev pritegne nov "
      "fiting, naprsne na mestu gde je zid cevi najtanji.",
      "Zato u Zemunu pre popravke merimo pritisak i gledamo stanje cevi na mestu gde "
      "se radi. Ako je deonica zarasla, popravka jednog spoja znači novo curenje za "
      "mesec dana, i bolje je to reći unapred nego posle."]),
   ],
   faq=[("Posle popravke je procurilo na drugom mestu — zašto?",
      "Kod zaraslih pocinkovanih cevi zid je mestimično stanjen, pa pritezanje novog "
      "fitinga naprsne cev tamo gde je najslabija. Zato pre popravke gledamo stanje "
      "deonice i kažemo unapred ako ima smisla menjati je celu.")],
 ),
 "vozdovac": dict(
   extra=[("Nagib odvoda: ono što se čišćenjem ne rešava",
     ["Voždovac se diže od Autokomande ka Banjici i Jajincima, a kosi teren utiče na "
      "ono što najčešće radimo. Kada se objekat gradi na kosini, odvod se mestimično "
      "polaže sa prevelikim ili premalim padom, a oba su problem — prevelik pad pušta "
      "vodu da pobegne pre čvrstog otpada, premali je zadržava.",
      "Posledica je zapušenje koje se vraća u predvidivim intervalima. Čišćenje tada "
      "radi tačno onoliko dugo koliko treba da se ponovo nakupi, pa se isti račun "
      "plaća dva i tri puta u godini. Rešenje nije jača mašina nego pregled.",
      "Snimanje kanalizacije kamerom na kosom terenu pokazuje tri stvari koje se "
      "drugačije ne vide: gde je pad pogrešan, gde je cev ulegla i dokle ide trasa. "
      "Posle toga se zna da li je u pitanju čišćenje ili prepravka deonice — a to su "
      "dva različita posla i dve različite cene."]),
   ],
   faq=[("Isti odvod se zapušava dva puta u godini. Vredi li snimanje kamerom?",
      "Na kosom terenu gotovo uvek vredi. Pregled pokazuje da li je nagib pogrešan ili "
      "je cev ulegla — to se čišćenjem ne rešava, pa se isti posao inače plaća više puta.")],
 ),
 "zvezdara": dict(
   extra=[("Zašto je na Zvezdari spoj važniji od cevi",
     ["Zvezdara nema jedan tip gradnje nego nekoliko: zgrade iz tridesetih oko "
      "Cvetkove pijace, stambeni blokovi iz sedamdesetih, kuće u Mirijevu i "
      "novogradnja ubačena između. Instalacije su u većini objekata menjane u "
      "delovima, kako je ko stizao i kako je bilo potrebno.",
      "Zato je najčešće mesto kvara prelaz sa starog na novo. Pocinkovana cev i PPR "
      "se različito šire, a spoj među njima često je napravljen fitingom koji je "
      "zatečen na licu mesta. Dok stoji, drži; kada se u blizini nešto radi ili kada "
      "pritisak skoči, popusti.",
      "U praksi to znači da se ovde ne traži „gde je pukla cev“ nego gde su spojevi. "
      "Ako znate da je u stanu nešto menjano i kada, to je najkorisniji podatak — "
      "sužava zonu pre nego što iko dođe."]),
   ],
   faq=[("Kako nalazite curenje kada ne znamo šta je u zidu?",
      "Polazimo od spojeva, jer na Zvezdari najčešće procuri na prelazu stare i nove "
      "cevi. Zonu sužavamo merenjem pritiska po deonicama i termovizijom, pa se otvara "
      "jedno mesto — ne ceo zid.")],
 ),
 "palilula": dict(
   extra=[("Niska kota: voda ulazi, a ne izlazi",
     ["Delovi Palilule prema Dunavu i Krnjači leže nisko, a to menja smer problema. "
      "U većini grada zapušenje znači da voda ne odlazi; ovde, kada je vodostaj visok "
      "ili posle jake kiše, voda iz gradske mreže ulazi natrag — kroz podni slivnik u "
      "podrumu, kroz odvod u prizemlju, ponekad kroz šolju.",
      "To nije kvar u vašoj instalaciji i čišćenje tu ne pomaže. Rešenje je "
      "nepovratni ventil na odvodu ili, kod objekata gde se ponavlja, podizanje "
      "sanitarnog čvora iznad kote vraćanja. Oba su planirani posao, ne hitna "
      "intervencija.",
      "Hitno je ono što se radi dok voda još ulazi: zatvaranje, ispumpavanje i "
      "privremeno zaustavljanje. Ako nas zovete u toj situaciji, recite odmah da se "
      "voda vraća a ne da sporo otiče — dolazimo sa drugom opremom."]),
   ],
   faq=[("Voda se posle kiše vraća kroz slivnik u podrumu. Pomaže li odgušenje?",
      "Ne, jer odvod nije zapušen — voda ulazi iz mreže zbog niske kote. Trajno rešenje "
      "je nepovratni ventil na odvodu ili podizanje sanitarnog čvora, a hitno se radi "
      "zatvaranje i ispumpavanje.")],
 ),
 "cukarica": dict(
   extra=[("Dve Čukarice u jednom pozivu",
     ["Čukarica je po poslu praktično dve opštine. Banovo brdo, Cerak i Julino brdo su "
      "planski građeni blokovi iz sedamdesetih i osamdesetih, sa tipskim razvodom i "
      "zajedničkim vertikalama koje su u radu četrdeset godina. Žarkovo, Sremčica, "
      "Umka i Ostružnica su pretežno kuće, mestimično na kosini i uz Savu.",
      "Zato je prvo pitanje na telefonu je li u pitanju zgrada ili kuća. U bloku je "
      "najverovatnije zajednička vertikala, radi se sa revizije i trošak ide na "
      "stambenu zajednicu. Kod kuće je dvorišni vod ili veza sa jamom, radi se iz "
      "dvorišta i trošak je vaš. To nije formalnost — od toga zavisi koja oprema "
      "izlazi na adresu."]),
   ],
   faq=[("Zašto pitate da li sam u zgradi ili u kući?",
      "Zato što su to dva različita posla. U bloku je najčešće zajednička vertikala i "
      "radi se sa revizije, a trošak ide na stambenu zajednicu; kod kuće je dvorišni vod "
      "i radi se iz dvorišta. Od toga zavisi i oprema koja izlazi.")],
 ),
 "rakovica": dict(
   extra=[("Treći izlazak košta više od jednog pregleda",
     ["Sa Rakovice nam se najčešće javljaju zbog zapušenja koje se vraća u isti stan. "
      "Blokovi su tipski, vertikale su iste starosti i presek im se sužava podjednako, "
      "pa kada počne, čišćenje drži sve kraće: prvi put godinu, drugi put nekoliko "
      "meseci, treći put nedeljama.",
      "To ne znači da stanari nešto rade pogrešno. Znači da uzrok nije ono što je "
      "sklonjeno, nego presek cevi niže niz trasu. Mašina svaki put raščisti nakupljeno "
      "iznad čepa i stvar radi dok se ponovo ne nakupi.",
      "Kada čujemo da je to treći put, ne predlažemo četvrto čišćenje nego pregled. "
      "Snimanje kamerom pokazuje koliko je presek stvarno sužen i da li je cev negde "
      "ulegla, a to su dva različita nalaza sa dva različita rešenja. Jedan pregled u "
      "tom trenutku izađe jeftinije od dva izlaska koja rešavaju posledicu."]),
   ],
   faq=[("Zapušenje se vraća svakih par meseci — šta predlažete?",
      "Pregled, ne novo čišćenje. Snimanje kamerom pokazuje koliko je presek vertikale "
      "sužen i ima li ulegnuća. Jedan pregled tada izađe jeftinije od dva izlaska koja "
      "rešavaju samo posledicu.")],
 ),
 "vracar": dict(
   extra=[("Novo kupatilo, stara vertikala",
     ["Vračar ima najveći udeo renoviranih stanova u starim zgradama, i to pravi "
      "specifičnu situaciju. U stanu je sve novo — pločice, sanitarija, razvod — a "
      "zajednička vertikala na koju je to vezano je ista ona iz vremena kada je zgrada "
      "građena.",
      "Dok se ništa ne menja, radi. Kada se u renoviranju pomeri odvod, doda tuš kabina "
      "sa ravnim sifonom ili promeni nagib priključka do vertikale, pokaže se da "
      "zajednički vod više ne prima isto. Zapušenje se tada vraća u stanu u kojem je "
      "sve novo, a vlasnik logično pretpostavlja da je greška u radovima.",
      "Druga strana istog problema je voda koja se pojavi kod komšije ispod. U zgradi "
      "sa sređenim kupatilima pitanje nije samo gde curi nego čija je instalacija, jer "
      "od toga zavisi ko plaća. Zato ovde počinjemo merenjem i nalaz dajemo napisan — "
      "sa njim se razgovara sa komšijom i upravnikom, a to je nešto drugo od reči "
      "protiv reči."]),
   ],
   faq=[("Komšija ispod kaže da mu curi od mene, a kod mene nema ništa.",
      "Prvo proveravamo da li vaša instalacija drži pritisak. Ako ne pada, vaše cevi ne "
      "propuštaju i izvor je u vertikali ili u drugom stanu. Nalaz dobijate napisan, za "
      "razgovor sa komšijom ili upravnikom.")],
 ),
 "stari-grad": dict(
   extra=[("Instalacija koja nema nacrt ni jednog metra",
     ["Na Starom gradu radimo u zgradama starijim od sto godina, u kojima je instalacija "
      "dodavana i prepravljana više puta, bez zapisa gde šta ide. Vertikale su ponekad "
      "premeštane, odvodi su vođeni kroz zidove koji su u međuvremenu probijani, a dve "
      "zgrade iz istog perioda i iste ulice mogu biti rešene potpuno različito.",
      "Zato ovde ne postoji tipičan slučaj i ne dajemo cenu po tipu posla pre izlaska. "
      "Prvo se traži trasa — kamerom kroz odvod i merenjem po deonicama — pa se tek "
      "onda zna šta se radi. Ponekad se pokaže da je najkraći put kroz prostor koji "
      "nije u vašem stanu, i to se dogovara sa susedima pre nego što se počne.",
      "Drugi deo posla ovde su lokali u prizemlju. Kuhinjski odvodi kafića i restorana "
      "vezani su na istu vertikalu kao stanovi iznad, pa masnoća iz lokala napravi čep "
      "koji pogodi stanare. Taj posao radimo van radnog vremena lokala i po planu, da "
      "se ne zatvara u špicu."]),
   ],
   faq=[("Radite li u lokalima van radnog vremena?",
      "Radimo i to je ovde pravilo, ne izuzetak. Kuhinjski odvodi se čiste pre otvaranja "
      "ili posle zatvaranja, po planu dogovorenom unapred, da se lokal ne zatvara u špicu.")],
 ),
 "savski-venac": dict(
   extra=[("Kada je obrada vrednija od popravke",
     ["Na Savskom vencu je posao često određen onim u čemu se radi, a ne samim kvarom. "
      "U stanovima i kućama sa skupom obradom — kamenom, velikim formatom keramike, "
      "parketom u celom nivou — cena popravke prestaje da bude glavna stavka. Glavna "
      "stavka je šta će ostati posle.",
      "Format keramike koji se više ne proizvodi ne može se nabaviti za zakrpu, pa "
      "jedan otvoren kvadrat znači prepravku celog zida ili poda. Kod kamena je i "
      "gore: ploča se najčešće ne može izvaditi i vratiti.",
      "Zbog toga ovde merenje nije dodatna usluga nego početak posla. Termovizija, "
      "akustično merenje i provera pritiska po deonicama sužavaju zonu sa prostorije "
      "na konkretno mesto, pa se otvara tačno tu, uz vašu saglasnost i posle "
      "obeležavanja. Na objektima ovog tipa merenje gotovo uvek izađe jeftinije od "
      "jednog pogrešno otvorenog mesta."]),
   ],
   faq=[("Imamo kamen i veliki format keramike — kako radite da se ne uništi obrada?",
      "Mesto prvo lociramo merenjem i obeležimo ga, pa otvaramo tačno tu i uz vašu "
      "saglasnost. Gde postoji revizioni otvor, radi se kroz njega. Merenje je ovde "
      "jeftinije od jednog pogrešno otvorenog mesta.")],
 ),
 "surcin": dict(
   extra=[("Duga parcela, dug priključak, nijedna revizija",
     ["U Surčinu su parcele duboke i objekat je najčešće daleko od ulice. Priključak od "
      "vodomera do kuće zato ume da bude trideset i više metara, a kod poslovnih "
      "objekata i duže. Pri tome revizionih šahtova duž trase gotovo nikada nema — "
      "polagalo se najkraćim putem i zatrpalo.",
      "Kada na takvom vodu procuri, u dvorištu se ne vidi ništa. Prvi znak je račun za "
      "vodu, ponekad posle mesec dana curenja. Kopati duž cele trase nema smisla: to je "
      "trošak koji pređe cenu nove linije.",
      "Posao zato počinje lociranjem. Geofon i akustično merenje obeleže mesto na "
      "površini, pa se otvara jedan do dva kvadrata. Kod poslovnih objekata uz to "
      "dolazi i pitanje kada se sme raditi — instalacije u proizvodnji i magacinima "
      "dirapu se u dogovorenom terminu, ne kad zatreba."]),
   ],
   faq=[("Imamo poslovni objekat — možete li raditi u dogovorenom terminu?",
      "Možemo i tako radimo kod pravnih lica. Planirane radove zakazujemo za termin koji "
      "ne prekida posao, radimo preko računa i po predračunu, a za redovno održavanje "
      "postoji i ugovor.")],
 ),
 "grocka": dict(
   extra=[("Objekat građen u fazama, instalacija dodavana kasnije",
     ["U Grockoj je veliki deo objekata rastao kroz decenije: osnovna kuća, pa "
      "dogradnja, pa pomoćni objekat, pa letnja kuhinja. Instalacija je pratila tu "
      "logiku i nastajala u slojevima, najčešće bez projekta i bez zapisa gde šta ide.",
      "Zbog toga je najveći deo posla ovde pronalaženje trase, a ne sama popravka. "
      "Odvodi su vođeni ispod betoniranih staza i dvorišnih ploča, revizija ima malo, "
      "a one koje postoje često su zatrpane ili zatvorene prilikom nekog kasnijeg "
      "betoniranja.",
      "Zato pre kopanja uvek predlažemo pregled kamerom kroz najbliži dostupan otvor. "
      "On pokazuje kuda trasa ide, gde je ulegla i gde je nagib pogrešan — i štedi "
      "kopanje po površini koju je posle potrebno vraćati."]),
   ],
   faq=[("Ne znamo kuda ide odvod kroz dvorište. Kako to utvrđujete?",
      "Kamerom kroz najbliži dostupan otvor. Sonda u kameri se prati odozgo, pa se trasa "
      "obeleži na površini. To je jeftinije od kopanja po betoniranim stazama koje posle "
      "treba vraćati.")],
 ),
 "obrenovac": dict(
   extra=[("Vlaga nije dokaz da nešto curi",
     ["Obrenovac ima visok nivo podzemnih voda i to je najčešći izvor zabune. Vlažan zid "
      "u podrumu, mokra podloga uz temelj i vlaga koja se vraća posle svakog većeg "
      "padavinskog perioda — sve to izgleda kao curenje sa instalacije, a najčešće nije.",
      "Razlika se utvrđuje jednostavno i brzo: voda se zatvori i gleda se da li pritisak "
      "u instalaciji pada. Ako ne pada, vodovod ne propušta i kopanje ne vodi nikuda — u "
      "pitanju je prodor iz tla i to je posao za hidroizolaciju, ne za vodoinstalatera.",
      "Taj pregled radimo i kada je očigledno da nije u pitanju instalacija, jer je to "
      "pola sata rada umesto nedelje nagađanja. Ako se pokaže da instalacija zaista "
      "propušta, mesto se zatim locira merenjem i otvara se jedno mesto."]),
   ],
   faq=[("Podrum je vlažan — da li je to curenje sa instalacije?",
      "Često nije. U Obrenovcu je uzrok obično visok nivo podzemnih voda. Proveravamo da "
      "li instalacija drži pritisak: ako drži, ne propušta i problem je prodor iz tla, "
      "što je posao za hidroizolaciju.")],
 ),
 "barajevo": dict(
   extra=[("Kada instalacija ne postoji ni na jednom papiru",
     ["U Barajevu je veći deo instalacija izveden bez projekta, a priključci su vođeni "
      "kako je bilo moguće u trenutku gradnje — ponekad preko susedne parcele, ponekad "
      "u dve etape sa spojem na pola puta. Nacrta nema, a ljudi koji su to radili često "
      "nisu dostupni.",
      "Zato cenu ovde ne možemo da kažemo po tipu posla, kao u gradu. Prvo se traži "
      "trasa, pa se zna šta se radi. Da ne bi bilo nejasnoća: za traženje kažemo cenu "
      "unapred, a cenu same popravke posle toga, kada se vidi šta je nađeno — i tek tada "
      "se počinje.",
      "Kod septičkih jama uz to ide i provera stanja jame. Puna ili zarasla jama daje "
      "istu sliku kao zapušen vod, pa ako je čistimo bez te provere, isti poziv se "
      "ponavlja za nedelju dana."]),
   ],
   faq=[("Ne znamo kuda ide priključak. Kako se dogovara cena?",
      "U dva koraka. Za traženje trase kažemo cenu unapred, a cenu popravke posle toga, "
      "kada se vidi šta je nađeno — i tek tada se počinje. Ništa se ne radi bez "
      "dogovorene cene.")],
 ),
 "lazarevac": dict(
   extra=[("Instalacija menjana u delovima, kroz više decenija",
     ["U Lazarevcu najčešće zatičemo instalacije koje su menjane parcijalno: jedna "
      "deonica sedamdesetih, druga devedesetih, treća prošle godine. Svaka je urađena "
      "materijalom svog vremena i svaka je spojena na onu pre nje.",
      "Mesto kvara je zato gotovo uvek na spoju generacija, a ne u sredini deonice. "
      "Praktična posledica je da popravka jednog spoja ovde često povuče drugi — kada "
      "se pritegne nov fiting na staru cev, popusti sledeća najslabija veza.",
      "Zato kod planiranih radova dajemo pisanu ponudu sa popisom po stavkama i kažemo "
      "koje se deonice preporučuje zameniti u istom izlasku. To je skuplje jednom nego "
      "jedna popravka, ali jeftinije od tri popravke u godinu dana — i vi odlučujete, "
      "sa cenama pred sobom."]),
   ],
   faq=[("Zašto predlažete zamenu cele deonice, a ne samo spoja?",
      "Zato što se na parcijalno menjanim instalacijama posle popravke jednog spoja "
      "najčešće javi sledeći. Dajemo pisanu ponudu sa oba rešenja i cenama, pa vi "
      "odlučujete šta se radi.")],
 ),
 "mladenovac": dict(
   extra=[("Jedan izlazak, više poslova",
     ["Mladenovac je udaljeniji deo grada i to menja način dogovora. Umesto da se "
      "izlazi tri puta zbog tri sitnice, ovde planirane poslove skupljamo u jedan "
      "termin: zamena ventila, servis bojlera, montaža sanitarije i provera dvorišnog "
      "voda mogu da se završe u istom dolasku.",
      "Za vas je to povoljnije, jer se izlazak ne plaća po poslu, a za nas je jedini "
      "način da radimo ovde bez obećanja koja ne možemo da ispunimo. Kada pozovete, "
      "pitamo ima li još nešto što stoji — i to nije prodaja nego računica.",
      "Hitni pozivi su druga priča i tu ne planiramo. Kada je pukla cev ili se voda "
      "izliva, kažemo realno vreme koje nam treba do Mladenovca, bez zaokruživanja "
      "nadole da bi zvučalo bolje."]),
   ],
   faq=[("Isplati li se zvati zbog jedne sitnice?",
      "Isplati se skupiti nekoliko poslova u jedan termin, jer se izlazak ne plaća po "
      "poslu. Kada pozovete, pitamo ima li još nešto što stoji — zamena ventila, servis "
      "bojlera, montaža sanitarije mogu u istom dolasku.")],
 ),
 "sopot": dict(
   extra=[("Zima je ovde najčešći uzrok poziva",
     ["U Sopotu i okolnim selima više je nezaštićenih instalacija nego u gradu: spoljne "
      "česme, vodovi do pomoćnih objekata i letnjih kuhinja, deonice položene plitko ili "
      "iznad zemlje. Prva noć sa jačim mrazom odatle pravi većinu zimskih intervencija.",
      "Puca na mestima koja se mogu predvideti — na česmi koja nije ispražnjena, na "
      "priključku objekta koji se zimi ne koristi, na deonici uz severni zid. Sve tri se "
      "zatvore i isprazne unapred, u poslu od pola sata.",
      "Kada već pukne, ne čeka se. Prvo se zatvara voda i radi privremeno rešenje da se "
      "objekat može koristiti, a trajna sanacija se dogovara posle, kada se vidi obim. "
      "Na ukopanom priključku se pre kopanja locira mesto — zimi, u zamrznutom tlu, "
      "kopanje duž trase je najgori mogući trošak."]),
   ],
   faq=[("Pukla je cev u dvorištu zimi. Šta radite prvo?",
      "Zatvaramo vodu i radimo privremeno rešenje da objekat može da se koristi, a trajnu "
      "sanaciju dogovaramo kada se vidi obim. Na ukopanom vodu mesto prvo lociramo — "
      "kopanje duž trase u zamrznutom tlu je najveći trošak.")],
 ),
}


# ============================================================ SEO PO LOKACIJI
# Klijent je tražio da svaka lokacija ima svoj naslov i opis i da tekstovi ne
# budu isti sa zamenjenim imenom opštine. Ovde je, po slugu:
#   title, description, i naslovi (H2) za četiri odeljka koji su ranije bili
#   isti na svim stranama: instalacije / zbog čega zovu / usluge / cena.
SEO = {
 "novi-beograd": dict(
   title="Vodoinstalater Novi Beograd — vertikale u blokovima, 0–24",
   desc="Vodoinstalater na Novom Beogradu: odgušenje zajedničkih vertikala u blokovima, servis ugradnih vodokotlića i detekcija curenja u podu. Dežurstvo 0–24.",
   h2i="Blokovska izgradnja i novogradnja — dve različite priče",
   h2z="Tri poziva koja se na Novom Beogradu ponavljaju",
   h2u="Šta najviše radimo u blokovima i novogradnji",
   h2c="Ko plaća vertikalu, a ko odvod u stanu"),
 "zemun": dict(
   title="Vodoinstalater Zemun — pocinkovane cevi i dvorišni vodovi",
   desc="Vodoinstalater u Zemunu: zamena zaraslih pocinkovanih instalacija, odgušenje dvorišne kanalizacije i šahtova i detekcija curenja na ukopanom vodu. 0–24.",
   h2i="Zemun je mešavina starog grada i naselja sa kućama",
   h2z="Zbog čega nas iz Zemuna najčešće zovu",
   h2u="Šta najviše radimo u Zemunu",
   h2c="Zašto se u Zemunu cena često odluči na vodomeru"),
 "vozdovac": dict(
   title="Vodoinstalater Voždovac — podrumski razvod i nagib odvoda",
   desc="Vodoinstalater na Voždovcu: zapušenja u podrumskom razvodu, spoljna kanalizacija kod kuća i snimanje kamerom kada je nagib odvoda pogrešan. Izlazak 0–24.",
   h2i="Kosi teren odlučuje kako teku odvodi na Voždovcu",
   h2z="Zbog čega nas sa Voždovca najčešće zovu",
   h2u="Šta najviše radimo na Voždovcu",
   h2c="Kada je jeftinije snimiti nego čistiti po treći put"),
 "zvezdara": dict(
   title="Vodoinstalater Zvezdara — spojevi starog i novog razvoda",
   desc="Vodoinstalater na Zvezdari: curenje na spoju pocinkovane i nove cevi, odvodi bez pravilnog nagiba i odgušenje vertikala u starijim zgradama. Izlazak 0–24.",
   h2i="Zgrade iz više epoha, instalacije menjane u delovima",
   h2z="Zbog čega nas sa Zvezdare najčešće zovu",
   h2u="Šta najviše radimo na Zvezdari",
   h2c="Cena kada se ne zna šta je u zidu"),
 "palilula": dict(
   title="Vodoinstalater Palilula — izlivanje u prizemlju i podrumu",
   desc="Vodoinstalater na Paliluli: voda koja se vraća u prizemlja i podrume, odgušenje spoljne kanalizacije i skrivena curenja u vlažnom tlu. Dežurstvo 0–24.",
   h2i="Niska kota i vlažno tlo menjaju sve na Paliluli",
   h2z="Zbog čega nas sa Palilule najčešće zovu",
   h2u="Šta najviše radimo na Paliluli",
   h2c="Cena i šta uraditi dok voda još ulazi"),
 "cukarica": dict(
   title="Vodoinstalater Čukarica — naslage u vertikalama i ventili",
   desc="Vodoinstalater na Čukarici: naslage u starim vertikalama, zapekli ugaoni i zaporni ventili, dvorišni vodovi i septičke jame. Dežurstvo 0–24 svih sedam dana.",
   h2i="Blokovi, stare zgrade i kuće u istoj opštini",
   h2z="Zbog čega nas sa Čukarice najčešće zovu",
   h2u="Šta najviše radimo na Čukarici",
   h2c="Zapekao ventil: jeftino unapred, skupo u poplavi"),
 "rakovica": dict(
   title="Vodoinstalater Rakovica — ponovljena zapušenja i kamera",
   desc="Vodoinstalater na Rakovici: zapušenja koja se vraćaju u isti stan, snimanje kanalizacije kamerom, stari vodokotlići i curenje u zidu. Dežurstvo 0–24.",
   h2i="Stambeni fond iz sedamdesetih i osamdesetih",
   h2z="Zbog čega nas sa Rakovice najčešće zovu",
   h2u="Šta najviše radimo na Rakovici",
   h2c="Kada treći izlazak košta više od jednog snimanja"),
 "vracar": dict(
   title="Vodoinstalater Vračar — curenje kod komšije i vertikale",
   desc="Vodoinstalater na Vračaru: voda curi kod komšije ispod, renovirano kupatilo na staroj vertikali i odgušenje zajedničkog voda. Merimo pre otvaranja, 0–24.",
   h2i="Sređena kupatila na instalacijama koje nisu sređene",
   h2z="Zbog čega nas sa Vračara najčešće zovu",
   h2u="Šta najviše radimo na Vračaru",
   h2c="Cena merenja i zašto je ono ovde najisplativije"),
 "stari-grad": dict(
   title="Vodoinstalater Stari grad — stare zgrade i odvodi lokala",
   desc="Vodoinstalater na Starom gradu: nepoznate trase u starim zgradama, kuhinjski odvodi lokala i izlivanje u prizemlju i podrumu. Rad van špica, 0–24.",
   h2i="Zgrade starije od sto godina i instalacije bez plana",
   h2z="Zbog čega nas sa Starog grada najčešće zovu",
   h2u="Šta najviše radimo na Starom gradu",
   h2c="Dogovor sa lokalima: rad van radnog vremena"),
 "savski-venac": dict(
   title="Vodoinstalater Savski venac — detekcija bez razbijanja",
   desc="Vodoinstalater na Savskom vencu: curenje u objektima sa skupom obradom, dugi dvorišni razvodi i ugradni sistemi u novogradnji. Prvo merimo, pa otvaramo.",
   h2i="Objekti u kojima je obrada vrednija od popravke",
   h2z="Zbog čega nas sa Savskog venca najčešće zovu",
   h2u="Šta najviše radimo na Savskom vencu",
   h2c="Zašto merenje ovde gotovo uvek izađe jeftinije"),
 "surcin": dict(
   title="Vodoinstalater Surčin — dvorišni priključci i objekti",
   desc="Vodoinstalater u Surčinu: curenje na dugom dvorišnom priključku, odgušenje spoljne kanalizacije i instalacije u poslovnim objektima. Dežurstvo 0–24.",
   h2i="Duge parcele, dugi priključci, malo revizija",
   h2z="Zbog čega nas iz Surčina najčešće zovu",
   h2u="Šta najviše radimo u Surčinu",
   h2c="Cena i šta je dobro znati pre izlaska"),
 "grocka": dict(
   title="Vodoinstalater Grocka — septičke jame i nepoznate trase",
   desc="Vodoinstalater u Grockoj: septičke jame i spoljna kanalizacija, vodovi ispod betoniranih površina i snimanje kamerom pre kopanja. Izlazak 0–24.",
   h2i="Objekti građeni u fazama, instalacije dodavane kasnije",
   h2z="Zbog čega nas iz Grocke najčešće zovu",
   h2u="Šta najviše radimo u Grockoj",
   h2c="Kada se isplati snimiti pre nego što se kopa"),
 "obrenovac": dict(
   title="Vodoinstalater Obrenovac — podzemne vode i podrumi",
   desc="Vodoinstalater u Obrenovcu: visok nivo podzemnih voda, spoljna kanalizacija kod kuća i podrumske instalacije. U vlažnom tlu prvo merimo, pa otvaramo.",
   h2i="Visok vodostaj menja ono što vidite kao curenje",
   h2z="Zbog čega nas iz Obrenovca najčešće zovu",
   h2u="Šta najviše radimo u Obrenovcu",
   h2c="Vlaga nije dokaz curenja — zato se prvo meri"),
 "barajevo": dict(
   title="Vodoinstalater Barajevo — dugi priključci bez projekta",
   desc="Vodoinstalater u Barajevu: dugi i netrasirani priključci, septičke jame i veze ka objektu, instalacije rađene bez projekta. Izlazak 0–24, cena unapred.",
   h2i="Instalacije koje nemaju nacrt ni jednog metra",
   h2z="Zbog čega nas iz Barajeva najčešće zovu",
   h2u="Šta najviše radimo u Barajevu",
   h2c="Kako se dogovara cena kada trasa nije poznata"),
 "lazarevac": dict(
   title="Vodoinstalater Lazarevac — planirani radovi i odgušenje",
   desc="Vodoinstalater u Lazarevcu: parcijalno menjane instalacije, odgušenje kod porodičnih kuća i planirani radovi sa pisanom ponudom. Dežurstvo 0–24.",
   h2i="Instalacije menjane u delovima, kroz više decenija",
   h2z="Zbog čega nas iz Lazarevca najčešće zovu",
   h2u="Šta najviše radimo u Lazarevcu",
   h2c="Planirani radovi: ponuda pre nego što se počne"),
 "mladenovac": dict(
   title="Vodoinstalater Mladenovac — dvorišne instalacije i bojleri",
   desc="Vodoinstalater u Mladenovcu: spoljne i dvorišne instalacije, vertikale u gradskom jezgru, servis bojlera i montaža sanitarije. Izlazak 0–24, račun.",
   h2i="Gradsko jezgro i naselja sa kućama oko njega",
   h2z="Zbog čega nas iz Mladenovca najčešće zovu",
   h2u="Šta najviše radimo u Mladenovcu",
   h2c="Više poslova u jednom izlasku — i zašto je povoljnije"),
 "sopot": dict(
   title="Vodoinstalater Sopot — ukopani priključci i dvorišni vodovi",
   desc="Vodoinstalater u Sopotu: dvorišni vodovi i jame, curenje na ukopanom priključku i instalacije u starijim kućama. Lociramo pre kopanja, izlazak 0–24.",
   h2i="Starije kuće i instalacije koje idu kroz dvorište",
   h2z="Zbog čega nas iz Sopota najčešće zovu",
   h2u="Šta najviše radimo u Sopotu",
   h2c="Zimi je najčešći poziv pukla dvorišna cev"),
}

# Naselja — isto, po slugu naselja.
SEO_NASELJA = {
 "altina": dict(
   title="Vodoinstalater Altina — spoj starog i novog razvoda",
   desc="Vodoinstalater na Altini: curenje na spoju stare i nove cevi, slab pritisak u višim delovima naselja i dvorišna kanalizacija. Izlazak 0–24, Zemun.",
   h2z="Zbog čega nas sa Altine najčešće zovu",
   h2u="Šta najviše radimo na Altini"),
 "batajnica": dict(
   title="Vodoinstalater Batajnica — dugi priključci i pucanje zimi",
   desc="Vodoinstalater u Batajnici: curenje na dugom dvorišnom priključku, spoljna kanalizacija i jame, pucanje cevi tokom zime. Lociramo pre kopanja, 0–24.",
   h2z="Zbog čega nas iz Batajnice najčešće zovu",
   h2u="Šta najviše radimo u Batajnici"),
 "medakovic": dict(
   title="Vodoinstalater Medaković — vertikale i podrumski razvod",
   desc="Vodoinstalater na Medakoviću: odgušenje zajedničkih vertikala, dug podrumski razvod i voda koja se vraća u prizemlja. Dežurstvo 0–24, Voždovac.",
   h2z="Zbog čega nas sa Medakovića najčešće zovu",
   h2u="Šta najviše radimo na Medakoviću"),
 "banjica": dict(
   title="Vodoinstalater Banjica — zapekli ventili i vertikale",
   desc="Vodoinstalater na Banjici: ugaoni i zaporni ventili koji ne zatvaraju, naslage u vertikalama i curenje u podu i podrumskim prostorijama. Izlazak 0–24.",
   h2z="Zbog čega nas sa Banjice najčešće zovu",
   h2u="Šta najviše radimo na Banjici"),
 "vidikovac": dict(
   title="Vodoinstalater Vidikovac — pritisak na višim spratovima",
   desc="Vodoinstalater na Vidikovcu: slab pritisak na višim spratovima, zapušenja koja se ponavljaju i vertikale u blokovima. Dežurstvo 0–24, opština Rakovica.",
   h2z="Zbog čega nas sa Vidikovca najčešće zovu",
   h2u="Šta najviše radimo na Vidikovcu"),
 "miljakovac": dict(
   title="Vodoinstalater Miljakovac — ponovljena zapušenja",
   desc="Vodoinstalater na Miljakovcu: zapušenje koje se vraća u isti stan, vertikale sa naslagama i mešovita zona kuća i zgrada. Snimanje kamerom, izlazak 0–24.",
   h2z="Zbog čega nas sa Miljakovca najčešće zovu",
   h2u="Šta najviše radimo na Miljakovcu"),
 "zarkovo": dict(
   title="Vodoinstalater Žarkovo — preopterećen priključak i kuće",
   desc="Vodoinstalater u Žarkovu: priključak preopterećen dogradnjom, dvorišni vodovi kod kuća i curenje na starim instalacijama. Izlazak 0–24, Čukarica.",
   h2z="Zbog čega nas iz Žarkova najčešće zovu",
   h2u="Šta najviše radimo u Žarkovu"),
 "banovo-brdo": dict(
   title="Vodoinstalater Banovo brdo — nov razvod na staroj cevi",
   desc="Vodoinstalater na Banovom brdu: nov razvod spojen na staru vertikalu, naslage u vertikalama i curenje u renoviranom kupatilu. Merimo pre otvaranja, 0–24.",
   h2z="Zbog čega nas sa Banovog brda najčešće zovu",
   h2u="Šta najviše radimo na Banovom brdu"),
}


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

# ===================================== DOPUNA ZA NASELJA KOJA SU SI BILA BLIZU
# Banjica, Banovo brdo, Medaković, Vidikovac i Miljakovac su po tekstu bili
# najsličniji jedan drugom. Ovde svaki dobija odeljak i pitanja koja postoje
# samo na njegovoj strani, a zajednički pasusi su skraćeni.
NASELJA_EXTRA = {
 "banjica": dict(
   extra=[("Zašto se na Banjici ventil pokvari pre cevi",
     ["Banjica je građena kao celina, u jednom potezu, i to se vidi po tome što se kvarovi "
      "pojavljuju grupno. Stanovi su dobili istu ugradnu armaturu u isto vreme, pa kada "
      "ugaoni ventili počnu da zapekaju, to se u istom ulazu dešava u više stanova u roku od "
      "nekoliko godina. Nije slučajnost nego starost serije.",
      "Problem je u tome što ventil koji godinama stoji otvoren spoji vreteno sa telom "
      "kamencem i korozijom. Dok sve radi, to nikome ne pada na pamet. Otkrije se tek kada "
      "pukne crevo do mašine i kada ventil treba da zatvori vodu — a ne ide. Odatle do "
      "stana ispod prođe nekoliko minuta.",
      "Na Banjici zato predlažemo nešto što na drugim lokacijama retko spominjemo: ako je "
      "stan u originalnom stanju, zamena ugaonih i zapornog ventila u mirnom terminu je "
      "posao od pola sata, i jedini koji pouzdano sprečava poplavu. Kada ventil menjamo u "
      "panici, uz vodu po stanu, cena je ista — ali šteta nije."]),
    ("Podrumske prostorije i vlaga koja ne dolazi iz instalacije",
     ["Drugi poziv po učestalosti sa Banjice nije kvar nego vlaga u podrumskim "
      "prostorijama i ostavama. U zgradama ovog tipa kroz podrum prolazi razvod za ceo "
      "ulaz, pa je prva pretpostavka uvek da negde propušta cev.",
      "Češće nije. Vlaga u podrumu na Banjici obično dolazi iz tla i kondenzacije na "
      "hladnim cevima, a ne iz curenja. Razlika se vidi merenjem: ako pritisak na razvodu "
      "ne pada, instalacija ne propušta i kopanje ničemu ne vodi. To merenje je posao od "
      "pola sata i jedini način da se zna pre nego što se nešto otvori."]),
   ],
   faq=[("Da li vredi preventivno menjati ventile u stanu na Banjici?",
      "U stanovima koji su ostali sa originalnom armaturom — vredi. Jednom godišnje "
      "zatvorite i otvorite glavni ventil u stanu: ako ide teško ili škripi, zamena u "
      "mirnom terminu je posao od pola sata, a cena ista kao kod hitnog izlaska."),
     ("Vlaga je u podrumskoj ostavi — je li to curenje sa instalacije?",
      "Ne obavezno, i to se može proveriti bez kopanja. Ako razvod u podrumu drži "
      "pritisak, instalacija ne propušta, a vlaga dolazi iz tla ili kondenzacije. "
      "Merenje traje oko pola sata i radi se pre nego što se bilo šta otvara.")],
 ),
 "banovo-brdo": dict(
   extra=[("Sređeno kupatilo na vertikali iz sedamdesetih",
     ["Banovo brdo ima veći udeo renoviranih stanova nego okolna naselja i iz toga dolazi "
      "najčešći poziv. Kupatilo je novo: nove pločice, nova sanitarija, nov razvod u "
      "stanu. Vertikala na koju je sve to vezano je ista ona iz sedamdesetih, suženog "
      "preseka i sa naslagama po zidu cevi.",
      "Dok se ne pomeri, to radi. Kada se u renoviranju odvod pomeri, kada se doda tuš "
      "kabina sa ravnim sifonom ili kada se promeni nagib priključka do vertikale, "
      "ispostavi se da zajednički vod više ne prima isto. Posledica je zapušenje koje "
      "se vraća, i to u stanu u kojem je sve novo.",
      "Zato u sređenom kupatilu na Banovom brdu ne počinjemo mašinom nego pregledom: "
      "snimanje kamerom pokazuje da li je presek vertikale sužen i gde je granica između "
      "novog razvoda u stanu i starog zajedničkog voda. Bez toga se ista intervencija "
      "plaća tri puta, a uzrok ostaje gde je bio."]),
    ("Kako se radi u kupatilu u koje je uloženo",
     ["Kada je kupatilo skupo obrađeno, cena popravke prestaje da bude glavna stavka — "
      "glavna stavka je šta će ostati posle. Keramika u formatu koji se više ne proizvodi "
      "ne može da se nabavi za zakrpu, pa svaki otvoren kvadrat znači prepravku celog zida.",
      "Zbog toga redosled okrećemo: prvo merenje, pa otvaranje. Termovizija i akustično "
      "merenje suze zonu sa cele prostorije na konkretno mesto, i tada se skida jedna do "
      "dve pločice, obeležene unapred i uz vašu saglasnost. Ako revizioni otvor postoji, "
      "radi se kroz njega i ništa se ne dira."]),
   ],
   faq=[("Renovirali smo kupatilo, a zapušenje se vraća — zašto?",
      "Najčešće zato što je nov razvod u stanu vezan na staru vertikalu suženog preseka, "
      "ili je u renoviranju promenjen nagib priključka. Snimanje kamerom pokazuje da li je "
      "uzrok u vašem odvodu ili u zajedničkom vodu — i ko snosi trošak."),
     ("Hoće li pločice morati da se obijaju?",
      "Trudimo se da ne. Mesto se prvo locira merenjem, pa se otvara jedno do dva mesta, "
      "a ako postoji revizioni otvor, radi se kroz njega. Šta će se otvoriti, kažemo i "
      "pokažemo pre nego što počnemo.")],
 ),
 "medakovic": dict(
   extra=[("Dug podrumski razvod i zašto se voda vraća u prizemlje",
     ["Medaković je građen na kosini i to je najvažnija stvar za razumevanje poziva "
      "odavde. Zgrade su postavljene u nizu po terenu, a horizontalni razvod kroz "
      "podrume je dugačak — ponekad ide ispod dva ili tri ulaza pre nego što izađe na "
      "gradski kolektor.",
      "Na dugom horizontalnom vodu naslage se nakupljaju neravnomerno i prvi znak ne "
      "dobija stan u kojem je uzrok. Voda se vraća tamo gde je kota najniža: kroz "
      "slivnik u kupatilu prizemlja ili u podrumskoj prostoriji. Domaćinstvo iz "
      "prizemlja prijavi problem, a čep je često dvadeset metara dalje i tri ulaza "
      "niže od njega.",
      "Zato se ovde ne radi iz stana koji je pozvao. Ide se na reviziju u podrumu, "
      "sa koje se vidi cela trasa, i radi se mašinom odgovarajuće dužine. Kada se isto "
      "mesto zapuši drugi put, snimanje kamerom pokazuje da li je problem u naslagama "
      "ili u ulegnutoj deonici — a to su dva različita posla i dve različite cene."]),
    ("Ko plaća kada se voda vrati u prizemlje",
     ["Horizontalni razvod kroz podrum i vertikale su zajednički delovi zgrade, pa "
      "trošak po pravilu ide na stambenu zajednicu, a ne na stan u kojem se voda "
      "pojavila. To je na Medakoviću praktično pitanje, ne teorijsko: ljudi iz prizemlja "
      "ovde najčešće plaćaju tuđe zapušenje, jer su prvi primetili.",
      "Da se to ne bi ponovilo, odmah utvrđujemo da li je čep u odvodu stana ili u "
      "zajedničkom vodu, i to zapisujemo. Račun izdajemo i na stambenu zajednicu, pa "
      "upravnik ima dokument sa kojim može da raspolaže."]),
   ],
   faq=[("Voda se vraća kroz slivnik u prizemlju — da li je uzrok u mom stanu?",
      "Na kosom terenu najčešće nije. Voda izlazi tamo gde je kota najniža, a čep je "
      "obično dalje na horizontalnom razvodu kroz podrum. Prvo utvrđujemo gde je, pa "
      "se radi sa revizije — ne iz stana."),
     ("Ko plaća odgušenje podrumskog razvoda?",
      "Horizontalni razvod kroz podrum je zajednički deo zgrade i trošak ide na stambenu "
      "zajednicu. Izdajemo račun i na stambenu zajednicu, a nalaz o tome gde je bio čep "
      "dajemo napisan.")],
 ),
 "vidikovac": dict(
   extra=[("Visina naselja i pritisak na gornjim spratovima",
     ["Vidikovac je jedna od najviših točaka u ovom delu grada i to se oseti na "
      "poslednjim spratovima. Pritisak je tamo po prirodi slabiji, jer gradska mreža "
      "mora da digne vodu više nego u nizinskim naseljima. Deo stanara zato misli da je "
      "u kvaru nešto u stanu.",
      "Razlika se prepoznaje brzo. Ako je pritisak slab na svim izlivima i u svakom "
      "trenutku, u pitanju je visina i stanje zajedničkog razvoda. Ako je slab samo na "
      "jednom mestu ili samo na toploj vodi, kvar je u stanu — zapušen perlator, zarasla "
      "fleksibilna veza, ventil koji nije do kraja otvoren ili kamenac u bojleru.",
      "To razdvajanje radimo pre nego što predložimo bilo šta. Nema smisla menjati cevi "
      "u stanu zbog nečega što dolazi od visine naselja, a ni obrnuto — javljati "
      "upravniku problem koji je u vašem perlatoru."]),
    ("Zapušenje koje se vraća u blokovima na Vidikovcu",
     ["Druga stvar zbog koje nas zovu sa Vidikovca je zapušenje koje se ponavlja u "
      "istom stanu. Blokovi su tipski i vertikale su iste starosti, pa kada presek "
      "počne da se sužava, čišćenje drži sve kraće — prvi put godinu, drugi put "
      "nekoliko meseci, treći put nedeljama.",
      "Kada čujemo da je to treći put, ne predlažemo četvrto čišćenje. Snimanje "
      "kamerom pokazuje koliko je presek stvarno sužen i da li je problem u naslagama "
      "ili u samoj cevi. Jedan pregled tada izađe jeftinije od dva izlaska koja rešavaju "
      "posledicu."]),
   ],
   faq=[("Slab pritisak na poslednjem spratu — je li to kvar u stanu?",
      "Zavisi od toga gde je slab. Ako je slab na svim izlivima stalno, u pitanju je "
      "visina naselja i stanje zajedničkog razvoda. Ako je slab samo na jednom mestu ili "
      "samo na toploj vodi, kvar je u stanu i rešava se na licu mesta."),
     ("Isti odvod se zapušava po treći put — šta predlažete?",
      "Da se pregleda, ne da se ponovo čisti. Snimanje kamerom pokazuje koliko je presek "
      "sužen i da li je cev ulegla. Jedan pregled tada izađe jeftinije od dva izlaska "
      "koja rešavaju samo posledicu.")],
 ),
 "miljakovac": dict(
   extra=[("Miljakovac I, II i III — tri naselja, tri vrste poziva",
     ["Miljakovac se u svakodnevnom govoru zove jednim imenom, ali za majstora to nisu "
      "iste adrese. Starija zona ima zgrade sa zajedničkim vertikalama i tipskim "
      "razvodom; novija ima objekte podignute kasnije, sa drugačijim rešenjem odvoda; a "
      "između je zona individualnih kuća sa dvorišnim vodovima.",
      "Zato prvo pitanje na telefonu nije koji je kvar nego koji je deo naselja i je li "
      "u pitanju zgrada ili kuća. U zgradi je verovatno zajednička vertikala i trošak "
      "ide na stambenu zajednicu; u kući je dvorišni vod i trošak je vaš. To nije "
      "formalnost — od toga zavisi i sa kog mesta se radi i koja oprema dolazi.",
      "Mešovita zona ima i svoju posebnost: tamo gde se kuće vezuju na mrežu građenu "
      "za manji broj objekata, javlja se preopterećen priključak. Simptom izgleda kao "
      "zapušenje, a nije — i čišćenjem se ne rešava."]),
    ("Kada se isti stan zapušava stalno",
     ["Najčešći ponovljeni poziv sa Miljakovca je zapušenje koje se vraća u isti stan. "
      "To gotovo nikada ne znači da stanari nešto rade pogrešno; znači da je uzrok niže "
      "niz trasu i da čišćenje svaki put skloni samo ono što se nakupilo iznad njega.",
      "Posle drugog puta ima smisla pregledati umesto čistiti. Kamera pokazuje tri "
      "stvari koje se drugačije ne vide: koliko je presek sužen, ima li ulegnuća na "
      "deonici i da li je negde nagib pogrešan. Prve dve se rešavaju mašinom i "
      "ispiranjem, treća ne — i bolje je to znati pre nego posle."]),
   ],
   faq=[("U kom delu Miljakovca radite?",
      "U celom — Miljakovac I, II i III, kao i zonu sa kućama. Na telefonu pitamo koji "
      "je deo i je li u pitanju zgrada ili kuća, jer od toga zavisi sa kog mesta se radi "
      "i koja oprema dolazi."),
     ("Zapušenje se vraća u isti stan svakih nekoliko meseci. Šta je uzrok?",
      "Uzrok je skoro uvek niže niz trasu, a čišćenje svaki put skloni samo nakupljeno "
      "iznad njega. Posle drugog puta predlažemo snimanje kamerom: ono pokazuje da li je "
      "presek sužen, ima li ulegnuća i je li nagib pogrešan.")],
 ),
 "altina": dict(
   extra=[("Dve generacije instalacija u istoj kući",
     ["Na Altini je veliki deo kuća rastao u fazama — jedan deo podignut pa useljen, "
      "drugi dozidan nekoliko godina kasnije, treći kada se steklo. Instalacija je "
      "pratila tu logiku: do starog dela ide pocinkovana cev, do dozidanog PPR ili "
      "pocinkovana druge debljine, a spoj je napravljen tamo gde je bilo najlakše.",
      "Taj spoj je gotovo uvek mesto kvara. Različiti materijali se različito šire i "
      "skupljaju, a na prelazu pocinkovane cevi na novu često stoji improvizovan "
      "fiting koji je godinama držao i onda popustio. Pošto je veza obično u zidu ili "
      "pod naknadno betoniranim podom, voda izlazi daleko od mesta gde propušta.",
      "Zato je na Altini najkorisniji podatak koji nam možete dati — kada je i koji "
      "deo kuće dograđivan. Time se zona traženja sužava pre nego što iko dođe, a "
      "merenjem se zatim nađe tačno mesto, umesto da se otvara duž cele trase."]),
    ("Slab pritisak u višim delovima naselja",
     ["Drugi poziv po učestalosti nije curenje nego slab pritisak, najčešće u ulicama "
      "koje su više od glavne. Tu se spajaju dva razloga: dugački priključci sa ulice "
      "i pocinkovane cevi koje su iznutra zarasle kamencem i korozijom do polovine "
      "preseka.",
      "Zamena perlatora i creva u tom slučaju ne pomaže — problem je u cevi, a ne u "
      "armaturi. Pre nego što predložimo zamenu deonice merimo pritisak na ulazu i na "
      "izlivu, da se vidi gde se zaista gubi. Ako se gubi na priključku, menja se "
      "priključak; ako je unutra, menja se razvod u objektu."]),
   ],
   faq=[("Dozidali smo deo kuće i curi negde u zidu — kako to nalazite?",
      "Spoj starog i novog razvoda je najčešće mesto kvara i obično je zazidan. Mesto "
      "lociramo merenjem — akustično i termovizijom — pa se otvara tačno tu. Recite nam "
      "kada je koji deo kuće građen; to najviše skraćuje traženje."),
     ("Slab pritisak u celoj kući — treba li menjati cevi?",
      "Prvo merimo gde se pritisak gubi: na priključku sa ulice ili u razvodu unutra. "
      "Kod zaraslih pocinkovanih cevi zamena armature ne pomaže, ali nema smisla menjati "
      "razvod ako je uzrok na priključku.")],
 ),
 "batajnica": dict(
   extra=[("Priključak od dvadeset metara i račun koji ne odgovara potrošnji",
     ["U starijem delu Batajnice priključak od vodomera do objekta nije kratak kao u "
      "gradu — ume da bude dvadeset i više metara ukopanog voda kroz dvorište, često "
      "postavljenog pre nego što je ulica dobila kanalizaciju i bez zapisa gde tačno ide.",
      "Kada tu negde procuri, u dvorištu se najčešće ne vidi ništa. Voda se razlije u "
      "tlo, a prvi znak je račun za vodu koji je dvostruko veći bez promene u "
      "potrošnji. Vlažna mrlja na površini pojavi se mnogo kasnije, i to retko tačno "
      "nad mestom curenja.",
      "Kopati duž cele trase u takvoj situaciji nema smisla — to je trošak koji često "
      "pređe cenu nove cevi. Mesto se locira geofonom i akustičnim merenjem, obeleži "
      "se na površini i otvara se jedan do dva kvadrata. Tek tada se zna da li se "
      "sanira deonica ili se vodi nova linija."]),
    ("Zima: šta puca prvo i šta se može sprečiti",
     ["Batajnica ima više nezaštićenih instalacija u dvorištu nego gradska naselja — "
      "spoljne česme, vodovi do pomoćnih objekata, deonice koje su postavljene plitko "
      "ili iznad zemlje. Prva hladna noć ispod nule odatle pravi većinu zimskih poziva.",
      "Puca uglavnom na predvidivim mestima: na spoljnoj česmi koja nije ispražnjena, "
      "na nezaštićenoj deonici uz zid i na priključku pomoćnog objekta koji se zimi ne "
      "koristi. Sve tri se zatvaraju i prazne unapred, u poslu od pola sata, a to je "
      "razlika između zatvorenog ventila u novembru i pukle cevi u januaru."]),
   ],
   faq=[("Račun za vodu je skočio, a u dvorištu nema vlage. Šta to znači?",
      "Najčešće curenje na ukopanom priključku. Voda ide u tlo i na površini se ne vidi "
      "mesecima. Mesto lociramo geofonom i obeležimo na površini, pa se kopa jedan do dva "
      "kvadrata umesto cele trase."),
     ("Kako da zimi sprečim pucanje dvorišnih cevi?",
      "Pre prvih mrazeva zatvorite i ispraznite spoljnu česmu i priključke pomoćnih "
      "objekata koje zimi ne koristite, a nezaštićene deonice izolujte. To je posao od "
      "pola sata i sprečava većinu zimskih kvarova.")],
 ),
 "zarkovo": dict(
   extra=[("Mreža građena za manje objekata nego što ih sada ima",
     ["Žarkovo je u poslednje dve decenije dobilo znatno više stambenih jedinica nego "
      "što je imalo kada je mreža polagana. Na istu uličnu liniju i isti priključak "
      "vezano je danas više domaćinstava, a kod objekata koji su nadograđeni — i "
      "nekoliko stanova na priključku predviđenom za jednu kuću.",
      "Simptom izgleda kao kvar, a nije. Voda sporo otiče u više izliva odjednom, "
      "odvod se puni kada rade dve mašine, pritisak pada u večernjim satima kada svi "
      "troše. Mašinsko čišćenje u tom slučaju pomogne na nekoliko dana, jer uzrok nije "
      "čep nego kapacitet.",
      "Razlika se utvrđuje pre nego što se bilo šta čisti: merenjem protoka i, kada "
      "treba, snimanjem kamerom. Ako je u pitanju preopterećen priključak, rešenje je "
      "nova deonica odgovarajućeg preseka ili razdvajanje priključaka — i to je posao "
      "koji se planira, ne hitna intervencija."]),
    ("Kuće prema Savi i dvorišni vodovi",
     ["Niži deo Žarkova, prema Savi, pretežno je individualna izgradnja sa dvorišnim "
      "vodovima i, u delovima bez priključka, sa septičkim jamama. Tu je najčešći "
      "posao spoljna kanalizacija: veza objekta sa jamom ili sa uličnim priključkom, "
      "revizioni šahtovi i vodovi ispod betoniranih staza.",
      "Kod tih objekata najviše vremena odnese pronalaženje revizije, pa ako znate gde "
      "je vodomerni šaht i gde je revizija na spoljnoj kanalizaciji, recite nam to na "
      "telefonu. Ako septička jama postoji, koristan je i podatak kada je poslednji put "
      "pražnjena — jer jama koja je puna daje istu sliku kao zapušen vod."]),
   ],
   faq=[("Voda sporo otiče u više izliva, a čišćenje pomaže na par dana. Zašto?",
      "Zato što uzrok verovatno nije čep nego kapacitet priključka — na njega je vezano "
      "više jedinica nego što je predviđeno. To se utvrđuje merenjem protoka, a rešava "
      "novom deonicom odgovarajućeg preseka, ne čišćenjem."),
     ("Šta je korisno znati pre izlaska kod kuće u Žarkovu?",
      "Gde je vodomerni šaht i gde je revizija na spoljnoj kanalizaciji. Ako imate "
      "septičku jamu, recite kada je poslednji put pražnjena — puna jama daje istu sliku "
      "kao zapušen vod, a to su dva različita posla.")],
 ),
}

NASELJA_CHIPS = [("lokacije/vodoinstalater-%s" % n["slug"], n["ime"]) for n in NASELJA]

for _n in NASELJA:
    NASELJA_PO_OPSTINI.setdefault(_n["opstina"], []).append(_n)

for n in NASELJA:
    slug = "lokacije/vodoinstalater-%s" % n["slug"]
    ime, lok = n["ime"], n["lok"]
    rod = BY_SLUG[n["opstina"]]
    prof = n["profil"]
    seo = SEO_NASELJA.get(n["slug"], {})
    p = {
        "slug": slug,
        "title": seo.get("title") or "Vodoinstalater %s — odgušenje i hitne intervencije" % ime,
        "desc": seo.get("desc") or (
            "Vodoinstalater %s: odgušenje kanalizacije, detekcija curenja vode i hitne "
            "intervencije 0–24. Ista cena kao u ostatku Beograda, račun i garancija." % ime),
        "h1": "Vodoinstalater %s" % ime,
        "crumbs": [H, ("lokacije", "Lokacije"),
                   ("lokacije/vodoinstalater-%s" % rod["slug"], rod["ime"]), (slug, ime)],
        "schema": "service",
        "service_type": "Vodoinstalaterske usluge",
        "area": ime,
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
    ] + NASELJA_EXTRA.get(n["slug"], {}).get("faq", [])
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
        + sec(cards(seo.get("h2z") or "Zbog čega nas najčešće zovu %s" % lok,
                    [("", t, d, "") for t, d in n["problemi"]], page=p),
              cls="sec sec-alt")
        + "".join(sec(prose(h, paras), cls="sec sec-alt" if i % 2 else "sec")
                  for i, (h, paras) in enumerate(NASELJA_EXTRA.get(n["slug"], {}).get("extra", [])))
        + sec(_usluge_cards_naselje(p, prof, n["card4"], seo.get("h2u")), cls="sec sec-alt")
        + sec(prose("Cena i dogovor %s" % lok,
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
    seo = SEO.get(o["slug"], {})
    p = {
        "slug": slug,
        "title": seo.get("title") or "Vodoinstalater %s — odgušenje i hitne intervencije" % ime,
        "desc": seo.get("desc") or (
            "Vodoinstalater %s: odgušenje kanalizacije, detekcija curenja vode i hitne "
            "intervencije 0–24. Okvirna cena pre izlaska, račun i garancija." % ime),
        "h1": "Vodoinstalater %s" % ime,
        "crumbs": [H, ("lokacije", "Lokacije"), (slug, ime)],
        "schema": "service",
        "service_type": "Vodoinstalaterske usluge",
        "area": ime,
    }
    prof = o["profil"]
    dop = OPSTINE_EXTRA.get(o["slug"], {})
    extra_faq = o.get("extra_faq", []) + dop.get("faq", [])
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
        + sec(prose(seo.get("h2i") or "Kakve instalacije zatičemo %s" % lok,
                    [o["karakter"], o["karakter2"]])
              + '\n    <p class="intro" style="margin-top:18px"><strong>Naselja koja pokrivamo:</strong> %s.</p>' % o["naselja"],
              cls="sec")
        + sec(cards(seo.get("h2z") or "Zbog čega nas najčešće zovu %s" % lok,
                    [("", t, d, "") for t, d in o["problemi"]],
                    page=p),
              cls="sec sec-alt")
        + "".join(sec(prose(h, paras), cls="sec sec-alt" if i % 2 else "sec")
                  for i, (h, paras) in enumerate(o.get("extra", []) + dop.get("extra", [])))
        + sec(_usluge_cards(p, prof, o["slug"], seo.get("h2u")), cls="sec")
        + sec(prose(seo.get("h2c") or "Cena i dogovor",
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
