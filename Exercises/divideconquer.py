def sumList(lista, index=0):
    if index > len(lista) - 1:  # Caso base
        return 0
    else:
        return lista[index] + sumList(lista, index + 1)
    
def lenList(lista):
    if len(lista) == 0:
        return 0
    else:
        return 1 + lenList(lista[1:])

def highestList(lista, highest = 0):
    if len(lista) == 0:
        return highest
    else:
        if lista[0] > highest:
            return highestList(lista[1:], highest = lista[0])
        else:
            return highestList(lista[1:], highest)

def binarySearch(lista, target):
    if lista[0] == target:
        return lista[0]
    elif lista[0] > target:
        return binarySearch(lista[:(len(lista) // 2) - 1], target)
    else:
        return binarySearch(lista[(len(lista) // 2) + 1:], target)

def quickSort(arr): # Minha versão
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        if arr[0] < arr[1]:
            return arr
        else: 
            return arr[::-1]
    else:
        pivot = int(arr[(len(arr) -1) // 2])
        return (quickSort([i for i in arr if i < pivot]) + ([i for i in arr if i == pivot]) + quickSort(([i for i in arr if i > pivot])))

def qsort(arr): # Versão do livro (sinceramente minha versão é melhor em alguns casos...)
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        menores = [i for i in arr if i <= pivot]
        maiores = [i for i in arr if i > pivot]
        return (qsort(maiores) + [pivot] + maiores)


def quickestSort(arr): # Minha versão 2
    if len(arr) < 2:
        return arr
    else:
        pivot = int(arr[(len(arr) -1) // 2])
        return (quickestSort([i for i in arr if i < pivot]) + ([i for i in arr if i == pivot]) + quickestSort(([i for i in arr if i > pivot])))

# print(sumList([2, 4, 6]))
# print(lenList([2, 4, 6]))
# print(highestList([2, 4, 6, 1, 20, 2, 3]))
# print(binarySearch([2, 4, 6, 1, 20, 2, 3], 2))
print(quickSort((1, 2, 3, 3, 1, 2, 2, 3, 5, 1)))
print(qsort((1, 2, 3, 3, 1, 2, 2, 3, 5, 1)))
print(quickestSort((1, 2, 3, 3, 1, 2, 2, 3, 5, 1)))