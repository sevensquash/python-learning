# #functions + default arguments
# def description(username, amount, due_date):
#     print(f"Dear user: {username}")
#     print(f"Please pay: {amount} by due-date: {due_date}.")

# description("rocky",17.5,"1-2-2026")

# #keyword arguments
# def cart(total, disocunt=0, tax=0.05):
#     return total * (1 - disocunt) * (1 + tax)

# print(cart(500))

# #arbritary arguments + keyword argument
# def introduction(*args,**kwargs):
#     for arg in args:
#         print(arg)
#     print()
#     for kwarg in kwargs.values():
#         print(kwarg)
#     return 0

# print(introduction("apple", "jhon", "rabbit", address="paris", home="wonderland"))

# #itratables
# my_dictionaries = {"A":1, "B":2, "C":3}
# for key,value in my_dictionaries.items():
#     print(f"{key} = {value}")

# #memembership operators
# email = "fake@gmail.com"
# if '@' in email and '.' in email:
#     print("Valid email")
# else:
#     print("Invalid email")

# #list comprehension
# box = [x for x in range(1,11)]
# print(box)
# box1 = [y*y for y in range(1,11)]
# print(box1)
# container = ["box1", "box2", "box3"]
# box2 = [smt[3] for smt in container]
# print(box2)
# num_box = [1,2,-3,4,-5,-6]
# box3 = [num for num in num_box if num > 0]
# print(box3)
# box4 = [num for num in num_box if num < 0]
# print(box4)

# password = (
#     'q','w','e','r','t','y','u','i','o','p','a','s','d',
#     'f','g','h','j','k','l','z','x','c','v','b','n','m')
# incame = []
# message = str(input("please input your msg here."))
# print(message)
# for char in message:
#     print(char, end=" ")
#     for key in range(0,26):
#         if char == password[key]:
#             incame.append(key)
# print(" ")

# e_pass = (
#     '!','@','#','$','%','^','&',"8",'*','(',')','|','~',
#     ':',';','?','>',',','<','I','N','s','5','a','w','2w'
# )
# print("Your encrypted msg:")
# for thing in incame:
#     print(e_pass[thing], end='')

# outcame = []
# d_msg = str(input("please enter a msg to decrypt"))
# for char in d_msg:
#     for num in range(0,26):
#         if char == e_pass[num]:
#             outcame.append(num)

# print("Your decrypted msg is:")
# for index in outcame:
#     print(password[index])

# encode = {
#     'a': '!', 'b': '@', 'c': '#', 'd': '$', 'e': '%',
#     'f': '^', 'g': '&', 'h': '*', 'i': '(', 'j': ')',
#     'k': '|', 'l': '~', 'm': ':', 'n': ';', 'o': '?',
#     'p': '>', 'q': ',', 'r': '<', 's': 'I', 't': 'N',
#     'u': 's', 'v': '5', 'w': 'a', 'x': 'w', 'y': '2', 'z': 'W'
# }

# msg = "apple"

# encrypted = ""
# for c in msg:
#     encrypted += encode.get(c, c)

# print(encrypted)

# #
# msg = "banana"
# encrypt = ""
# for x in msg:
#     encrypt += encode.get(x,x)
# print(encrypt)

# #match case
# #executes a code if a value matches case
# #cleaner code lesser syntax replacement of elseif statements syntax is more reabable

# def isweekend(day):
#     match day:
#         case "sunday" | "saturday":
#             return True
#         case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
#             return False
        
# print(isweekend("monday"))

# def language(word):
#     match word:
#         case "lumiere":
#             return "light"
#         case "hambre":
#             return "hungry"
#         case "konichiwa":
#             return "hello"
# print(str(language("hambre")))
        

# #modulus 

# import math as m 
# from math import e
# print(m.pi)
# print(e)

# a,b,c,d = 1,2,3,4
# import hand as h

# result = h.square(2)
# print(result)

# def show_balance(balance):
#     print(f"Your current balance is: {balance}")

