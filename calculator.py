import os
def add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations_dict={
    "+":add,
    "-":Subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1 = float(input("enter the first number:"))
    for Symbol in operations_dict:
        print(Symbol)
    continue_flag = True
    while continue_flag:
        op_symbol = input("pick an ooperation :")
        number2 = float(input("enter the next number:"))
        calculator_function = operations_dict[op_symbol]
        output = calculator_function(number1, number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        Should_continue = input(f"enter the 'y to continue calculation with {output} or 'n' to start a new calculation or 'x' to  exit :").lower()
        if Should_continue == 'y':
            number1 = output
        elif Should_continue == 'n':
            Should_continue==False
            os.system('cls')
            calculator()
        else:
            continue_flag = False
            print("thank's  for choosing this calculator")


calculator()



