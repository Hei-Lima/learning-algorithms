graph = {}

graph["toco"] = ["alice", "claire", "bob"]
graph["alice"] = ["peggy"]
graph["bob"] = ["peggy", "anuj"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["thom"] = []
graph["peggy"] = []
graph["jonny"] = [True]

def generateList(graph, name, arr):
    for i in graph[name]:
        arr.append(i)
    return arr

def check(graph, start):
    arr = generateList(graph, start, [])
    for person in arr:
        if True not in graph[person]:
            arr = generateList(graph, person, arr)
            print(f"{person} não é um vendedor de mangas!")
        else:
            print(f"{person} é o vendedor de mangas.")
            return person
        
print(check(graph, "toco"))