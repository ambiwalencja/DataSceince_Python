# Napisz funkcję, która posortuje listę liczb w porządku niemalejącym.

def sort_list_from_input(string):
    try:
        my_list = eval(f'[{string}]')
        print(sorted(my_list))
    except Exception as e:
        print(f"Error: >> {e} << - please make sure you give numeric values separated by comma and try again")
    return True


my_string = input("Give a list of numbers, separated by comma:")
sort_list_from_input(my_string)