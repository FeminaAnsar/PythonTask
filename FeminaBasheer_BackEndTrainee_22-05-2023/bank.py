# Python Program to replicate bank transaction: min balance 500, ask user to the amount to withdraw,
# print the balance amount after withdrawal, if user enters an amount greater than balance: print::
# insufficient balance.if balance is below 500 print an alert message : your account balance is
# "available_balance", Please  keep your account balance above Rs.500 to avoid unwanted charges.
accBal=int(input("Enter Account Balance:"))
withdraw=int(input("Enter withdraw amount:"))
if withdraw<accBal:
     bal=accBal-withdraw
     print("Account Balance is:",bal)
else:
     bal=accBal
     print("Insufficient Balance!!!")
if bal<500:
     print("Your account balance is ",bal,"Please  keep your account balance above Rs.500 to avoid unwanted charges")

