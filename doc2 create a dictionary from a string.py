

Sample_string ='w3resource'
counter={}
for i in Sample_string:
    if i not in counter:
        counter[i]=1
    else:
        counter[i]+=1
print(counter)


