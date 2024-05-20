### Clasificador de Cataratas
## Descripción del Proyecto
En este proyecto desarrollamos un clasificador de cataratas inmaduras y maduras en base a un dataset de imágenes obtenido en Kaggle. Este proyecto ayudaría a identificar de manera más rápida la madurez de cataratas que tiene una persona.

Descripción del Dataset
Para el proyecto estamos utilizando un dataset de Kaggle. El dataset que estamos utilizando contiene 410 imágenes categorizadas en dos clases: cataratas inmaduras y maduras. Este dataset está diseñado para realizar practicas de Machine Learning.

El dataset contiene 410 imágenes de residuos etiquetados en varias categorías:

Inmaduro: 411 imágenes.

Maduro: 420 imágenes.

Estas categorías se encuentran en sus correspondientes carpetas.

Para mayor información, ingresar al siguiente link: [Cataract Classification Dataset](https://www.kaggle.com/datasets/akshayramakrishnan28/cataract-classification-dataset).

## Instrucciones
# Obtener, generar o aumentar un set de datos.
El data set utilizado para el proyecto fue obtenido en Kaggle, descargado y luego posicionado en una carpeta dentro de drive, para su siguiente manipulación dentro del código.

# Hacer la separación de los sets de prueba y entrenamiento.
Utilizamos la función de scikit-learn train-test-split, en la cual se puso los siguientes parámetros:

Entrenamiento: 80%.
Prueba: 20%.

## Técnicas de escalamiento.
Las técnicas de escalamiento usadas fueron las siguientes:

rescale = 1/255: Normaliza los valores de los píxeles de las imágenes dividiéndolos por 255. Esto escala los valores de los píxeles para que estén en el rango [0, 1]. Asegura que los valores de los píxeles estén en una escala adecuada para el procesamiento por el modelo.

rotation_range = 40: Aplica una rotación aleatoria a las imágenes dentro del rango especificado en grados. Introduce variabilidad en las imágenes.

width_shift_range = 0.1: Realiza un desplazamiento horizontal aleatorio a las imágenes dentro del rango especificado. En este caso utilizamos 0.1 para que los desechos no salgan demasiado de la imagen.

height_shift_range = 0.1: Realiza un desplazamiento vertical aleatorio a las imágenes dentro del rango especificado. En este caso utilizamos 0.1 para que los desechos no salgan demasiado de la imagen.

zoom_range = 0.05: Aplica un zoom aleatorio a las imágenes dentro del rango especificado. Estamos utilizando 0.05 para crear imágenes variadas que no modifiquen demasiado la imagen original.

horizontal_flip = True: Voltea horizontalmente aleatoriamente las imágenes. Agrega variabilidad al conjunto de datos al reflejar las imágenes horizontalmente.

fill_mode='reflect': Especifica cómo rellenar los píxeles que pueden quedar vacíos después de aplicar transformaciones. Estamos utilizando reflect para rellenar con valores reflejados los píxeles que quedan vacíos para mantener la integridad visual de las imágenes.

## Licencia
Bajo la licencia de CreativeCommons por el uso del Cataract Classification Dataset.

## Autor
Andrés Magaña Pérez - andresmagania02@gmail.com
