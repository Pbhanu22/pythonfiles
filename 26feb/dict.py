thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
"""print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))

t1 = dict(name = "John", age = 36, country = "Norway")
print(t1)

x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)"""
thisdict["year"] = 2018
print(thisdict)

thisdict.update({"year": 2020})
print(thisdict)

thisdict.pop("model")
print(thisdict)


del thisdict["year"]
print(thisdict)
print(thisdict)

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict1)
print(mydict)




myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)