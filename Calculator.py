


while True:
    num1 = float(input("Enter First number:"))
    num2 = float(input("Enter Second number:"))
    

    while True:
        operator = input("Enter operator (+, -, *, /):")

        if operator not in ['+', '-', '*', '/']:
            print ("Invalid operator!")
            continue

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2 

        print("Result:", result)
        continue_calc = input("Do another Calculation? (y/n)")
        if continue_calc.lower() != 'y':
            break