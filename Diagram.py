import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca file JSON
data = pd.read_json('fire.json')

st.title('Visualisasi Data')

# Memilih kolom untuk ditampilkan
# column = st.selectbox('Pilih Kolom', data.columns)

# Menghitung frekuensi nilai pada kolom yang dipilih
# value_counts = data[column].value_counts()
value_counts = data["Object_Detection"].value_counts()

# Membuat diagram batang
fig, ax = plt.subplots()
ax.bar(value_counts.index, value_counts.values)
plt.xlabel("Object Detection") #column)
plt.ylabel('Count')
plt.title('Object Detection')

# Menampilkan diagram batang menggunakan Streamlit
st.pyplot(fig)
