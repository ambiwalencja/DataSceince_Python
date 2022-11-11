# Napisz funkcję, która przyjmie dwie listy liczb całkowitych, i zwróci listę liczb występujących w pierwszej
# i nie występujących w drugiej liście, posortowana rosnąco względem ilości wystąpień w pierwszej liście.

def compare_lists(list1, list2):
    diff_list = []
    for digit in list1:
        if digit not in list2:  # czy tak można???
            diff_list.append(digit)
    diff_list = sorted(diff_list, key = diff_list.count)
    return diff_list


print(compare_lists([1,1,2,2,2,3,4,5,9,9,9,9], [3,4,5,6,7]))