# def deposit(balance):
#     print("how much would you like to deposit")
#     put = float(input("Enter amount"))
#     if put <= 0:
#         print("No deposit action were carried out")
#         return balance
#     else:
#         balance += put
#         print(f"Your new balance is: {balance}")
#         return balance

# def withdraw(balance):
#     if balance <= 0:
#         print("You are broke")
#         return balance
#     else:
#         take = float(input("How much would you like to withdraw"))
#         if take <= balance:
#             balance -= take
#             print(f"Your withdrawed {take} and your new balance is: {balance}")
#             return balance
#         else:
#             print(f"at your current balance you can withdraw max {balance}")
#             print(f"if you like to withdraw your max balance then press yes")
#             choice = str(input("yes?"))
#             if choice.lower() == "yes":
#                 print(f"your have withdrawn {balance}")
#                 balance = 0
#                 print("")
#                 return balance

# def option(result, balance):
#         match result:
#             case 1:
#                 balance = deposit(balance)
#             case 2:
#                 balance = withdraw(balance)
#             case 3:
#                 show_balance(balance)
#             case 4:
#                 print("Thank you for banking with us.")
#                 return balance, False
#             case _:
#                 print("Please enter num from option only.")
#         return balance, True

# balance = 0
# isrunning = True

# while isrunning:
#     print("welcome to archi bank")
#     print("1.deposit 2.withdraw 3.show_balance 4.quit")
#     try:
#         result = int(input("Please enter option number."))
#         balance, isrunning = option(result, balance)
#     except ValueError:
#         print("Invalid input please enter a num")

#slut machine 
# import random
# def spin():
#     symbols = ['🍒','🔔','🏆','💎','🌟']
#     return [random.choice(symbols) for _ in range(3)]
# def printing(result):
#     print(f"{result[0]},{result[1]},{result[2]}")
# def reward(result,bet):
#     if result[0] == result[1] and result[1] == result[2]:
#         print("Jackpot")
#         return bet*3
#     elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
#         print("congratulations")
#         return bet*2
#     else:
#         print("You lost the bet")
#         return 0

# def main():
#     balance = 100
#     betting = True
#     while betting:
#         print("Welcome to slot machine")
#         print("Press q to quit")
#         try:
#             bet = str(input("Please enter your bet"))
#             if bet == "q" or bet == "Q":
#                 break
#             bet = float(bet)
#             if bet <= 0 or bet > balance:
#                 print("Insufficient funds")
#                 continue
            
#             print(f"You betted ${bet}")
#             balance -= bet
#             print(f"Your new balance is: {balance}")
#             result = spin()
#             printing(result)
#             balance += reward(result,bet)
#             print(f"Your current balance is: {balance}")
#         except ValueError:
#             print("Invalid input")

# if __name__ == "__main__":
#     main()


#slot machine 
# import random 
# def give_prize(spin_result,bet,balance):
#     if spin_result[0] == spin_result[1] and spin_result[1] == spin_result[2]:
#         print("Jackpot")
#         return balance + (bet * 3)
#     elif spin_result[0] == spin_result[1] or spin_result[1] == spin_result[2] or spin_result[0] == spin_result[2]:
#         print("congratulations")
#         return balance + (bet * 2)
#     else:
#         print("You lose!")
#         return balance

# def show_spin_result(spin_result):
#     print(" | ".join(spin_result))
# def do_spin():
#     symbols = ['🍒','🔔','🏆','💎','🌟']
#     return [random.choice(symbols) for _ in range(3)]

# balance = 100
# isrunning = True 

# while isrunning:
#     print("----------------------------")
#     print("welcome to slut machine")
#     print("----------------------------")
#     symbols = ['🍒','🔔','🏆','💎','🌟']

#     try:
#         bet = str(input("Place your bet"))

#         bet = float(bet)
#         if bet <= 0 or bet > balance:
#             print("Insufficient funds moving to next round")
#             continue
#         balance -= bet
#         print(f"Your current balance is: {balance}")

