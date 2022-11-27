from Account import Account

class Customer:
    def __init__(self, f, l, customerPin):
        self.__fName = f
        self.__lName = l
        self.__customerPin = customerPin
    
    def getFirstName(self):
        return self.__fName
    
    def getLastName(self):
        return self.__lName
    
    def getCustomerPin(self):
        return self.__customerPin
    
    def getAccountList(self):
        return self.__account
    
    def getAccount(self):
        return self.__account
    
    def setAccount(self,account):
        self.__account = account
        




    