items = [
    {"radio": (3000, 4)},
    {"laptop": (2000, 3)},
    {"guitar": (1500, 1)},
    {"iphone": (2000, 1)},
    {"mp3": (1000, 1)}
]

def knapsack(items, capacity):
    n = len(items)
    grid = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name = list(items[i - 1].keys())[0]
        item_value = list(items[i - 1].values())[0][0]
        item_weight = list(items[i - 1].values())[0][1]
        
        for j in range(capacity + 1):
            if item_weight <= j:
                grid[i][j] = max(grid[i - 1][j], item_value + grid[i - 1][j - item_weight])
            else:
                grid[i][j] = grid[i - 1][j]

    result = []
    w = capacity
    for i in range(n, 0, -1):
        if grid[i][w] != grid[i - 1][w]:
            result.append(list(items[i - 1].keys())[0])
            w -= list(items[i - 1].values())[0][1]

    return result

capacity = 4
result = knapsack(items, capacity)
print(result)
