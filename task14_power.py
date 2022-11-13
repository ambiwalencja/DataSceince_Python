# Napisz (przy pomocy rekurencji) funkcję realizującą potęgowanie.
# Funkcja przyjmuje dwie liczby całkowite, będące podstawą i wykładnikiem potęgi.

def power(n, m):
    if m == 0:
        return 1
    return n*power(n,m-1)

print(power(2,8))

