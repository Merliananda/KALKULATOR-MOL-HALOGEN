import streamlit as st
st.image("https://hids0.files.wordpress.com/2024/05/gambar-kelompok-5bjarbjirr.jpg")    

test = st.sidebar.selectbox("Navigation", ['Pendahuluan', 'Informasi Golongan Halogen',"Kalkulator Perhitungan mol Golongan Halogen"])

if test == "Pendahuluan":
        st.title(':violet[Informasi Unsur Periodik dan Kalkulator Perhitungan mol Golongan Halogen]')
    
        tombol=st.button('OLEH KELOMPOK 5')

        if tombol:
                st.write('▪ Kizhaya Allaida Azis (2360159)')
                st.write('▪ Merliana Ananda Putri (2360173)')
                st.write('▪ Nada Nabilah (2360196)')
                st.write('▪ Nazwa Aqilla Nasution (2360210)')
                st.write('▪ Wafiqah Azzahra Brira Amar (2360288)')
        st.markdown('''👩🏻‍🔬Halo sobat kimia, selamat datang di web kami.👩🏻‍🔬''')
        st.markdown('''Aplikasi ini dapat membantu kalian untuk mengenal lebih dalam mengenai Unsur Golongan Halogen''')

            
if test == "Informasi Golongan Halogen":

   tab1,tab2= st.tabs(["Informasi Golongan Halogen","Kegunaan Golongan Halogen"])

   with tab1:
        st.header("Informasi Golongan Halogen")
        st.write('Halogen adalah kelompok unsur kimia yang berada pada golongan 7 (VII atau VIIA) di tabel periodik. Halogen menandakan unsur-unsur yang menghasilkan garam jika bereaksi dengan logam. Halogen juga merupakan golongan dengan keelektronegatifan tertinggi, jadi ia juga merupakan golongan paling non-logam.')
        
   with tab2:
        st.header("Kegunaan Golongan Halogen")
        st.header(':blue[1. Industri Pulp dan Kertas]')
        st.write ('Salah satu unsur halogen yang sangat penting, klorin, digunakan dalam produksi pulp dan kertas. Selain itu, klorin juga membantu dalam memutihkan produk.') 
        st.header(':blue[2. Produksi obat-obatan]') 
        st.write('Brom digunakan dalam produksi obat-obatan sebagai bahan baku dalam produksi obat-obatan yang digunakan dalam pengobatan penyakit tertentu.')    
        st.header(':blue[3. Pemutih di Produksi Tekstil]')
        st.write('Bromin dan klorin adalah dua jenis unsur halogen yang digunakan sebagai agen pemutih. Biasanya pemutih ini digunakan untuk pembuatan bahan tekstil.')
        st.header(':blue[4. Kertas Foto]')
        st.write('Potassium bromide terbentuk saat bromin bereaksi dengan potasium. Hasilnya digunakan dalam produksi kertas foto.') 
        st.header(':blue[5. Industri Obat-obatan]')
        st.write('Beberapa jenis unsur halogen seperti klorin, fluorin, dan iodin bisa digunakan untuk berbagai jenis obat-obatan. Ketiga unsur ini sering juga digunakan sebagai pengganti di klinik kesehatan.')
        st.header(':blue[6. Garam Meja]')
        st.write(':blue Salah satu halogen paling penting, klorin, akan bereaksi saat dicampurkan dengan sodium. Keduanya digunakan untuk membuat garam meja. Iodine juga ditambahkan ke garam meja untuk kesehatan tiroid.')

