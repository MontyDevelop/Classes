# condition

# on the basis of conditions our code has to take decisions

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation you want '+','-','*','/'")

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num2 - num1)
elif operation == '*':
    print(num2 * num1)
elif operation == '/':
    print(num1 / num2)