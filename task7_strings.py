# Napisz funkcję przyjmujacą napis i zwracającą informacje ile liter i cyfr jest w napisie.

def count_letters_and_numbers(my_string):
    digits, letters = 0, 0
    for char in my_string:
        if char.isdigit():
            digits += 1
        if char.isalpha():
            letters += 1
    return digits, letters

result = count_letters_and_numbers('kjhjk4563j*&*^')
print(f'Number of digits: {result[0]}, number of letters: {result[1]}')