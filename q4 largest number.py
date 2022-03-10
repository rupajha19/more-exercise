a=int(input("enter number::"))
b=int(input("enter number::"))
c=int(input("enter number::"))
if a>b and a>c:
    print(a,"a is largest number")
elif b>a and b>c:
    print(b,"b is largest number")
elif c>b and c>b:
    print(c,"c is greater number")
else:
    print("lesser number")