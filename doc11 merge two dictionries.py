# Q11.Write a Python script to merge two Python dictionaries
a={"a":1,"b":3,"c":4}
b={"d":5,"e":6,"f":7}
c={}
for dict in(a,b):
    for key,value in dict.items():
        c[key]=value
print(c)
