class ATM:
    def __init__(self):
        self.__balance=0
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Rs {amount} Deposited successfully.")
            print()
        else:
            print("Amount should be greater than 0.")
            print()
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            print()
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
            print()
        else:
            print("Insufficient balance.")
            print()
        
    def check_balance(self):
        print(f"Current balance: ₹ {self.__balance}")
        
c= ATM()
c.deposit(1000)
c.deposit(-90)
c.withdraw(1001)
c.withdraw(100)
c.check_balance()