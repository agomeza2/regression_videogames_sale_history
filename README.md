# regression_videogames_sale_history
Modelos de regresion para el dataset del historial de ventas de videojuegos. Regression for videogames history sales dataset

Preprocessing/Preprocesamiento:
reemplazo de valores NaN:Filling NaN values
Conversion de valores categoricos a numericos:Label Enconding categorical values
Escalado de numeros de 0.0 a 1.0:Scaling numerical values (including categorical ones)
Modelos/Models:
 Regresion XGBOOST:XGBOOST Regression 
 Regresion de arboles de desiciones:descisionTreeRegression
 Regresion logistica:Logistic Regression
producto: pkl/vg.pkl

Despliegue/Deploy:
Streamlit app
streamlit/app_streamlit.py

funcionamiento/works

1) python /data_preprocessing/limpiezatrans.py 
2) python /regression_models/modelos.py 
3) streamlit run app_streamlit.py  
