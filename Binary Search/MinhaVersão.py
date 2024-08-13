lista = list(x for x in range(240000))
number = 23132

cont = 0

baixo = 0
alto = len(lista) - 1

meio = alto

while lista[meio] != number:
    meio = (baixo + alto)//2
    if lista[meio] > number:
        alto = meio - 1
    else:
        baixo = meio + 1
    cont += 1

print(f"O número {number} foi encontrado em {cont} iterações.")