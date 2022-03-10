# Q24.
# Write a Python program to combine values in python list of dictionaries. 
from typing import Counter


Sample_data= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, 
{'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
from collections import Counter
a=Counter()
for i in Sample_data:
    a[i['item']]+=i['amount']
print(a)