def newpass():
    p = (input("Enter your Current password:"))
    if p not in password or password.index(p) != i:
        print("Incorrect password")
        print("Account Blocked")
    elif password.index(p) == i:
        np = input("Enter your new password:")
        rnp = input("confirm your new password:")
        if np == rnp:
            np = password.index(pas)
            print("Your Password updated successfully.")
        else:
            print("New password and current password didn't matched")
            newpass()
            
def bal(i, p):
    if p not in pin or pin.index(p) != i:
        print("Invalid pin")
        print("End")
    else:
        print("Your balance is", (balance[i]))


def deposit(i, d, p):
    if p not in pin or pin.index(p) != i:
        print("Invalid pin")
        print("End")
    else:
        print("your amount is deposited")
        o = input("Do you want to display your balance? y/n")
        if o == 'y':
            print(d+balance[i])



def withdraw(i, am, p):
    if p not in pin or pin.index(p) != i:
        print("Invalid pin")
        print("End")
    elif am > balance[i]:
        print("Insufficient Amount")
    else:
        print("Collect your Amount")
        o = input("Do you want to display your balance? y/n")
        if o == 'y':
            print(balance[i]-am)



def choice():
    print('''             1.Withdraw
                       2.Deposit
                       3.Balance
                       4.Change Password''')
    ch = int(input("Enter your choice:"))


    valid_choices = [1, 2, 3, 4]
    if ch not in valid_choices:
        print(f"Invalid choice. Valid options are {valid_choices}")
        choice()

    elif ch == 1:
        am = int(input("Enter amount to withdraw:"))
        p = int(input("Enter your pin:"))
        withdraw(i, am, p)
    elif ch == 2:
        d = int(input("Enter amount to deposit:"))
        p = int(input("Enter your pin:"))
        deposit(i, d, p)
    elif ch == 3:
        p = int(input("Enter your pin:"))
        bal(i, p)
    elif ch == 4:
        newpass()



def paswd(i, pas):
    if pas not in password or password.index(pas) != i:
        pw = input("Enter your password again, 2 attempts left:")
        if pw not in password or password.index(pw) != i:
            pws = input("Enter your password again, 1 attempt left:")
            if pws not in password or password.index(pws) != i:
                print("Your Account blocked")
            else:
                choice()
        else:
            choice()
    else:
        choice()


username = ["Priyanka", "Anusha", "Chandhana", "Nandhini"]
password = ["priya", "anu", "chandhu", "nandhu"]
pin = [2004, 2002, 1234, 4321]
balance = [10000, 12000, 9000, 8000]

user = input("Enter Username:")
if user not in username:
    print("User doesn't exist")
    print("End")
else:
    i = username.index(user)
    pas = input("Enter your Password:")
    paswd(i, pas)
