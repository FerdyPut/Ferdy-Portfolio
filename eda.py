import streamlit as st
import nbformat
from nbconvert import HTMLExporter

def tampilkan_eda():
        st.subheader("📊 Portofolio: Exploratory Data Analysis")
        st.write("Berisi contoh project dashboard, eksplorasi data, dan laporan berbasis analisis.")

        # Sub-sub-menu for Data Analyst
        data_analyst_sub_menu = st.selectbox(
            "Pilih Sub-Menu Data Analyst", 
            ["Dashboard", "Eksplorasi Data", "Laporan Berbasis Analisis"]
        )

        st.session_state.sub_sub_menu = data_analyst_sub_menu  # Set the sub-sub-menu to the selected option

        if st.session_state.sub_sub_menu == "Dashboard":
            st.write("Contoh project dashboard yang telah Anda buat.")
        elif st.session_state.sub_sub_menu == "Eksplorasi Data":
            st.write("Contoh project eksplorasi data yang telah Anda lakukan.")
        elif st.session_state.sub_sub_menu == "Laporan Berbasis Analisis":
            st.write("Contoh laporan berbasis analisis data.")