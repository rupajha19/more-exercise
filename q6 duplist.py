string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
final_list=[]
for i in string_list:
    if i  not in final_list:
        final_list.append(i)
print(final_list)
