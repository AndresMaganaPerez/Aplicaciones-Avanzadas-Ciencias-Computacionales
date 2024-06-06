# Clasificador de Cataratas
## Descripción del Proyecto
En este proyecto desarrollamos un clasificador de cataratas inmaduras y maduras en base a un dataset de imágenes obtenido en Kaggle. Este proyecto ayudaría a identificar de manera más rápida la madurez de cataratas que tiene una persona.

## Descripción del Dataset
Para el proyecto estamos utilizando un dataset de Kaggle. El dataset que estamos utilizando contiene 410 imágenes categorizadas en dos clases: cataratas inmaduras y maduras. Este dataset está diseñado para realizar practicas de Machine Learning.

El dataset contiene 410 imágenes de residuos etiquetados en varias categorías:

Inmaduro: 214 imágenes.

Maduro: 196 imágenes.

Estas categorías se encuentran en sus correspondientes carpetas.

Para mayor información, ingresar al siguiente link: [Cataract Classification Dataset](https://www.kaggle.com/datasets/akshayramakrishnan28/cataract-classification-dataset).

# Proceso
## Obtener, generar o aumentar un set de datos.
El data set utilizado para el proyecto fue obtenido en Kaggle, descargado y luego posicionado en una carpeta dentro de drive, para su siguiente manipulación dentro del código.

## Preprocesado y Split de Entrenamiento y Validación.
Utilizando la función de [split-folders](https://pypi.org/project/split-folders/) de python, la carpeta de imágenes descargada desde Kaggle la dividimos de la siguiente forma:

* Entrenamiento: 60%
* Validación: 20%
* Prueba: 20%

Despues de haberlas dividido, las subimos a Google Drive para su uso dentro del modelo. En el repositorio se pueden encontrar las **carpetas** de *train*, que es el de las imágenes antes de hacer el split, y *output*, que es la carpeta ya divida.

## Técnicas de escalamiento para aumentación y preprocesado
Las técnicas de escalamiento usadas fueron las siguientes:

- rescale - redimensiona las imágenes en una escala de 0 a 255.
- rotation_range - el rango de rotación que puede aplicar.
- width_shift_range - cambios horizontales aleatorios.
- height_shift_range - cambios verticales aleatorios.
- shear_range - crea un estilo de distorsión aleatoria.
- zoom_range - zooms aleatorios en las imágenes.
- horizontal_flip - cambia la imagen horizontalmente con un 50% de probabilidad.

Estas técnicas se utilizaron con la función de [ImageDataGenerator](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator). Esta función crea imágenes modificadas con las técnicas determinadas, en el momento que se corre el código, sin generar espacio en el disco duro. Esto nos ayuda a obtener más datos para entrenar al modelo que creamos.

## Modelo VGG16 Convolutional Neural Network (CNN)
Para crear nuestro modelo utilizamos una arquitectura conocida y estandarizada, la arquitectura **VGG16**[1][2]. Esta arquitectura proviene de Visual Geometry Group (VGG) de Oxford. En general las arquitecturas de VGG son bastante conocidas en el área de Visión Computacional y Deep Learning. Las Convolutional Layers se encargan de extraer diferentes características de las imágenes, como esquinas, texturas, etc. Entre más capas haya, más abstractas se vuelven estas características. Estas las va aprendiendo y las va dejando en tensores, que son de 3 dimensiones. Las capas densas se utilizan para seguir aprendiendo y después realizar las predicciones. Para que las características aprendidas pasen de la confolutional layers a las dense layers se utiliza la capa flatten, que convierte los tensores en un vector y que este pueda ser utilizado por las capas densas.

El optimizador se utiliza para reducir la función de pérdida (loss). En este caso utilizamos * "Adaptive Moment Estimation" * o Adam como optimizador. Utilizamos este optimizador porque tiene bastante buen performance en múltiples tareas y es menos sensible a los cambios que se hagan en los hiperparámetros.

La función de loss se le conoce también como función de objetivo, y se utiliza para saber qué tan bien son las predicciones con las verdaderas etiquetas. Para la función de loss, utilizamos binary_crossentropy ya que es un problema de clasificación binario. Esta da un resultado de presencia o ausencia de una clase. Otras funciones de loss como Mean Square Error o Categorical Crossentropy son utilizadas para otro tipos de tareas, específicamente Categorical Crossentropy se utiliza para clasificación de más de una clase.

Por último, las métricas se utilizan para medir el performance del modelo. En este caso utilizamos accuracy el cual se enfoca en calcular el porcentaje de predicciones correctas. Otro tipo de métricas se llegan a utilizar con datasets desbalanceados. Ya que en esta práctica estamos aprendiendo por primera vez cómo hacer un modelo de Machine Learning, utilizamos accuracy, además de que estamos utilizando un data set balanceado.


Elegí utilizar esta arquitectura ya que a comparación de algunas otras no tiene tantas capas en el modelo, cuenta con 16, mientras otras llegan a contar con alrededor de 20 o hasta más de 100 capas. Además, dentro de estas arquitecturas, tiene un accuracy promedio del 74.4%. 

![image](https://github.com/AndresMaganaPerez/Aplicaciones-Avanzadas-Ciencias-Computacionales/assets/88801753/bd153ce4-5031-4ce5-8184-30ff6f362cbd)

Para mi primer modelo de Deep Learning, creo que fue una arquitectura correcta ya que pude entender cómo funciona y el porqué de las cosas que implementé en el código.

## Resultados
### Primera Ronda
En la primera ronda utilizamos un valor para las épocas de 10, y esto nos arrojó los siguientes valores:

![image](https://github.com/AndresMaganaPerez/Aplicaciones-Avanzadas-Ciencias-Computacionales/assets/88801753/06359d1b-a0e3-475d-8fd5-d3302a7c9451)

Como podemos ver, el accuracy tiene un incremento gradual, que es algo que buscamos con esta métrica, ya que significa que el modelo va aprendiendo. Del otro modo, el loss va disminuyendo y se queda muy cerca del 0, dando una salida que buscamos también ya que significa que hay menos errores por parte del modelo.

A la hora de probarlo con los valores de **testing** obtuvimos un accuracy del **84%**.

Estas fueron las predicciones que arrojó el modelo:

![image](https://github.com/AndresMaganaPerez/Aplicaciones-Avanzadas-Ciencias-Computacionales/assets/88801753/f9073ac0-314b-4e6a-979b-94e2581656bb)

Y esta fue la matriz de confusión de la ronda:

![image](https://github.com/AndresMaganaPerez/Aplicaciones-Avanzadas-Ciencias-Computacionales/assets/88801753/93c14fb2-3563-4688-a580-b0596443cf7a)

Precisión inmaduro: 0.84

Recall inmaduro: 1.0

Precisión maduro: 0.67

Recall maduro: 0.67


## Licencia
Bajo la licencia de [CreativeCommons](https://creativecommons.org/licenses/by-sa/4.0/) por el uso del Cataract Classification Dataset.

## Autor
Instituto Tecnológico de Monterrey

Andrés Magaña Pérez - andresmagania02@gmail.com

## Referencias
[1] L. Chen, S. Li, Q. Bai, J. Yang, S. Jiang, and Y. Miao, "Review of Image Classification Algorithms Based on Convolutional Neural Networks," Remote Sensing, vol. 13, no. 22, p. 4712, Nov. 2021. [Online]. Available: https://doi.org/10.3390/rs13224712.

[2] K. Simonyan and A. Zisserman, "Very Deep Convolutional Networks for Large-Scale Image Recognition," arXiv preprint arXiv:1409.1556, Sep. 2014. [Online]. Available: https://arxiv.org/pdf/1409.1556
