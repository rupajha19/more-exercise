# Q3.Write a Python script to generate and print a dictionary that contains a number
#  (between 1 and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.


# num=int(input("enter number.."))
# dic={}
# for i in range(num+1):
#     dic[i]=i*i
# print(dic)

num=int(input("enter number.."))
i=0
dic={}
while i<=(num):
    dic[i]=i*i
    i+=1
print(dic)


