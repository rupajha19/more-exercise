list1=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
c=[]
for i in range(len(list1)):
    for j in (list1[i]):
        if list1[i][j] not in c:
            c.append(list1[i][j])
print(c)
