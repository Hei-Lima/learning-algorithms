def value(string):
    sum = 0
    for item in string:
        sum += ord(item)
    return sum


def hashf(string, sizeof = 20):
    hash = value(string) % sizeof
    return {hash: string}

lista = []

lista.append(hashf("Banana"))
lista.append(hashf("Mazana"))
lista.append(hashf("Batata"))
lista.append(hashf("Biscoito"))


print(lista)

