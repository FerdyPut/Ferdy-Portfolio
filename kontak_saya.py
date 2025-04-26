import streamlit as st

def tampilkan_kontak():
    st.title("📬 Kontak")
    st.info("Ingin mengetahui lebih lanjut, silahkan hubungi saya: *(Feel Free)*")

    # CSS styling angka emas + efek zoom saat hover
    st.markdown(
        """
        <style>
        .gold-box {
            background-color: #FFD700;
            color: black;
            padding: 2px 8px;
            border-radius: 5px;
            font-weight: bold;
            display: inline-block;
            margin-right: 8px;
            transition: transform 0.2s ease-in-out;
            cursor: pointer;
        }
        .gold-box:hover {
            transform: scale(1.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # LinkedIn
    st.markdown(
        """
        <span class="gold-box">1.</span> [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/ferdypput)
        """,
        unsafe_allow_html=True
    )

    # GitHub
    st.markdown(
        """
        <span class="gold-box">2.</span> [![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/FerdyPut)
        """,
        unsafe_allow_html=True
    )

    # Email
    st.markdown(
        """
        <span class="gold-box">3.</span> [![Email](https://img.shields.io/badge/Email-ferdyansyahpputra@gmail.com-red)](mailto:ferdyansyahpputra@gmail.com)
        """,
        unsafe_allow_html=True
    )

    # No HP
    st.markdown(
        """
        <span class="gold-box">4.</span> [![WhatsApp](https://img.shields.io/badge/WhatsApp-085232654077-brightgreen)](https://wa.me/6285232654077)
        """,
        unsafe_allow_html=True
    )

    # Instagram
    st.markdown(
        """
        <span class="gold-box">5.</span> [![Instagram](https://img.shields.io/badge/Instagram-@ferd.dyputr_-ff69b4)](https://www.instagram.com/fer.dyputr_)
        """,
        unsafe_allow_html=True
    )

    st.markdown("<hr>",unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .lego-text {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-top: 50px;
            justify-content: center;
            animation: split 3s ease-in-out forwards;
        }

        .lego-block {
            background-color: #f4b400;
            color: white;
            font-weight: bold;
            padding: 12px 14px;
            font-size: 30px;
            border-radius: 6px;
            box-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            transition: transform 0.2s ease-in-out;
            opacity: 0;
            transform: translate(0, -100px);
        }

        .lego-text .lego-block:nth-child(1) {
            animation: appear 1s ease-in 0.5s forwards;
        }
        .lego-text .lego-block:nth-child(2) {
            animation: appear 1s ease-in 0.6s forwards;
        }
        .lego-text .lego-block:nth-child(3) {
            animation: appear 1s ease-in 0.7s forwards;
        }
        .lego-text .lego-block:nth-child(4) {
            animation: appear 1s ease-in 0.8s forwards;
        }
        .lego-text .lego-block:nth-child(5) {
            animation: appear 1s ease-in 0.9s forwards;
        }
        .lego-text .lego-block:nth-child(6) {
            animation: appear 1s ease-in 1s forwards;
        }
        .lego-text .lego-block:nth-child(7) {
            animation: appear 1s ease-in 1.1s forwards;
        }
        .lego-text .lego-block:nth-child(8) {
            animation: appear 1s ease-in 1.2s forwards;
        }
        .lego-text .lego-block:nth-child(9) {
            animation: appear 1s ease-in 1.3s forwards;
        }
        .lego-text .lego-block:nth-child(10) {
            animation: appear 1s ease-in 1.4s forwards;
        }
        .lego-text .lego-block:nth-child(11) {
            animation: appear 1s ease-in 1.5s forwards;
        }
                .lego-text .lego-block:nth-child(12) {
            animation: appear 1s ease-in 1.5s forwards;
        }

        @keyframes split {
            0% {
                transform: scale(0);
                opacity: 0;
            }
            50% {
                transform: scale(2);
                opacity: 0.5;
            }
            100% {
                transform: scale(1);
                opacity: 1;
            }
        }

        @keyframes appear {
            0% {
                opacity: 0;
                transform: translate(0, -100px);
            }
            100% {
                opacity: 1;
                transform: translate(0, 0);
            }
        }
        </style>

        <div class="lego-text">
            <div class="lego-block">T</div>
            <div class="lego-block">E</div>
            <div class="lego-block">R</div>
            <div class="lego-block">I</div>
            <div class="lego-block">M</div>
            <div class="lego-block">A</div>
            <div style="width: 10px;"></div>
            <div class="lego-block">K</div>
            <div class="lego-block">A</div>
            <div class="lego-block">S</div>
            <div class="lego-block">I</div>
            <div class="lego-block">H</div>
            
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("⬅️ Back to Home"):
        st.session_state.clear()  # Reset semua session_state
        st.rerun()  # Reload ulang app biar tampil dari awal