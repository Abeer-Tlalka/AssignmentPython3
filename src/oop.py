# 1. Create a class representing a Circle with attributes for radius and methods to calculate area and circumference.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius


# 2. Write a class to model a bank account with deposit and withdrawal functionalities.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance


# 3. Implement a class representing a Book with attributes like title, author, and year, and a method to display details.
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# 4. Develop a program using classes to calculate the area and perimeter of a rectangle.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)




# 5. Write a Python program to demonstrate inheritance using shapes (e.g., Rectangle and Square).




# 6. Create a class to model a student with attributes for name and marks, and methods to calculate grade.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"
        
    

# 7. Implement a program to demonstrate polymorphism with a parent class Animal and subclasses Dog and Cat.
# 8. Write a class to implement a simple library management system.
# 9. Create a class to model a complex number with methods for addition, subtraction, and multiplication.
# 10. Write a Python program to demonstrate method overloading and method overriding.
# 11. Develop a program using a class to validate and format email addresses.
# 12. Create a Person class with a class method to count the number of instances created.
# 13. Implement a class for a stack data structure using object-oriented principles.
# 14. Write a program to demonstrate multiple inheritance.
# 15. Create a Python class to represent a Fraction with methods for arithmetic operations.
# 16. Write a class to model a simple Queue data structure.
# 17. Develop a class that uses private attributes and getter/setter methods.
# 18. Implement a Python class to model a Point in 2D space and calculate the distance between two points.
# 19. Write a program demonstrating the use of static methods in Python.
# 20. Create a class to implement a priority queue.