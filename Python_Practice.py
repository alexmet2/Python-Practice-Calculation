def MyDivision(x,y):
    print("Doing the division")
    return (x/y)
def MyMultiplication(x,y):
    print("Doing the multiplication")
    return (x*y)
def MySubtraction(x,y):
    print("Doing the subtraction")
    return (x-y)
def MyAddition(x,y):
    print("Doing the addition")
    return (x+y)
def MyMenu():
    print("This is the menu")
    print("Press 1 for addition")
    print("Press 2 for substraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    choice = input("What is your choise?")
    return choice
def MyCalculation():
    ch = MyMenu()
    num1 = int (input ("Enter your first number"))
    num2 = int (input ("Enter your second number"))
    if ch == 1:
        result = MyAddition(num1,num2)
    elif ch == 2:
        result = MySubtraction(num1,num2)
    elif ch == 3:
        result = MyMultiplication(num1,num2)
    elif ch == 4:
        result = MyDivision(num1,num2)
    print("Your result is ",result)
MyCalculation()
