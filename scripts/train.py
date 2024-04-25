# train.py

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
#import opendatasets as od
import joblib

# Leer los datos
train_data = pd.read_csv('./train.csv')

# Copiar los datos
train_dt = train_data.copy()

# Eliminar columnas irrelevantes
columns_to_drop = ['PassengerId', 'Cabin', 'Name']
train_dt.drop(columns_to_drop, axis=1, inplace=True)

# Codificar la columna 'Transported'
lb_encoder = LabelEncoder()
train_dt['Transported'] = lb_encoder.fit_transform(train_dt['Transported'])

# Procesar valores faltantes en los datos de entrenamiento
for i in train_dt.columns:
    if (train_dt[i].isnull().sum() / len(train_dt)) * 100 < 30:
        if train_dt[i].dtype == 'object':
            train_dt[i] = train_dt[i].fillna(train_dt[i].mode()[0])
        else:
            train_dt[i] = train_dt[i].fillna(train_dt[i].median())
    else:
        train_dt = train_dt.drop(i, axis=1)

# Codificar características categóricas
features = ['HomePlanet', 'CryoSleep', 'Destination', 'VIP']
encoder = OrdinalEncoder()
train_dt[features] = encoder.fit_transform(train_dt[features])

# Dividir datos en características y etiquetas
X = train_dt.drop(['Transported'], axis=1)
y = train_dt['Transported']

# Dividir datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el modelo
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib.dump(clf, 'spaceship_titanic_model.pkl')