#         spin_result = do_spin()

#         show_spin_result(spin_result)

#         print("before prize")
#         balance = give_prize(spin_result,bet,balance)
#         print("After prize")
#         print(f"Your new balance is: {balance}")

#     except ValueError:
#         print("Invalid input")

#encryption and decryption 

# import random 
# import string 

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()
# random.shuffle(key)
# print(f"chars: {chars}")
# print(f"key: {key}")

# #encrypt

# plain_word = str(input("How message would you like to encrypte."))
# cipher_text = ""
# for letter in plain_word:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"Your original msg: {plain_word}")
# print(f"Your encrypted msg: {cipher_text}")

# #decrypt 

# encrypted_text = str(input("what message would you like to decrypt"))
# dichiper_text = ""
# for letter in encrypted_text:
#     index = key.index(letter)
#     dichiper_text += chars[index]

# print(f"text dechiphered: {dichiper_text}")

# import random

# hangman = {
#     0:("   ",
#        "   ",
#        "   "),
#     1:(" o ",
#        "   ",
#        "   "),
#     2:(" o ",
#        " | ",
#        "   "),
#     3:(" o ",
#        "/| ",
#        "   "),
#     4:(" o ",
#        "/|\\",
#        "   "),
#     5:(" o ",
#        "/|\\",
#        "/  "),
#     6:(" o ",
#        "/|\\",
#        "/ \\"),}

# incorrect_guess = 0
# guesses = 0
# words = ["apple","timber","bear","propane","aromatic","centripetal"]

# sentence_to_guess = random.choice(words)

# hidden_word = ["_"] * len(sentence_to_guess)
# guessed_letter = []

# for i in hangman[incorrect_guess]:
#     print(i)

# for i in hidden_word:
#     print(i, end= " ")

# print("\n")

# while incorrect_guess < 7:
#     guess_letter = str(input("Guess a letter: "))
#     if guess_letter in guessed_letter:
#         print("You have already guess that letter retry!")
#         continue
#     guesses += 1
#     guessed_letter.append(guess_letter)
#     if guess_letter in sentence_to_guess:
#         for i in range(len(sentence_to_guess)):
#             if guess_letter == sentence_to_guess[i]:
#                 hidden_word[i] = guess_letter
#     else:
#         incorrect_guess += 1
#         print("You guessed wrong!")

#     for i in hangman[incorrect_guess]:
#         print(i)
#     for i in hidden_word:
#         print(i, end= " ")
#     print("\n")

#     if hidden_word == list(sentence_to_guess):
#         print("Congratulations")
        
#         break
#     elif incorrect_guess == 6:
#         print("You lost the game")
#         break
# print(f"you guesses: {guesses} times.")
# print(f"you incorrect guesses: {incorrect_guess}")
# print("Letters you guessed:")
# print(",".join(guessed_letter))

#revisio encryption 

# import random 
# import string 

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()
# #why when I assigned shuffled value to key it returns none
# #key = random.shuffle(key)
# random.shuffle(key)

# #encryption 

# plain_text = str(input("What secret message would you like to encrypt: "))
# encrypted_text = ""
# for letter in plain_text:
#     index = chars.index(letter)
#     encrypted_text += key[index]

# print(f"Your encrypted text: {encrypted_text}")

# #decryption 

# dichiper_text = str(input("what message would you like to dichiper: "))
# decrpted_text = ""
# for letter in dichiper_text:
#     index = key.index(letter)
#     decrpted_text += chars[index]

# print(f"Your decrypted text: {decrpted_text}")

#revision banking system 

# def deposit_cash(balance):
#     deposit_amount = float(input("How much amount would you like to deposit: "))
#     if deposit_amount <= 0:
#         print("Invalid deposit amount")
#         return balance
#     else:
#         new_balance = balance + deposit_amount
#         print(f"Your new balance is: {new_balance}")
#         return new_balance

