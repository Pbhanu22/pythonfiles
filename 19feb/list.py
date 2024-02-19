#thislist = ["apple", "banana", "cherry"]
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
'''print(len(thislist))

print(type(thislist))
'''
"""
#thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
thislist[1]='canberry'
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist.remove("banana")
print(thislist)
thislist.pop(1)
print(thislist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist = [x for x in fruits if "a" in x]

print(newlist)"""

a=[14,21,13,54,15,6,27,82,9,44]
a.sort()
print(a)

a.sort(reverse = True)
print(a)
a.reverse()
print(a)
b= a.copy()
print(b.count(15))
