# python String
# basic String with print method 
# print("Hello")
""" Assign  a variable 
a = "Hello"
print(a)"""
# Multi line Strings 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
print(a)
# Acessing String as array indexing 
a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)
  
a = "Hello, World!"
print(len(a)) 

txt = "The best things in life are free!"
print("free" not in txt)
# Slicing of a String 
b = "Hello, World!"
print(b[2:5])

print("Slice from First")
b = "Hello, World!"
print(b[:5])
print("Slice from End")
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])
# modify strings 
a = "Hello, World!"
print(a.lower())


a = "Hello, World!"
print(a.replace("H", "J"))
print(a.split(","))
print(a.capitalize())
print(a.casefold())
print(a.center(30))
print(a.encode())
print(a.endswith("!")) 
print(a.find("hello"))
print(a.index("e"))
txt= "ciencia2k24"
print(txt.isalnum())
print(txt.isalpha())
print(txt.isdecimal())
print(txt.isdigit())
print(txt.isspace())
print(txt.isprintable())
print(txt.isupper())
print(txt.islower())
b="    Bhanu"
print(b.lstrip())
c="Bhanu    "
print(c.rstrip())
d="    Bhanu    " 
print(d.strip())

a = "Hello"
b = "World"
c = a +" "+ b
print(c)"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))