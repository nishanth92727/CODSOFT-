print("Welcome to Nishanth's Calculator")

operation = input("Enter the operation to perform (+, -, *, /): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"

print("Result:", result)
