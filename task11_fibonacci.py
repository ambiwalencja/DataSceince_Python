# Utworz funkcję, która przyjmie argument int n i obliczy n-ta liczbę ciagu Fibonacciego.

def fibonacci_element(n):
    fnpp = 0 # wyraz pierwszy, później wykorzystywany jako wyraz n-2
    fnp = 1 # wyraz drugi, później wykorzystywany jako wyraz n-1
    if n == 1:
        return fnpp
    if n == 2:
        return fnp
    fn = 0 # bieżący element
    for fn in range(3,n+1):
        fn = fnpp + fnp
        fnpp = fnp
        fnp = fn
    return fn

n = 10
print(f'{n} wyraz ciągu fibonacciego to {fibonacci_element(n)}')