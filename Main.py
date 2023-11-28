import math
import copy
from Grafo import Grafo


g = Grafo()
gInicial = Grafo()

# Creando intersecciones (nodos)
g.agregar_vertices("50-10")
g.agregar_vertices("50-11")
g.agregar_vertices("50-12")
g.agregar_vertices("50-13")
g.agregar_vertices("50-14")

g.agregar_vertices("51-10")
g.agregar_vertices("51-11")
g.agregar_vertices("51-12")
g.agregar_vertices("51-13")
g.agregar_vertices("51-14")

g.agregar_vertices("52-10")
g.agregar_vertices("52-11")
g.agregar_vertices("52-12")
g.agregar_vertices("52-13")
g.agregar_vertices("52-14")

g.agregar_vertices("53-10")
g.agregar_vertices("53-11")
g.agregar_vertices("53-12")
g.agregar_vertices("53-13")
g.agregar_vertices("53-14")

g.agregar_vertices("54-10")
g.agregar_vertices("54-11")
g.agregar_vertices("54-12")
g.agregar_vertices("54-13")
g.agregar_vertices("54-14")

# Creando calles
g.agregar_arista("50-10", "50-11", 5, False)
g.agregar_arista("50-11", "50-12", 5, False)
g.agregar_arista("50-12", "50-13", 5, False)
g.agregar_arista("50-13", "50-14", 5, False)

g.agregar_arista("51-10", "51-11", 10, False)
g.agregar_arista("51-11", "51-12", 10, False)
g.agregar_arista("51-12", "51-13", 10, False)
g.agregar_arista("51-13", "51-14", 10, False)

g.agregar_arista("52-10", "52-11", 5, False)
g.agregar_arista("52-11", "52-12", 5, False)
g.agregar_arista("52-12", "52-13", 5, False)
g.agregar_arista("52-13", "52-14", 5, False)

g.agregar_arista("53-10", "53-11", 5, False)
g.agregar_arista("53-11", "53-12", 5, False)
g.agregar_arista("53-12", "53-13", 5, False)
g.agregar_arista("53-13", "53-14", 5, False)

g.agregar_arista("54-10", "54-11", 5, False)
g.agregar_arista("54-11", "54-12", 5, False)
g.agregar_arista("54-12", "54-13", 5, False)
g.agregar_arista("54-13", "54-14", 5, False)

# Creando carreras
g.agregar_arista("50-10", "51-10", 5, False)
g.agregar_arista("51-10", "52-10", 5, False)
g.agregar_arista("52-10", "53-10", 5, False)
g.agregar_arista("53-10", "54-10", 5, False)

g.agregar_arista("50-11", "51-11", 5, False)
g.agregar_arista("51-11", "52-11", 5, False)
g.agregar_arista("52-11", "53-11", 5, False)
g.agregar_arista("53-11", "54-11", 5, False)

g.agregar_arista("50-12", "51-12", 7, False)
g.agregar_arista("51-12", "52-12", 7, False)
g.agregar_arista("52-12", "53-12", 7, False)
g.agregar_arista("53-12", "54-12", 7, False)

g.agregar_arista("50-13", "51-13", 7, False)
g.agregar_arista("51-13", "52-13", 7, False)
g.agregar_arista("52-13", "53-13", 7, False)
g.agregar_arista("53-13", "54-13", 7, False)

g.agregar_arista("50-14", "51-14", 7, False)
g.agregar_arista("51-14", "52-14", 7, False)
g.agregar_arista("52-14", "53-14", 7, False)
g.agregar_arista("53-14", "54-14", 7, False)

gInicial = copy.deepcopy(g)

destino = input('\n\nBienvenidos, Javier y Andreína!\nIntroduzcan su destino deseado aquí:\n\n--> ')
while True:
    if destino.lower() == 'the darkness':
        g.CaminoCortoJavierAndreina("54-14", "52-13", "50-14")
    elif destino.lower() == 'la pasion' or destino.lower() == 'la pasión':
        g.CaminoCortoJavierAndreina("54-14", "52-13", "54-11")
    elif destino.lower() == 'mi rolita':
        g.CaminoCortoJavierAndreina("54-14", "52-13", "50-12")
    elif destino.lower() == 'sensacion' or destino.lower() == 'sensación':
        g.CaminoCortoJavierAndreina("54-14", "52-13", "50-10")
    else:
        print('Destino no encontrado.')
        destino = input('Introduzca su destino deseado aquí:\n\n--> ')