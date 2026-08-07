decider = ""

while decider != "n":
    x = float(input("First number: "))
    y = float(input("Second number: "))
    operator = input("Operator (+, -, *, /): ")
    if operator == "+":
        result = x + y
    if operator == "-":
        result = x - y
    if operator == "*":
        result = x * y
    if operator == "/":
        result = x / y
    print(result)
    decider = input("Another calculation? (y/n): ")
    
