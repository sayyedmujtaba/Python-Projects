import time
print("=== Welcome to DMAS calculator ===")
print("Write an expression or 'q' to quit: ")

while True:
    expression = input("\nWrite an input: ")
    if expression == "q":
        print("Quitting...")
        time.sleep(1) # will delay the next line by 1 second
        print("Goodbye!")
        break
    try:
        result = eval(expression) #eval(): a built-in function that evaluates a string as BODMAS expression
        print(f"Result: {result}")
    except ZeroDivisionError: # raise an exception for dividing by zero
        print("Expression can't be divided by zero.")
    except Exception:
        print("Invalid expression.")