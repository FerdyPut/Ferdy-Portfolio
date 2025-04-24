import streamlit as st
from datetime import datetime
import pytz
# Mendapatkan waktu Jakarta
jakarta_tz = pytz.timezone('Asia/Jakarta')
now = datetime.now(jakarta_tz)

# Menentukan waktu dalam kategori
if 5 <= now.hour < 11:
    greeting = "Selamat Pagi"
elif 11 <= now.hour < 15:
    greeting = "Selamat Siang"
elif 15 <= now.hour < 18:
    greeting = "Selamat Sore"
else:
    greeting = "Selamat Malam"

def tampilkan_halaman_umum():
    st.info("Selamat datang di portofolio saya!")
    st.markdown(f"""
    - **{greeting}**, Terima kasih atas kesempatan yang diberikan. Portofolio ini dibuat
                mengenai diri saya dan juga beberapa project yang saya kerjakan terkait passion yang saya sebagai
                **Data Analyst/Data Scientist**.    
    - Menu pada portofolio website ini bisa dipilih pada bagian **Navbar Menu (sebelah kiri)**, terdapat beberapa 
        menu, yaitu **Tentang Saya, Portofolio, dan Kontak Saya**.


    """)
