# Set 
# acessing of sets
"""
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
for x in thisset:
  print(x)
print("banana" in thisset)
thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
print(len(thisset))
print(type(thisset))
set1 = {"abc", 34, True, 40, "male"}
print(set1)

ns=set(("Chakri", "bhanu", "charan")) # note the double round-brackets
print(ns)
"""

#Remove of items 
"""thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
"""
# union() joining of sets 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
