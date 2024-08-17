lista = [1, 2, 3, 4, 4, 5, 6, 7]
recList = [1, 2, [3,4], [5,6]]

# 1. Write a Python program to calculate the sum of a list of numbers using recursion. 
def sumList(lista, index=0):
    if index > len(lista) - 1:  # Caso base
        return 0
    else:
        return lista[index] + sumList(lista, index + 1)

# 2. Write a Python program to convert an integer to a string in any base using recursion.
def convert(integer, base, string = ""):
    alpha = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    if integer < base:
        return (string + str(integer))[::-1]
    else: 
        return convert(integer // base, base, string + str(alpha[int(integer % base)]))

# 3. Write a Python program to sum recursion lists using recursion. 
def sumListRec(lista, index=0):
    # Verifica se uma lista acabou (caso base)
    if index > len(lista) - 1:
        return 0
    # Se não acabou, e o proximo objeto é uma lista, entre dentro dela.
    elif type(lista[index]) == list:
        return sumListRec(lista[index], index=0) + sumListRec(lista, index + 1)
    # Recursivamente adicione
    else:
        return lista[index] + sumListRec(lista, index + 1)


# 4. Write a Python program to get the factorial of a non-negative integer using recursion. 
def fac(x):
    if x == 1:
        return 1
    else:
        return x * fac(x -1)
    
# 5. Write a Python program to solve the Fibonacci sequence using recursion. 
def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

# 6. Write a Python program to get the sum of a non-negative integer using recursion. 
def sumDigits(x):
    if x // 10 == 0:
        return 0
    else:
        return x % 10 + sumDigits(x // 10)

print(sumList(lista))
print(convert(40, 16))
print(sumListRec(recList)) # 21
print(fac(3)) # 21
print(fibonacci(8))
print(sumDigits(4220))