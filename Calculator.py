while(True):
    print("Hi,Welcome to the python calculator")
    print("1.Addition(+)")
    print("2.Subtraction(-)")
    print("3.Multiplication(*)")
    print("4.Division(/)")
    print("5.power(**)")
    print("6.Exit")

    choice=input("Choose an option (1-6):..")

    if(choice=="6"):
        print("Thank you for using the calculator. Goodbye!")
        break
    try:
        num1=float(input("Enter a number:.."))
        num2=float(input("Enter another number:.."))
        print("Your numbers are:",num1,"and",num2)

        if(choice=="1"):
            print("your answer is:",num1+num2)
        elif(choice=="2"):
            print("your answer is:",num1-num2)
        elif(choice=="3"):
            print("your answer is:",num1*num2)
        elif(choice=="4"):
            print("your answer is:",num1/num2)
        elif(choice=="5"):
            print("your answer is:",num1**num2)
        else:
            print("Invalid operation")
        
        Extra=input("Do you want to continue? (y/n):..")
        if(Extra=="n"):
            break
        elif(Extra=="y"):
            continue
        else:
            print("Invalid input.Restarting the calculater")
    
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")