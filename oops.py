
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
        
