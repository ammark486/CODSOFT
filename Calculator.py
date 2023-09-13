def Calculator():
    print("----------------------------CALCULATOR---------------------------------")
    Num1= float(input("Enter First Number: \n"))
    Option=input("Enter your Operation ( + , - , * , / ): \n")
    Num2= float(input("Enter Second Number: "))

    match Option:
        case "+":
            print("Sum of Two numbers are: " + str(Num1 + Num2))
        case "-":
            print("Difference of Two numbers are: " + str(Num1 - Num2))  
        case "/":
            if(Num2!=0):
                print("devision of Two numbers are: " + str(Num1 / Num2))
            else:
                print("Error: Division by zero is not allowed.") 
        case "*":
            print("multiply of Two numbers are: " + str(Num1 * Num2)) 
        case _:
            print("Error: Enter a correct operation!! ") 
        
Calculator()
                  