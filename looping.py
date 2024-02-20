for x in "banana":
  print(x)
  
  
i = 1
while i < 6:
  print(i)
  i += 1
  
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
  
  
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


a = 33
b = 200
if b > a:
  print("b is greater than a")
  
  
  
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


if a > b: print("a is greater than b")


a = 2
b = 330
print("A") if a > b else print("B")



a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")



a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
  
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
  
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
    
a = 33
b = 200

if b > a:
  pass