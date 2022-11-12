# Napisz funkcję, która przyjmie słownik mapujący imiona na wzrost,
# a następnie zwróci listę zawierającą imiona posortowane według wzrostu malejąco.

def sort_by_value(dictionary):
    temp_list = [(key, value) for key, value in dictionary.items()]
    return [element[0] for element in sorted(temp_list, key = lambda x: x[1], reverse=True)]

persons = {'anna': 165, 'barbara': 170, 'cecylia': 159, 'damian': 182, 'elżbieta': 177}
print(sort_by_value(persons))
