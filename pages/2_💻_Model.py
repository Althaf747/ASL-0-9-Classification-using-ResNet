import streamlit as st
import torch
from torchvision import models
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

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
