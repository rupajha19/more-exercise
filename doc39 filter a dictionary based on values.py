
# Q39.Write a Python program to filter a dictionary based on values. 
Original_Dictionary={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

marks={key:value for key,value in Original_Dictionary.items()if value>=170}
print(marks)