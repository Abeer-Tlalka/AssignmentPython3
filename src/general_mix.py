# 1. Write a Python program to sort a list of tuples by the second element.
def sort_by_second_element(lst):
    '''
    function to sort a list of tuples by the second element
    :param lst: list of tuples
    :return: sorted list of tuples
    '''
    return sorted(lst, key=lambda x: x[1])
# 2. Develop a program to find the second largest element in a list.
def find_second_largest(lst):
    '''
    function to find the second largest element in a list
    :param lst: list
    :return: second largest element
    '''
    #after we sorted the list, the second largest element is the second element from the end
    return sorted(lst)[-2]


# 3. Create a function to count the frequency of elements in a list.
def count_frequency(lst):
    '''
    function to count the frequency of elements in a list
    :param lst: list
    :return: dictionary with elements as keys and their frequency as values
    '''
   
    freq_dict = {}  # Create an empty dictionary to store frequencies
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1  # Increment count if item already exists
        else:
            freq_dict[item] = 1  # Initialize count if item is new
    return freq_dict


# 4. Write a Python program to generate all subsets of a given set.
def generate_subsets(input_set):
    '''
    Function to generate all subsets of a given set
    :param input_set: A set (or list) from which subsets are generated
    :return: A list of all subsets
    '''
    result = [[]]  # Start with the empty subset
    for element in input_set:
        # Create new subsets by adding the element to each existing subset
        new_subsets = []
        for subset in result:
            new_subsets.append(subset + [element])  # Add the current element to each subset
        result.extend(new_subsets)  # Add new subsets to the result
    
    return result

# 5. Implement a program to find the most common element in a list.
def find_most_common(lst):
    '''
    function to find the most common element in a list
    :param lst: list
    :return: most common element
    '''
    return max(set(lst), key=lst.count)