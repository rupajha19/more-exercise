# 21.Write a Python program to print all unique values in a dictionary. 

from typing import ValuesView


Sample_Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
 {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
uniqe_value=set(a for dic in Sample_Data for a in dic.values())
print("unique_value",uniqe_value)