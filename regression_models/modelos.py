import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error 
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

df = pd.read_csv('../data_preprocessing/output/vg_sales_limpio.csv')
#Separamos variables en features (x) y target (y)
x = df.drop('Global_Sales',axis=1)
y = df['Global_Sales']

#dividimos en entrenamiento y prueba
X_train, X_test, y_train, y_test =train_test_split(x,y, test_size=0.30, random_state=42)

#print(X_train.head())

#entrenamos los modelos
#1. Regresion Logistica

log_model= LogisticRegression(max_iter=1000)
log_model.fit(X_train, (y_train > y_train.mean()).astype(int))
y_pred_log =log_model.predict(X_test)

#2. Xgboost

xg_model=XGBRegressor(random_state=42)
xg_model.fit(X_train, y_train)
y_pred_xg =xg_model.predict(X_test)

#3. Arbol de decision

tree_model= DecisionTreeRegressor(random_state=42)
tree_model.fit(X_train, y_train)
y_pred_tree =tree_model.predict(X_test)

mse_log =mean_squared_error(y_test, y_pred_log)
mse_tree =mean_squared_error(y_test, y_pred_tree)
mse_xg =mean_squared_error(y_test, y_pred_xg)

print('mse logRegression:')
print(mse_log)
print('El mse de arbol de decisi es:')
print(mse_tree)
print('El mse de xboostRegression es:')
print(mse_xg)

#El mejor modelo es random forest con el 87% de accuracy
#Exportamos en un pkl
pickle.dump(tree_model,open('../pkl/vg.pkl','wb'))
