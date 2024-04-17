print("Welcome to ABC bank")
loan_no = input("Enter a loan number: ")
due_amount = int(input("Enter due amount: "))
days  = int(input("Enter a number of days missed: "))
print("--------------------invoice-------------")
print("loan no                : ",loan_no)
print("due amount             : ",due_amount)
print("Day missed             : ",days)


if days == 0:
    fine_amount = due_amount * 0/100
    print("Fine_amount          : ",fine_amount)
    print("Total payable amount : ",fine_amount+due_amount)

elif days >=1 and days<=5:
    fine_amount = due_amount * 5/100
    print("Fine_amount          : ",fine_amount)
    print("Total payable amount : ",fine_amount+due_amount)

elif days >=6 and days <=10:
    fine_amount = due_amount * 10/100
    print("Fine_amount          : ",fine_amount)
    print("Total payable amount : ",fine_amount+due_amount)

else:
    print("Due date passed more than 10 days. contact admin")

    
