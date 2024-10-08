def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: Division by zero'


def calculator():
    operation = input('Enter the operation ( +, -, *, / ): ')
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    result = 0

    if operation == '+':
        result = add(num1, num2)

    elif operation == '-':
        result = subtract(num1, num2)

    elif operation == '*':
        result = multiply(num1, num2)

    elif operation == '/':
        result = divide(num1, num2)

    else:
        print('Error: Invalid operation!')

    print(f'Result: {result}')


calculator()