telefone = dict()

option = "trash"

def insert():
    print("_____________________________________________")
    print("Insira nome: ", end="")
    nome = input()
    print("Insira numero: ", end="")
    numero = input()
    return (nome, numero)

def name():
    print("_____________________________________________")
    print("Insira nome: ", end="")
    nome = input()
    return nome

while option != "":
    print("_____________________________________________")
    print("Opcoes: Insirir Numero (I)  Procurar Nome (N)")
    option = input()
    if option == "I":
        buffer = insert()
        telefone[buffer[0]] = buffer[1]
    elif option == "N":
        buffer = name()
        if buffer not in telefone:
            print("Nao encontrado")
            continue
        print(telefone[buffer])
    else:
        option = ""
    
