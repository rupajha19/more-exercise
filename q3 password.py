print("Make Strong Password::")
a=(input("enter any lower case and upper case::"))
if a>="A" or a>="Z" or a>="a" or a>="z":
    pass
    special_chr=input("enter special chr::")
    if special_chr>="&" or special_chr>="@" or special_chr>="#":
        pass
        digit=(input("enter atleast 16 digit::"))
        if len(digit)>0:
            pass
            print(a+special_chr+str(digit))
            print("your password is strong")
        else:
            print("your password is not strong",digit)
    else:
        print("less then 8b digit")
else:
    print("there is no special chr")







