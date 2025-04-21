# Log all pairs of array

boxes = [1,2,3,4,5]

def log_all_pairs(arr):
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