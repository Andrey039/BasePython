"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    power_list = []
    power = 2
    for number in args:
        power_list.append(number ** power)
    return power_list


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(nums_list, list_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if list_type == 'even':
        event_list = []
        for nums in nums_list:
            if int(nums) % 2 == 0:
                event_list.append(nums)
        return event_list

    if list_type == 'odd':
        odd_list = []
        for nums in nums_list:
            if int(nums) % 2 != 0:
                odd_list.append(nums)
        return odd_list

    if list_type == 'prime':
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

# Example
#print(filter_numbers([1, 2, 3, 4, 10, 24], PRIME))