if test == "Informasi Golongan Halogen":
        st.title(':blue[Yuk Mengenal Lebih Jauh Golongan Halogen 😊]')
       
        tab1,tab2,tab3,tab4,tab5= st.tabs(["Unsur Fluorin (F)","Unsur Klorin (Cl)","Unsur Bromin (Br)","Unsur Yodium (I)","Unsur Astatin (At)"])
        
        with tab1:
                st.header(':green[Unsur Fluorin (F)]')
                g1, g2, g3 =st.columns([1,2,1])
                with g1:
                   st.write('')
                with g3:
                   st.write('')
                with g2:
                   st.image('https://www.mastah.org/wp-content/uploads/2017/11/Fluor-F-Pengertian-Rumus-Kimia-dan-Fungsinya.jpg')

                st.header(':green[Sejarah Fluorin (F)]')
                st.write('adalah suatu unsur kimia dalam tabel periodik yang memiliki lambang F dan nomor atom 9. Namanya berasal dari bahasa Latin fluere, berarti "mengalir". Dia yaitu gas halogen univalen beracun berwarna kuning-hijau yg paling reaktif secara kimia dan elektronegatif dari segala unsur. Dalam bentuk murninya, dia sangat berbahaya, mampu menyebabkan pembakaran kimia parah begitu berhubungan dengan kulit. Orang yg dikenal sebagai penemu Fluor adalah seorang ahli kimia Prancis bernama Ferdinand Frederick Henri Moissan.')

                st.header(':green[Fakta Menarik Tentang Fluorin (F)]')
                st.write('1. Henri Moissan, yang pertama kali mengisolasi fluorin, juga menghasilkan berlian buatan pertama di dunia dengan menerapkan tekanan besar pada arang.')
                st.write('2. Fluorin adalah unsur reaktif paling secara kimia. Unsur Ini bereaksi seringkali sangat kuat dengan semua elemen lainnya kecuali oksigen, helium, neon dan kripton.') 
                st.write('3. Fluorin adalah unsur yang paling elektronegatif. Ini berarti bahwa dalam molekul fluorin menarik elektron lebih kuat daripada unsur lainnya.')
                st.write('4. Asam hidrofluorat, HF, melarutkan gelas. Ion fluoride memiliki afinitas tinggi untuk kalsium dan dapat menyebabkan kematian dengan mengganggu metabolisme kalsium darah tubuh saat diserap melalui kulit.')
       
                st.header(':green[Penampilan dan Karakteristik]')
                st.write('Efek berbahaya dari Fluorin sangat beracun dan korosif. Karakteristik Fluorin yaitu yang paling reaktif dan paling elektronegatif dari semua unsur. Fluorin adalah gas kuning pucat, diatomik, sangat korosif, mudah terbakar, dengan bau yang menyengat. Fluorin adalah halogen paling ringan. Unsur ini bereaksi keras dengan air untuk menghasilkan oksigen dan asam hidrofluorik yang sangat korosif.')
                st.header(':green[Sifat Fisik]')
                st.write('▪ Lambang dan Golongan:	F, Golongan VIII A,halogen dan non logam.')
                st.write('▪ Warna:	Kuning pucat')
                st.write('▪ Massa atom:	18,998403')                 
                st.write('▪ Bentuk:	gas')
                st.write('▪ Titik leleh:	-219.6 oC, 53.6 K')
                st.write('▪ Titik didih:	-188.1 oC, 85.1 K')
                         


        with tab2:
                st.header("Unsur Klorin (Cl)")
                g1, g2, g3 =st.columns([1,2,1])
                with g1:
                   st.write('')
                with g3:
                   st.write('')
                with g2:
                   st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Chlorine_in_bottle.jpg/330px-Chlorine_in_bottle.jpg')

                st.header("Sejarah Klorin (Cl)")
                st.write('Pada tahun 1810 konsensus ilmiah menyatakan bahwa unsur yang sekarang kita sebut klorin sebenarnya adalah senyawa yang mengandung oksigen. Ahli kimia Inggris Sir Humphry Davy menemukan bahwa konsensus itu salah, dia tidak bisa mendapatkan gas kuning-hijau baru untuk bereaksi dengan elektroda arang, yang membuatnya percaya bahwa itu mungkin tidak mengandung oksigen. Dalam reaksi dengan fosfor dan amonia, ia mendemonstrasikan gas baru tersebut tidak mengandung oksigen. Dia menggunakan timbunan volta berukuran besar 2000 untuk mengetahui apakah dia bisa mengekstrak oksigen dari senyawa fosfor dan sulfur gas, tapi sekali lagi dia tidak menemukan oksigen. Pada tahun 1811, Davy menyimpulkan gas baru itu sebenarnya adalah elemen baru. Dia menamakannya klorin, dari kata Yunani ‘chloros,’ yang berarti hijau pucat atau hijau kuning.')

                st.header("Fakta Menarik Tentang Klorin (Cl)")
                st.write('1. Reaksi rantai pertama yang ditemukan bukanlah reaksi nuklir, tetapi adalah reaksi berantai kimia. Ditemukan pada tahun 1913 oleh Max Bodenstein, yang melihat campuran gas klorin dan hidrogen meledak saat dipicu oleh cahaya. Mekanisme reaksi berantai sepenuhnya dijelaskan pada tahun 1918 oleh Walther Nernst.')
                st.write('2. Lautan di bumi mengandung sejumlah besar klorin. Jika klorin ini dilepaskan sebagai gas, beratnya akan 5x lebih besar dari atmosfer arus total bumi. (Lautan kita mengandung sekitar 2,6 x 1016 metrik ton klorin, kebanyakan sebagai natrium klorida.)')
                st.write('3. Klorin tidak hanya berlimpah di lautan kita, selain itu klorin adalah elemen keenam yang paling melimpah di kerak bumi.')
                st.write('4. Terkena sejumlah kecil klorin, meski untuk waktu yang singkat, bisa mematikan. Kematian diperkirakan terjadi pada 1 bagian dalam seribu klorin di udara (atau kadang-kadang pada konsentrasi yang lebih rendah).')
                st.write('5. Klorin lebih berat dari pada udara. Saat dilepaskan, ia membentuk selimut beracun yang hanyut seiring angin. Klorin digunakan sebagai senjata kimia dalam Perang Dunia I, pertama kali pada tahun 1915 oleh tentara Jerman dan kemudian oleh Sekutu Barat. Senjata itu tidak ‘efektif’ seperti yang diharapkan, karena klorin mudah dideteksi oleh baunya yang kuat. Selain itu juga klorin larut dalam air, sehingga tentara dapat melindungi diri dari dampak terburuknya dengan cara bernapas melalui kain lembab.')

                st.header('Penampilan dan Karakteristik')
                st.write('Efek berbahaya dari Klorin adalah gas beracun yang mengiritasi kulit, mata dan sistem pernafasan. Karakteristik Klorin adalah gas kuning keabu-abuan, diatomik, padat dengan bau tajam (bau pemutih). Klorin tidak ditemukan bebas di alam karena mudah bergabung dengan hampir semua elemen lainnya. Klorin terjadi di alam terutama sebagai garam biasa (NaCl), karnala [KMgCl2.6 (H20)], dan sylvite (KCl). Dalam bentuk cair dan padat, ini adalah zat pemutihan, pengoksidasi dan desinfektan yang kuat.')
                st.header('Sifat Fisik')
                st.write('▪ Lambang dan Golongan:	Cl, Golongan VIII A,halogen dan non logam.')
                st.write('▪ Warna:	Kuning kehijauan')
                st.write('▪ Massa atom:	35,453')                 
                st.write('▪ Bentuk:	gas')
                st.write('▪ Titik leleh:	-219.6 oC, 53.6 K')
                st.write('▪ Titik didih:	-188.1 oC, 85.1 K')
                
        with tab3:
                st.header(':brown[Unsur Bromin(Br)]')
                g1, g2, g3 =st.columns([1,2,1])
                with g1:
                   st.write('')
                with g3:
                   st.write('')
                with g2:
                   st.image('https://cdn.mos.cms.futurecdn.net/S6SNpRNQFXaMCyyYttoQcc.jpg')

                st.header(':brown[Sejarah Bromin (Br)]')
                st.write('Pada tahun 1824 Antoine Balard, berusia 21, sedang mempelajari kehidupan tanaman di rawa garam di Montpellier, Prancis. Dia menjadi tertarik dengan deposit garam yang dia lihat dan mulai menginvestigasi deposit garam tersebut. Dia mengambil air asin (air laut yanggaramnya dipekatkan dengan menguapkan airnya) dan mengkristalkan garan darinya. Dia mengambil cairan yang tersisa dan menjenuhkannya dengan klorin. Dia kemudian menyaring larutan untuk meninggalkan cairan merah tua. Waspada terhadap kemungkinan bahwa dia telah menemukan sesuatu yang sangat menarik, Balard memberi amplop tertutup kepada Akademi Perancis yang berisi hasil awal nya pada tahun 1824. Dia akhirnya menerbitkan hasilnya pada tahun 1826, memberikan bukti bahwa zat yang dia temukan adalah ‘tubuh sederhana’ baru, yaitu sebuah elemen, bukan senyawa Sebagai yang pertama mempublikasikan, ia menjadi penemu bromin. Akademi Perancis menamai unsur baru setelah kromosom Yunani untuk ‘bau busuk’  karena brom, cukup sederhana dan  berbau busuk.')
        
                st.header(':brown[Fakta Menarik tentang Bromin (Br)]')
                st.write('1. Bromin digunakan dalam pemurnian air, obat-obatan, dan pembersih.')
                st.write('2. Bromin juga digunakan untuk menurunkan emisi merkuri dari pembangkit listrik tenaga batu bara hingga 90%. Penambahan brom ke dalam proses mengoksidasi merkuri, sehingga lebih mudah diperoleh kembali dengan menggunakan perangkat pengontrol emisi.')
                st.write('3. Tubuh manusia mengandung sekitar 0,0004 persen bromin, namun tidak diketahui kegunaan bromin dalam tubuh manusia.')
                st.write('4. Bahan kimia bromida secara historis telah digunakan sebagai obat penenang dan antikonvulsan. Secara khusus, natrium bromida dan kalium bromida digunakan pada abad kesembilan belas dan kedua puluh sebelum digantikan oleh kloral hidrat, yang kemudian digantikan oleh barbiturat dan obat-obatan lainnya.')
                st.header(':brown[Penampilan dan Karakteristik]')
                st.write('Efek berbahaya dari Bromin adalah beracun dan menyebabkan kulit terbakar adalah gas beracun yang mengiritasi kulit. Karakteristik Bromin yaitu Brom murni dalam bentuk diatomik, Br2. Bromin adalah satu-satunya elemen nonmetalik yang cair pada suhu biasa. Bromin merupakan cairan padat dan kemerahan yang mudah menguap dengan mudah pada suhu kamar sampai uap merah dengan bau seperti klorin yang kuat. Bromin kurang reaktif daripada klor atau fluorin tapi lebih reaktif daripada yodium. Brom ini membentuk senyawa dengan banyak unsur dan, seperti klorin, bertindak sebagai agen pemutih.')
                st.header(':brown[Sifat Fisik]') 
                st.write('▪ Lambang dan Golongan:	Br, Golongan VIII A,  halogen dan non logam.')
                st.write('▪ Warna:	Merah')
                st.write('▪ Massa atom:	79,904')                 
                st.write('▪ Bentuk:	Liquid')
                st.write('▪ Titik leleh:	265,95 K | -7,2 °C | 19,04 °F')
                st.write('▪ Titik didih:	331,95 K | 58,8 °C | 137,84 °F')
       
        with tab4:
                st.header(':orange[Unsur Yodium (I)]')
                g1, g2, g3 =st.columns([1,2,1])
                with g1:
                   st.write('')
                with g3:
                   st.write('')
                with g2:
                   st.image('https://cdn.britannica.com/68/132468-050-9DE736C3/Iodine.jpg')

                st.header(':orange[Sejarah Yodium (I)]')
                st.write('Yodium ditemukan oleh Bernard Courtois pada tahun 1811 di Perancis. Courtois mencoba untuk mengambil Kalium Klorida dari rumput laut. Setelah mengkristalkan kalium klorida, ia menambahkan asam sulfat ke cairan yang tersisa. Ini, agak mengejutkan karenamenghasilkan uap ungu, yang kental menjadi kristal gelap. Ini adalah kristal yodium pertama yang pernah dibuat.')
                st.write('Courtois mempelajari zat baru ini dan menemukan bahwa keduanya bisa dikombinasikan dengan fosfor dan hidrogen, namun tidak membentuk senyawa dengan mudah bila dikombinasikan dengan karbon atau oksigen. Dia juga menemukan bahwa bila dicampur dengan amonia, maka zat tersebut membentuk padatan berwarna coklat (nitrogen triiodide) yang meledak saat sedikit tersentuh. Nama yodium berasal dari karya Yunani iodes yang berarti ungu.')


                st.header(':orange[Fakta Menarik Yodium (I)]')
                st.write('1. Yodium mengatur metabolisme: Yodium adalah unsur utama hormon tiroid yang penting untuk pertumbuhan dan metabolisme dalam tubuh manusia.Kelenjar tiroid berhubungan dengan laju metabolisme kita, mengontrol energi sel dan terlibat dalam hampir semua proses di dalam tubuh.Jika tiroid tidak mendapatkan cukup yodium, tiroid akan berhenti berfungsi secara efektif dan membengkak sehingga menyebabkan terbentuknya benjolan di bagian depan leher yang disebut gondok.')
                st.write('2. Otak kita membutuhkan yodium Yodium sangat penting untuk perkembangan otak janin. Hal ini sangat penting pada tiga bulan pertama kehamilan karena pertumbuhan kelenjar tiroid bayi baru mulai terlihat pada usia sekitar 14 minggu.')
                st.write('3. Yodium radioaktif dapat menyembuhkan kanker Paparan isotop yodium radioaktif bisa sangat berbahaya. Setelah bencana nuklir di Chernobyl, anak-anak terkena kanker tiroid karena mengonsumsi susu yang diproduksi secara lokal.Namun hal ini juga dapat dimanfaatkan untuk kebaikan: kita dapat menggunakan yodium radioaktif, zat yang sama yang dilepaskan setelah insiden nuklir, untuk mengobati kanker tiroid. Yodium radioaktif diarahkan pada sel-sel yang ingin kita bunuh, termasuk sel-sel kanker yang berasal dari tiroid yang telah menyebar ke bagian lain dari tubuh. Meski dosis yang lebih kecil dapat menyebabkan kanker, namun dosis yang tepat dapat mengobatinya.')
                st.write('4. Dapat digunakan untuk mengawetkan cat. Cat berbahan dasar air rentan terhadap kontaminasi, jamur dan jamur, serta memerlukan antimikroba atau biosida untuk bertindak sebagai pengawet. Dan di situlah peran yodium. Biosida berbahan dasar yodium sering digunakan sebagai pengawet dalam kaleng, serta membantu mencegah tumbuhnya jamur setelah aplikasi. Tidak ada yang menginginkan cetakan berjamur')
                st.header(':orange[Penampilan dan Karakteristik]')
                st.write('Efek berbahaya dari Yodium dalam dosis kecil, yodium sedikit beracun dan sangat beracun dalam jumlah besar. Yodium unsur adalah iritasi yang dapat menyebabkan luka pada kulit. Uap yodium menyebabkan iritasi mata ekstrim. Karakteristik Yodium adalah non logam, namun unsur tersebut menampilkan beberapa sifat logam. Bila dilarutkan dalam kloroform, karbon tetraklorida atau karbon disulfida, yodium menghasilkan larutan berwarna ungu. Larutan ini hampir tidak larut dalam air, merupakan larutan yang berwarna kuning.')
                st.header(':orange[Sifat Fisik]') 
                st.write('▪ Lambang dan Golongan:	I, Golongan VIII A,  halogen dan non logam.')
                st.write('▪ Warna:	Biru Keabu-abuan')
                st.write('▪ Massa atom:	126,90447')                 
                st.write('▪ Bentuk:	Solid')
                st.write('▪ Titik leleh:	386,85 K | 113,7 °C | 236,66 °F')
                st.write('▪ Titik didih:	457,4 K | 184,25 °C | 363,65 °F')
                
        with tab5:
                st.header(':red[Unsur Astatin (At)]')
                g1, g2, g3 =st.columns([1,2,1])
                with g1:
                   st.write('')
                with g3:
                   st.write('')
                with g2:
                   st.image('https://th.bing.com/th/id/OIP.TkH3MRvOhVqRXuRhXaQ2PgHaEK?rs=1&pid=ImgDetMain')

                st.header(':red[Sejarah Astatin (At)]')
                st.write('Astatine pertama kali diproduksi pada tahun 1940 oleh Dale R. Coson, Kenneth Ross Mackenzie dan Emilio Segrè di University of California, Berkeley. Segrè, bekerja dengan Carlo Perrier, sebelumnya telah mensintesis teknesium pada tahun 1937.')
                st.write('Astatine dibuat dengan membombardir bismut-209 dengan partikel alfa dalam siklotron (akselerator partikel) untuk diproduksi, setelah emisi dua neutron, astatine-211. Para ilmuwan menemukan bahwa isotop yang mereka buat bersifat radioaktif, jadi mereka menamakan unsur tersebut dengan menggunakan kata astatos Yunani yang berarti tidak stabil. Sekarang diketahui bahwa tidak ada isotop astatine yang stabil, isotop terpanjang yang tinggal, astatine-210, memiliki waktu paruh 8,3 jam. Tiga tahun kemudian, astatine ditemukan di alam oleh Berta Karlik dan Traude Bernert sebagai zat antara dalam rangkaian peluruhan radioaktif. Jejak elemen muncul secara alami di uranium dan mineral thorium sebagai produk peluruhan. Pada waktu tertentu, sekitar 25 gram astatine alami ada di planet kita.')

                st.header(':red[Fakta Menarik Astatin (At)]')
                st.write('1. Astatine dinamakan menurut kata Yunani astatos, yang berarti tidak stabil (Jefferson Laboratory).')
                st.write('2. Hanya ada sekitar 25 gram astatine alami di kerak bumi pada waktu tertentu (Chemicool).')
                st.write('3. Menurut Lenntech, astatine adalah unsur kimia halogen terberat yang pernah diketahui. Menurut Elemental Matter, unsur halogen, termasuk astatine, memiliki sifat serupa.')
                
                st.write(':red[Sifat-sifatnya antara lain:]')
                st.write('- termasuk unsur golongan nonlogam')
                st.write('- memiliki titik leleh dan titik didih yang rendah')
                st.write('- rapuh saat padat')
                st.write('- konduktor panas dan listrik yang buruk')
                st.write('- bersifat diatomik (molekulnya mengandung dua atom).')
                st.write('4. Astatine paling tidak reaktif dan memiliki sifat logam paling banyak dibandingkan kelompok unsur halogen lainnya (Chemicool).')
                st.write('5. Astatine sangat radioaktif namun hampir tidak menimbulkan efek kesehatan atau lingkungan sama sekali karena kelangkaan dan waktu paruh yang sangat singkat (Lenntech).')
                st.write('6. Meskipun jika seseorang bersentuhan dengannya, astatine diperkirakan menumpuk di kelenjar tiroid serupa dengan yodium.')
                st.header(':red[Penampilan dan Karakteristik]')
                st.write('Efek berbahaya dari Astatin adalah sangat radioaktif. Karakteristiknya adalah dan hanya tersedia dalam jumlah kecil. Sifat-sifatnya disimpulkan dari posisinya di tabel periodik dan dengan mempelajari kimia dalam larutan yang sangat encer. Seperti halogen lainnya, astatine diharapkan bisa membentuk garam dengan logam seperti natrium. Astatin juga dapat bereaksi dengan hidrogen untuk membentuk hidrogen astatide, yang bila dilarutkan dalam air, membentuk asam hidrokarbon. Astatin adalah yang paling tidak reaktif secara kimia dari halogen dan menunjukkan sifat logam dari kelompok halogen.')
                st.header(':red[Sifat Fisik]') 
                st.write('▪ Lambang dan Golongan:	At, Golongan VIII A,  halogen dan non logam.')
                st.write('▪ Warna:	Perak')
                st.write('▪ Massa atom:	210')                 
                st.write('▪ Bentuk:	Solid')
                st.write('▪ Titik leleh:	575,15 K | 302 °C | 575,6 °F')
                st.write('▪ Titik didih:	610,15 K | 337 °C | 638,6 °F')
    
if test == "Kalkulator Perhitungan mol Golongan Halogen":
                st.title(':blue[🧮 Menghitung mol Golongan Halogen 🧮]')

                st.header('🧪 Atom Relatif (Ar) Golongan Halogen 🧪')
                st.write('▪ Fluorin (F)  =19')
                st.write('▪ Klorin (Cl) =35,5')
                st.write('▪ Bromin (Br) =80')
                st.write('▪ Iodin (I)  =127')
                st.write('▪ Astatin (At) =210')

                st.header('🧮 Kalkulator Menghitung mol 🧮')
                options=st.selectbox('Nama Unsur Golongan Halogen',['F','Cl','Br','I','At'])
               
                x = st.number_input('Masukkan Massa Padatan dari Unsur Golongan Halogen yang Telah dipilih dalam Satuan g:')
                y = st.number_input('Masukkan Massa Atom Relatif (Ar) Golongan Halogen yang telah dipilih dalam satuan g/mol')

                tombol = st.button('Hitung Jumlah mol dari Suatu Golongan Halogen')

                if tombol:
                        jumlah_mol = x/y
                        st.success(f'Jumlah mol Adalah {options} {jumlah_mol}')