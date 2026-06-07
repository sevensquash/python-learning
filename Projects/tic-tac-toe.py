import random 

spaces = [" "," "," "," "," "," "," "," "," "]
isrunning = True 
human_symbol = "O"
computer_symbol = "X"

def Check_winner(spaces):
    if spaces[0] != " " and spaces[0] == spaces[1] == spaces[2]:
        print(f"Winner: {spaces[0]}")
        return False
    elif spaces[3] != " " and spaces[3] == spaces[4] == spaces[5]:
        print(f"Winner: {spaces[3]}")
        return False
    elif spaces[6] != " " and spaces[6] == spaces[7] == spaces[8]:
        print(f"Winner: {spaces[6]}")
        return False
    elif spaces[0] != " " and spaces[0] == spaces[4] == spaces[8]:
        print(f"Winner: {spaces[0]}")
        return False
    elif spaces[2] != " " and spaces[2] == spaces[4] == spaces[8]:
        print(f"Winner: {spaces[2]}")
        return False
    elif spaces[0] != " " and spaces[0] == spaces[3] == spaces[6]:
        print(f"Winner: {spaces[0]}")
        return False
    elif spaces[1] != " " and spaces[1] == spaces[4] == spaces[7]:
        print(f"Winner: {spaces[1]}")
        return False
    elif spaces[2] != " " and spaces[2] == spaces[5] == spaces[8]:
        print(f"Winner: {spaces[2]}")
        return False
    elif " " not in spaces:
        print("It's a tie!")
        return False
    return True

def computer_turn(spaces):
    available_space = [index for index,space in enumerate(spaces) if space == " "]
    if spaces.count(" ") != 0:
        spaces[random.choice(available_space)] = computer_symbol
        if " " not in spaces:
            return False
        else:
            return True
    else:
        print("Board full cannot move anymore")
    

def human_turn(spaces):
    if " " not in spaces:
        return False
    print(f"Places available: ")
    for index, space in enumerate(spaces):
        if space == " ":
            print(index + 1, end= " ")
    print("\n")
    retry = True
    while retry:
        try:
            human_input = int(input("Please enter where would you like to place: ")) 
            #impossible conditon human_input > 9 and human_input <= 0
            if human_input > 9 or human_input <= 0:
                print("Please choose only form available space.Retry!")
            else:
                human_input -= 1
                if spaces[human_input] != " ":
                    print("Place taken. retry!")
                    retry = True
                else:
                    spaces[human_input] = human_symbol
                    retry = False
                    return True
        except ValueError:
            print("Invalid input")
            continue

                
def display_board(spaces):
    print(" | | ")
    print(f"{spaces[0]}|{spaces[1]}|{spaces[2]}")
    print("_|_|_")
    print(" | | ")
    print(f"{spaces[3]}|{spaces[4]}|{spaces[5]}")
    print("_|_|_")
    print(" | | ")
    print(f"{spaces[6]}|{spaces[7]}|{spaces[8]}")
     

while isrunning:
    display_board(spaces)
    isrunning = human_turn(spaces)
    isrunning = Check_winner(spaces)
    if not isrunning:
        display_board(spaces)
        break
    isrunning = computer_turn(spaces)
    isrunning = Check_winner(spaces)
    if not isrunning:
        display_board(spaces)
        break
    print("\n")