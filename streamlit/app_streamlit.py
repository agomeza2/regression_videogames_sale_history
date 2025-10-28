import streamlit as st
import joblib 
import numpy as np 
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pkl_path = os.path.join(BASE_DIR,"../pkl/vg.pkl") 
modelo = joblib.load(pkl_path)
st.title("Prediccion de Ventas de videojuegos")
st.write("Modelo de regresion de arboles de decisiones") 

col1, col2 = st.columns(2)

with col1:
    rank = st.number_input("Ranking", min_value=0.0,max_value=1.0, step=0.01)
    name = st.number_input("Nombre" , min_value=0.0,max_value=1.0, step=0.01)
    platform = st.number_input("Plataforma", min_value=0.0,max_value=1.0, step=0.01)
    year = st.number_input("anno", min_value=0.0,max_value=1.0, step=0.01)
    genre = st.number_input("genera",min_value=0.0,max_value=1.0,step=0.01)
with col2:
    publisher = st.number_input("editor", min_value=0.0,max_value=1.0, step=0.01)
    na_sales = st.number_input("ventas Norte Americanas" , min_value=0.0,max_value=1.0, step=0.01)
    eu_sales = st.number_input("ventas europeas", min_value=0.0,max_value=1.0, step=0.01)
    jp_sales = st.number_input("ventas japon", min_value=0.0,max_value=1.0, step=0.01)
    other_sales=st.number_input("otras ventas",min_value=0.0,max_value=1.0,step=0.01) 
 
if st.button("Predecir "):
    datos = np.array([[rank,name,platform,year,genre,publisher, na_sales,eu_sales, jp_sales,other_sales]]) 
    pred = modelo.predict(datos)[0]
    st.write(pred)
              
      
