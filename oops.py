
class Employee :
    language ="python"
    salary =12000


    def getInfo(self):
        print(f" the language is{self. language} . the salary is self salary{self.salary}")

    def greet(self):
        print("good morning")


harry =Employee()
harry.greet()

# program 2
class student:
    def _init__(self,name,marks):
         self.name=name
         self.marks=marks
    def get_avg(self):
        sum =0
        for val  in self.marks:
            sum +=val
        print("hi",self.name,"your avg score:",sum/3)

s1=student("jashwanth",[99,98,97])
s1.get.avg()
s1.name="jashwanth"
s1.get.avg()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating an object
s1 = Student("Jashwanth", 20)
s1.display_info()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Object creation
r = Rectangle(10, 5)
print("Area of rectangle:", r.area())

class Car:
    def __init__(self):
        self.brand = "Toyota"
        self.model = "Innova"

    def show(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

c = Car()
c.show()

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"{self.name}'s Balance: ₹{self.balance}")

# Using the class
acc = BankAccount("Jashwanth", 5000)
acc.deposit(1500)
acc.withdraw(2000)
acc.show_balance()


# Example: Encapsulation with private variable
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Object
account = BankAccount(1000)
account.deposit(500)
print("Balance:", account.get_balance())

# Example: Method Overriding
class Bird:
    def fly(self):
        print("Some birds can fly.")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high.")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly.")

# Objects
birds = [Sparrow(), Ostrich()]
for b in birds:
    b.fly()   # Same method, different behavior

# Base class
class Animal:
    def speak(self):
        print("This animal makes a sound")

# Derived class
class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

# Derived class
class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")

# Objects
d = Dog()
c = Cat()

d.speak()
c.speak()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

c = Circle(5)
s = Square(4)

print("Circle Area:", c.area())
print("Square Area:", s.area())


# Create an array (list)
arr = [10, 20, 30, 40, 50]

# Display array elements
print("Array:", arr)

# Access elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# Insert element
arr.append(60)
print("After append:", arr)

# Remove element
arr.remove(30)
print("After removing 30:", arr)

# Update element
arr[1] = 25
print("After updating:", arr)

# Length of array
print("Length:", len(arr))


# Writing data to a file
file = open("example.txt", "w")  # "w" = write mode
file.write("Hello, this is the first line!\n")
file.write("This is the second line.")
file.close()
print("File created and data written successfully!")

with open("example.txt", "r") as f1, open("copy.txt", "w") as f2:
    for line in f1:
        f2.write(line)
print("File copied successfully!")

# Append data
file = open("example.txt", "a")  # "a" = append mode
file.write("\nThis line is appended!")
file.close()
print("Data appended successfully!")


        
