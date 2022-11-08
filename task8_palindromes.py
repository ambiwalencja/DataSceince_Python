# Napisz funkcję, która sprawdzi, czy 2 napisy są palindromami.

def is_palindrome(my_string):
    n = len(my_string) // 2
    for index, char in enumerate(my_string[:n]):
        if char != my_string[-index-1]:
            return False
    return True

words = ['lkjhjkl', 'ergerggr']
for word in words:
    if is_palindrome(word):
        print(f'{word} is a palindrome.')
    else:
        print(f'{word} is not a palindrome.')
