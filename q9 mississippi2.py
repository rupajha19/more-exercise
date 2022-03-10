word="MISSISSIPPI"
counter={}
for i in word:
    if i not in counter:
        counter[i]=1
    else:
        counter[i]+=1
print(counter)


