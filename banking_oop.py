class BankAccount:
    def __init__(self,acc_holder,acc_num,balance):
        self.acc_holder=acc_holder
        self.acc_num=acc_num
        self.balance=balance
        
    def display(self):
        print(f"Account holder: {self.acc_holder}")
        print(f"Account Number: {self.acc_num}")
        print(f"Balance: {self.balance}")
        print()
    
    def deposit(self,amount):
        if amount<=0:
            print('invalid amount')
        else:
            self.balance+=amount
            print(f"Rs {amount} deposited successfully")
            print(f"Current Balance: Rs {self.balance}")
        print()
    
    def withdraw(self,amount):
        if amount<=0:
            print('invalid amount')
        elif amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawal Successful.\n Remaining Balance: Rs {self.balance}")
        else:
            print('Insufficient Balance')
        print()
        
    def check_balance(self):
        print(f"Current Balance: Rs {self.balance}")
        print()
    
    def transfer(self,other_acc,amount):
        if amount<=0:
            print('invalid amount')
        elif amount<=self.balance:
            print(f"Rs {amount} transferred successfully")
            self.balance-=amount
            other_acc.balance+=amount
            print(f"{self.acc_holder} Balance: Rs {self.balance}")
            print(f"{other_acc.acc_holder} Balance : Rs {other_acc.balance}")
        else:
            print('insufficient balance')
        print()
acc1=BankAccount('Parvani',999,100)
acc2=BankAccount('Jenny',87,49)
acc3=BankAccount('Cathy',76,100)

l=[acc1,acc2,acc3]
for i in l:
    i.display()
    i.deposit(50)
    i.withdraw(50)
    i.check_balance()
    print()
acc1.transfer(acc2,1)