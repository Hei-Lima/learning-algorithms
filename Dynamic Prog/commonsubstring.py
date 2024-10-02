# Compararei duas palavras, como no livro

def find_substring(word_a, word_b):
    grid = grid = [[0] * len(word_b) for _ in range(len(word_a))]
    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                grid[i][j] = grid[i-1][j-1] + 1
            else:
                grid[i][j] = 0
    return grid
    
print(find_substring("pista", "pista"))

