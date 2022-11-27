class Account:
    def __init__(self, balance):
        self.__balance = balance
        
    def getBalance(self):
        return self.__balance
    
    def getAccountName(self):
        return self.__accountName
  
    def deposit(self, amt):
        if amt > 0:
            print("$" + str(amt) + " deposited \n")
            self.__balance += amt
            print("You balance is now $" + str(self.__balance))
            return True
        else:
            print("Please deposit more than $0.00 only. \n")
            return False
    
    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
            print("$" + str(amt) + " withdrawn \n")
            print("Your balance is now $"+ str(self.__balance))
            return True
        else:
            print("Insufficient amount of funds. \n")
            return False
        