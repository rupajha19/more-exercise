# Q25. Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.
Sample_string='w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
counter={}
for i in Sample_string:
    if i not in counter:
        counter[i]=1
    else:
        counter[i]+=1
print(counter)