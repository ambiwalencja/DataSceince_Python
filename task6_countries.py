# Wybierz kilka państw i stwórz dla każdego słownik, który będzie zawierać dane o nazwie państwa, powierzchni,
# liczbie mieszkańców, PKB per capita (PPP). Napisz funkcję, która dla listy słowników będzie wypisywać listę
# państw uszeregowanych według: * powierzchni * liczby ludności * gęstości zaludnienia * PKB per capita (PPP)

# https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary

def sort_by(list, key):
    sorted_list = sorted(list, key=lambda x: x[key])
    return sorted_list


list_of_countries = [
    {'name': "A", 'area': 295875478, 'citizens': 482827, 'PPP': 19384},
    {'name': "B", 'area': 765786, 'citizens': 2389476, 'PPP': 34857},
    {'name': "C", 'area': 34857893475, 'citizens': 8348578347, 'PPP': 9163},
    {'name': "D", 'area': 4309478, 'citizens': 634897528, 'PPP': 79847},
    {'name': "E", 'area': 296728746, 'citizens': 1885897, 'PPP': 9542368}
]

for country in sort_by(list_of_countries, 'citizens'):
    print(country)
