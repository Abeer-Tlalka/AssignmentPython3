# 1. Write a program to merge two dictionaries.
def merge_dict(dict1, dict2):
    '''
    function to merge two dictionaries
    :param dict1: dictionary 1  
    :param dict2: dictionary 2
    :return: merged dictionary
    '''
    #{**dict1, **dict2}
    merged = {}  

    # Add all key-value pairs from dict1
    for key in dict1:
        merged[key] = dict1[key]

    # Add all key-value pairs from dict2
    for key in dict2:
        merged[key] = dict2[key]

    return merged
    
# 2. Create a program to sort a dictionary by keys or values.
def sort_dict(dict1):
    '''
    function to sort a dictionary
    :param dict1: dictionary
    :return: sorted dictionary
    '''
    return dict(sorted(dict1.items()))

# 3. Write a Python function to check if a key exists in a dictionary.
def check_key(dict1, key):
    '''
    function to check if a key exists in a dictionary
    :param dict1: dictionary
    :param key: key
    :return: True if key exists, False otherwise
    '''
    return key in dict1

# 4. Implement a program to invert the keys and values of a dictionary.
def invert_dict(dict1):
    '''
    function to invert the keys and values of a dictionary
    :param dict1: dictionary
    :return: inverted dictionary
    '''
    return {value: key for key, value in dict1.items()}



# dict1= {'a': 1, 'b': 2, 'c': 3}
# dict2= {'d': 4, 'e': 5, 'f': 6}
# print(merge_dict(dict1, dict2))