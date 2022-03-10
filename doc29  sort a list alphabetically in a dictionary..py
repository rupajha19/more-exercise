# Q29.Write a Python program to sort a list alphabetically in a dictionary.
num={'a1':[2,3,1],'a2':[5,4,7],'a3':[6,8,9]}
b={x: sorted(y) for x,y in num.items()}
print(b)
