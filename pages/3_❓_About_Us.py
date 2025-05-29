import streamlit as st
from PIL import Image
import base64

# Styling untuk judul About Us agar selalu muncul dan di tengah
st.markdown("""
<style>
h1 {
    text-align: center;
    font-weight: bold;
    font-size: 40px;
    margin-bottom: 40px;
}
.author-block {
    text-align: center;
    margin-bottom: 40px;
}
.author-name {
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: 5px;
}
.author-email a {
    text-decoration: none;
    color: #1E90FF;
    font-size: 14px;
}
.author-email a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# Judul tetap tampil di atas dan di tengah
st.title("About Us")

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

def show_author(image_path, name, email):
    image = Image.open(image_path)
    st.markdown(f'<div class="author-block">', unsafe_allow_html=True)
    st.image(image, caption="", width=250)
    st.markdown(f'<p class="author-name">{name}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="author-email"><a href="mailto:{email}">{email}</a></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    show_author("images/Althaf.JPG", "Althaf Rizqullah", "althafrizq@student.telkomuniversity.ac.id")

with col2:
    show_author("images/a.JPG", "Evelyn Emery Dahayu", "evelynayu95@student.telkomuniversity.ac.id")
