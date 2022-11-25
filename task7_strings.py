# Napisz funkcję przyjmujacą napis i zwracającą informacje ile liter i cyfr jest w napisie.

def count_letters_and_numbers(my_string):
    digits, letters = 0, 0
    for char in my_string:
        if char.isdigit():
            digits += 1
        if char.isalpha():
            letters += 1
    return digits, letters

# podpowiedź - użyć list comprehension
# https://stackoverflow.com/questions/35758968/count-in-python-list-comprehension

def count_letters_and_numbers_2(my_string):
    digits = len([1 for char in my_string if char.isdigit()])
    letters = len([1 for char in my_string if char.isalpha()])
    return digits, letters

result = count_letters_and_numbers_2('kjhjk4563j*&*^')
print(f'Number of digits: {result[0]}, number of letters: {result[1]}')
