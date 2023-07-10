import streamlit as st
import mysql.connector
import base64
import pandas as pd
from io import BytesIO
from PIL import Image

# Fungsi untuk menghubungkan ke database

# Membaca file JSON
def data():
    data = pd.read_json('fire.json')
    return data
    
# def create_connection():
#     connection = mysql.connector.connect(
#         host='localhost',
#         user='root',  # Ganti dengan username Anda
#         password='',  # Ganti dengan password Anda
#         database='web_service'  # Ganti dengan nama database Anda
#     )
#     return connection

# def get_image_encode():
#     conn = create_connection()
#     query = "SELECT Image From fire ORDER BY Object_Detection = 'Person' DESC "
#     cursor = conn.cursor()
#     cursor.execute(query)
#     image_list = cursor.fetchall()

#     conn.close()
#     return image_list

# def Tanggal():
#     conn = create_connection()
#     query = "SELECT Date_Time From fire ORDER BY Object_Detection = 'Person' DESC "
#     cursor = conn.cursor()
#     cursor.execute(query)
#     TGL = cursor.fetchall()

#     conn.close()
#     return TGL


def decode_image(encode_string):
    decode_bytes = base64.b64decode(encode_string)
    img = Image.open(BytesIO(decode_bytes))
    return img
    
def main():
    # st.title("Human History")
    # encode_image = get_image_encode()
    # tanggal = Tanggal()
    # for encoded_image, tanggal in zip(encode_image, tanggal):
    #     decoded_image = decode_image(encoded_image[0])
    #     st.image(decoded_image, use_column_width=True)
    #     st.write(tanggal[0])

    st.title("Human History")
    data = get_image_data()
    for item in data:
        encoded_image = item['Image']
        tanggal = item['Date_Time']
        decoded_image = decode_image(encoded_image)
        st.image(decoded_image, caption=tanggal, use_column_width=True)



if __name__ == '__main__':
    main()
