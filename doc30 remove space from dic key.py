#Q30.Write a Python program to remove spaces from dictionary keys.
Original_dictionary= {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
new_dict={x.translate({32:None}):y
    for x,y in Original_dictionary.items()}
print("new dictionary is",new_dict)















