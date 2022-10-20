
def check_if_divisible(num_1, num_2):
    if num_1 % num_2 == 0:
        divisible = 'divisible'
    else:
        divisible = 'not divisible'
    return divisible

# execution


print('Give two numbers to check if the first one is divisible by the second one.')
number_1 = int(input('Write the first number:'))
number_2 = int(input('Now write the second one:'))
print(check_if_divisible(number_1, number_2))