import streamlit as st

def tampilkan_porto():
    st.info("Ini adalah List Portofolio Project saya!")
    st.markdown("""
        <style>
            .white-box {
                background-color: white;
                padding: 3px 8px;
                border-radius: 5px;
                margin-bottom: 5px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                transition: transform 0.3s;
            }
            .gold-box {
                background-color: gold;
                padding: 3px 8px;
                border-radius: 5px;
                margin-bottom: 5px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                transition: transform 0.3s;
            }
            .white-box:hover, .gold-box:hover {
                transform: scale(1.05);
            }
            .check-icon {
                color: green;
                font-size: 18px;
            }
        </style>
        Pada Menu ini akan menampilkan beberapa project yang telah saya lakukan terkait Data Analyst dan Data Scientist:
        <ul>
            <li><span class="white-box">1. Exploratory Data Analysis on Bootcamp <span class="check-icon">✔️</span></span></li>
            <li><span class="white-box">2. SQL Project <span class="check-icon">Segera</span></span></li>
            <li><span class="white-box">3. Scrapping Project <span class="check-icon">Segera</span></span></li>
            <li><span class="white-box">4. A/B Testing Project <span class="check-icon">Segera</span></span></li>
            <li><span class="gold-box">5. Dashboard with Power BI <span class="check-icon">Segera</span></span></li>
            <li><span class="gold-box">6. Hypotesis Testing <span class="check-icon">Segera</span></span></li>
            <li><span class="gold-box">7 Unsupervised Learning <span class="check-icon">Segera</span></span></li>
            <li><span class="gold-box">8 Supervised Learning <span class="check-icon">Segera</span></span></li>
            <li><span class="gold-box">9. Hypertuning of Machine Learning <span class="check-icon">✔️</span></span></li>
        </ul>
    """, unsafe_allow_html=True)
