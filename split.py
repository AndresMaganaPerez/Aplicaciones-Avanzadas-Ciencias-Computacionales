""" 
Data Split

Utilizamos la librería de python para dividir las clases en training, validation y testing.
Determinamos un ratio de 80% para entrenar y afinar el modelo, con un 60% en training y un 
20% en validation, y el 20% restante para testing. 

"""

import splitfolders

# Hacemos el split de las clases Immature y Mature

splitfolders.ratio(r"./train/", output="output",
    seed=1337, ratio=(.6, .2, .2), group_prefix=None, move=False) # default values