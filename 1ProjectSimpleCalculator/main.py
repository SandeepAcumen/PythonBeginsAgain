try:

    a = int(input("Enter the first number : "))
    b = int(input("Enter the Second number : "))

    print("If you want Addition press +\nIf you want Subtration press -\nIf you want multiplication press *\nIf you want DIvition press /\n")
    
    o = input(("Enter the Operator : "))
    match o:
        case "+":
            print(f"The result of addition is  {a +b}  ")

        case "-":
            print(f"The result of sutration is {a -b}")

        case "*":
            print(f"The result of multiplication is  {a * b}")

        case "/":
            print(f"The dicition is {a / b}")

        case default:
            print("Enter wrong operator")
        
        
except Exception as e:
    print("Enter the valid code")
