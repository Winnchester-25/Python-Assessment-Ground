# Asking user fir teh first number and converting it to float
num1 = float(input("Enter first number: "))

# Asking user for the second number and converting it to float
num2 = float(input("Enter second number: "))

# Asking user for the operation to be performed
operation = input("Enter the operation to be performed (+, -, *, /): ")

# Performing the operation based on the user input
if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)  

elif operation == "/":
    print(num1 / num2)