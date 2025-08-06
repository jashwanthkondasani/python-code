
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

        
