import streamlit as st
from PIL import Image

# CSS untuk menengahkan judul About Us
center_title_style = """
    <style>
    .center-title {
        text-align: center;
        font-weight: bold;
        font-size: 40px;
        margin-bottom: 40px;
    }
    </style>
"""

st.markdown(center_title_style, unsafe_allow_html=True)
st.markdown('<h1 class="center-title">About Us</h1>', unsafe_allow_html=True)

def show_author(image_path, name, position, contact):
    image = Image.open(image_path)
    st.image(image, caption="Foto Author", width=250)
    st.markdown(f"**{name}**")
    st.markdown(f"Posisi: {position}")
    st.markdown(f"Kontak: [{contact}](mailto:{contact})")

col1, col2 = st.columns(2)

with col1:
    show_author("images/a.JPG", "Rgsrgs", "Perencana Tambang", "rg.email@example.com")

with col2:
    show_author("images/a.JPG", "Nama Kedua", "Posisi Kedua", "email.kedua@example.com")