# def withdraw_cash(balance):
#     withdraw_amount = float(input("How much would you like to withdraw: "))
#     if withdraw_amount > balance  or withdraw_amount <=0:
#         print("Invalid amount")
#         return balance
#     else:
#         new_balance = balance - withdraw_amount
#         print(f"Your new balance is: {new_balance}")
#         return new_balance
    
# def show_balance(balance):
#     print(f"Your current balance: {balance}")

# def option(balance, action):
#     match(action):
#         case 1:
#             show_balance(balance)
#         case 2:
#             balance = deposit_cash(balance)
#         case 3:
#             balance = withdraw_cash(balance)
#         case 4:
#             print("Thank you for banking with us.")
#             return balance, False
#         case _:
#             print("Please choose form option 1-4")
#     return balance, True

# BALANCE = 0
# balance = BALANCE
# isrunning = True 

# while isrunning:
#     print("Welcome to archi bank.")
#     print("1.show balance, 2.deposit cash, 3.withdraw cash, 4.quit")
#     try:
#         action = int(input("choose your action: "))
#         balance, isrunning = option(balance, action)
#     except ValueError:
#         print("Invalid input. Please try again")
#         continue


#slut machine 
# import random
# def display_result(spin_result):
#     print("|".join(spin_result))

# def spin_reel(bet_amount,symbols):
#     return [random.choice(symbols) for _ in range(3)]

# def reward_system(spin_result,bet_amount,balance):
#     if spin_result[0] == spin_result[1] and spin_result[1] == spin_result[2]:
#         print("Jackpot")
#         return balance + bet_amount * 3
#     elif spin_result[0] == spin_result[1] or spin_result[1] == spin_result[2] or spin_result[0] == spin_result[2]:
#         print("Congratulations")
#         return balance + bet_amount * 2
#     else:
#         print("You lost.")
#         return balance

# BALANCE = 100
# balance = BALANCE
# isrunning = True

# while isrunning:
#     print("Welcome to archi cashino.")
#     symbols = ['🍒','🔔','🏆','💎','🌟']
#     print("|".join(symbols))
#     print("Spin reel or press 'Q' to quit")
#     print(f"Your balance: {balance}")
#     try:
#         bet_amount = str(input("How much would you like to bet."))
#         if bet_amount.lower() == "q":
#             print("Thank you for playing with us.")
#             isrunning = False
#             break

#         bet_amount = float(bet_amount)
#         if bet_amount <= balance and bet_amount != 0:
#             balance -= bet_amount
#             print(f"Your current balance: {balance}")
#             spin_result = spin_reel(bet_amount,symbols)
#             display_result(spin_result)
#             balance = reward_system(spin_result, bet_amount,balance)
#             print(f"Your new balance: {balance}")

#     except ValueError:
#         print("Invalid input Please try again.")
#         continue

# import random 
# spaces = [" "," "," "," "," "," "," "," "," "]
# isrunning = True 
# human_symbol = "O"
# computer_symbol = "X"
# def Check_winner(spaces):
#     if spaces[0] != " " and spaces[0] == spaces[1] == spaces[2]:
#         print(f"Winner: {spaces[0]}")
#         return False
#     elif spaces[3] != " " and spaces[3] == spaces[4] == spaces[5]:
#         print(f"Winner: {spaces[3]}")
#         return False
#     elif spaces[6] != " " and spaces[6] == spaces[7] == spaces[8]:
#         print(f"Winner: {spaces[6]}")
#         return False
#     elif spaces[0] != " " and spaces[0] == spaces[4] == spaces[8]:
#         print(f"Winner: {spaces[0]}")
#         return False
#     elif spaces[2] != " " and spaces[2] == spaces[4] == spaces[8]:
#         print(f"Winner: {spaces[2]}")
#         return False
#     elif spaces[0] != " " and spaces[0] == spaces[3] == spaces[6]:
#         print(f"Winner: {spaces[0]}")
#         return False
#     elif spaces[1] != " " and spaces[1] == spaces[4] == spaces[7]:
#         print(f"Winner: {spaces[1]}")
#         return False
#     elif spaces[2] != " " and spaces[2] == spaces[5] == spaces[8]:
#         print(f"Winner: {spaces[2]}")
#         return False
#     elif " " not in spaces:
#         print("It's a tie!")
#         return False
#     return True

