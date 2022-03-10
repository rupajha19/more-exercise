my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
a=[]
max=0
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        b=i
a.append(b)
my_dict.pop(b)
second_max=0
for i in my_dict:
    if my_dict[i]>second_max:
        second_max=my_dict[i]
        c=i
a.append(c)
my_dict.pop(c)
third_max=0
for i in my_dict:
    if my_dict[i]>third_max:
        third_max=my_dict[i]
        d=i
a.append(d)
print(a)



