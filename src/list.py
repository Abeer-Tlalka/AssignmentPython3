# 1. Write a Python program to remove duplicates from a list.
def remove_duplicates(lst):
    '''
    function to remove duplicates from a list
    :param lst: list
    :return: list without duplicates
    '''
    #we can use set to remove duplicates,but i will use a loop
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

# 2. Develop a program to find the largest and smallest numbers in a list.
def find_largest_smallest(numbers):
    '''
    function to find the largest and smallest numbers in a list
    :param numbers: list of numbers
    :return: largest and smallest numbers
    '''
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest

# 3. Write a function to rotate a list by a given number of positions.
def rotate_list(lst, n):
    '''
    function to rotate a list by a given number of positions
    :param lst: list
    :param n: number of positions
    :return: rotated list
    '''
    return lst[n:] + lst[:n]
# 4. Create a program to find all unique elements in two lists.
def find_unique_elements(lst1, lst2):
    '''
    function to find all unique elements in two lists
    :param lst1: first list
    :param lst2: second list
    :return: unique elements
    '''
    result = []
    for i in lst1:
        if i not in lst2:
            result.append(i)
     # Check elements in lst2 that are not in lst1
    for i in lst2:
        if i not in lst1 and i not in result:  # Check if it's not already in result
            result.append(i)
    return result 

# 5. Write a Python program to flatten a nested list.
def flatten_list(lst):
    '''
    function to flatten a nested list
    :param lst: nested list
    :return: flattened list
    '''
    result = []
    for i in lst:
        #check if i is a list
        if isinstance(i, list):
            #flatten the list
            result.extend(flatten_list(i))
        else:
            #add the element to the result
            result.append(i)
    return result