"""
This file comtains about the 
variables in detail 
"""
""" x=10 
print(x)
print(type(x))
"""

x = 5
y = "John"
print(x)
print(y)
print(type(x))
print(type(y))

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)
print('Assigning multiple values ') 
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
print('Assigning one value to multiple variable ')
x = y = z = "Orange"
print(x)
print(y)
print(z)
print("Unpack of variables")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

# declaring legal variables 
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print("Declaring of varible names:") 
# Camel case
myVariableName ="Name"
print(myVariableName)
# pascal 
MyVariableName = "John"
print(MyVariableName)
#Snake case 
my_variable_name = "John"
print(my_variable_name)

print("Global declaration of variables and keyword ")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
