graph = {}

graph["start"] = {}
graph["start"]["A"] = 6
graph["start"]["B"] = 2

graph["A"] = {}
graph["A"]["end"] = 1 

graph["B"] = {}
graph["B"]["end"] = 5
graph["B"]["A"] = 3

graph["end"] = {}

# - CUSTOS -
costs = {}

costs["start"] = 0

costs["A"] = 6

costs["B"] = 2

costs["end"] = float("inf")

# - PAIS -
parents = {}

parents["A"] = "start"

parents["B"] = "start"
 
parents["end"] = None

def dijkstra(graph, costs, parents):
    processed = []
    node = find_cheaper_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_cheaper_node(costs, processed)

    return find_shortest_path(costs, parents)


def find_cheaper_node(costs, processed):
    cheaper_node = None
    cheaper_cost = float("inf")

    for node in costs:
        if costs[node] < cheaper_cost and node not in processed:
            cheaper_cost = costs[node]
            cheaper_node = node
    return cheaper_node


def find_shortest_path(costs, parents):
    node = "end"
    path = []
    while node != "start":
        path.append(node)
        node = parents[node]
    return (path[::-1], costs["end"])

print(dijkstra(graph, costs, parents))