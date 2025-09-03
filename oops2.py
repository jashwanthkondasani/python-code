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

