import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Membaca file CSV
data = pd.read_csv('fire.csv')

# Memilih kolom yang ingin ditampilkan
kolom = st.selectbox('Pilih kolom', data.columns)

# Menghitung frekuensi nilai dalam kolom
value_counts = data[kolom].value_counts()

# Membuat diagram batang
fig, ax = plt.subplots()
ax.bar(value_counts.index, value_counts.values)

# Mengatur label dan judul
ax.set_xlabel(kolom)
ax.set_ylabel('Frekuensi')
ax.set_title('Diagram Batang')

# Menampilkan diagram batang di Streamlit
st.pyplot(fig)
