"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    power_list = [nums ** 2 for nums in args]
    return power_list


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(nums_list):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает лист простых чисел.
    """
    prime_list = []
    for nums in nums_list:
        if nums > 1:
            count = 0
            divisor = 2
            while divisor < nums:
                if nums % divisor == 0:
                    count += 1
                divisor += 1
            if count == 0:
                prime_list.append(nums)
    return prime_list


def filter_numbers(nums_list, list_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if list_type == EVEN:
        event_list = [nums for nums in nums_list if nums % 2 == 0]
        return event_list

    elif list_type == ODD:
        odd_list = [nums for nums in nums_list if nums % 2 != 0]
        return odd_list

    elif list_type == PRIME:
        return is_prime(nums_list)


# Example
print(filter_numbers([1, 2, 3, 4, 10, 24 , 17], PRIME))
# print(power_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
