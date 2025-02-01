
import math
# 1. Write a program to print "Hello, World!" and experiment with string formatting.
def hello_world():
    '''
    function to print "Hello, World!"
    '''
    print("Hello, World!")
    

# 2. Calculate the area of a circle given its radius as input.
def area_of_circle(radius):
    '''
    function to calculate the area of a circle
    :param radius: radius of the circle
    :return: area of the circle
    '''
    return math.pi* radius ** 2

# 3. Write a Python program to swap two variables without using a third variable.
def swap(a, b):
    '''
    function to swap two variables without using a third variable
    :param a: first variable
    :param b: second variable
    :return: swapped variables
    '''
    a = a + b
    b = a - b
    a = a - b
    return a, b
# 4. Write a program to check whether a given number is positive, negative, or zero.
def check_number(num):
    '''
    function to check whether a given number is positive, negative, or zero
    :param num: number
    :return: string
    '''
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


# 5. Create a function to calculate the factorial of a given number.
def factorial(num):
    '''
    function to calculate the factorial of a given number
    :param num: number
    :return: factorial
    '''
    #there is a built-in function math.factorial(num) that can be used, but i will implement it myself
    for i in range(1, num):
        num *= i
    return num

# 6. Write a program to display the Fibonacci sequence up to a certain number.
def fibonacci(n):
    ''' 
    function to display the Fibonacci sequence up to a certain number
    :param n: number
    :return: sequence
    '''
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# 7. Develop a program to check whether a number is prime.
def is_prime(num):
    '''
    function to check whether a number is prime
    :param num: number
    :return: boolean
    '''
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 8. Create a Python function to reverse a given string.
def reverse_string(s):
    '''
    function to reverse a given string
    :param s: string
    :return: reversed string
    '''
    return s[::-1]


# 9.  Write a function to count the occurrences of a specific character in a string.
def count_occurrences(s, char):
    '''
    function to count the occurrences of a specific character in a string
    :param s: string
    :param char: character
    :return: number of occurrences
    '''
    #another solution is to use loop with a counter, but i will use count method
    return s.count(char)


# 10. Write a Python program to find the greatest of three numbers.
def greatest_number(a, b, c):
    '''
    function to find the greatest of three numbers
    :param a: first number
    :param b: second number
    :param c: third number
    :return: greatest number
    '''
    return max(a, b, c)

# 11. Build a program to calculate the sum of digits of a given number.
def sum_of_digits(num):
    '''
    function to calculate the sum of digits of a given number
    :param num: number
    :return: sum of digits
    '''
    #another solution is to use loop to iterate over the digits, but i will use list comprehension
    return sum(int(i) for i in str(num))


# 12. Create a program to convert temperature from Celsius to Fahrenheit and vice versa.
def convert_temperature(temp, unit):
    '''
    function to convert temperature from Celsius to Fahrenheit and vice versa
    :param temp: temperature
    :param unit: unit (Celsius or Fahrenheit)
    :return: converted temperature
    '''
    if unit == "Celsius":
        return (temp * 9/5) + 32
    elif unit == "Fahrenheit":
        return (temp - 32) * 5/9
    else:
        return "Invalid unit"
    
    
# 13. Write a Python function to check if a string is a palindrome.
def is_palindrome(s):
    '''
    function to check if a string is a palindrome
    :param s: string
    :return: boolean
    '''
    return s == s[::-1]



# 14. Implement a program to find the sum of the first N natural numbers.
def sum_of_natural_numbers(n):
    '''
    function to find the sum of the first N natural numbers
    :param n: number
    :return: sum of the first N natural numbers
    '''
    return n * (n + 1) // 2


# 15. Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.
def gcd(a, b):
    '''
    function to find the GCD (Greatest Common Divisor) of two numbers
    :param a: first number
    :param b: second number
    :return: GCD
    '''
    while b:
        a, b = b, a % b
    return a





# hello_world()
