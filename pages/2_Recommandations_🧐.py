import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import donnees
df = pd.read_csv('data/moodie_tmdb.csv', index_col=0)
df=df.sort_values(by='original_title',ascending=True)

st.header("Moodie 🎬")

# ------------------- Jeu de données --------------------
if st.checkbox('Visionner le jeu de données',value=True):
    pass
else:
    st.write(df[['original_title','genre_names']])

# ------------------ Question 1 ------------------------
st.selectbox("Es-tu fatigué aujourd'hui ?", ['Ouais, éclaté au sol', 'Non, je suis bien'])

# ------------------ Question 2 ------------------------
st.selectbox("As-tu envie d'apprendre ?", ["J'ai compris, envoie le reportage !","Non, pas forcément"])

# ------------------ Question 3 ------------------------
st.selectbox("Dans quelle ambiance veux-tu être transporté ?",["Lets'go US or UK","Ambiance latine","La France des terroirs"])