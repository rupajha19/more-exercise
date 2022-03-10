number_student=int(input("enter student number::"))
expence=int(input("enter expence::"))
spend=number_student*expence
if spend<=50000:
    print("budget ke andar hai")
else:
    print("budget ke bahar hai")