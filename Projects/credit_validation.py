def fix(value):
    return (value//10) + (value%10)

def luhn_method(card_num):
    total = 0 
    for index, value in enumerate(reversed(card_num)):
        if value == " ":
            continue

        value = int(value)

        if index % 2 == 0:
            total += value
        else:
            value = value*2
            if value > 9:
                total += fix(value)
            else:
                total += value
    return total

while True:
    try:
        card_num = input("Card number: ")
        result = luhn_method(card_num)
        if result % 10 == 0:
            print("Valid")
        else:
            print("Invalid")
        break
    except ValueError:
        print("Value error")
        continue