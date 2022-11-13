# Napisz funkcję przyjmującą jeden parametr list zawierający liczby całkowite i zwracającą element,
# który pojawia się na liście najczęściej.

def find_most_frequent(_list):
    try:
        for element in _list:
            int(element)
    except ValueError:
        print("Make sure your list contains only integers and try again.")
    else:
        return sorted(_list, key = _list.count, reverse = True)[0]

my_list = [4, 20, 43, 1, 5, 9, 20, 567, 22, 16, 3, 5, 20]
print(find_most_frequent(my_list))