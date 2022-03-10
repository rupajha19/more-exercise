# Q38.. Write a Python program to drop empty Items from a given Dictionary. 



dict={'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
print("New Dictionary after droping empty items")
dict={key:value for (key,value)in dict.items()if value is not None}
print(dict)

