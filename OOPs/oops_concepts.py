# Generated from: oops_concepts.ipynb
# Converted at: 2026-06-13T10:43:02.171Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# Classes & Objects

class Student:
    subject = "Python"
    college = "ABC"
    year = "4th year"

stu1 = Student()
stu2 = Student()

print(stu1.subject, stu1.college, stu1.year)
print(stu2.subject, stu2.college, stu2.year)

# Default Constructor
class Student:
    def __init__(self):
        print("constructor was called")

stu1 = Student()

# Parameterized Constructor
class Student:
    def __init__(self, name):
        self.name = name

stu1 = Student("Rahul")
stu2 = Student("Harshita")

print(stu1.name, stu2.name)

# Attributes
class Student:
    college = "ABC college"        # class attribute
    def __init__(self, name, gpa): # instance attributes
        self.name = name
        self.gpa = gpa

stu1 = Student("Rahul", 8.7)
stu2 = Student("Harshita", 9.4)

print(f"{stu1.name} studying in {stu1.college} has {stu1.gpa} cgpa.")

# class attributes can also be accessed with class name
print(f"{stu2.name} studying in {Student.college} has {stu2.gpa} cgpa.") 

# Methods
class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM):
        self.RAM = RAM

    def get_info(self):   # Instance Method
        print(f"Laptop has {self.RAM} RAM & storage type is {self.storage_type}")

    @classmethod          # Class Method
    def get_storage_type(cls):
        print(f"storage type is {cls.storage_type}")

    @staticmethod         # Static Method
    def cal_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"final price = {final_price}")

l1 = Laptop("16 GB")

l1.get_info() 
Laptop.get_storage_type()
l1.cal_discount(40_000, 10)

# Encapsulation

class BankAccount:
    def __init__(self, name, balance):
        self.name = name            # public
        self.__balance = balance    # private

    def get_balance(self):         # getter
        return self.__balance

    def set_balance(self, new_balance):  # setter
        self.__balance = new_balance

acc1 = BankAccount("Rahul", 50000)
print(acc1.get_balance())
acc1.set_balance(60000)
print(acc1.get_balance())

# Inheritance - Single Inheritance

class Employee:             # parent class
    start_time = "9AM"
    end_time = "5PM"

class Teacher(Employee):    # child class
    def __init__(self, subject):
        self.subject = subject

t1 = Teacher("Data Science")

print(t1.subject, t1.start_time, t1.end_time)

# Multi-level Inheritance

class Employee:             
    start_time = "9AM"
    end_time = "5PM"

class AdminStaff(Employee):     
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):    
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

acc1 = Accountant(50_000, "CA")

print(acc1.salary, acc1.role, acc1.start_time, acc1.end_time)

# Multiple Inheritance

class Teacher:             
    def __init__(self, salary):
        self.salary = salary

class Student():     
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):    
    def __init__(self, name, salary, gpa):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta = TA("Rahul", 50_000, 7.5)

print(ta.name, ta.salary, ta.gpa)

# Abstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()

# Polymorphism

# Example - Operator Overloading
print(1 + 2)    # adds 2 numbers
print("1" + "2") # concatenates 2 strings

# Function Overriding
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Animal()
dog = Dog()

a.sound()  # Some generic sound
dog.sound()  # Bark

# Duck Typing
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

class Robot:
    def speak(self):
        print("Beep Boop")

def make_it_speak(entity):
    entity.speak()  # doesn’t care about type

d = Dog()
c = Cat()
r = Robot()

for e in [d, c, r]:
    make_it_speak(e)