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


print(sumList([2, 4, 6]))
print(lenList([2, 4, 6]))
print(highestList([2, 4, 6, 1, 20, 2, 3]))
print(binarySearch([2, 4, 6, 1, 20, 2, 3], 2))
