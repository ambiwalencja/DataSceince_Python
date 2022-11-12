# Używając zagnieżdżonych pętli, stwórz funkcję, która wydrukuje następujący wzór:
# *
# * $
# * $ *
# * $ * $
# * $ * $ *
# * $ * $
# * $ *
# * $
# *

def print_pattern(n):
    for i in range(1,n,1):
        for j in range(i):
            if j % 2 == 0:
                print('*', end=' ')
            if j % 2 == 1:
                print('$', end=' ')
        print('',end='\n')
    for i in range(n,0,-1):
        for j in range(i):
            if j % 2 == 0:
                print('*', end=' ')
            if j % 2 == 1:
                print('$', end=' ')
        print('',end='\n')

print_pattern(5)