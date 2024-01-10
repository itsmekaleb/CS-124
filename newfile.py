while True:
    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

   
    choice = input("Enter your choice (1-5): ")

   
    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Result: ", result)
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Result: ", result)
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Result: ", result)
    elif choice == '4':
        num1 = float(input("Enter dividend: "))
        num2 = float(input("Enter divisor: "))
        if num2 != 0:
            result = num1 / num2
            print("Result: ", result)
        else:
            print("Error: Cannot divide by zero.")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
