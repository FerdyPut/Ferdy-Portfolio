import streamlit as st

def tampilkan_tentang_saya():
    st.title("👋 Tentang Saya")
    st.success("Ini adalah menu bagian perkenalan mengenai saya secara menyeluruh")

    tab1, tab2, tab3,tab4, tab5 = st.tabs(["Profil Saya", "Pendidikan" , "Pengalaman", "Sertifikat", "Skills"])

    with tab1:
        col1, col2 = st.columns([1, 4])  # proporsi bisa diubah sesuai keinginan

        with col1:
            st.image(
                "https://www.dropbox.com/scl/fi/a8phjdi8h4ifye0q1lbw1/IMJ09756-2.jpg?rlkey=9vtaxvh5frj8acaxowcxoppqn&st=5v4yb10i&raw=1",
                width=120  # ukuran gambar bisa disesuaikan
            )

        with col2:
            st.markdown("""
                        <div style='padding-top: 10px; margin-left: -20px; text-align: justify;'>
                Halo semuanya! Perkenalkan, saya Ferdyansyah Permana Putra aka <b>Ferdy</b>, lulusan dari program studi Statistika Bisnis di Institut Teknologi Sepuluh Nopember (ITS).  
                Saya memiliki ketertarikan dan semangat yang besar di bidang <b>Data Analyst/Data Scientist</b>, terutama dalam mengeksplorasi data, membangun insight yang berdampak,  
                serta menyajikannya melalui visualisasi yang informatif untuk mendukung proses <b>pengambilan keputusan strategis</b>.
                    </div>
            """, unsafe_allow_html=True)
        st.markdown(
            """
            <div style='text-align: justify;'>
            <b>Saat ini</b>, saya sedang memperdalam kemampuan saya melalui program bootcamp di <b>DIBIMBING.ID (Full Stack Data Scientist</b>,  
                sebagai bagian dari upaya saya untuk terus berkembang di dunia data terutama Data Analyst/Data Scientist.
            </div>
            <p>
            <div style="display: flex; justify-content: center;">
                <img src="https://www.dropbox.com/scl/fi/595juaruen2kqchs2ozh0/Big-Data.jpg?rlkey=te6s30egvw0laktsnk22wvdio&st=bnl1y5sk&raw=1" width="200" />
            </div>
            <p style="text-align: center;">Source: https://ilm.uai.ac.id/</p>
            """,
            unsafe_allow_html=True
        )

        st.markdown(""" 
            <div style='text-align: justify;'>
            Passion saya pada bidang data bermula dari rasa ingin tahu yang tinggi terhadap pola, tren, dan bagaimana data dapat digunakan secara efektif untuk mendorong pertumbuhan dan inovasi bisnis. 
            Saya percaya bahwa kekuatan data terletak pada bagaimana kita memahaminya dan menerjemahkannya menjadi aksi yang bernilai.

            Berikut beberapa pengalaman yang mendukung perjalanan saya di bidang ini:
                 
            - Menjadi Asisten Dosen di bidang Eksplorasi dan Visualisasi Data (Tahun 2023)
            - Menjadi Asisten Dosen di bidang Statistika Non Parametrik (Tahun 2023)
            - Magang di PT. Telekomunikasi Indonesia, Tbk. sebagai Data Processing and Visualization (2024)
                  
            Saya selalu terbuka terhadap kolaborasi, tantangan baru, dan kesempatan untuk terus berkembang sebagai seorang Data Analyst/Scientist 
            yang tidak hanya menganalisis data, tetapi juga memberikan nilai strategis dari informasi yang ada. **Sehingga, bisa berkontribusi positif kepada perusahaan nantinya
            dengan informasi yang saya lakukan sebagai Data Analyst/Data Scientist**.
                </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.write("### Pendidikan")

        # State untuk aktivitas
        if "show_activity" not in st.session_state:
            st.session_state["show_activity"] = False

        def toggle_activity():
            st.session_state["show_activity"] = not st.session_state["show_activity"]

        col1, col2, = st.columns([2, 1])
        with col1:
            # Box Title ITS dengan efek hover & zoom saat diklik
            st.markdown(
                """
                <style>
                .zoom-box {
                    background-color: white; 
                    padding: 5px 10px; 
                    border-radius: 5px; 
                    display: inline-block; 
                    margin-bottom: 10px;
                    cursor: pointer;
                    transition: transform 0.2s ease-in-out;
                    
                }
                .zoom-box:hover {
                    transform: scale(1.05);
                }
                .modal {
                    display: none; 
                    position: fixed; 
                    z-index: 99; 
                    padding-top: 100px; 
                    left: 0;
                    top: 0;
                    width: 100%; 
                    height: 100%;
                    background-color: rgba(0,0,0,0.7);
                }
                .modal-content {
                    margin: auto;
                    display: block;
                    width: 300px;
                }
                </style>
                <div class="zoom-box" onclick="document.getElementById('modal-img').style.display='block'">
                    <strong>Institut Teknologi Sepuluh Nopember</strong>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <style>
                .sticky-container {
                    position: sticky;
                    top: 10px; /* Adjust this value to set the top position */
                    z-index: 10;
                }
                </style>

                <div class="sticky-container">
                    <div style="display: flex; align-items: center;">
                        <img src="https://katamata.wordpress.com/wp-content/uploads/2011/12/lambang-its-png-v1.png" width="100" style="margin-right: 10px;" />
                        <div>
                            <span><strong>Jurusan:</strong> Statistika Bisnis</span>
                            <p style="margin-top: 5px;"><strong>Periode:</strong> Sept 2020 - Sept 2024</p>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.button("Aktivitas/Kegiatan", on_click=toggle_activity)
            if st.session_state["show_activity"]:
                st.markdown(
                    """
                    **Aktivitas Selama Kuliah:**
                    - Menjadi asisten dosen beberapa mata kuliah yang relevan dengan passion saya sebagai Data Analyst/Data Scientist.
                    - Pernah aktif mengikuti beberapa kegiatan kepanitiaan organisasi (himpunan), seperti: Sigma Sambang Kampung, Event Welcome Vokasi 2022, Acara Pelepasan Wisuda, Acara Lomba jurusan
                        yaitu OLFACTION 2021 dan SINCOMP 2022.
                    - Mengikuti beberapa lomba, salah satunya diadakan di Universitas Airlangga Tahun 2023
                    - Mengikuti beberapa pelatihan mengenai *soft skills* dan *hard skills*, seperti LKMM TD, LKMW TD, Pelatihan Manajemen
                        Mutu, Pelatihan Manajemen Resiko, dan lainnya.
                    - Menjuarai lomba Vokasi Project Tahun 2023 dan AESEC di Univeristas Airlangga Tahun 2023.
                    """,
                    unsafe_allow_html=True
                )
        st.markdown("<hr>", unsafe_allow_html=True)
        with tab3:
            st.write("### Pengalaman")
                # State untuk aktivitas
            if "show_activity2" not in st.session_state:
                st.session_state["show_activity2"] = False

            def toggle_activity2():
                st.session_state["show_activity2"] = not st.session_state["show_activity2"]

            if "show_activity3" not in st.session_state:
                st.session_state["show_activity3"] = False

            def toggle_activity3():
                st.session_state["show_activity3"] = not st.session_state["show_activity3"]

            if "show_activity4" not in st.session_state:
                st.session_state["show_activity4"] = False

            def toggle_activity4():
                st.session_state["show_activity4"] = not st.session_state["show_activity4"]

            col1, col2, = st.columns([2, 1])
            with col1:
                # Box Title
                st.markdown(
                    """
                    <style>
                    .zoom-box {
                        background-color: white; 
                        padding: 5px 10px; 
                        border-radius: 5px; 
                        display: inline-block; 
                        margin-bottom: 10px;
                        cursor: pointer;
                        transition: transform 0.2s ease-in-out;
                        
                    }
                    .zoom-box:hover {
                        transform: scale(1.05);
                    }
                    .modal {
                        display: none; 
                        position: fixed; 
                        z-index: 99; 
                        padding-top: 100px; 
                        left: 0;
                        top: 0;
                        width: 100%; 
                        height: 100%;
                        background-color: rgba(0,0,0,0.7);
                    }
                    .modal-content {
                        margin: auto;
                        display: block;
                        width: 300px;
                    }
                    </style>
                    <div class="zoom-box" onclick="document.getElementById('modal-img').style.display='block'">
                        <strong>1. PT. Siantar Top, tbk.</strong>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <style>
                    .sticky-container {
                        position: sticky;
                        top: 10px; /* Adjust this value to set the top position */
                        z-index: 10;
                    }
                    </style>

                    <div class="sticky-container">
                        <div style="display: flex; align-items: center;">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/Logo_Siantar_Top.svg" width="100" style="margin-right: 10px;" />
                            <div>
                                <span><strong>Divisi:</strong> Business Support Information (BSI) - Data Analyst</span>
                                <p style="margin-top: 5px;"><strong>Periode:</strong> Jan 2025 - Sekarang</p>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                st.button("Jobdesk", on_click=toggle_activity2, key="button2")
                if st.session_state["show_activity2"]:
                    st.markdown(
                        """
                        **Jobdesk:**
                        - Menganalisis data-data terkait Sales, Promo, dan Distributor menggunakan Excel dan Python.
                        - Menghandle survei promo yaitu 2 HCO, HCO Lokal dan Chain, dimana membuat google form untuk inputan survei
                            kepada surveyor terkait promo produk Siantar Top. Nantinya, menganalisis hasil survei promo dengan Excel sebagai
                            reporting untuk divisi Audit Marketing dan divisi Product Group Marketing. Survei Promo dilakukan setiap bulan, dengan total
                            kebutuhan survei promo berdasarkan WO (Working Order) sebanyak 50+ WO.
                        - Mengimprove google form pada survei promo dengan membuat **Web Streamlit Python** untuk lebih fleksibel dalam mengolah
                            dan menganalisis hasil survei promonya.
                        - Mengolah dan menganalisis survei pemerataan, AV, dan 4P Produk Siantar Top dan Kompetitor dari segi harga, omset,
                            dan varian yang laku sebagai kebutuhan informasi mengenai produk Siantar Top dengan produk Kompetitor. Survei ini
                            dilakukan sesuai permintaan WO oleh divisi Product Group Marketing.
                        - Mengolah survei *Goes to School* terkait produk *awareness* pada produk Siantar Top yang dilakukan
                            di berbagai kalangan responden (SD, SMP, dan SMA) pada wilayah yang terpilih. Hal ini, nantinya akan dilakukan reporting
                            untuk kebutuhan divisi Product Group Marketing terkait informasi produk Siantar Top di kalangan masyarakat. Survei ini
                            dilakukan dalam setahun.
                        - Melakukan update data dan review reporting harian untuk Outstanding area Medan dan Target SO vs SJ area Bekasi
                        - Mengembangkan sistem web streamlit pada pengolahan data di divisi BSI untuk kebutuhan pengolahan dan analisis data agar
                            lebih fleksibel.
                        """,
                        unsafe_allow_html=True
                    )
            st.markdown("<hr>", unsafe_allow_html=True)
#----------------------------------KERJA 2
            col1, col2, = st.columns([2, 1])
            with col1:
                # Box Title
                st.markdown(
                    """
                    <style>
                    .zoom-box {
                        background-color: white; 
                        padding: 5px 10px; 
                        border-radius: 5px; 
                        display: inline-block; 
                        margin-bottom: 10px;
                        cursor: pointer;
                        transition: transform 0.2s ease-in-out;
                        
                    }
                    .zoom-box:hover {
                        transform: scale(1.05);
                    }
                    .modal {
                        display: none; 
                        position: fixed; 
                        z-index: 99; 
                        padding-top: 100px; 
                        left: 0;
                        top: 0;
                        width: 100%; 
                        height: 100%;
                        background-color: rgba(0,0,0,0.7);
                    }
                    .modal-content {
                        margin: auto;
                        display: block;
                        width: 300px;
                    }
                    </style>
                    <div class="zoom-box" onclick="document.getElementById('modal-img').style.display='block'">
                        <strong>2. PT. Telekomunikasi Indonesia, tbk</strong>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <style>
                    .sticky-container {
                        position: sticky;
                        top: 10px; /* Adjust this value to set the top position */
                        z-index: 10;
                    }
                    </style>

                    <div class="sticky-container">
                        <div style="display: flex; align-items: center;">
                            <img src="https://upload.wikimedia.org/wikipedia/id/c/c4/Telkom_Indonesia_2013.svg" width="100" style="margin-right: 10px;" />
                            <div>
                                <span><strong>Divisi:</strong> Tribe Knowledge Management - Data Processing and Visualization Internship</span>
                                <p style="margin-top: 5px;"><strong>Periode:</strong> Feb 2024 - Jul 2024 </p>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                st.button("Jobdesk", on_click=toggle_activity3, key="button3")
                if st.session_state["show_activity3"]:
                    st.markdown(
                        """
                        **Jobdesk:**
                        - Menghandle 3 project utama, KM Metrics, Microcontent, dan Knowledge Power Up
                        - Membuat dashoard dari 3 project utama untuk kebutuhan informasi sebagai evaluasi dan pengukuran
                            terkait kinerja karyawan Telkom. Dashboard dibuat menggunakan Looker Google Studio.
                        - Melakukan weekly meeting setiap hari Senin dan juga melakukan meeting bersama mentor dan partner terkait
                            project-project yang akan diolah. 
                        - Melakukan pengolahan, pembersihan, dan analisis data menggunakan Spreadsheet dan Python untuk kebutuhan
                            dashboard. Data yang digunakan, yaitu Knowledge Power Up, KM Metrics, dan Microcontent yang berkaitan dengan konten-
                            konten yang sudah diimplementasikan.
                        - Melakukan review atau presentasi dari project utama sebagai hasil dan juga evaluasi dari project.
                        """,
                        unsafe_allow_html=True
                    )
            st.markdown("<hr>", unsafe_allow_html=True)
#----------------------------------KERJA 3
            col1, col2, = st.columns([2, 1])
            with col1:
                # Box Title
                st.markdown(
                    """
                    <style>
                    .zoom-box {
                        background-color: white; 
                        padding: 5px 10px; 
                        border-radius: 5px; 
                        display: inline-block; 
                        margin-bottom: 10px;
                        cursor: pointer;
                        transition: transform 0.2s ease-in-out;
                        
                    }
                    .zoom-box:hover {
                        transform: scale(1.05);
                    }
                    .modal {
                        display: none; 
                        position: fixed; 
                        z-index: 99; 
                        padding-top: 100px; 
                        left: 0;
                        top: 0;
                        width: 100%; 
                        height: 100%;
                        background-color: rgba(0,0,0,0.7);
                    }
                    .modal-content {
                        margin: auto;
                        display: block;
                        width: 300px;
                    }
                    </style>
                    <div class="zoom-box" onclick="document.getElementById('modal-img').style.display='block'">
                        <strong>3. Statistika Bisnis - ITS</strong>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <style>
                    .sticky-container {
                        position: sticky;
                        top: 10px; /* Adjust this value to set the top position */
                        z-index: 10;
                    }
                    </style>

                    <div class="sticky-container">
                        <div style="display: flex; align-items: center;">
                        <img src="https://katamata.wordpress.com/wp-content/uploads/2011/12/lambang-its-png-v1.png" width="100" style="margin-right: 10px;" />
                            <div>
                                <span><strong>Divisi:</strong> Asisten Dosen </span>
                                <p style="margin-top: 5px;"><strong>Periode:</strong> Mar 2023 - Dec 2023 </p>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                st.button("Jobdesk", on_click=toggle_activity4, key="button4")
                if st.session_state["show_activity4"]:
                    st.markdown(
                        """
                        **Jobdesk:**
                        - Menghandle sekitar 35+ mahasiswa dalam pengajaran mata kuliah Statistika Non Parametrik dan Eksplorasi Visualisasi Data
                        - Membimbing dan mengajarkan mahasiswa terkait mata kulih terkait sesuai kurikulum, sekaligus memberikan kasus-kasus nyata
                            yang berguna untuk dilakukan analisis menggunakan metode yang sesuai dengan bantuan alat statistika dan visualisasi.
                        - Mengajarkan alat statistika (Minitab dan SPSS) dan alat visualisasi (Looker Google Studio, Power BI, Tableau, dan R Shiny by R Studio)
                        - Memberikan tugas praktik dari kasus-kasus yang nyata kemudian dipresentasikan hasil analisa yang berguna bagi pemangku kepentingan.
                        - Melakukan pembahasan sekaligus evaluasi terkait mata kuliah terkait secara teoritis, sebagai pengukuran mahasiswa
                            dalam memelajari materi selama perkuliahan.
                        - Mendapatkan target nilai yang mumpuni diatas 85+ dari kedua mata kuliah terkait, sehingga mencapai target minimal yaitu 80.
                        """,
                        unsafe_allow_html=True
                    )
            st.markdown("<hr>", unsafe_allow_html=True)
        
        with tab4:
            st.write("### Sertifikat dan Penghargaan")
            st.success("Berikut kumpulan sertifikat dan penghargaan selama masa perkuliahan")
            dropbox_url = "https://www.dropbox.com/scl/fi/twk16n29sms6e9r7p33jb/PORTFOLIO-ENGLISH-1.pdf?rlkey=g1m81m08mn5yo1dah344lgd06&st=wcgmc6mn&raw=1"

            st.markdown(
                f'<iframe src="{dropbox_url}" width="700" height="1000"></iframe>',
                unsafe_allow_html=True
            )
            st.markdown("<hr>", unsafe_allow_html=True)

        with tab5:
            st.write("### 💼 Skills/Keterampilan")
            st.markdown("""
            <style>
            .skill-box {
                background-color: white;
                padding: 10px 15px;
                margin-bottom: 8px;
                border-radius: 10px;
                box-shadow: 1px 2px 5px rgba(0,0,0,0.1);
                transition: transform 0.2s ease;
                display: flex;
                align-items: center;
            }

            .skill-box:hover {
                transform: scale(1.02);
                box-shadow: 2px 4px 10px rgba(0,0,0,0.15);
            }

            .skill-logo {
                width: 30px;
                margin-right: 15px;
            }
            </style>
            """, unsafe_allow_html=True)

            # Isi konten skills
            skills_with_logos = [
                ("https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg", "Power BI", "Dashboard dan Analysis (Intermediate)"),
                ("https://upload.wikimedia.org/wikipedia/commons/4/4c/Looker.svg", "Looker Studio", "Dashboard dan Analysis (Intermediate)"),
                ("https://upload.wikimedia.org/wikipedia/commons/0/01/Tableau_Software_Logo_Small.png", "Tableau", "Dashboard dan Analysis (Intermediate)"),
                ("https://www.r-project.org/logo/Rlogo.png", "R Studio", "Dashboard dan Analysis (Intermediate)"),
                ("https://cdn-icons-png.flaticon.com/512/5968/5968350.png", "Python & Streamlit", "Dashboard, Analysis, dan Web Development (Intermediate)"),
                ("https://cdn-icons-png.flaticon.com/512/5968/5968342.png", "PostgreSQL", "ETL (Intermediate)"),
                ("https://upload.wikimedia.org/wikipedia/commons/d/d2/Minitab_Logo.svg", "Minitab", "Analysis (Intermediate)"),
                ("https://upload.wikimedia.org/wikipedia/commons/7/78/SPSS_An_IBM_Company_logo.svg", "SPSS", "Analysis (Intermediate)"),
                ("https://cdn-icons-png.flaticon.com/512/732/732221.png", "Microsoft Office", "Word, PowerPoint, Excel (Advanced)"),
            ]

            # Tampilkan tiap skill dalam box
            for logo_url, name, desc in skills_with_logos:
                st.markdown(f"""
                <div class="skill-box">
                    <img src="{logo_url}" class="skill-logo">
                    <div>
                        <b>{name}</b><br>{desc}
                    </div>
                </div>
                """, unsafe_allow_html=True)
    if st.button("⬅️ Back to Home"):
        st.session_state.clear()  # Reset semua session_state
        st.rerun()  # Reload ulang app biar tampil dari awal