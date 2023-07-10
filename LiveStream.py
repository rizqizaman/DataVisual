import streamlit as st
import cv2
from PIL import Image
    
st.title('Live Stream menggunakan Streamlit')

    # Membuka kamera
cap = cv2.VideoCapture(0)

    # Looping untuk menampilkan livestream
while True:
  ret, frame = cap.read()
  frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Menampilkan livestream pada halaman web Streamlit
  st.image(frame_rgb, channels='RGB')