lista = list(x for x in range(240000))
number = 23132
cont = 0

def pesquisa_binaria(lista, item):
    cont = 0
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            print(f"O número {number} foi encontrado em {cont} iterações.")
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
        cont += 1
    return None
    
pesquisa_binaria(lista, number)