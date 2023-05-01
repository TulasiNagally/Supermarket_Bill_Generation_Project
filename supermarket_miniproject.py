from datetime import datetime

# get the customer name and address
name = input("Enter your name: ")
address = input("Enter your address: ")
print("list of items and prices")

# create a dictionary to store the items and their prices
itemsandprices = {
"maggi/gram"       :  20.00,
"milk/litre"       :  80.00, 
"soaps/each"       :  60.00,
"peanuts/kg"       :  80.00,
"coffeepowder/kg"  :  200.00,
"riceflour/kg"     :  40.00,
"wheatflour/kg"    :  35.00,
"oil/litre"        :  130.00,
"sugar/kg"         :  30.00,
"eggs/dozen"       :  60.00
 }
for key, value in itemsandprices.items():
    print(key,' - ',value)

# # initialize the total cost to 0
total_cost = 0

# get the items and their quantities from the user using a for loop
items = {}
for i in range(7):
    sno = i + 1
    item = input("Enter the item name: ")
    if item in itemsandprices:
        quantity = int(input("Enter the quantity: "))
        items[item] = {"sno": sno, "quantity": quantity, "price": itemsandprices[item]}
    else:
        print("Sorry, that item is not available.")
        continue
        
# print the bill in a table format
print("{:^60}".format("TulasiSupermarket"))
print("-" * 60)
print("{:<10}{:<20}".format("Customer Name:",name))
print("{:<5}{:<10}".format("Address:",address))
print("{:<5} {:<15} {:<10} {:<10}".format("Sno", "Item", "Quantity", "Price (Rs.)"))
print("-" * 60)
for item, item_details in items.items():
    print("{:<5} {:<15} {:<10} Rs.{:<10}".format(item_details["sno"], item, item_details["quantity"], item_details["price"]))
    total_cost += item_details["price"] * item_details["quantity"]
print("{:>31} Rs.{:<10}".format("Final price:", total_cost))
print("-" * 60)
print("{:^60}".format("thank you for visting"))



