import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from general_mix import *

def test_sort_by_second_element():
    lst = [(1, 2), (3, 4), (5, 6)]
    sorted_lst = sort_by_second_element(lst)
    assert sorted_lst == [(1, 2), (3, 4), (5, 6)]
    
def test_find_second_largest():
    lst = [1, 2, 3, 4, 5]
    second_largest = find_second_largest(lst)
    assert second_largest == 4
    
def test_count_frequency():
    lst = [1, 2, 3, 4, 5]
    freq_dict = count_frequency(lst)
    assert freq_dict == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    

def test_generate_subsets():
    lst = [1, 2, 3]
    subsets = generate_subsets(lst)
    assert subsets == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    
def test_find_most_common():
    lst = [1, 2, 3, 4, 5]
    most_common = find_most_common(lst)
    assert most_common == 1