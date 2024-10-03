import math

users = {
    "toco": (4, 2, 3, 4),
    "biles": (3, 2, 3, 4),
    "montana": (2, 2, 1, 2),
    "neuve": (2, 2, 3, 3),
    "binet": (5, 1, 5, 2),
    "liitle": (4, 2, 3, 4),
    "vito": (1, 1, 3, 4),
}

def rank_closest_neighbors(users, root):
    rank = {}
    root_values = users[root]
    for user, values in users.items():
        if user is not root:
            formula = 0
            for i in range(len(values)):
                formula += (values[i] - root_values[i]) ** 2
                rank.update({user: formula})
    return rank


def format(rank, size):
    sorted_list = sorted(rank.items(), key=lambda x: x[1])
    print(f"Closest {size} neighbors: {sorted_list[:size]}")

        

rank = rank_closest_neighbors(users, "toco")
print(rank)
format(rank, 3)