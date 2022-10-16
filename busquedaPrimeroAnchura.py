#el codigo es mas interesante aumentado el costo pero aun tiene o viendo los resultados que hay la misma similitud de tiempos del codigo implementado sin costo al de ahora
#pero aun hay que decir que para mas valores sigue teniendo los mismos problemas que el otro codigo sin el costo


from Nodos import Nodo
import time
import random

def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)

    while (not resuelto) and len(nodos_frontera) != 0:

        costo_ordenado = sorted(nodos_frontera, reverse=True, key= lambda x: x.get_costo())
        for i in range(0, len(costo_ordenado)):
            if costo_ordenado[i].get_estado() == solucion:
                print(f'felicidades se hallo la solucion con el costo: {costo_ordenado[i].get_estado()}')
                break
            print(costo_ordenado[i].get_costo(), costo_ordenado[i].get_estado())
  
        
        print("-------------->")
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada\=[-p0i98]
            resuelto = True
            return nodo_actual
        else:
            # expandir nodos hijo
            for i in range (0, len(nodo_actual.get_estado())-1):
                hijos = nodo_actual.get_estado().copy()
                temp = hijos[i]    
                hijos[i] = hijos[i+1]
                hijos[i+1] = temp
                hijo_n = Nodo(hijos)
                #introduce los hijos a lista de nodo actual y frontera
                if not hijo_n.en_lista(nodos_visitados) and not hijo_n.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo_n)
                    nodos_frontera.append(hijo_n)
                #asiga un costo cualquiera a cada nodo
                if hijo_n.get_costo() == None:
                    hijo_n.set_costo(random.randrange(1, 11))


if __name__ == "__main__":
    estado_inicial = [6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6]
    inicio = time.time()
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    fin = time.time()
    for i in resultado:
        if i == solucion:
            print(f'Felicidades ha llegado a la solucion que es: {i}')
            break
        print(f'pasa por nodo {i}')

    print("tiempo de encontrar solucion: ", fin-inicio)