import streamlit as st

st.set_page_config(page_title="Portofolio Ferdy", layout="wide")

# Sidebar dengan ekspansi submenu
st.sidebar.title("Navigasi")
main_menu = st.sidebar.radio("Menu Utama", ["Tentang Saya", "Portofolio Project", "Kontak Saya"])

if main_menu == "Tentang Saya":
    st.title("👋 Tentang Saya")
    st.write("""
    Halo! Saya Ferdyansyah Permana Putra, mahasiswa Statistika Bisnis ITS.
    Saya memiliki pengalaman di bidang Data Analysis, Visualisasi, dan Machine Learning.
    Saat ini saya aktif sebagai asisten dosen dan pernah magang di PT Telkom dan lainnya.
    """)

elif main_menu == "Portofolio Project":
    submenu = st.sidebar.radio("Kategori Portofolio", ["Data Analyst", "Machine Learning"])

    if submenu == "Data Analyst":
        st.title("📊 Portofolio: Data Analyst")
        tab1, tab2 = st.tabs(["Dashboard", "Visualisasi"])
        with tab1:
            st.write("Contoh dashboard Looker Studio, Power BI, atau lainnya.")
        with tab2:
            st.write("Contoh visualisasi tren, bar chart, atau insight lainnya.")

    elif submenu == "Machine Learning":
        st.title("🤖 Portofolio: Machine Learning")
        tab1, tab2, tab3 = st.tabs(["Modeling", "Evaluasi", "Kesimpulan"])
        with tab1:
            st.write("Contoh model prediksi churn, klasifikasi, regresi, dll.")
        with tab2:
            st.write("Metrik evaluasi seperti AUC, F1-score, dan Confusion Matrix.")
        with tab3:
            st.write("Insight dari hasil model dan potensi implementasi.")

elif main_menu == "Kontak Saya":
    st.title("📫 Kontak Saya")
    st.markdown("""
    - 📧 Email: ferdy@example.com  
    - 📱 WhatsApp: 08xxxxxxxxxx  
    - 🌐 LinkedIn: [linkedin.com/in/ferdy](https://linkedin.com/in/ferdy)  
    - 📁 GitHub: [github.com/ferdyputra](https://github.com/ferdyputra)
    """)

