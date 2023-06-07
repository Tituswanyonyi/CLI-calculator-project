import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def calculate(operator, operand1, operand2):
    if operator in operators:
        return operators[operator](operand1, operand2)
    else:
        raise ValueError("Invalid operator")


def main():
    print("CLI Calculator")
    print("==============")

    while True:
        try:
            operator = input("Enter operator (+, -, *, /): ")
            if operator == 'q':
                break
            operand1 = float(input("Enter first operand: "))
            operand2 = float(input("Enter second operand: "))

            result = calculate(operator, operand1, operand2)

            print("Result:", result)

        except ValueError as e:
            print("Error:", str(e))
        except ZeroDivisionError:
            print("Error: Division by zero")


if __name__ == '__main__':
    main()
