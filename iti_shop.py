Products=[
'Apple', 
'Banana', 
'Cherry'
]


price= {
'Apple' : 40,
'Banana': 30,
'Cherry': 70,
}


Quantity= {
'Apple' : 200,
'Banana': 150,
'Cherry': 95,
}
h=1
print("----------------------------")
print("Hello in ITI Shop : ")
while h:
    print('For Owner Menu press number    1')
    print('For Customer Menu press number 2')
    print('For Exit press number          0')
    condition=int(input())
    if condition==1:
        print("----------------------------")
        print("Hello Owner")
        print("Add new products           press 1")
        print("Check Products Prices      press 2")
        print("Check Products Quantity    press 3")
        print("Change cost                press 4")
        print("to exist                   press 0")
        condition1=int(input())
        if condition1==1:
            n1=input("Please Enter The Name of Item : ")
            p1=int(input("Please Enter The price of Item : "))
            p2=int(input("Please Enter The Quantity of Item : "))
            price[n1]=p1
            Quantity[n1]=p2
            Products.append(n1)
            print("Successfully Added")
            print("----------------------------")
            print("press 1 to return to the main menue")
            print("press 0 to Exit")
            v=int(input())
            if v==1:
                continue
            if v==0:
                break
            else:
                while True:
                    print("Wrong Name")
                    print("Please Try Again")
                    b=int(input())
                    if b ==1:
                        continue
                    elif b==0:
                        break
                
        elif condition1==2:
            print(price)
            print("----------------------------")
            print("press 1 to return to the main menue")
            print("press 0 to Exit")
            v=int(input())
            if v==1:
                continue
            if v==0:
                break
            else:
                while True:
                    print("Wrong Name")
                    print("Please Try Again")
                    b=int(input())
                    if b ==1:
                        continue
                    elif b==0:
                        break
        elif condition1==3:
            print(Quantity)
            print("----------------------------")
            print("press 1 to return to the main menue")
            print("press 0 to Exit")
            v=int(input())
            if v==1:
                continue
            if v==0:
                break
            else:
                while True:
                    print("Wrong Name")
                    print("Please Try Again")
                    b=int(input())
                    if b ==1:
                        continue
                    elif b==0:
                        break
        elif condition1==4:
            print("Enter Your Option From The Next Choices")
            print(Products)
            c1=input()
            if c1 not in Products:
                while True:
                    print("Wrong Name")
                    print("Please Try Again")
                    c1=input()
                    if c1 in Products:
                        break                   
            print("Enter New Price")
            c2=int(input())
            price[c1]=c2
            print("Product With New Prices Will be",price)
            print("----------------------------")
            print("press 1 to return to the main menue")
            print("press 0 to Exit")
            v=int(input())
            if v==1:
                continue
            if v==0:
                break
            else:
                while True:
                    print("Wrong Name")
                    print("Please Try Again")
                    b=int(input())
                    if b ==1:
                        continue
                    elif b==0:
                        break
        elif condition1==0:
            break            
    
    elif condition==2:
        print("----------------------------")
        print("Hello Customer")
        print("To show The Prices Of our products       press 1")
        print("To show The Quantity Of our products     press 2")
        print("To Buy from our products                 press 3")
        print("To print the bill                        press 4")
        print("To exist                                 press 0")
        condition2=int(input())
        if condition2==1:
            print(price)
            print("----------------------------")
            print("press 1 to return to the main menue")
            print("press 0 to Exit")
            v=int(input())
            if v==1:
                continue
            if v==0:
                break
            else:
                while True:
                    print("Wrong Name")
                    print("Please Try Again")
                    b=int(input())
                    if b ==1:
                        continue
                    elif b==0:
                        break 
        elif condition2==2:
            print(Quantity)
            print("----------------------------")
            print("press 1 to return to the main menue")
            print("press 0 to Exit")
            v=int(input())
            if v==1:
                continue
            if v==0:
                break
            else:
                while True:
                    print("Wrong Name")
                    print("Please Try Again")
                    b=int(input())
                    if b ==1:
                        continue
                    elif b==0:
                        break    
        elif condition2==3:
            print(Products)
            n1=input("Please Enter The Name of Item : ")
            if n1 not in Products:
                while True:
                    print("Wrong Name")
                    print("Please Try Again")
                    n1=input()
                    if n1 in Products:
                        break                   
            p2=int(input("Please Enter The Quantity of Item : "))
            Quantity[n1]-=p2
            print("Order Placed")
            print("----------------------------")
            print("press 1 to return to the main menue")
            print("press 0 to Exit")
            v=int(input())
            if v==1:
                continue
            if v==0:
                break
            else:
                while True:
                    print("Wrong Name")
                    print("Please Try Again")
                    b=int(input())
                    if b ==1:
                        continue
                    elif b==0:
                        break            
        elif condition2==4:
            print("Your Bill = ",p2*price[n1])
            print("----------------------------")
            print("press 1 to return to the main menue")
            print("press 0 to Exit")
            v=int(input())
            if v==1:
                continue
            if v==0:
                break
            else:
                while True:
                    print("Wrong Name")
                    print("Please Try Again")
                    b=int(input())
                    if b ==1:
                        continue
                    elif b==0:
                        break
        elif condition2==0:
            break       
    elif condition==0:
        h=0
print("Thank You For Visiting Our Shop")