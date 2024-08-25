# Implicando que não exista colisões

lista = lst = [None] * 10

def value(string): # conseguir o valor numerico da string. 
    sum = 0
    for item in string:
        sum += ord(item)
    return sum


def hashf(string, sizeof = 10): # hash aleatorio que eu fiz.
    hash = value(string) % sizeof + 1
    return hash

lista[hashf("Maçã")] = 0.67
lista[hashf("Banana")] = 1.23


print(lista[hashf("Banana")])
print(lista[hashf("Maçã")])
print(lista)
