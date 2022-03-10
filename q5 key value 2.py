list1=["one","two","three","four","five","six"]
list2=[1,2,3,4,5,6]
list3={}
for key in list1:
    for value in list2:
        list3[key]=value
        list2.remove(value)
        break
print(list3)