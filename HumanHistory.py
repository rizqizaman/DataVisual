# import streamlit as st
# import base64
# import pandas as pd
# from io import BytesIO
# from PIL import Image

# data = pd.read_json('fire.json')
# encode_image_list = data['Image']
# tanggal = data['Date_Time']

# def decode_image(encode_string):
#     decode_bytes = base64.b64decode(encode_string)
#     img = Image.open(BytesIO(decode_bytes))
#     return img
# st.title("Decoded Images")
# for encoded_image, tanggal in zip(encode_image_list, tanggal):
#     decoded_image = decode_image(encoded_image)
#     st.image(decoded_image, use_column_width=True)
#     st.write(tanggal)


import streamlit as st
import base64
import pandas as pd
from io import BytesIO
from PIL import Image
from datetime import datetime

data = pd.read_json('nama_file.json')
data['Date_Time'] = pd.to_datetime(data['Date_Time'])
data = data.sort_values('Date_Time', ascending=False)
encode_image_list = data['Image']


def decode_image(encode_string):
    decode_bytes = base64.b64decode(encode_string)
    img = Image.open(BytesIO(decode_bytes))
    return img
    
st.title("Data Berdasarkan Tanggal Terupdate")
# for index, row in data.iterrows():
#     st.write("Tanggal:", row['Date_Time'])
#     st.image(row['Image'])

    
# st.title("Decoded Images")
# for encoded_image, tanggal in zip(encode_image_list, tanggal):
#     decoded_image = decode_image(encoded_image)
#     st.image(decoded_image, use_column_width=True)
#     st.write(tanggal)

 for _, row in data.iterrows():
    encoded_image = row['Image']
    tanggal = row['Date_Time']
    decoded_image = decode_image(encoded_image)

        # Menampilkan gambar dan tanggal
    st.image(decoded_image, caption=str(tanggal), use_column_width=True)

