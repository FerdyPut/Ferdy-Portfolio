import streamlit as st

# Sidebar Navigation
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Beranda", "Analisis", "Tentang"])

st.title("Aplikasi Web Streamlit Sederhana")

if page == "Beranda":
    st.subheader("Selamat datang di Beranda!")

    # Tabs di dalam halaman Beranda
    tab1, tab2 = st.tabs(["Statistik", "Grafik"])
    with tab1:
        st.write("Ini adalah konten tab Statistik.")
        st.metric("Jumlah User", 120)
    with tab2:
        st.write("Ini adalah konten tab Grafik.")
        st.line_chart([1, 3, 2, 4])

elif page == "Analisis":
    st.subheader("Halaman Analisis")

    tab1, tab2, tab3 = st.tabs(["Ringkasan", "Detail", "Kesimpulan"])
    with tab1:
        st.write("Analisis Ringkasan di sini.")
    with tab2:
        st.write("Detail data analisis.")
    with tab3:
        st.write("Kesimpulan dari analisis.")

elif page == "Tentang":
    st.subheader("Tentang Aplikasi Ini")
    st.markdown("""
    Aplikasi ini dibuat menggunakan Streamlit dengan navigasi sidebar
    dan tab di dalam halaman.
    """)

