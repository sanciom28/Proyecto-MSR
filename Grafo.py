import math
import copy

class Grafo:

    def __init__(self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range(0)]

    def imprimir_matriz(self, m, texto):
        cadena = ""

        for c in range(len(m)):
            cadena += "|" + str(self.vertices[c])

        cadena += "\n " + (" -" * len(m))

        for f in range(len(m)):
            cadena += "\n" + str(self.vertices[f]) + " |"
            for c in range(len(m)):
                if texto:
                    cadena += "\t" + str(m[f][c])
                else:
                    if f == c and (m[f][c] is None or m[f][c] == 0):
                        cadena += " " + "\\"
                    else:
                        if m[f][c] is None or math.isinf(m[f][c]):
                            cadena += " " + "X"
                        else:
                            cadena += " " + str(m[f][c])

        cadena += "\n"
        print(cadena)

    @staticmethod
    def contenido_en(lista, k):
        if lista.count(k) == 0:
            return False
        return True

    def esta_en_vertices(self, v):
        if self.vertices.count(v) == 0:
            return False
        return True

    def agregar_vertices(self, v):
        if self.esta_en_vertices(v):
            return False
        # Si no esta contenido.
        self.vertices.append(v)

        # Se redimensiona la matriz de adyacencia.
        # Para preparalarla para agregar más Aristas.
        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas+1) for i in range(columnas+1)]

        # Se recorre la matriz y se copia su contenido dentro de la matriz más grande.
        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]

        # Se iguala la matriz a la matriz más grande.
        self.matriz = matriz_aux
        return True

    def agregar_arista(self, inicio, fin, valor, dirijida):
        if not (self.esta_en_vertices(inicio)) or not (self.esta_en_vertices(fin)):
            return False
        # Si estan contenidos en la lista de vertices.
        self.matriz[self.vertices.index(
            inicio)][self.vertices.index(fin)] = valor

        # Si la arista entrante no es dirijida.
        # Instancio una Arista en sentido contrario de Fin a Inicio.
        if not dirijida:
            self.matriz[self.vertices.index(
                fin)][self.vertices.index(inicio)] = valor
        return True

    def obtener_sucesores(self, v):
        pos_vertice = self.vertices.index(v)

        list_sucesores = []

        for i in range(len(self.matriz)):
            if self.matriz[pos_vertice][i] is not None:
                list_sucesores.append(self.vertices[i])

        return list_sucesores

    def imprimir_camino(self, camino):
        if camino[0] == '54-14':
            print('\nCamino que Javier debe seguir:\n')
        else:
            print('\nCamino que Andreína debe seguir:\n')
        for i in camino:
                print(f'Calle {i[0]}{i[1]} con carrera {i[3]}{i[4]}')

    def imprimir_varios_caminos(self, camino1, camino2):
        if camino1[0] == '54-14':
            nombre = 'Javier'
        else:
            nombre = 'Andreina'
        print(f'\n{nombre} puede tomar cualquiera de estos dos caminos:\n')
        for i in camino1:
                print(f'Calle {i[0]}{i[1]} con carrera {i[3]}{i[4]}')
        print('')
        for i in camino2:
                print(f'Calle {i[0]}{i[1]} con carrera {i[3]}{i[4]}')

    # Aciclico.
    def camino(self, k, v2):
        # Con ciclos.
        return self.__camino(k, v2, [])

    def __camino(self, k, v2, visitados):
        if k == v2:
            return True

        visitados.append(k)
        sucesores = self.obtener_sucesores(k)

        for vertice in sucesores:
            if not self.contenido_en(visitados, vertice):
                if self.__camino(vertice, v2, visitados):
                    return True

        return False

    # Es un booleano que verifica si todos los nodos estan marcados
    def allMarked(self, marcados):
        for i in range(marcados.__len__()):
            if not marcados[i]:
                return False
        return True

    # Se utiliza para verificar el menor de los no marcados en un vector
    def MinValueNotMarked(self, pesos, marcados):
        # Inicializamos min en un numero infinito 999
        min = 999

        # Se inicializa pos en una posicion imposible para guardar el valor luego
        pos = -1

        # Se recorre el vector de pesos
        for i in range(pesos.__len__()):

            # Si se encuentra un vertice menor que la variable auxiliar y que no este
            # Ligado a un vertice marcado se remplaza la posicion y se guarda el valor
            if pesos[i] < min and not marcados[i]:
                min = pesos[i]
                pos = i
        return pos

    # Se hace lo mismo que para pesosDijkstra con la diferencia que se retorna
    # Un vector de recorridos
    def RecorridoDijkstra(self, inicio):
        pesos = []
        recorridos = []
        marcados = []

        pesos = [999 for i in range(self.matriz.__len__())]
        marcados = [False for i in range(self.matriz.__len__())]
        recorridos = [0 for i in range(self.matriz.__len__())]
        pesos[self.vertices.index(inicio)] = 0

        while (not self.allMarked(marcados)):
            aux = self.MinValueNotMarked(pesos, marcados)
            if aux == -1:
                break
            marcados[aux] = True
            for i in range(self.matriz.__len__()):
                if self.matriz[aux][i] != None:
                    p = self.matriz[aux][i]
                    if p + pesos[aux] < pesos[i]:
                        pesos[i] = p + pesos[aux]
                        recorridos[i] = self.vertices[aux]
        return recorridos

    # Se utiliza para verificar todos los pesos de los nodos para llegar a inicio
    def PesosDijkstra(self, inicio):
        pesos = []
        recorridos = []
        marcados = []

        # Se inicializan todos los nodos con un valor infinito en este caso 999
        pesos = [999 for i in range(self.matriz.__len__())]
        # Se crea una lista que contieen los espacios del tamano de la matriz con False
        # Verfica que los nodos ya esten recorridos
        marcados = [False for i in range(self.matriz.__len__())]

        # Colocamos una lista con 0 del tamano de la matriz original
        recorridos = [0 for i in range(self.matriz.__len__())]

        # Inicializamos la posicion del vertice inicial dentro del vector de pesos
        # Con un peso de 0
        pesos[self.vertices.index(inicio)] = 0

        # Mientras que se encuentren vertices sin marcar dentro del vector Marcados
        # Se ejecuta
        while (not self.allMarked(marcados)):
            # Se inicializa una variable auxiliar con el menor valor de los vertices
            # No marcados que se encuentren dentro del vector pesos
            aux = self.MinValueNotMarked(pesos, marcados)

            # Si no existe el valor termina el proceso
            if aux <= -1:
                break
            # Se marca el vertice auxiliar dentro del vector de vertices marcados
            marcados[aux] = True

            # Se recorre la matriz de adyacencia
            # Buscando los vertices adyacentes a la variable auxiliar
            for i in range(self.matriz.__len__()):
                # Si existe un vertice adyacente al nodo auxiliar
                if self.matriz[aux][i] != None:
                    # Se instancia una variable p para guardar el peso
                    p = self.matriz[aux][i]

                    # Si el peso del vertice adyacente + el peso del recorrido realizado
                    # es menor al peso del recorrido anterior dentro del vector de pesos
                    # Se reemplaza
                    if p + pesos[aux] < pesos[i]:
                        pesos[i] = p + pesos[aux]
                        recorridos[i] = self.vertices[aux]
        # verificando
        for i in range(len(pesos)):
            if pesos[i] > 100:
                pesos[i] = pesos[i]-94
        return pesos

    # Se hace para tomar el camino mas corto (Retorna una lista)
    def DijkstraCamino(self, inicio, fin):
        # Se obtienen todos los caminos de Dijkstra desde el nodo inicio
        recorridos = self.RecorridoDijkstra(inicio)

        # Se inicializa la lista de salidas con el nodo final
        salida = [fin]

        # Verificar que el nodo inicio sea diferente que el ultimo elemento
        # De la lista de salida y agregamos a la lista de salida
        while inicio != salida[salida.__len__()-1]:
            # Revisar si existe un camino mínimo alterno y agregrar a variante
            salida.append(
                recorridos[self.vertices.index(salida[salida.__len__()-1])])

        # Revertimos la lista para que quede en su forma original
        recorridos = list(reversed(salida))
        # Se retorna una lista con los recorridos
        return recorridos

    # SE UTILIZA PARA CREAR EL GRAFO
    def DijkstraGrafo(self, inicio, fin):
        # Si la lista de vertices no contiene el vertice inicio o el vertice final
        # No se puede recorrer
        if self.vertices.index(inicio) == -1 or self.vertices.index(fin) == -1:
            return None
        # Se instancia un grafo para guardar la informacion
        g = Grafo()

        # Se encuentra el camino (Retorna una lista)
        recorrido = self.DijkstraCamino(inicio, fin)
        # print(recorrido)

        # Retorna la lista de pesos de los grafos
        pesos = self.PesosDijkstra(inicio)

        # Retorna el peso del grafo total
        pesosCamino = pesos[self.vertices.index(fin)]

        # Se agregan los vertices al nuevo grafo
        for i in recorrido:
            g.agregar_vertices(i)

        # Se agregan las aristas de los vertices del nuevo grafo
        # Con el peso en cada vertice desde el inicio hasta ese vertice
        for i in range(recorrido.__len__()-1):
            pesosAux = self.PesosDijkstra(recorrido[i])
            pesosCaminoAux = pesosAux[self.vertices.index(recorrido[i+1])]
            g.agregar_arista(
                recorrido[i], recorrido[i+1], pesosCaminoAux, True)

        return g

    # Se hace doble Dijkstra y se modifican las matrices
    def CaminoCortoJavierAndreina(self, inicioJavier, inicioAndreina, fin):

        g = copy.deepcopy(self)
        grafoSegundaVuelta = copy.deepcopy(self)
        gd = g.DijkstraGrafo(inicioJavier, fin)
        gdPesos = gd.PesosDijkstra(inicioJavier)

        
        lista_vertices_j1 = list(gd.vertices)

        # Guarda el peso de Javier recorrido 1
        gdPesosJ1 = gdPesos[gdPesos.__len__()-1]

        # Se hace para colocar los nodos ya visitados por Javier
        # Que no sean visitados por Andreina
        # Para evitar que se crucen
        for i in gd.vertices:
            for a in range(g.matriz[g.vertices.index(i)].__len__()):
                if g.matriz[g.vertices.index(i)][a] != None:
                    g.matriz[g.vertices.index(i)][a] = 999

            for a in g.matriz:
                if a[0] != None :
                    a[0] = 99

        gd2 = g.DijkstraGrafo(inicioAndreina, fin)
        pesosg2 = gd2.PesosDijkstra(inicioAndreina)
        
        lista_vertices_a1 = list(gd2.vertices)
        
        # Guarda el peso de Andreina Recorrido 1
        gdPesosA1 = pesosg2[pesosg2.__len__()-1]+(2*pesosg2.__len__()-2)

        # La segunda vuelta comienza con Andreina
        gdSegundaVuelta = grafoSegundaVuelta.DijkstraGrafo(
            inicioAndreina, fin)
        pesosgdSegundaVuelta = gdSegundaVuelta.PesosDijkstra(inicioAndreina)
        lista_vertices_a2 = list(gdSegundaVuelta.vertices)

        # Guarda el peso de Andreina recorrido 2
        gdPesosA2 = pesosgdSegundaVuelta[pesosgdSegundaVuelta.__len__(
        )-1]+(2*pesosgdSegundaVuelta.__len__()-2)
        for i in gdSegundaVuelta.vertices:
            for a in range(grafoSegundaVuelta.matriz[grafoSegundaVuelta.vertices.index(i)].__len__()):
                if grafoSegundaVuelta.matriz[grafoSegundaVuelta.vertices.index(i)][a] != None:
                    grafoSegundaVuelta.matriz[grafoSegundaVuelta.vertices.index(
                        i)][a] = 999

            for a in grafoSegundaVuelta.matriz:
                if (a[0] != None):
                    a[0] = 99

        # JAVIER SEGUNDA VUELTA
        gd2SegundaVuelta = grafoSegundaVuelta.DijkstraGrafo(
            inicioJavier, fin)
        pesosgd2SegundaVuelta = gd2SegundaVuelta.PesosDijkstra(inicioJavier)
        lista_vertices_j2 = list(gd2SegundaVuelta.vertices)

        # Guarda el peso de Javier recorrido 2
        gdPesosJ2 = pesosgd2SegundaVuelta[pesosgd2SegundaVuelta.__len__()-1]

        # analizar recorrido mínimo
        min(gdPesosA1+gdPesosJ1,gdPesosA2+gdPesosJ2)
        costo1 = gdPesosA1+gdPesosJ1
        costo2 = gdPesosA2+gdPesosJ2

        # cualquier iteración sirve
        if costo1 == costo2:
            # si hay un solo camino más corto
            if lista_vertices_a1 == lista_vertices_a2 and lista_vertices_j1 == lista_vertices_j2:
                g.imprimir_camino(lista_vertices_j1)
                g.imprimir_camino(lista_vertices_a1)
            # si Javier puede tomar más de una ruta
            elif lista_vertices_a1 == lista_vertices_a2:
                g.imprimir_varios_caminos(lista_vertices_j1,lista_vertices_j2)
                g.imprimir_camino(lista_vertices_a1)
            # si Andreina puede tomar más de una ruta
            elif lista_vertices_j1 == lista_vertices_j2:
                g.imprimir_camino(lista_vertices_j1)
                g.imprimir_varios_caminos(lista_vertices_a1,lista_vertices_a2)
            # si ambos pueden escoger más de una ruta
            else:
                g.imprimir_varios_caminos(lista_vertices_j1,lista_vertices_j2)
                g.imprimir_varios_caminos(lista_vertices_a1,lista_vertices_a2)
                print('\nNOTA: para no cruzarse, ambos deben escoger o el primer camino o el segundo camino.')

        # la primera iteración es la mejor
        elif costo1 < costo2:
            g.imprimir_camino(lista_vertices_j1)
            g.imprimir_camino(lista_vertices_a1)

        # la segunda iteración es la mejor
        else:
            g.imprimir_camino(lista_vertices_j2)
            g.imprimir_camino(lista_vertices_a2)

        tiempo_j = min(gdPesosJ1,gdPesosJ2)
        tiempo_a = min(gdPesosA1,gdPesosA2)

        print('\nTiempo final de Javier: '+str(tiempo_j)+' minutos\n')
        print('Tiempo final de Andreina: '+str(tiempo_a)+' minutos\n')

        if tiempo_j < tiempo_a:
            print('Para que lleguen al mismo tiempo, Andreína debe salir de su casa '+str(tiempo_a-tiempo_j)+' minutos antes que Javier.\n')
        elif tiempo_j > tiempo_a:
            print('Para que lleguen al mismo tiempo, Javier debe salir de su casa '+str(tiempo_j-tiempo_a)+' minutos antes que Andreína.\n')
        else:
            print('Para que lleguen al mismo tiempo, deben salir al mismo tiempo.\n')

        exit()
