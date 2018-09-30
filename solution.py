def arithmetic(a, b, operand):
    if operand == '+':
        return a + b
    elif operand == '-':
        return a - b
    elif operand == '*':
        return a * b
    elif operand == '/':
        if b != 0:
            return a / b
        
        return 'Error'
    else:
        return 'Unknown operation'


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operand = input('Enter operand: ')

print('Result: ', arithmetic(num1, num2, operand))