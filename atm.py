import option as option
print ("wellcome srikanth bank")
restart = ('y')
chances = 3
balance = 500
while chances >= 0:
    pin = int(input("please enter your pin: "))
    if pin == (1234) :
        print("your entered pin correctly\n")
        while restart not in ('n', 'no', 'N', 'NO'):
            print("press 1 for balance\n")
            print("press 2 for withdraw\n")
            print("press 3 for pay\n")
            print("press 4 for return card\n")
            option = int(input("choose option: \n"))
            if option == 1 :
                print(balance)
                restart = input("would you like to go back?")
                if restart in ('n', 'no', 'N', 'NO'):
                    print("thankyou")
                    break
            elif option == 2 :
                option2 = ('y')
                withdrawlamount = int(input("please enter amount: "))
                if withdrawlamount <= balance :
                    balance = balance - withdrawlamount
                    print(balance)
                    restart = input("would you like to go back?")
                    if restart in ('n', 'no', 'N', 'NO'):
                        print("thankyou")
                        break
                elif withdrawlamount >= balance:
                    print("please enter desired amount: ")
                    restart = ('y')

            elif option == 3 :
                payamount = int(input("please enter payamount: "))
                balance = balance + payamount
                print(balance)
                restart = input("would you like to go back?")
                if restart in ('n', 'no', 'N', 'NO'):
                    print("thankyou")
                    break
            elif option == 4 :
                print("return to card")
            else:
                print("please enter correct option")
                restart = ('y')
                break

    if pin != (1234) :
        print("please enter correct password")
        restart = ('y')
        chances = chances - 1
        if chances == 0:
            print("no more chances")
            restart = ('y')
            break
    break