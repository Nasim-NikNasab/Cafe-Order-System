#Cafe System

# 4 Order History
Order_History = []
Order_History.append(["Nasim", 60.5])

#1 Variables
Cafe_Name = "Monolo"
print(f"Welcome to {Cafe_Name} Cafe !")
Coffee_Price = 60.5
print("Coffee_Price : 60.5 T ")
Cups_Available = 100

#2 Input
Customer_Name : str = input("Enter Customer Name: ")
Cups_Number : int = int(input("Enter Cups Number: "))

#3 Order Validation
if Cups_Number <= Cups_Available:
    print("Your order has been placed successfully")
    total_price = Coffee_Price * Cups_Number
    if total_price > 3 :
        total_price -= total_price/10
        print("Your total cost is $" + str(total_price))
        Order_History.append([Customer_Name, total_price])
        # 5 Orders List
        for order in Order_History:
            print(order)
        exit()
else:
    print("Sorry, your order has not been placed successfully")
    exit()



