import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from basic_mix import *
def test_hello_world():
    assert hello_world() == None
    
    
def test_area_of_circle():
    assert area_of_circle(5) == 78.53981633974483
    
def test_swap():
    assert swap(5, 10) == (10, 5)
    
def test_check_number():
    assert check_number(5) == "Positive"
    assert check_number(-5) == "Negative"
    assert check_number(0) == "Zero"

def test_factorial():
    assert factorial(5) == 120
    
def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    
def test_is_prime():
    assert is_prime(5) == True
    
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    
    
def test_count_occurrences():
    assert count_occurrences("hello", "l") == 2
    
def test_greatest_number():
    assert greatest_number(5, 10, 15) == 15
    assert greatest_number(10, 5, 15) == 15
    assert greatest_number(10, 15, 5) == 15

def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    
def test_convert_temperature():
    assert convert_temperature(100, "Celsius") == 212.0
    assert convert_temperature(212, "Fahrenheit") == 100.0
    
def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False

def test_sum_of_natural_numbers():
    assert sum_of_natural_numbers(5) == 15
    assert sum_of_natural_numbers(10) == 55
    
def test_gcd():
    assert gcd(12, 18) == 6