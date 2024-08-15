lista = list(range(240000000))
number = 23132

def BinarySearch(item, lista):
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == item:
            return mid
        elif lista[mid] < item: 
            low = mid + 1
        else:
            high = mid - 1

print(BinarySearch(number, lista))