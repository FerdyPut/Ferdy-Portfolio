import streamlit as st

# === SETUP ===
st.set_page_config(page_title="Portofolio Ferdy", layout="wide")

# --- CSS Kustom: Header dengan Foto Interaktif ---
st.markdown(
    """
    <style>
    @keyframes rotatePhoto {
        from {transform: rotateY(0deg);}
        to {transform: rotateY(360deg);}
    }

    .profile-container {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 20px;
    }

    .profile-pic {
        width: 150px;
        height: 150px;
        border-radius: 100%;
        object-fit: cover;
        animation: rotatePhoto 8s linear infinite;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    .main-title {
        font-size: 2em;
        font-weight: bold;
        font-family: Arial, sans-serif;
        color: #C5172E;  /* Ganti dengan warna yang kamu suka */
    }
    </style>

    <div class="profile-container">
        <img src="https://raw.githubusercontent.com/FerdyPut/Ferdy-Portfolio/refs/heads/main/foto.jpeg?token=GHSAT0AAAAAADAOB3JNJWYPFTFEXRSVKNOG2AKGLOQ" class="profile-pic">
        <div class="main-title">Welcome to My Portfolio! </div>
    </div>
    """,
    unsafe_allow_html=True
)


# === Session State ===
if "main_menu" not in st.session_state:
    st.session_state.main_menu = "Tentang Saya"
if "sub_menu" not in st.session_state:
    st.session_state.sub_menu = ""

# === SIDEBAR ===

st.sidebar.markdown(
    """
    <style>
    .sidebar-title {
        font-size: 12px;  /* Ukuran font kecil */
        font-weight: bold;
        font-family: Arial, sans-serif;
        color: black;  /* Warna hitam */
        display: flex;
        align-items: center;
        gap: 10px;  /* Jarak antara ikon dan teks */
        margin-bottom: -20px;
    }

    .menu-logo {
        font-size: 18px;  /* Ukuran ikon logo */
    }
    </style>

    <div class="sidebar-title">
        <span class="menu-logo">🔽</span>  <!-- Menambahkan emoji sebagai ikon -->
        Menu My Portfolio!
    </div>
    <hr>
    """,
    unsafe_allow_html=True
)

if st.sidebar.button("Tentang Saya"):
    st.session_state.main_menu = "Tentang Saya"
    st.session_state.sub_menu = ""

if st.sidebar.button("Portofolio Project"):
    st.session_state.main_menu = "Portofolio Project"

if st.session_state.main_menu == "Portofolio Project":
    with st.sidebar:
        col1, col2 = st.columns([0.2, 0.8])
        with col2:
            if st.button("📊 Data Analyst"):
                st.session_state.sub_menu = "Data Analyst"
            if st.button("🤖 Machine Learning"):
                st.session_state.sub_menu = "Machine Learning"

if st.sidebar.button("Kontak Saya"):
    st.session_state.main_menu = "Kontak Saya"
    st.session_state.sub_menu = ""

# === MAIN CONTENT ===
if st.session_state.main_menu == "Tentang Saya":
    st.subheader("👋 Tentang Saya")

    tab1, tab2 = st.tabs(["Profil Singkat", "Riwayat & Skill"])

    with tab1:
        st.write("""
        Halo! Saya Ferdy, mahasiswa Statistika Bisnis ITS dengan minat besar dalam data science, machine learning, dan visualisasi data.
        Saya suka membuat dashboard interaktif, memproses data, dan membagikan insight berdasarkan data.
        """)

    with tab2:
        st.write("### 📘 Pendidikan")
        st.write("- Statistika Bisnis - Institut Teknologi Sepuluh Nopember")

        st.write("### 🛠️ Skillset")
        st.markdown("""
        - Python (Pandas, Sklearn, Streamlit)  
        - Looker Studio, Power BI  
        - SQL, Excel (Pivot Table, Lookup)  
        - Dashboarding & Data Visualization
        """)

elif st.session_state.main_menu == "Portofolio Project":
    if st.session_state.sub_menu == "Data Analyst":
        st.subheader("📊 Portofolio: Data Analyst")
        st.write("Berisi contoh project dashboard, eksplorasi data, dan laporan berbasis analisis.")
    elif st.session_state.sub_menu == "Machine Learning":
        st.subheader("🤖 Portofolio: Machine Learning")
        st.write("Berisi project prediksi churn, klasifikasi, regresi, dan evaluasi model.")
    else:
        st.info("Silakan pilih salah satu subkategori di sidebar.")

elif st.session_state.main_menu == "Kontak Saya":
    st.subheader("📫 Kontak Saya")
    st.markdown("""
    - 📧 Email: ferdy@example.com  
    - 📱 WhatsApp: 08xxxxxxx  
    - 🔗 LinkedIn: [linkedin.com/in/ferdy](https://linkedin.com/in/ferdy)
    """)
