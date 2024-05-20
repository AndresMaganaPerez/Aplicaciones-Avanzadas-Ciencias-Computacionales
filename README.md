### Clasificador de Cataratas
## Descripción del Proyecto
En este proyecto desarrollamos un clasificador de cataratas inmaduras y maduras en base a un dataset de imágenes obtenido en Kaggle. Este proyecto ayudaría a identificar de manera más rápida la madurez de cataratas que tiene una persona.

Descripción del Dataset
Para el proyecto estamos utilizando un dataset de Kaggle. El dataset que estamos utilizando contiene 410 imágenes categorizadas en dos clases: cataratas inmaduras y maduras. Este dataset está diseñado para realizar practicas de Machine Learning.

El dataset contiene 410 imágenes de residuos etiquetados en varias categorías:

Inmaduro: 214 imágenes.

Maduro: 196 imágenes.

Estas categorías se encuentran en sus correspondientes carpetas.

Para mayor información, ingresar al siguiente link: [Cataract Classification Dataset](https://www.kaggle.com/datasets/akshayramakrishnan28/cataract-classification-dataset).

## Pasos
# Obtener, generar o aumentar un set de datos.
El data set utilizado para el proyecto fue obtenido en Kaggle, descargado y luego posicionado en una carpeta dentro de drive, para su siguiente manipulación dentro del código.

# Preprocesado y Split de Entrenamiento y Validación.
Con la función de keras, ImageDataGenerator, dentro de los parámetros, se declaró un balanceo para los datos de entrenamiento y prueba, de la siguiente forma:

Entrenamiento: 80%.
Prueba: 20%.

## Técnicas de escalamiento.
Las técnicas de escalamiento usadas fueron las siguientes:

- rescale - redimensiona las imágenes en una escala de 0 a 255.
- rotation_range - el rango de rotación que puede aplicar.
- width_shift_range - cambios horizontales aleatorios.
- height_shift_range - cambios verticales aleatorios.
- shear_range - crea un estilo de distorsión aleatoria.
- zoom_range - zooms aleatorios en las imágenes.
- horizontal_flip - cambia la imagen horizontalmente con un 50% de probabilidad.

## Licencia
Bajo la licencia de [CreativeCommons](https://creativecommons.org/licenses/by-sa/4.0/) por el uso del Cataract Classification Dataset.

## Autor
Andrés Magaña Pérez - andresmagania02@gmail.com
