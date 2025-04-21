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