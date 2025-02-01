import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from list import *

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 4]
    
def test_find_largest_smallest():
    assert find_largest_smallest([1, 2, 3, 4, 5]) == (5, 1)
    
def test_rotate_list():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    
def test_find_unique_elements():
    assert find_unique_elements([1, 2, 3, 4], [2, 3, 5, 6]) == [1, 4, 5, 6]
    
def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]