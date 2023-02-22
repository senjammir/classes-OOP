
class Customer: #create customer class

    def __init__(self,customerid, name, address, email, phone, member_status): #add attributes
        self.__customerid = customerid
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = member_status






class Transaction: #create transaction class

    def __init__(self, date, item_name, cost, customerid): #add attributes
        self.__date = date
        self.__item_name = item_name
        self.__cost = cost
        self.__customerid = customerid

    