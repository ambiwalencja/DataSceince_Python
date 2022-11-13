# Napisz (przy pomocy rekurencji) funkcję realizującą potęgowanie.
# Funkcja przyjmuje dwie liczby całkowite, będące podstawą i wykładnikiem potęgi.

# def power(n, m):
#     result = 1
#     for i in range(m):
#         result = result * n
#     return result

# sama wpadłam tylko na rozwiązanie bez-rekurekcyjne, poniższe rozwiązanie zgapione z sieci
def power2(n, m):
    if m == 0:
        return 1
    return n*power2(n,m-1)

print(power2(2,8))

