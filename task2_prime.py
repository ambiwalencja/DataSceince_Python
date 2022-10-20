# Napisz funkcję, która wypisze wszystkie liczby pierwsze mniejsze od liczby będącej argumentem funkcji.

def print_primes(number):
    prime_numbers_list = []
    if number == 1:
        return prime_numbers_list
    else:
        prime_numbers_list.append(1)
        if number == 2:
            return prime_numbers_list
        else:
            temporary_list = []  # lista przetrzymująca wszystkie liczby mniejsze od aktualnie obrabiajem
            for i in range(2, number):  # bierzemy po kolei każdą liczbę mniejszą od number
                temporary_list.append(i)  # do listy pomocniczej dodajemy bieżącą liczbę, zaczynając od 2
                for j in temporary_list:
                    if (j != i) and (i % j == 0):  # jeśli i podzielne przez j to następne i
                        break
                    elif j == i:   # jak doszliśmy do i = j to dodajemy i do listy
                        prime_numbers_list.append(i)
                        continue
                    else:   # dopóki nie jest równe i nie jest podzielne to następne j
                        continue
        return prime_numbers_list


# execution
my_number = int(input('Give an integer number to display a liet of all prime numbers smaller than it:'))
print(print_primes(my_number))
