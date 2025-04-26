import streamlit as st
import nbformat
import base64
from io import BytesIO, StringIO
from PIL import Image
import pandas as pd
import requests

def tampilkan_eda():
        st.subheader("📊 Portofolio: Exploratory Data Analysis")
        st.info("""
                Berikut merupakan Project Exploratory Data Analysis saya menggunakan Google Colab
                Data yang digunakan adalah dataset e-commerce. Tujuan EDA ini adalah untuk mendapatkan
                informasi-informasi penting terkait e-commerce dari segi konteks bisnis yang bisa
                bermanfaat bagi perusahaan.
                """)

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
                        .project-link {
                            text-decoration: none;
                            color: #007BFF;
                            font-weight: bold;
                        }

                        .project-link:hover {
                            text-decoration: underline;
                            color: #0056b3;
                        }
                    </style>
                    <span class="white-box">   
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/1024px-Octicons-mark-github.svg.png" alt="GitHub Logo" style="width: 20px; height: 20px; margin-right: -480px;">
                    Link Project Github: <a href="https://github.com/FerdyPut/Exploratory-Data-Analysis-of-E-Commerce" target="_blank" class="project-link"> Project EDA</a></span>
                    <p>
                    """, unsafe_allow_html=True)
        
        # --------- FILE PATH DARI GITHUB ---------
        NOTEBOOK_PATH = "https://www.dropbox.com/scl/fi/go6yc9nfi0vjohepwdtxw/Exploratory_of_Data_Analysis_at_E_Commerce_Dataset.ipynb?rlkey=qlqo3gepe7fcjjpck57nroxk3&st=peozh82s&dl=1"
        DATA_PATH = "https://www.dropbox.com/scl/fi/gk24f4f79f2dw8b9xo969/ecommerce.csv?rlkey=pcvyla9d8q7vrt2504ghuxupv&st=ot0cfutm&dl=1"
        # -----------------------------------------

        # Load notebook
        response = requests.get(NOTEBOOK_PATH)
        notebook = nbformat.reads(response.text, as_version=4)

        # Load dataset
        df = pd.read_csv(DATA_PATH)

        # Tampil semua isi notebook
        for idx, cell in enumerate(notebook.cells):
            with st.expander(f"Cell {idx+1} - {cell.cell_type.capitalize()}", expanded=True):
                if cell.cell_type == 'markdown':
                    st.markdown(cell.source)
                elif cell.cell_type == 'code':
                    st.code(cell.source, language='python')
                    
                    if 'outputs' in cell:
                        for output in cell.outputs:
                            if output.output_type == 'stream':
                                st.text(output.text)
                            elif output.output_type in ['execute_result', 'display_data']:
                                if 'image/png' in output.data:
                                    image_data = base64.b64decode(output.data['image/png'])
                                    image = Image.open(BytesIO(image_data))
                                    st.image(image)
                                elif 'text/plain' in output.data:
                                    text_output = output.data['text/plain']
                                    # Deteksi output dataframe
                                    if df is not None and "InvoiceNo" in text_output and "StockCode" in text_output:
                                        st.success("Detected DataFrame output, showing real dataframe 👇")
                                        st.dataframe(df.head(100))
                                    else:
                                        st.text(text_output)
                            elif output.output_type == 'error':
                                st.error('\n'.join(output.traceback))