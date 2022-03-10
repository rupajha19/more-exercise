a={}
n=int(input("enter any element::"))
for i in range(n):
    name=input("enter your name::")
    age=int(input("enter age::"))
    a.update({name:age})
print(a)


