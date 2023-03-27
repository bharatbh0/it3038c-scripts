while True:
    print("Calculator ")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("5 for Exponentiation")

    choice= input("Enter your choice from above (1-5): ")

    #int only lets the user use whole number
    num1 = int(input("Enter your First choice: "))
    num2 = int(input("Enter your Second choice: "))

    #Check the users choice 
    if choice == "1":
        print(num1,"+", num2,)
        print("Answer is", (num1+num2))

    elif choice == "2":
        print(num1,"-", num2)
        print("Answer is", (num1-num2))

    elif choice == "3":
        print(num1,"*", num2)
        print("Answer is", (num1*num2))

    elif choice == "4":
        if num2 == 0.0:     #Can't divide by 0
            print("Divide by 0 Error")
        else:
            print(num1,"/", num2)
            print("Answer is", (num1/num2))

    elif choice == "5":
        print("{} ** {} ={}". format(num1,num2,num1**num2))
        print("Answer is", (num1**num2))

    else:
        print("Invalded Choice: Try again")
    a = input("continue? (Y/N): ")
    if a == "Y":
        choice()
    elif a == "N":
        print("Shutting down...")
        break
    else:
        print("Invalied input")
        break
