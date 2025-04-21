# Log all pairs of array

boxes = [1,2,3,4,5]

def log_all_pairs(arr: List[int]) -> None:
    """
    This function takes an array and logs all pairs of elements in the array.
    :param arr: list of numbers
    :return: None
    """
    for i in range(len(arr)): # O(n)
        for j in range(len(arr)): # O(n)
            print(arr[i], arr[j]) # O(1)
            
log_all_pairs(boxes)
# The time complexity of this function is O(n^2) because there are two nested loops.

def boooo(n: List[int]) -> None:
    """
    This function takes an integer n and prints 'boooo' n times.
    :param n: integer
    :return: None
    """
    for i in range(len(n)):  # Time Complexity - O(n)
        print("booooo!")
        
boooo([1,2,3,4,5])

def array_of_hi_n_times(n: int) -> list[str]:
    """
    This function takes an integer n and returns an array of 'hi' n times.
    :param n: integer
    :return: list of 'hi'
    """
    hi = []
    for i in range(n):
        hi.append("hi") 
    return hi

array_of_hi_n_times(5)
# The space complexity of this function is O(n) because we are creating an array of size n.

def sum_of_n_numbers(n: int) -> int:
    """
    This function takes an integer n and returns the sum of numbers from 1 to n.
    :param n: integer
    :return: sum of numbers
    """
    total = 0
    for i in range(n):
        total += i
    return total

print(sum_of_n_numbers(100000))