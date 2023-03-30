# -*- coding: utf-8 -*-
"""Lab8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rsENLM5HGz_T-z0COikxGwgs3CSOcsHW
"""

#Cargamos el Archivo de Entrenamiento y de Prueba 
from google.colab import files
from IPython.display import Image

uploaded = files.upload()

#Importar librerias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Cargar los datos de entrenamiento desde el archivo CSV
train_data = pd.read_csv('train.csv')

# Separar las características de entrada (valores de píxel) de las etiquetas de clase
X_train = train_data.drop('label', axis=1).values
y_train = train_data['label'].values

# Escalar los datos de entrada
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Crear una instancia de Perceptron y entrenar el modelo
ppn = Perceptron()
ppn.fit(X_train, y_train)

# Evaluar la precisión del modelo en los datos de entrenamiento
y_pred = ppn.predict(X_train)
accuracy = accuracy_score(y_train, y_pred)
print('Precision:', accuracy)

# Cargar datos de prueba
new_data = pd.read_csv('testmodificado.csv')
new_img = new_data.values[0]

# Realizar la predicción
prediction = ppn.predict([new_img])

# Graficar la Imagen
new_img = new_img.reshape(28, 28)
print("La imagen es:")
plt.imshow(new_img, cmap="gray")
plt.show()
print("Predicción del modelo:", prediction)