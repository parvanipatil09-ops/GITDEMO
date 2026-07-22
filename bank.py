#Menu: Deposit, Withdraw, Check Balance, Exit; use separate functions; prevent negative balance.
depo=0
def deposit():
    global depo
    depo+=int(input('enter amount to deposit: '))
    print("Deposited")
    print() 

def withdraw(amount):
    global depo
    if amount<=depo:
        depo-=amount
        print('withdrawl successfully completed')
    else:
        print('not sufficient balance,enter a smaller amount')
    print()

def check_balance():
    print('The current balance is',depo)
    print()
    
while True:
    print('1. DEPOSIT')
    print('2. WITHDRAW')
    print('3.CHECK BALANCE')
    print('4.EXIT')
    print()
    print()
    try:
        ch=int(input('enter choice(1-4):  '))
        if ch==1:
            deposit()
        elif ch==2:
            amount=int(input('enter amount to be withdrawn: '))
            withdraw(amount)
        elif ch==3:
            check_balance()
        elif ch==4:
            break
    except Exception:
        print('invalid choice')
        print()