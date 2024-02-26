dict1 = {1: 'a', 2: 'b'}
dict2 = {2: 'c', 4: 'd'}
"""dict3= dict2.copy()
dict3.update(dict1)
print(dict3)"""
print(dict1|dict2)




lista = [1, 2, 2, 5, 8, 4, 4, 8]
l1 = []
count = 0
for item in lista:
    if item not in l1:
        count += 1
        l1.append(item)
print("unique items:", count)



my_dict = {'Name': 'Bhanu', 'Age': 21, 'Gender': 'Male'}

if my_dict.get('Nail') is not None:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")