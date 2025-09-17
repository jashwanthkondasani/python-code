// max element in array

a=[11,12,23,24,25,26,27]
max_element=a[0]
for i in range(len(a)):
    if a[i]> max_element:
        max_element=a[i]
print(max_element)

// max element in array
a=[99,100,102,122]
min_element=a[0]
for i in range(len(a)):
    if a[i]<min_element:
        min_element=a[i]
print(min_element)


// min and max elements of arrays 
arr=[1,2,3,4,5,6,7,8,100,0]
mini=arr[0]
maxi=arr[0]

for i in range(len(arr)):
   if  arr[i]<mini:
    mini=arr[i]

   if  arr[i]>maxi:
    maxi=arr[i]

print(mini)
print(maxi)

// add of two numbers
def add_numbers(a,b):
        return a+b
    
result=add_numbers(1,3)
print("sum is:",result)

# sub of two numbers
def sub_numbers(x,y):
    
    return x-y

result=sub_numbers(8,7)
print("sub is:",result)

# multi of two numbers
def mult_numbers(a,b):
    
    return a*b

result=mult_numbers(2,3)
print("mult is:",result)

#  div of two numbers 
def div_numbers(a,b):
    
    return a /b

result=div_numbers(44,2)
print("division of the numbers is :",result)









