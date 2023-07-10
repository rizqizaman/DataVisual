import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('aset/fire.json')
plt.figure(figsize=(15, 5))
# sns.countplot(data=df, x=['Api Besar', 'Api Kecil'], order=df['Notif_Deteksi'].value_counts().index[:])
sns.countplot(data=df, x='Notif_Deteksi', order=df['Notif_Deteksi'].value_counts().index[:])

    
