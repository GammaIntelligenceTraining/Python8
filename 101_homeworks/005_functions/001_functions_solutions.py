"""
Под каждым комментарием нужно написать одну функцию
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# Write a function that takes a list of numbers
# And returns same list but numbers multiplied by 2
# input: list of numbers
# output: list of numbers multiplied by 2
def multiplied_by_two(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result

print(multiplied_by_two([1, 2, 3, 4, 5]))


# Write a function that takes a list of numbers
# And returns same list but numbers multiplied by 4
# USE PREVIOUS FUNCTION TO CREATE THIS ONE
# input: list of numbers
# output: list of numbers multiplied by 4
def multiplied_by_four(numbers):
    return multiplied_by_two(multiplied_by_two(numbers))

print(multiplied_by_four([1, 2, 3, 4, 5]))


# Write a function that will check if users input is palindrome
# "Able was I ere I saw Elba" is a palindrome!!!
# input: nothing
# output: boolean
def check_for_palindrome():
    user_input = input('Please enter a word or phrase to check: ')
    user_input =  user_input.replace(' ', '').replace(',', '').replace('.', '').lower()
    if user_input == user_input[::-1]:
        print('Is palindrome!')
        return True
    else:
        print('Not a palindrome')
        return False

print(check_for_palindrome())


# Write a function that prints a list of squared numbers from 1 to 30
# input: nothing
# output: nothing
def list_of_squares():
    result = []
    for num in range(1, 31):
        result.append(num ** 2)
    print(result)

list_of_squares()


# Write a function that multiplies all numbers in a list provided by user
# input: nothing
# output: float of multiplied numbers
def multiply_all_user_numbers():
    user_input = input('Please enter numbers separated by space: ').split()
    result = 1
    for num in user_input:
        result *= float(num)
    return result

print(multiply_all_user_numbers())