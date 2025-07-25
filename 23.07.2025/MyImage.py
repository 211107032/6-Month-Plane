import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="MyImage Image Processor", layout="wide")

# Title
st.title("MyImage - Multi-Color Channel Visualizer")

# Load image from local path
@st.cache_data
def load_image():
    path = r"C:\Users\milind rajput\Desktop\6Month _DataScience\23.07.2025\Milind Rajput.jpg"
    return Image.open(path).convert("RGB")

# Load and display image
Peacock = load_image()
st.image(Peacock, caption="Original MyImage Image", use_container_width=True)

# Convert to NumPy array
Peacock_np = np.array(Peacock)
R, G, B = Peacock_np[:, :, 0], Peacock_np[:, :, 1], Peacock_np[:, :, 2]

# Create channel images
red_img = np.zeros_like(Peacock_np)
green_img = np.zeros_like(Peacock_np)
blue_img = np.zeros_like(Peacock_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

Peacock_gray = Peacock.convert("L").resize((100,100))
Peacock_gray_np = np.array(Peacock_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(2, 1))
ax.imshow(Peacock_gray_np, cmap=colormap)
ax.axis("off")
st.pyplot(fig)
