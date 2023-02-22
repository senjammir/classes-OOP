import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

"""Run program with first customer then second customer by commenting out the first customer"""
#customer = fc.Customer(570, "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dsellyarft@gmpg.org", "254-555-9362", False)
customer = fc.Customer(569, "Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", "ahimsworthfs@list-manage.com", "254-555-2273", True)

order_total = 0 #running count of order

print(f"Customer Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")


for key,value in dict.items():  #for loop to iterate through dictionary

    if customer.get_customerid() == value[3]: #check to see if customer id matches with customer id in each transaction
        transaction = fc.Transaction(value[0], value[1], value[2], value[3]) #if found then add that transaction details to the attributes of the transaction class
        print(f"Oder Item: {transaction.get_item_name()}   Price: ${int(transaction.get_cost()):,.2f}")
        current_cost =  transaction.get_cost() #variable to calculate the cost to be added to the running total
        order_total += int(current_cost) #add the cost to the running to total

print(f"Total Cost: ${order_total:,.2f}")  #orint the order total

if customer.get_member_status():
    discount = order_total * 0.2
    print(f"Member Discount: ${discount:,.2f}")
    print(f"Total Cost after discount: ${(order_total - discount):,.2f}")








