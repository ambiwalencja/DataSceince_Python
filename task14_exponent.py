# Napisz (przy pomocy rekurencji) funkcję realizującą potęgowanie.
# Funkcja przyjmuje dwie liczby całkowite, będące podstawą i wykładnikiem potęgi.

def exponentiation(n, m):
    result = 1
    for i in range(m):
        result = result * n
    return result

print(exponentiation(2,8))