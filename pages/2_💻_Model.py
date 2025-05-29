import streamlit as st
import torch
from torchvision import models
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
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

@st.cache_resource
def load_model(path):
    model = models.resnet18(pretrained=False)
    model.fc = nn.Linear(512, 10)
    state_dict = torch.load(path, map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)
    model.eval()
    return model

model = load_model('best_model.pth')

st.title("Demo Prediksi Model ASL")

uploaded_file = st.file_uploader("Upload gambar tangan ASL", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Gambar Input (RGB)", use_container_width=True)

    transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
    ])

    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(input_tensor)
        probs = torch.nn.functional.softmax(output, dim=1)
        confidence, pred_class = torch.max(probs, 1)

    st.write(f"Prediksi kelas: {pred_class.item()} dengan confidence: {confidence.item():.4f}")
