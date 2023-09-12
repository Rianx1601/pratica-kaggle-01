import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQr-LOrYgj7bms8Gxp98pmYllO5GxFFPIXvqUbMTM0wJAePhzMRhu0B6-uhV44zgw-A36i2AemzisCz/pub?gid=1313189961&single=true&output=csv"

data = pd.read_csv(url, on_bad_lines='skip')


aa = sns.histplot(data['Popularity'], kde=True, color='g', bins=20)   
st.pyplot(aa.figure)


st.title("As 10 músicas mais populares!")
fig, ax = plt.subplots()
ax = sns.barplot(x="Name", y="Popularity", data=data.groupby(['Name']).sum().sort_values('Popularity', ascending=False).iloc[:10].reset_index())
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set(xlabel='Músicas', ylabel='Popularidade')
st.pyplot(fig)


st.title("Os 10 álbuns Mais populares!")
fig, ax = plt.subplots()
ax = sns.barplot(x="Album", y="Popularity", data=data.groupby(['Album']).sum().sort_values('Popularity', ascending=False).iloc[:10].reset_index())
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set(xlabel='Álbuns', ylabel='Popularidade')
st.pyplot(fig)
