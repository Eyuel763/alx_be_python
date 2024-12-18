first_number = int(input("Enter the first number:" ))
second_number = int(input("Enter the second number: "))
operator = (input("Choose the operation (+, -, *, /): "))

match operator:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number
        case "/":
            if second_number == 0:
                result = "Division by zero error"
            else:
                result = first_number / second_number
        case _:
            result = "Invalid operator"

print("The result is", result)