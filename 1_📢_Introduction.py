import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = "images/bg.jpg"
img_base64 = get_base64_of_bin_file(img_path)

page_bg_img = f'''
<style>
.stApp {{
background-image: 
    linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)),
    url("data:image/png;base64,{img_base64}");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
background-position: center;
}}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("ASL digit 0-9 Classification Using ResNet-18")
st.markdown("""
Ini adalah aplikasi demo untuk memprediksi huruf ASL (American Sign Language) menggunakan model ResNet18.
Anda dapat mencoba mengunggah gambar tangan dan melihat prediksi model secara realtime.
""")
