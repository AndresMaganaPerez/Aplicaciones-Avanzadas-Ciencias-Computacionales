import numpy as np
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo 
  
# Importamos el data set iris (id 53) del repositorio UCI
iris = fetch_ucirepo(id=53) 
  
# Extrae las características (features) y las etiquetas (targets)
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
# print(iris.metadata) 
# # variable information 
# print(iris.variables) 

# Utilizamos la librería de train_test_split de scikit-learn para dividir los datos
"""  
train_test_split recibe diferentes parámetros:  
- arrays = los arreglos donde se van a vaciar los splits
- test_size = el tamaño de prueba que sería 20% en este caso y el 80% de entrenamiento
- train_size = el tamaño de entrenamiento que en este caso está implícito
- random_state = asegura la reproducibilidad de la división de datos.
- shuffle = genera un mezclado de datos de los datos (V/F)
- stratify = se utiliza para que la división de datos mantenga la misma proporción de clases que el conjunto original

"""
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, shuffle=True)