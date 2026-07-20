num1=int(input('enter number 1 : '))
num2=int(input('enter number 2: '))
while True:
    try:
        ch=int(input('''choose operator
             1)Addition
             2)Subtraction
             3)Multiplication
             4)Division
             5 for exit): '''))
        if ch==1:
            print(f"{num1}+{num2}= {num1+num2}")
        elif ch==2:
            print(f"{num1}-{num2}= {num1-num2}")
        elif ch==3:
            print(f"{num1}*{num2}= {num1*num2}")
        elif ch==4:
            print(f"{num1}/{num2}= {num1/num2}")
        elif  ch==5:
            break
        
    except ZeroDivisionError:
        print('num2 cant be 0')
    except ValueError:
        print('invalid values')