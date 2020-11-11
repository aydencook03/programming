def divide(first,second):
    while True:
        try:
            final = float(first)/float(second)
            break
        except ZeroDivisionError:
            print("Can't Divide By Zero")
            second = input("Enter Second Number: ")
    secondNum = second
    return final

while True:
    firstNum = input("Enter a Number: ")
    secondNum = input("Enter a Second Number: ")
    operation = input("Add(+), Subtract(-), Multiply(*), or Divide(/)? ")
    if operation == "+":
        result = float(firstNum) + float(secondNum)
    elif operation == "-":
        result = float(firstNum) - float(secondNum)
    elif operation == "*":
        result = float(firstNum) * float(secondNum)
    elif operation == "/":
        result = divide(firstNum,secondNum)
    print(firstNum + ' ' + operation + ' ' + secondNum + ' = ' + str(result))
    break
