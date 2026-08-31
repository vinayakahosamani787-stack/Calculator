print("====Calculator====")
def menu():
    print("1. Addition\n2. Subraction\n3. Multiplication\n4. Division\n5. Exit\n")
def add(a,b):
    sum=a+b
    return sum
def sub(a,b):
    diff=a-b
    return diff
def Mul(a,b):
    mul=a*b
    return mul
def Div(a,b):
    try:
        div=a/b
        print(f"Division:{div}")
    except ZeroDivisionError:
        print("Divison by zero is not possible")
    else:
        print("No error")
    finally:
        print("End")
while True:
    menu()
    choice=int(input("Enter your choice: "))
    if choice==5:
        print("Exit")
        break
    if choice in [1,2,3,4]:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        if choice==1:
            print(f"Addition:{add(a,b)}")
        elif choice==2:
            print(f"Subtraction:{sub(a,b)}")
        elif choice==3:
            print(f"Multiplication:{Mul(a,b)}")
        elif choice==4:
                Div(a,b)
    else:
        print("Invalid choice")


        
         

           
