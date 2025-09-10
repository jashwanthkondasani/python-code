  date-09/09/2025

print("jai sri ram ")
print(" this is kondasanijashwanth kumar reddy from yerraguntlabavi " \
"i am studied at sri venkateswara college of engeneering at tirupati" 
    )


basic programms of python 
 addition of two numbers

a=10
b=20
print(a+b)

 method 2 
a=int(input(" enter 1 number "))
b=int(input("enter 2 number "))
print(a+b)\


guess_game.py
-----------------
The computer picks a random number between 1 and 100.
The player tries to guess it, and the program tells
whether the guess is too high or too low.


 programms using loops 

 biggest of four numbers 

a=int(input("enter the 1st number "))
b=int(input("enter the 2st number "))
c=int(input("enter the 3st number "))
d=int(input("enter the 4st number "))
if a>b and a>c and a>d :
  print(" a is greater ")
elif b>a and b>c and b>d:
  print("  b is greater ")
elif c>a and c>b and c>d:

  print(" c is greater ")
else:
  print(" d is greater ")

 factorial of a number 

 sum of the numbers 

num=int(input(" enter the number "))
sum=0
for i in range(num+1):
  sum+=i
print(sum)

 sum of numbers in given range 
a=int(input("enter the first number "))
b=int(input("enter the second  number "))
sum=0
for i in range(a,b+1):
  sum+=i
print(sum)

check weather it is an leap year or not
year=int(input(" enter the year"))
if (year%400==0) or (year%4==0 and year%100!=0):
  print(" it is a leap year ")
else:
  print(" it is an not an leap year ")

 num = 1234
temp = num
reverse = 0

while num > 0:
    remainder = num % 10          # get last digit
    reverse = (reverse * 10) + remainder  # build reversed number
    num = num // 10               # remove last digit

print(reverse)
