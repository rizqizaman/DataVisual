import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca file JSON
data = pd.read_json('fire.json')

st.title('Diagram Batang dari File JSON')

# Memilih kolom untuk ditampilkan
column = st.selectbox('Pilih Kolom', data.columns)

# Menghitung frekuensi nilai pada kolom yang dipilih
value_counts = data[column].value_counts()

# Membuat diagram batang
fig, ax = plt.subplots()
ax.bar(value_counts.index, value_counts.values)
plt.xlabel(column)
plt.ylabel('Frekuensi')
plt.title('Diagram Batang')

# Menampilkan diagram batang menggunakan Streamlit
st.pyplot(fig)
