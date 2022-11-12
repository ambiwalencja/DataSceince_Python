# Napisz funkcję, która zwróci które urodziny będą obchodziły w tym roku osoby urodzone w latach
# podanych w liście będącej argumentem wejściowym danej funkcji.

from datetime import date


def how_old(list):
    current_year = date.today().year
    age_list = []
    for year in list:
        age_list.append(current_year - year)
    return age_list


years = [1991, 1845, 2000, 2005, 1965, 1998, 1935]
# print(how_old(years)) # <-- wynik albo w postasci listy
for year, age in zip(years, how_old(years)): # <-- albo jakiegoś fancy komunikatu
    print(f'Person born in {year} is {age} years old.')
