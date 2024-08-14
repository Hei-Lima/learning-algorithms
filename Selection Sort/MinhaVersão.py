import random
import math

lista = list(range(0, 1200, 5))
random.shuffle(lista)

def SelectionSort(lista):
    for i in range(len(lista)):
        smallest = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[smallest]:
                smallest = j
        lista[i], lista[smallest] = lista[smallest], lista[i] 

    return lista

print(f"{(SelectionSort(lista))}")
