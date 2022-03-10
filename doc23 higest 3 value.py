# Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

a={'item1':43,'item2':20,'item3':4.7,'item4':6.8,'item5':9}
max=0
for i in a:
    if a[i]>max:
        max=a[i]
        b=i
print(b,max)
second_max=0
for i in a:
    if a[i]>second_max:
        if a[i]!=max:
            second_max=a[i]
            b=i
print(b,second_max)
third_max=0
for i in a:
    if a[i]>third_max:
        if a[i]!=max and a[i]!=second_max:
            third_max=a[i]
            b=i
print(b,third_max)


