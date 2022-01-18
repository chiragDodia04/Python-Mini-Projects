#Add
def add(n1, n2):
    return n1+n2
#Subtract
def subtract(n1, n2):
    return n2-n1
#Division
def divide(n1, n2):
    return n2/n1
#Multiply
def multiply(n1, n2):
    return n1*n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}
def calculator():
    num1 = float(input("first number:"))

    for symbol in operations:
       print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("pick the symbol from the list:")
        num2 = float(input("Next number:"))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"type yes to continue with {answer} or type no to start new calculation:") == "yes":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()