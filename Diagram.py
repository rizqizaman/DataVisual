import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_json('fire.json')

st.title('Visualisasi Data')

plt.figure(figsize=(15, 5))
sns.countplot(data=df, x='Object_Detection', order=df['Object_Detection'].value_counts().index[:])
plt.xlabel('Object Detectioni')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)

st.pyplot()
