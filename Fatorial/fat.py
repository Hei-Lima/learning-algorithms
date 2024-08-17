def multiply(x):
    if x == 1: # caso base
        return 1
    else: # caso recursivo
        return x * multiply(x-1)
    

print(multiply(4))