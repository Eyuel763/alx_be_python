first_number = int(input("Enter the first number:" ))
second_number = int(input("Enter the second number: "))
operation = (input("Choose the operation (+, -, *, /): "))

match operation:
        case '+':
            print("The result is", first_number + second_number)
        case '-':
            print("The result is", first_number - second_number)
        case '*':
            print("The result is", first_number * second_number)
        case '/':
            if second_number == 0:
                print("Division by zero error")
            else:
                print("The result is", first_number / second_number)
        case _:
            print("Invalid operator")

