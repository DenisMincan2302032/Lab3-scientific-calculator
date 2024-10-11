import math
from math import sin, cos, tan
def add():
    number = float(input("Please enter the first number to your addition:"))
    number1 = float(input("Plese enter the second number to your addition:"))
    numresult = number + number1 
    print("Your operation result is", numresult)



def subtract():
    subnum = float(input("Please enter the first number to your subtraction:"))
    subnum1 = float(input("Please enter the second number to your subtraction:"))
    subresult = subnum + subnum1
    print("Your operation result is", subresult)


def multiply():
    multnumber = float(input("Please enter the first number to your multiplication:"))
    multnumber1 = float(input("Please enter the second number to your multiplication:"))
    multresult = multnumber * multnumber1
    print("Your operation result is", multresult)

def div():
    divnum = float(input("Please enter the first number to your division:"))
    divnum1 = float(input("Please enter the second number to your division:"))
    try:
        print(divnum/divnum1)
    except ZeroDivisionError:
        print("Error. It is mathematically impossible to divide by zero.")

def square():
    squarenum = float(input("Please enter the number to find the square root for:"))
    squareresult = math.sqrt(squarenum)
    print("The result of your operation is", squareresult)



def sin():
    sin_number = float(input("Please enter the number for your sin operation:"))
    sin_number_radian = math.radians(sin_number)
    sin_result = math.sin(sin_number_radian)
    print("The sine of", sin_number, "is", sin_result)

def cos():
    cos_number = float(input("Please enter the number for your cos operation:"))
    cos_number_radian = math.radians(cos_number)
    cos_result = math.cos(cos_number_radian)
    print("The cosine of", cos_number, "is", cos_result)


def tan():
    tan_number = float(input("Please enter the number for your tan operation:"))
    tan_number_radian = math.radians(tan_number)
    tan_result = math.tan(tan_number_radian)
    print("The tangent of", tan_number, "is", tan_result)


def log():
    loginput = float(input("Enter the number you would like to find the logarithmics of:"))
    logbase = float(input("Enter the base of your logarithmics:"))
    logresult = math.log(loginput, logbase)
    print("The logarithmic of", loginput, "with a base of", logbase, "is", logresult)

def main_menu():
    while True:
        print("Welcome to the Scientific Calculator Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Sine")
        print("7. Cosin")
        print("8. Tangent")
        print("9. Logarithmics")
        userchoice = input("Enter your choice")
        if userchoice == "1":
            add()
        elif userchoice == "2":
            subtract()
        elif userchoice == "3":
            multiply()
        elif userchoice == "4":
            div()
        elif userchoice == "5":
            square()
        elif userchoice == "6":
            sin()
        elif userchoice == "7":
            cos()
        elif userchoice == "8":
            tan()
        elif userchoice == "9":
            log()
        else:
            print("Invalid option, try again")
            continue
        exit = input("Would you like to exit the program? y/n")
        if exit == "y":
            print("Goodbye")
            break
        else:
            continue

main_menu()



