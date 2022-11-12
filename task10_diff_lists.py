# Napisz funkcję, która przyjmie dwie listy liczb całkowitych, i zwróci listę liczb występujących w pierwszej
# i nie występujących w drugiej liście, posortowana rosnąco względem ilości wystąpień w pierwszej liście.

def compare_lists(list1, list2):
    diff_list = []
    for digit in list1:
        if digit not in list2:  # czy tak można???
            diff_list.append(digit)
    diff_list = sorted(diff_list, key = diff_list.count)
    return diff_list

list_1 = [1,1,2,2,2,3,4,5,9,9,9,9]
list_2 = [3,4,5,6,7]
print(compare_lists(list_1, list_2))
