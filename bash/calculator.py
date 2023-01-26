print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")

choice= input("Enter your choice from above (1-4): ")

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

else:
    print("Invalded Choice: Try again")