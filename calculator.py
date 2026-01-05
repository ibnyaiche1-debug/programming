def calculator(a,b,operation):
    if operation=="addition" :
        return a+b
    elif operation=="soustraction" :
        return a-b
    elif operation=="division":
        return a/b
    elif operation=="multiplication":
        return a*b
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter the operation (addition, soustraction, division, multiplication): ")
result = calculator(a, b, operation)
print("The result is:", result)