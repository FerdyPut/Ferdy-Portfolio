import streamlit as st

# === SETUP ===
st.set_page_config(page_title="Portofolio Ferdy", layout="wide")

#CSS umum
st.markdown(
        """
        <style>
        @keyframes rotatePhoto {
            from {transform: rotateY(0deg);}
            to {transform: rotateY(360deg);}
        }
        
            /* Warna latar belakang utama */
            .stApp {
                background-color: #F2F6D0;
                color: black;
            }

            /* Sidebar */
            section[data-testid="stSidebar"] {
                background-color: #FEBA17;
            }
            </style>
            """,unsafe_allow_html=True)


# --- CSS Kustom: Header dengan Foto Interaktif ---
if "show_intro" not in st.session_state:
    st.session_state.show_intro = True  # Default: tampilkan intro

if st.session_state.show_intro:    
    st.markdown(
        """
        <style>
        @keyframes rotatePhoto {
            from {transform: rotateY(0deg);}
            to {transform: rotateY(360deg);}
        }
        
            /* Warna latar belakang utama */
            .stApp {
                background-color: #F2F6D0;
                color: black;
            }

            /* Sidebar */
            section[data-testid="stSidebar"] {
                background-color: #FEBA17;
            }
        .profile-container {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 20px;
        }

        .profile-pic {
            width: 90px;
            height: 90px;
            border-radius: 100%;
            object-fit: cover;
            animation: rotatePhoto 8s linear infinite;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: #343131;  /* Ganti dengan warna yang kamu suka */
        }
        </style>

        <div class="profile-container">
                <!-- Gambar dari st.image menggunakan HTML -->
                <img src="https://www.dropbox.com/scl/fi/d2xuotgv7gthq548ksp48/foto.jpeg?rlkey=hzsuytp11xmj80r7vox7eqh1p&st=iyp7yovu&raw=1" class="profile-pic">
            <div class="main-title">Welcome to My Portfolio!</div>
        </div>
        <hr>
    """,unsafe_allow_html=True)


# === Session State ===
if "main_menu" not in st.session_state:
    st.session_state.main_menu = "Halaman Umum"
if "sub_menu" not in st.session_state:
    st.session_state.sub_menu = ""
if "tampilkan_halaman_umum" not in st.session_state:
    st.session_state.tampilkan_halaman_umum = True  # Menyimpan status untuk menampilkan halaman umum
if "show_intro" not in st.session_state:
    st.session_state.show_intro = True
if "sub_sub_menu" not in st.session_state:
    st.session_state.sub_sub_menu = ""  # handle hierarchy

# Mengecek dan menampilkan Halaman Umum hanya pada pemuatan pertama kali
if st.session_state.tampilkan_halaman_umum:
    import halaman_umum  # Pastikan halaman_umum diimpor hanya sekali
    halaman_umum.tampilkan_halaman_umum()  # Fungsi untuk menampilkan halaman umum
    st.session_state.tampilkan_halaman_umum = False  # Set menjadi False setelah ditampilkan
    st.session_state.show_intro = False


# === SIDEBAR ===

st.sidebar.markdown(
    """
    <style>
    .sidebar-title {
        font-size: 18px;  /* Ukuran font kecil */
        font-weight: bold;
        color: black;  /* Warna hitam */
        display: flex;
        align-items: center;
        gap: 5px;  /* Jarak antara ikon dan teks */
        margin-bottom: -20px;
    }

    .menu-logo {
        font-size: 18px;  /* Ukuran ikon logo */
    }
    </style>

    <div class="sidebar-title">
        <span class="menu-logo">🔽</span>  <!-- Menambahkan emoji sebagai ikon -->
        MENU
    </div>
    <hr>
    """,
    unsafe_allow_html=True
)


if st.sidebar.button("👥 Tentang Saya"):
    st.session_state.main_menu = "Tentang Saya"
    st.session_state.sub_menu = ""
    st.session_state.sub_sub_menu = ""  # Reset sub-sub-menu

if st.sidebar.button(":chart_with_upwards_trend: Portofolio Project"):
    st.session_state.main_menu = "Portofolio Project"
    st.session_state.sub_menu = ""  # Make sure sub_menu is reset when clicking "Portofolio Project"
    st.session_state.sub_sub_menu = ""  # Reset sub-sub-menu
    
if st.session_state.main_menu == "Portofolio Project":
    with st.sidebar:
        col1, col2 = st.columns([0.2, 0.8])
        with col2:
            if st.button("📊 Data Analyst - Exploratory Data Analysis "):
                st.session_state.sub_menu = "Data Analyst - Exploratory Data Analysis"
                st.session_state.sub_sub_menu = ""  # Reset sub-sub-menu when sub-menu is selected
            if st.button("🤖 Machine Learning"):
                st.session_state.sub_menu = "Machine Learning"
                st.session_state.sub_sub_menu = ""  # Reset sub-sub-menu

if st.sidebar.button(" :email: Kontak Saya"):
    st.session_state.main_menu = "Kontak Saya"
    st.session_state.sub_menu = ""  # Reset sub-menu
    st.session_state.sub_sub_menu = ""  # Reset sub-sub-menu


# MAIN CONTENT DISPLAY BASED ON SELECTED MENUS
if st.session_state.main_menu == "Tentang Saya":
    import tentang_saya
    tentang_saya.tampilkan_tentang_saya()

elif st.session_state.main_menu == "Portofolio Project":
    # Show the main content for Portofolio Project only if no sub-menu is selected
    if st.session_state.sub_menu == "":
        import portofolio
        portofolio.tampilkan_porto()

    # Show content for Data Analyst sub-menu
    elif st.session_state.sub_menu == "Data Analyst - Exploratory Data Analysis":
        import eda
        eda.tampilkan_eda()
 

    # Show content for Machine Learning sub-menu
    elif st.session_state.sub_menu == "Machine Learning":
        st.subheader("🤖 Portofolio: Machine Learning")
        st.write("Berisi project prediksi churn, klasifikasi, regresi, dan evaluasi model.")
        
        # Option to add further sub-sub-menu if required for Machine Learning
        ml_sub_menu = st.selectbox("Pilih Project Machine Learning", ["Churn Prediction", "Classification", "Regression"])
        st.session_state.sub_sub_menu = ml_sub_menu  # Set the sub-sub-menu for Machine Learning

        if st.session_state.sub_sub_menu == "Churn Prediction":
            st.write("Project prediksi churn menggunakan algoritma regresi logistik.")
        elif st.session_state.sub_sub_menu == "Classification":
            st.write("Project klasifikasi menggunakan algoritma Random Forest.")
        elif st.session_state.sub_sub_menu == "Regression":
            st.write("Project regresi untuk prediksi harga menggunakan regresi linier.")

    else:
        st.info("Silakan pilih menu lain di sidebar.")

elif st.session_state.main_menu == "Kontak Saya":
    import kontak_saya
    kontak_saya.tampilkan_kontak()


