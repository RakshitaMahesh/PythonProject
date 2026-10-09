import time
password=7420
Balance=10000
print("Welcome to pentagon ATM")
print("insert your card")
print("Press 1.yes 2.no")
card=int(input())
if card==1:
    print("select your language")
    print("1.English 2.Kannada 3.Hindi")
    lang=int(input())
    if lang==1:
        print("enter your pin")
        pin=int(input())
        if pin==password:
            print("select your option")
            print("press 1.Bal enq 2.withdrawl")
            choice=int(input())
            if choice==1:
                print("your available balance is",Balance)
            elif choice==2:
                print("Enter the amount")
                amt=int(input())
                print("your transaction is processing")
                time.sleep(5)
                print("please collect the cash")
                time.sleep(4)
                print("do you want to check your balance")
                print("press 1.yes 2.no")
                choice1=int(input())
                if choice1==1:
                    print("Your available balance is",Balance-amt)
                    print("Thank you visit again")
                else:
                    print("Thank you visit again")
            else:
                print("invalid option")
        else:
            print("INvalid pin")
    else:
        print("PLEASE SELECT ENGLISH")
else:
    print("insert your card properly")


