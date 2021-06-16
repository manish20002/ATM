print('Welcome To ethical_hacking_python BANK ATM')
restart=('y')
chances = 3
balance = 9999.50
while chances >= 0:
    pin = int(input('please Enter 4 Digit pin :   '))
    if pin == (1234):
        print('you have entered your pin correctly')
        print('press 1 for your Bank Balance')
        print('press 2 for withdrawl cash')
        print('press 3 for upi payments')
        print('press 4 for Return Card\n')
        while restart not in ('n', 'NO', 'no', 'N'):
            print('yoy have entered your pin correctly')
            print('press 1 for your Bank Balance')
            print('press 2 for withdrawl cash')
            print('press 3 for upi payments')
            print('press 4 for Return Card')
            option = int(input('What Would You Choose?:   '))
            if option == 1:
                print('Your Bank Balance is $', balance)
                restart = input(' Would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('THANKS YOU VISIT AGAIN ')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would You Like to withdraw? 100,200,500,2000 for other enter 1:  '))

            if withdrawl in [100,200,500,2000]:
                balance=balance - withdrawl
                print('\n YOUR BALANCE ID NOW $', balance)
                restart = input('Would you like to go back?')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('THANK YOU')
                    break
                elif withdrawl != [100,200,500,2000]:
                    print('Invalid Amount, Please Re-try\n')
                    restart=('y')
                elif withdrawl == 1:
                    withdrawl = float(input('please enter desired amount:'))

            elif option == 3:
                pay_in = float(input('how much would you like to pay? '))
                balance = balance + pay_in
                print('\n your balance is now $', balance)
                restart = input('would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('THANK YOU')
                    break
            elif option == 4:
                print('please wait whilst your card is returned...\n')
                print('THANKS YOU ')
                break
            else:
                print('please enter correct number\n')
                restart = ('y')
    elif pin != ('1234'):
        print('not valid')
        chances = chances -1
        if chances ==0:
            print('\n No MORE TRIES')
            break


