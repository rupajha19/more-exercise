dic =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}

count=0
for i in dic.values():
    for j in i:
        count=count+1
print(count)


    