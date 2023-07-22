# 1) Create a program that calculates the total cost of items purchased at a store. Prompt the user
# to enter the quantity and price of each item, and use operators and conditional statements to calculate
# the total cost. Display the final cost to the user.

i_tot=0
while True:
        i_name=input("Enter name of product:")
        i_pr=float(input("Enter price of product:"))
        i_qu=float(input("Enter quantity:"))
        i_tot+=i_pr*i_qu
        print(i_name," ",i_pr," ",i_qu," ",i_pr*i_qu)
        an_item=input("If there is another item to purchase? (yes/no): ")
        if an_item=="no":
            break
print("Total cost:",i_tot)


