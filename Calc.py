print("Hello , This Calculator has two modes : ")
print("scientific and programming")
print("For scientific Please Enter Num 1 ")
print("For Programming Please Enter Num 2 ")
sc=int(input())
if sc==1 :
    print("Hello in Programming Mode")
    num1=int(input("Enter The First Number "))
    num2=int(input("Enter The Second Number "))
    operation=int(input("For Summation Enter 1 - For Substraction Enter 2 - For Multiplication Enter 3 - For Division Enter 4 : "))
    if operation==1:
        print("Summation = ",num1+num2)
    elif operation==2:
        print("Substraction = ",num1-num2)
    elif operation==3:
        print("Multiplication = ",num1*num2)
    elif operation==4:
        print("Division = ",num1/num2)
elif sc==2 :
    print("Hello in Scientific Mode")
    print("Please Enter The option ")
    x=int(input("For Decimal Press 1--For Binary Press 2--For Ocatl Press 3--For Hexa Press 4 : "))
    if x==1:
        n=int(input("Please Enter The Number in decimal "))
        BinNum=bin(n)
        OctNum=oct(n)
        HexNum=hex(n)
        print("your Num in bin =",BinNum[2:])
        print("your Num in oct =",OctNum[2:])
        print("your Num in Hex =",HexNum[2:])
    if x==2:
        n=input("Please Enter The Number in Binary ")
        d = int(n, base=2)
        DecNum=d
        OctNum=oct(d)
        HexNum=hex(d)
        print("your Num in dec =",DecNum)
        print("your Num in oct =",OctNum[2:])
        print("your Num in Hex =",HexNum[2:])
    if x==3:
        n=input("Please Enter The Number in Octal ")
        d = int(n, base=8)
        DecNum=d
        BinNum=bin(d)
        HexNum=hex(d)
        print("your Num in dec =",DecNum)
        print("your Num in Bin =",BinNum[2:])
        print("your Num in Hex =",HexNum[2:])
    if x==4:
        n=input("Please Enter The Number in Hexa ")
        d = int(n, base=16)
        DecNum=d
        BinNum=bin(d)
        OctNum=oct(d)
        print("your Num in dec =",DecNum)
        print("your Num in Bin =",BinNum[2:])
        print("your Num in Oct =",OctNum[2:])