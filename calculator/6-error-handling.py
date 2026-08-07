decider = ""
op = ["+", '-', "*", "/"]

while decider != "n":
    try:
        x = float(input("First number: "))
        y = float(input("Second number: "))
        operator = input("Operator (+, -, *, /): ")
        
        if operator not in op:
            print("Invalid operator.")
        else:
            if operator == "/":
                if y != 0:
                    result = x / y
                    print(result)
                else:
                    print("Cannot divide by zero.")
            else:
                if operator == "+":
                    result = x + y
                if operator == "-":
                    result = x - y
                if operator == "*":
                    result = x * y
                print(result)
    except ValueError:
        print("Invalid number.")
            
    decider = input("Another calculation? (y/n): ")