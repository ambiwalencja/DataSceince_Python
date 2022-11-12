# Napisz funkcję, która przyjmie argumenty nazwane imie i wzrost a następnie utworzy wpis do globalnego słownika.
# Dodaj co najmniej 5 wpisów.

persons = {}

def add_record_to_dict(name, height):
    persons[name] = height

def fill_data(names_list, heights_list):
    for i, name in enumerate(names_list):
        add_record_to_dict(name, heights_list[i])

names = ['anna', 'barbara', 'cecylia', 'damian', 'elżbieta']
heights = [165, 170, 159, 182, 177]

fill_data(names, heights)
print(persons)