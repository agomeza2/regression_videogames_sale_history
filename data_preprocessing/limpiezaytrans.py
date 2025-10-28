import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('vgsales.csv')
df['Year'].fillna(df['Year'].mean(),inplace=True)
df['Publisher'].fillna(df['Publisher'].mode().iloc[0],inplace=True)   
print(df.isna().sum()) 
#print(df.head())

#codificar variables categoricas

'''
Usar label encoding o el metodo replace cuando la varibale tiene un orden natural
(ordinal). Usar onehotencoding u otro cuando la variable es nomminal
'''
#Para este ejemplo usamos label encoding
columnas_cateogricas=['Name','Platform','Genre','Publisher']
encoder=LabelEncoder()
for col in columnas_cateogricas:
    df[col] =encoder.fit_transform(df[col])

#consultar como se puede crear un diccionario para saber que numero le corresponde a cada variable
#print(df.head())
'''
Escalar la variables numericas, esto se hace para controlar el rango de las variables.
Algunos modelos sobre todo, los de redes neuronales son suceptibles a variables no homogeneas.
Se puede usar Minmax scaler, los valores quedan en un rango entre 0 y 1, otros metodos son
standar scaling
'''
#Usamos Minmaxscaler
scaler = MinMaxScaler()
columnas_numericas = ['Rank','Year','NA_Sales','EU_Sales','JP_Sales','Other_Sales']
df[columnas_numericas] =scaler.fit_transform(df[columnas_numericas])
#print(df.head())

#creamos el archivo con los datos transformados
df.to_csv('output/vg_sales_limpio.csv',index=False)
