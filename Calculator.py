print("A Simple Calculator (CLI)")
while True:
    while True: 
        try:
            n1=float(input("Enter number 1:"))
            break
        except ValueError:
            print("Invalid input")
            
    while True: 
        try:
            n2=float(input("Enter number 2:"))
            break
        except ValueError:
            print("Invalid input")
    
    while True: 
        op=input("Enter operation(+,-,*,/):")
        if op not in ["+","-","/","*"]:
            print("Invalid")
        else: 
            break
            
    if op=="+":
        result=n1+n2
    elif op=="-":
        result=n1-n2
    elif op=="*":
        result=n1*n2
    elif op=="/":
        if n2!=0:
            result=round(n1/n2,2)
        else:
            result="Error: Divison by Zero!"
    else:
        result="Invalid"
    print("Result:",result)
    while True:
        check=input("Do you wanna Continue(n/y):").lower()
        if check in ["n","no"]:
            exit()
        elif check in ["y","yes"]:
            break
    