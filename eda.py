import streamlit as st
import nbformat
from nbconvert import HTMLExporter
import requests

def tampilkan_eda():
        st.subheader("📊 Portofolio: Exploratory Data Analysis")
        st.write("Berisi contoh project dashboard, eksplorasi data, dan laporan berbasis analisis.")


        # Function to download and convert the notebook to HTML
        def convert_notebook_from_github(github_raw_url):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            # Download the notebook content
            response = requests.get(github_raw_url, headers=headers)
            
            # Check if the response is valid
            if response.status_code == 200:
                notebook_content = nbformat.read(response.content, as_version=4)

                # Convert notebook to HTML
                html_exporter = HTMLExporter()
                body, resources = html_exporter.from_notebook_node(notebook_content)
                return body
            else:
                return "Error: Could not fetch the notebook from GitHub."

        # Streamlit app to display notebook
        st.title("Display Jupyter Notebook from GitHub")

        # URL of your GitHub notebook's raw content
        github_raw_url = "https://raw.githubusercontent.com/FerdyPut/Exploratory-Data-Analysis-of-E-Commerce/main/Exploratory_of_Data_Analysis_at_E_Commerce_Dataset.ipynb"

        # Convert and display the notebook
        notebook_html = convert_notebook_from_github(github_raw_url)
        st.markdown(notebook_html, unsafe_allow_html=True)