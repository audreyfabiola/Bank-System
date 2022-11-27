from Account import Account
from Customer import Customer
from Bank import Bank

# START MENU

class BankSystem:
    def __init__(self, data):
        self.__data = data

        self.__authenticated_user_idx = None
        
        self.__bank = Bank("AUDREY'S BANK")
        for idx, data in enumerate(self.__data):
            self.__bank.addCustomer(data["f"], data["l"], data["customerPin"])
            self.__bank.getCustomer(idx).setAccount(Account(data["balance"]))


        self.__mainMenu()

    def __mainMenu(self):
        # options to choose whether user is administrator or customer
        isNotExit = True 
        while isNotExit:
            try:
                print(" ")
                print("-------------------------------")
                print("🏦 Welcome to Audrey's Bank 🏦")
                print("-------------------------------")
                print("1. Administrator login")
                print("2. Customer login")
                print("3. Exit")
                print(" ")
                choice = int(input("Choose your option: "))
                isNotExit = self.__runMainMenu(choice)
            except ValueError:
                print("Please enter a valid option. \n")
        

    def __runMainMenu(self,choice):
        loop = 1
        while loop == 1:
            if choice == 1: #administrator login
                if self.__authorizeAdmin() == True:
                    self.__adminMenu()
                return True
            elif choice == 2: #customer login
                if self.__authorizeCustomer() == True:
                    self.__accountMenu()
                return True
            elif choice == 3: #exit the bank system
                loop = 0
                print("Thank you for using Audrey's Bank. See you again ♡ \n")

                return False

# ADMINISTRATOR

    def __authorizeAdmin(self):
        adminPin = input("Enter your pin: ")
        while not self.__adminPin(adminPin):
            print("Incorrect pin. Please try again.")
            adminPin = input("Enter your pin: ")

    def __adminPin(self, adminPin):
        if adminPin == "1234":
            self.__adminMenu()
            return True

        return False

    def __adminMenu(self):
        # options you have when logged in as an administrator
        isNotExit = True
        while isNotExit:
            try:
                print(" ")
                print("---------------------------")
                print("What would you like to do?")
                print("---------------------------")
                print("1. Add customer")
                print("2. Delete customer")
                print("3. Edit Customer")
                print("4. Search Customer")
                print("5. Back")
                print(" ")
                choice = int(input("Choose your option: "))
                isNotExit = self.__runAdminMenu(choice)
            except ValueError:
                print("Please enter a valid option. \n")
            


    def __runAdminMenu(self, choice):
        loop = 1
        while loop == 1:
            if choice == 1: #add customer
                f = input("First Name: ")
                l = input("Last Name: ")
                customerPin = input("Pin: ")
                balance = input("Balance: ")

                self.__data.append(
                    {
                        "f": f,
                        "l": l,
                        "customerPin": customerPin,
                        "balance": int(balance)
                    }
                )
                
                self.__bank.addCustomer(f, l, customerPin)
                self.__bank.getCustomer(len(self.__data)-1).setAccount(Account(int(balance)))
                return True
                
            elif choice == 2: #delete customer

                delete = input("Which customer index do you want to delete?: ")

                del self.__data[int(delete)]

                print("Successfully deleted.")

                return True
                    
            elif choice == 3: #edit customer

                edited = input("Which customer index do you want to edit?: ")

                if int(edited) > len(self.__data)-1:
                    print(f"There are only {len(self.__data)} customers in our database. Please enter a proper value.")
                else: 
                    f = input("First Name: ")
                    l = input("Last Name: ")
                    customerPin = input("Pin: ")
                    balance = input("Balance: ")

                    self.__data[int(edited)] = {
                            "f": f,
                            "l": l,
                            "customerPin": customerPin,
                            "balance" : int(balance)
                        }

                print("Successfully edited.")
                
                return True
    

            elif choice == 4: #search customer
                for idx, data in enumerate(self.__data):
                    print(f"""
Customer ID-{idx}:
    > First Name: {data["f"]}
    > Last Name: {data["l"]}
    > Customer Pin: {data["customerPin"]}
    > Balance: ${data["balance"]}
                        """)
                return True

            elif choice == 5: #back to start menu
                loop = 0
                print("Thank you for your hardwork (＾▽＾) \n")
                return False

        
# CUSTOMER
            
    def __authorizeCustomer(self):
        cred_f = input("First Name: ")
        cred_l = input("Last Name: ")
        cred_customerPin = input("Pin: ")
        
        while not self.__check_cred_by_name(cred_f, cred_l, cred_customerPin):
            print("Incorrect credential. Please try again.")
            cred_f = input("First Name: ")
            cred_l = input("Last Name: ")
            cred_customerPin = input("Pin: ")

        return True
        
    def __check_cred_by_name(self, f, l, customerPin):
        for idx, data in enumerate(self.__data):
            if f == data["f"] and l == data["l"] and customerPin == data["customerPin"]:
                self.__authenticated_user_idx = idx
                return True
            
        return False

    def __accountMenu(self):
        # options you have when logged in as a customer
        isNotExit = True
        while isNotExit:
            try:
                print(" ")
                print("---------------------------")
                print("What would you like to do?")
                print("---------------------------")
                print("1. Deposit money")
                print("2. Withdraw money")
                print("3. Check balance")
                print("4. Back")
                print(" ")
                choice = int(input("Choose your option: "))
                isNotExit = self.__runAccountMenu(choice)
            except ValueError:
                print("Please enter a valid option. \n")


    def __runAccountMenu(self, choice):
        loop = 1
        while loop == 1:

            if choice == 1: #deposit money
                try:
                    amt = int(input("Enter amount to be deposited: $"))
                    
                    deposit = self.__bank.getCustomer(self.__authenticated_user_idx).getAccount().deposit(amt)
                except ValueError:
                    print("Please deposit more than $0.00 only. \n")
                 
                return True
                
            elif choice == 2: #withdraw money
                try:
                    amt = int(input("Enter amount to be withdrawn: $"))
                    withdraw = self.__bank.getCustomer(self.__authenticated_user_idx).getAccount().withdraw(amt)
                except ValueError:
                    print("Insufficient amount of funds. \n")

                return True
                
            elif choice == 3: #check balance
                balance = self.__bank.getCustomer(self.__authenticated_user_idx).getAccount().getBalance()
                print("Your balance is $" + str(balance))

                return True
                
            elif choice == 4: #back to start menu 
                loop = 0
                
                return False

