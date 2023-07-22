# 1) print insufficient balance if user enter an amount greater than acc balance

acc_bal=int(input("Enter account balance:"))
withdraw=int(input("Enter amount to withdraw:"))
bal=acc_bal-withdraw
if withdraw>acc_bal:
    print("Insufficient balance!!!")
else:
    print("Account balance :",bal)