# def computer_turn(spaces):
#     available_space = [index for index,space in enumerate(spaces) if space == " "]
#     if spaces.count(" ") != 0:
#         spaces[random.choice(available_space)] = computer_symbol
#         if " " not in spaces:
#             return False
#         else:
#             return True
#     else:
#         print("Board full cannot move anymore")
    

# def human_turn(spaces):
#     if " " not in spaces:
#         return False
#     print(f"Places available: ")
#     for index, space in enumerate(spaces):
#         if space == " ":
#             print(index + 1, end= " ")
#     print("\n")
#     retry = True
#     while retry:
#         try:
#             human_input = int(input("Please enter where would you like to place: ")) 
#             #impossible conditon human_input > 9 and human_input <= 0
#             if human_input > 9 or human_input <= 0:
#                 print("Please choose only form available space.Retry!")
#             else:
#                 human_input -= 1
#                 if spaces[human_input] != " ":
#                     print("Place taken. retry!")
#                     retry = True
#                 else:
#                     spaces[human_input] = human_symbol
#                     retry = False
#                     return True
#         except ValueError:
#             print("Invalid input")
#             continue

                
# def display_board(spaces):
#     print(" | | ")
#     print(f"{spaces[0]}|{spaces[1]}|{spaces[2]}")
#     print("_|_|_")
#     print(" | | ")
#     print(f"{spaces[3]}|{spaces[4]}|{spaces[5]}")
#     print("_|_|_")
#     print(" | | ")
#     print(f"{spaces[6]}|{spaces[7]}|{spaces[8]}")
     

# while isrunning:
#     display_board(spaces)
#     isrunning = human_turn(spaces)
#     isrunning = Check_winner(spaces)
#     if not isrunning:
#         display_board(spaces)
#         break
#     isrunning = computer_turn(spaces)
#     isrunning = Check_winner(spaces)
#     if not isrunning:
#         display_board(spaces)
#         break
#     print("\n")

    
#Object oriented programming 

# class Car:
#     wheels = 4 
#     def __init__(self,model,year,color,for_sale):
#         self.car_name = model 
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

#     def drive(self, fruit):
#         print(f"This car {self.car_name} can drive")
#     def honk(self):
#         print("This car can honk.")

# Car1 = Car("Mustang",2025,"Blue",False)
# print(Car1.car_name)
# print(Car.wheels)

# name = "jhon"
# Car.joke = name
# print(Car.joke)

#chat-gpt challenge

# class Dog:
#     brithday = 2
#     def __init__(self,name,age,breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def info(self):
#         print(f"{self.name} name is {self.name}")
#     def bark(self):
#         print(f"{self.name} can bark!")
#     def brithday(self):
#         print(f"{self.name} brithday is in: {self.brithday} ")

# class Dog:
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def info(self):
#         print(f"{self.name} is {self.age} years old")

#     def bark(self):
#         print(f"{self.name} can bark!")

#     def birthday(self):
#         self.age += 1
#         print(f"{self.name} is now {self.age} years old")

# Dog1 = Dog("Rufus",3,"Golden retriver")
# print(Dog1.name)
# Dog1.age = 5
# print(Dog1.age)
# print(Dog1.breed)
# Dog1.info()
# Dog1.bark()
# Dog1.birthday()

# Dog2 = Dog("Benzene",3,"husky")
# print(Dog2.name)
# print(Dog2.age)
# print(Dog2.breed)
# Dog2.info()
# Dog2.bark()
# Dog2.birthday()

#decorators
