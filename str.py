a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
  
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
  
  # slicing of strings 
b = "Hello, World!"
print(b[2:5])
  
  #Slice From the Start
  b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing 
b = "Hello, World!"
print(b[-5:-2])


# Modify of Strings

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

# The strip() method removes any whitespace
# from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# replace of String 
a = "Hello, World!"
print(a.replace("H", "J"))

'''split() method returns a list where the text between
 the specified separator becomes the list items'''
 
 a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# String concatenation 
a = "Hello"
b = "World"
c = a + b
print(c)


a = "Hello"
b = "World"
c = a + " " + b
print(c)

'''The format() method takes the passed arguments, formats them, 
and places them in the string where the placeholders {}'''
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# escape characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

"""\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value  """

txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 


txt = "Hello\nWorld!"
print(txt) 

txt = "Hello\rWorld!"
print(txt) 

txt = "Hello\tWorld!"
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#octal 
txt = "\110\145\154\154\157"
print(txt) 

# Hexad decimal 
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

