#revision banking system 

def deposit_cash(balance):
    deposit_amount = float(input("How much amount would you like to deposit: "))
    if deposit_amount <= 0:
        print("Invalid deposit amount")
        return balance
    else:
        new_balance = balance + deposit_amount
        print(f"Your new balance is: {new_balance}")
        return new_balance

def withdraw_cash(balance):
    withdraw_amount = float(input("How much would you like to withdraw: "))
    if withdraw_amount > balance  or withdraw_amount <=0:
        print("Invalid amount")
        return balance
    else:
        new_balance = balance - withdraw_amount
        print(f"Your new balance is: {new_balance}")
        return new_balance
    
def show_balance(balance):
    print(f"Your current balance: {balance}")

def option(balance, action):
    match(action):
        case 1:
            show_balance(balance)
        case 2:
            balance = deposit_cash(balance)
        case 3:
            balance = withdraw_cash(balance)
        case 4:
            print("Thank you for banking with us.")
            return balance, False
        case _:
            print("Please choose form option 1-4")
    return balance, True

BALANCE = 0
balance = BALANCE
isrunning = True 

while isrunning:
    print("Welcome to archi bank.")
    print("1.show balance, 2.deposit cash, 3.withdraw cash, 4.quit")
    try:
        action = int(input("choose your action: "))
        balance, isrunning = option(balance, action)
    except ValueError:
        print("Invalid input. Please try again")
        continue