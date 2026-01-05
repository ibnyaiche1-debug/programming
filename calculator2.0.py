def calculator(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."
    except Exception as e:
        return f"Invalid input: {e}"

# User input
expression = input("Enter the operation (e.g., 5 + 3, 10 / 2): ")

result = calculator(expression)
print(f"Result: {result}")

