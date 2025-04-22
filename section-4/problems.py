# A program for finding a matching element from the first list in second list
# list1 = ['a', 'b', 'c', 'd']
# list2 = ['d', 'e', 'f', 'g']
# result True

def matching_elements(list1: list[str], list2: list[str]) -> bool:
    """
    This function takes two lists and returns True if there is a matching element in both lists.
    :param list1: first list
    :param list2: second list
    :return: True if there is a matching element in both lists, False otherwise
    """
    for i in range(len(list1)): # O(n)
        for j in range(len(list2)):
            if(list1[i] == list2[j]):
                return True
    return False
# Time Complexity - O(n^2)

def matching_elements_2(list1: list[str], list2: list[str]) -> bool:
    items_map = {}
    for i in range(len(list1)):
        items_map[list1[i]] = True
    
    for i in range(len(list2)):
        if items_map.get(list2[i]):
            return True
    return False

# Time Complexity - O(n)
print(matching_elements_2( ['a', 'b', 'c', 'd'], ['d', 'e', 'f', 'g']))