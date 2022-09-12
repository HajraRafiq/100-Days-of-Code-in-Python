from art import logo
import os
print(logo)

    

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculate():
    num1= float(input("Enter first number\n"))
    print("----------------------------------------")
    for op in operations:
        print(op)
    print("----------------------------------------")

    repeat = True
    while repeat:

        operation_symbol = input("Pick and operation\n")

        num2 = float(input("Enter next number\n"))
        calculation=operations[operation_symbol]
        answer = calculation(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y to continue calculating with {answer}: or type'n to start new calculation\n") == "y":
            num1=answer
        else:
            os.system('clear')
            calculate()
            repeat = False
        
calculate()