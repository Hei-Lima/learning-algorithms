lista = list(range(0,240000000,5))
number = 23132

def binarySearch(lista, item):

    high = len(lista) - 1
    low = 0
    cont = 0

    while low <= high:
        middle = (high + low) // 2
        if lista[middle] == item:
            print(f"Item {item} was found on address {middle} after {cont} iterations")
            return middle
        elif lista[middle] < item:
            high = middle - 1
        else:
            low = middle + 1
        cont += 1
    print(f"Item {item} was not found after {cont} iterations")
    return None

binarySearch(lista, number)