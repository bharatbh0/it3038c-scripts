while True:
    print("Calculator ")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("5 for Exponentiation")
    print("6 for Quit")

    choice = input("Enter your choice from above (1-6): ")

    if choice == "6":
        print("Shutting down...")
        break

    # int only lets the user use whole number
    num1 = int(input("Enter your First choice: "))
    num2 = int(input("Enter your Second choice: "))

    # Check the users choice
    if choice == "1":
        print(num1, "+", num2,)
        print("Answer is", (num1+num2))

    elif choice == "2":
        print(num1, "-", num2)
        print("Answer is", (num1-num2))

    elif choice == "3":
        print(num1, "*", num2)
        print("Answer is", (num1*num2))

    elif choice == "4":
        if num2 == 0.0:  # Can't divide by 0
            print("Divide by 0 Error")
        else:
            print(num1, "/", num2)
            print("Answer is", (num1/num2))

    elif choice == "5":
        print("{} ** {} ={}". format(num1, num2, num1**num2))
        print("Answer is", (num1**num2))

    else:
        print("Invalded Choice: Try again")

    a = input("Tap Enter to continue:")
