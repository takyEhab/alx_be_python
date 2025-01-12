def perform_operation(num1: float , num2: float, operation: str):
    match operation:
        case "add":
            answer = num1 + num2
        case "subtract":
            answer = num1 - num2
            print(f"The result is {num1 - num2}.")
        case "multiply":
            answer = num1 * num2
            print(f"The result is {num1 * num2}.")
        case "divide":
            if num2 == 0:
                return "Cannot divide by zero."
            answer = num1 / num2
            print(f"The result is {num1 / num2}.")
        case _:
            answer = "Invalid operation."
            print("Invalid operation.")
    return answer