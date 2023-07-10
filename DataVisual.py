import streamlit as st
import mysql.connector
# import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import base64

# Fungsi untuk menghubungkan ke database
def create_connection():
    connection = mysql.connector.connect(
    # connection = psycopg2.connect(
        host='localhost',
        user='id20864486_bakaranpawon2023',  # Ganti dengan username Anda
        port='3306',
        password='Bakaranpawon2023#',  # Ganti dengan password Anda
        database='id20864486_bakaran'  # Ganti dengan nama database Anda
    )

conn = create_connection()
    # cursor = conn.cursor()
    # Menambahkan Kolom Hari pada database
query = "SELECT Object_Detection, Location FROM fire ORDER BY Date_Time = NOW()"  # Ganti dengan nama tabel yang ingin Anda ambil datanya
    # query = "SELECT * FROM fire"  # Ganti dengan nama tabel yang ingin Anda ambil datanya

    # cursor.execute(query)
    # col0 = [column[0] for column in cursor.description]
    # data = cursor.fetchall()
df = pd.read_sql_query(query, conn)

    # cursor.close()
conn.close()

    # return col0, data
    
st.title("Visualisasi Data dari Database")
tabel = get_data()
column_list = list(tabel.columns)
selected_column = st.selectbox("Pilih kolom:", column_list)

    # Mengambil data pada kolom terpilih
data = tabel[selected_column]

    # Menghitung frekuensi nilai pada kolom terpilih
value_counts = data.value_counts()

    # Membuat diagram bar menggunakan matplotlib
fig, ax = plt.subplots()
value_counts.plot(kind='bar')
ax.set_xlabel(selected_column)
ax.set_ylabel("Jumlah")
ax.set_title(f"Diagram Bar dari {selected_column}")
st.pyplot(fig)
    
# st.title("Visualisasi Data dari Database")
