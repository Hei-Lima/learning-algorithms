from collections import deque

graph = {}

graph["toco"] = ["alice", "claire", "bob"]
graph["alice"] = ["peggy"]
graph["bob"] = ["peggy", "anuj"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["thom"] = []
graph["peggy"] = []
graph["jonny"] = [True]



def search(graph, start):
    fila = deque()
    fila += graph[start]

    while fila:
        pessoa = fila.popleft
        if pessoa is True:
            print(pessoa, "é um vendedor de manga")
        else:
            fila += graph[pessoa]
    print("Tem ninguém não")
    return None

search(graph, "toco")