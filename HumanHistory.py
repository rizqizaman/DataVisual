import streamlit as st
import base64
import pandas as pd
from io import BytesIO
from PIL import Image

data = pd.read_json('fire.json')
encode_image_list = data['Image']

def decode_image(encode_string):
    decode_bytes = base64.b64decode(encode_string)
    img = Image.open(BytesIO(decode_bytes))
    return img
st.title("Decoded Images")
for encode_image in encode_image_list:
    decoded_image = decode_image(encode_image)
    st.image(decoded_image, use_column_width=True)
