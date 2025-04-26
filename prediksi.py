
import streamlit as st
import nbformat
import base64
from io import BytesIO, StringIO
from PIL import Image
import pandas as pd
import requests
import joblib
import tempfile
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import scipy.stats as stats
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
from statsmodels.tools.tools import add_constant
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import make_scorer, recall_score
from imblearn.over_sampling import SMOTE
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
import time

def tampilkan_prediksi():
        st.subheader("🤖 Portofolio: Machine Learning")
        st.success(""" Pada portofolio Machine Learning ini ada bagian 2 bab, yaitu: Hasil dari project saya di github Hypertuning Machine Learning pada Churn Customer
                   dan Alat Testing Prediksi Churn Hypertuning Machine Learning Menggunakan Best Model (SVM).
                   
                   """)
        tab0, tab1 = st.tabs(['Hasil Project Machine Learning on Github','Alat Prediksi [Testing]'])

        with tab0:
            st.info("""
                        Berikut merupakan Project Hypertuning Machine Learning. Tujuannya untuk memprediksi Churn pelanggan
                        disuatu perusahaan sehingga bisa mengantisipasi potensi churn kedepannya.
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
                        Link Project Github: <a href="https://github.com/FerdyPut/Hypertuning-Machine-Learning-of-Churn-Prediction/blob/main/Prediction%20of%20Churn%20Using%20Hypertuning%20Parameter%20(Machine%20Learning).ipynb" target="_blank" class="project-link"> Project ML</a></span>
                        <p>
                        """, unsafe_allow_html=True)
            
            # --------- FILE PATH DARI GITHUB ---------
            NOTEBOOK_PATH = "https://www.dropbox.com/scl/fi/wvpotiswjjjv9vqnqowwo/HW_HPTUNING_Ferdyansyah_Permana_Putra.ipynb?rlkey=wd5wvd9a07s4pl2328ejlcw2i&st=stlhee6m&dl=1"
            DATA_PATH = "https://www.dropbox.com/scl/fi/xu266ivq58vdr9y01bzgo/churn-1.csv?rlkey=fj5vtyk5ji4xg1knpory7x5th&st=871w7ddj&dl=1"
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
        with tab1:
            st.warning("""
                        Ini untuk tahapan uji coba prediksi Machine Learning menggunakan SVM Classifier pada data churn ketika
                        ada data baru. Dimana, Tahapan ini berdasarkan model yang sudah di latih sebelumnya dan menggunakan 
                        parameter yang optimal
                        """)  
            #mode = st.selectbox("Pilih Mode Input", ["Single Input", "Upload Excel"]) --> jika mau 2mode
            URL1 = "https://www.dropbox.com/scl/fi/o7brxqg0oowgn62refm0n/svm_pipeline_grid-1.joblib?rlkey=ypk6e28dp46dcmtvwny7oj5w7&st=md3s80s2&dl=1"
            # Download model
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                response = requests.get(URL1)
                tmp.write(response.content)
                tmp_path = tmp.name

            # Load model
            model_pipeline = joblib.load(tmp_path)


            # Initialize the LabelEncoders (Ensure that they are trained once on the training data)
            le_gender = LabelEncoder()
            le_partner = LabelEncoder()
            le_dependents = LabelEncoder()
            le_paperless = LabelEncoder()
            le_payment = LabelEncoder()
            le_contract = LabelEncoder()

            # Fit encoder with training data (Do this step only once during training)
            le_gender.fit(["Male", "Female"])
            le_partner.fit(["Yes", "No"])
            le_dependents.fit(["Yes", "No"])
            le_paperless.fit(["Yes", "No"])
            le_payment.fit(["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
            le_contract.fit(["Month-to-month", "One year", "Two year"])

            # Function to encode the input using LabelEncoder
            def encode_input_with_labelencoder(gender, senior, partner, dependents, tenure, contract, paperless, payment, monthly_charges):
                # Label Encoding for categorical features
                gender_encoded = le_gender.transform([gender])[0]
                partner_encoded = le_partner.transform([partner])[0]
                dependents_encoded = le_dependents.transform([dependents])[0]
                paperless_encoded = le_paperless.transform([paperless])[0]

                # Senior is already binary (0 or 1)
                senior_encoded = senior
                
                # Numerical values are kept as is
                tenure_encoded = tenure
                monthly_charges_encoded = monthly_charges

                # Label Encoding for PaymentMethod and Contract
                payment_encoded = le_payment.transform([payment])[0]
                contract_encoded = le_contract.transform([contract])[0]

                # Combine everything into a single array
                encoded_input = np.array([
                    gender_encoded, senior_encoded, partner_encoded, dependents_encoded,
                    tenure_encoded, paperless_encoded, monthly_charges_encoded, 
                    payment_encoded, contract_encoded
                ])

                return encoded_input

            # Fungsi untuk prediksi dan evaluasi akurasi dan recall
            def prepare_model_for_prediction(model_pipeline, gender, senior, partner, dependents, tenure, contract, paperless, payment, monthly_charges, true_label=None):
                encoded_input = encode_input_with_labelencoder(gender, senior, partner, dependents, tenure, contract, paperless, payment, monthly_charges)
                
                column_names = [
                    "Gender", "SeniorCitizen", "Partner", "Dependents", "Tenure", "Contract", 
                    "PaperlessBilling", "PaymentMethod", "MonthlyCharges"
                ]
                
                input_data = pd.DataFrame([encoded_input], columns=column_names)

                # Prediksi
                prediction = model_pipeline.predict(input_data)
                
                # Menentukan label berdasarkan prediksi
                if prediction == 1:
                    pred_label = "Pelanggan Potensi Churn"
                else:
                    pred_label = "Pelanggan Tidak Berpotensi Churn"
                
                # Menghitung akurasi dan recall jika true_label ada
                if true_label is not None:
                    recall = recall_score([true_label], prediction)
                    return pred_label, recall
                
                return pred_label

            #----------------------------INPUTAN STREAMLIT
            gender = st.selectbox("Gender", ["Male", "Female"])
            senior = st.selectbox("Senior Citizen", [0, 1])
            partner = st.selectbox("Partner", ["Yes", "No"])
            dependents = st.selectbox("Dependents", ["Yes", "No"])
            tenure = st.number_input("Tenure", min_value=0)
            contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
            paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
            payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
            monthly_charges = st.number_input("Monthly Charges", min_value=0.0)

            true_label = 1
            # Prediksi
            result = prepare_model_for_prediction(model_pipeline, gender, senior, partner, dependents, tenure, contract, paperless, payment, monthly_charges, true_label)
            
            # Pisahkan result ke dua variabel
            if isinstance(result, tuple):
                pred_label, recall = result
            else:
                pred_label = result
                recall = None
            
            # Tombol Prediksi
            if st.button("Prediksi Churn"):
                # Inisialisasi progress bar
                progress = st.progress(0, text="Memproses prediksi...")

                # Simulasi loading (bisa dihapus kalau nggak perlu delay)
                for percent_complete in range(0, 101, 10):
                    time.sleep(0.1)  # Delay kecil untuk animasi
                    progress.progress(percent_complete, text=f"Memproses prediksi... ({percent_complete}%)")

                # Selesai
                progress.empty()  # Menghilangkan progress bar
                st.success(f"Hasil Prediksi: {pred_label}")
 