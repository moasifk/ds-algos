"""
This is a simple program to demonstrate the order of n.
The program will take a list of numbers and print the sum of the numbers in the list.
The program will also print the time taken to execute the program.
"""

def sum_of_numbers(numbers):
    """
    This function takes a list of numbers and returns the sum of the numbers.
    :param numbers: list of numbers
    :return: sum of numbers
    """
    total = 0
    for number in numbers: # O(n)
        total += number # O(n)
    return total

def order_of_1():
    """
    This function demonstrates the order of 1.
    It takes a list of numbers and returns the first number in the list.
    :return: first number in the list
    """
    numbers = [1, 2, 3, 4, 5]
    return numbers[0] # O(1)

def order_of_n():   
    """
    This function demonstrates the order of n.
    It takes a list of numbers and returns the sum of the numbers in the list.
    :return: sum of numbers
    """
    numbers = [1, 2, 3, 4, 5]
    return sum_of_numbers(numbers) # O(n)

def order_of_log_n(numbers: str, number_to_find: int) -> int:
    """
    This function demonstrates the order of log n. O(log n)
    It takes a list of numbers and returns the position of a particular number.
    :return: position of specific number
    """
    numbers = [1, 2, 3, 4, 5]
    number_to_find = 3  
    left = 0
    right = len(numbers) - 1
    while left <= right: # O(log n)
        mid = (left + right) // 2
        if numbers[mid] == number_to_find:
            return mid
        elif numbers[mid] < number_to_find:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # number not found

print(order_of_log_n([1,4,5,6,7], 4))
