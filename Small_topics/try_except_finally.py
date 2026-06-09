# return doesnt stop finally

def calculator(operator,num1,num2):
    match(operator):
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '/':
            return num1 / num2
        case '*':
            return num1 * num2
        case '%':
            # % means how much is left over also remainder
            return num1 % num2
        case _:
            return "something went wrong"
try:
    operator = str(input("what operaotr you like to use: "))
    num1 = float(input("what is num1: "))
    num2 = float(input("what is num2: "))
    result = calculator(operator,num1,num2)
    print(result)
except ZeroDivisionError:
    print("zero division error")
except ValueError:
    print("Data type input invalid")
finally:
    print("Program finsihed!")
