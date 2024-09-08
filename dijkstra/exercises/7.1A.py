graph_a = {}
graph_a["start"] = {}
graph_a["start"]["A"] = 2
graph_a["start"]["B"] = 5

graph_a["A"] = {}
graph_a["A"]["C"] = 8
graph_a["A"]["D"] = 7

graph_a["B"] = {}
graph_a["B"]["D"] = 4

graph_a["C"] = {}
graph_a["C"]["end"] = 6

graph_a["D"] = {}
graph_a["D"]["C"] = 1
graph_a["D"]["end"] = 2

graph_a["end"] = {}

# - CUSTOS -
costs = {}
costs["start"] = 0
costs["A"] = float("inf")
costs["B"] = float("inf")
costs["C"] = float("inf")
costs["D"] = float("inf")
costs["end"] = float("inf")

# - PAIS -
parents = {}
parents["A"] = None
parents["B"] = None
parents["C"] = None
parents["D"] = None
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

print(dijkstra(graph_a, costs, parents))