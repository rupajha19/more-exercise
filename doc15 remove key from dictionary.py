# Q15.Write a Python program to remove a key from a dictionary.

dict={"a":2,"b":5,"c":6,"d":5}
if "d" in dict:
    del dict["d"]
print(dict)