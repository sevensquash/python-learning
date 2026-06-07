#slot machine

import random

def display_result(spin_result):
    print("|".join(spin_result))

def spin_reel(bet_amount,symbols):
    return [random.choice(symbols) for _ in range(3)]

def reward_system(spin_result,bet_amount,balance):
    if spin_result[0] == spin_result[1] and spin_result[1] == spin_result[2]:
        print("Jackpot")
        return balance + bet_amount * 3
    elif spin_result[0] == spin_result[1] or spin_result[1] == spin_result[2] or spin_result[0] == spin_result[2]:
        print("Congratulations")
        return balance + bet_amount * 2
    else:
        print("You lost.")
        return balance

BALANCE = 100
balance = BALANCE
isrunning = True

while isrunning:
    print("Welcome to archi cashino.")
    symbols = ['🍒','🔔','🏆','💎','🌟']
    print("|".join(symbols))
    print("Spin reel or press 'Q' to quit")
    print(f"Your balance: {balance}")
    try:
        bet_amount = str(input("How much would you like to bet."))
        if bet_amount.lower() == "q":
            print("Thank you for playing with us.")
            isrunning = False
            break

        bet_amount = float(bet_amount)
        if bet_amount <= balance and bet_amount != 0:
            balance -= bet_amount
            print(f"Your current balance: {balance}")
            spin_result = spin_reel(bet_amount,symbols)
            display_result(spin_result)
            balance = reward_system(spin_result, bet_amount,balance)
            print(f"Your new balance: {balance}")

    except ValueError:
        print("Invalid input Please try again.")
        continue