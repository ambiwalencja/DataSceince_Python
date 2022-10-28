# Napisz funkcję, która dla dwóch list liczbowych zwróci listę zawierającą tylko te elementy,
# które należą do obydwu list wejściowych.

def list_intersection(list1, list2):
    intersection = []
    for i in list1:
        for j in list2:
            if i == j:
                intersection.append(i)
    return intersection


numeric_list_1 = [1, 2, 3, 4, 5]
numeric_list_2 = [2, 6, 34, 8, 9, 1]
# numeric_list_1 = eval(f'[{input("First numeric list:")}]')
# numeric_list_2 = eval(f'[{input("Second numeric list:")}]')
print(f'The intersection of lists is: {list_intersection(numeric_list_1, numeric_list_2)}')
