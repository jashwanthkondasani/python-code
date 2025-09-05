# creating a class and object 

class nani:
    def __init__(self,n,o):
        self.name=n
        self.occupation=0
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"player tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots film")
    def speaks(self):
        print(self.name,"hi how are you")

jash=nani("jashwanth ","actor")
jash.do_work()
jash.speaks()

#  inheritance
class A:
   def feature1(self):
        print(" feature 1 is working")

   def feature2(self):
        print("feature 2 is working")

class B(A):
    def feature3(self):
        print(" feature 3 is working")

    def feature4(self):
        print("feature 4 is working")
class C(B):
    def feature5(self):
        print(" feature 5 is working")

    def feature6(self):
        print("feature 6 is working")


a1=A()
a2=A()



a1.feature1()
a2.feature2()
b1=B()
b2=B()



b1.feature1()
b2.feature2()

c1=C()
c2=C()



C1.feature1()
C2.feature2()

class Grandparent:
    def show(self):
        print("I am the Grandparent")

class Parent(Grandparent):
    def display(self):
        print("I am the Parent")

class Child(Parent):
    def print_info(self):
        print("I am the Child")

# Usage
c = Child()
c.show()
c.display()
c.print_info()

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))
 def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

# Base class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started!")

# Derived class (inherits from Car)
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        # call parent constructor
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        # Override parent method
        print(f"{self.year} {self.brand} {self.model} (Electric) - Battery: {self.battery_capacity} kWh")

    def charge(self):
        print(f"{self.brand} {self.model} is charging...")

# Derived class (inherits from Car)
class SportsCar(Car):
    def __init__(self, brand, model, year, horsepower):
        super().__init__(brand, model, year)
        self.horsepower = horsepower

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} (Sports) - {self.horsepower} HP")

    def turbo_boost(self):
        print(f"{self.brand} {self.model} is using turbo boost!")

# Create objects
car1 = Car("Toyota", "Corolla", 2020)
ev1 = ElectricCar("Tesla", "Model 3", 2023, 75)
sports1 = SportsCar("Ferrari", "488 GTB", 2022, 660)

# Use methods
car1.display_info()
car1.start_engine()

ev1.display_info()
ev1.start_engine()
ev1.charge()

sports1.display_info()
sports1.start_engine()
sports1.turbo_boost()

# out put
2020 Toyota Corolla
Toyota Corolla's engine started!
2023 Tesla Model 3 (Electric) - Battery: 75 kWh
Tesla Model 3's engine started!
Tesla Model 3 is charging...
2022 Ferrari 488 GTB (Sports) - 660 HP
Ferrari 488 GTB's engine started!
Ferrari 488 GTB is using turbo boost!
