# .Write a Python program to match key values in two dictionaries. 
a={'key1': 1, 'key2': 3, 'key3': 2}
b={'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

# we use %s The % symbol is used in Python with a large variety of data 
# #types and configurations. %s specifically is used to perform concatenation of strings together.
# # It allows us to format a value inside a string. It is used to incorporate another string within a string.
for key,value in set(a.items()) & set(b.items()):
    print('%s:%s 1 is present in both x and y')

    