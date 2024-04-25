# predict.py

import pandas as pd
import joblib
from sklearn.preprocessing import OrdinalEncoder

# Cargar el modelo entrenado
model = joblib.load('spaceship_titanic_model.pkl')

# Leer el conjunto de datos de entrada
input_data = pd.read_csv('input_data.csv')  # Cambia 'input_data.csv' al nombre de tu archivo CSV de entrada

# Eliminar columnas irrelevantes
columns_to_drop = ['PassengerId', 'Cabin', 'Name']
input_data.drop(columns_to_drop, axis=1, inplace=True)

# Codificar características categóricas
features = ['HomePlanet', 'CryoSleep', 'Destination', 'VIP']
encoder = OrdinalEncoder()
input_data[features] = encoder.fit_transform(input_data[features])

# Realizar predicciones
predictions = model.predict(input_data)

# Agregar las predicciones al conjunto de datos de entrada
input_data['Predicted_Transported'] = predictions

# Guardar el conjunto de datos con las predicciones
input_data.to_csv('predictions.csv', index=False)  # Guarda las predicciones en un archivo CSV llamado 'predictions.csv'