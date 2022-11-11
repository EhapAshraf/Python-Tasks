from os import system, name
from time import sleep
system('cls')
for q in range(5):
    print()
    
    for i in range(11):
      for j in range(10):
        if i==5 or j==4 or (j==5 and i>=1 and i<=9) or (j==6 and i>=2 and i<=8) or (j==7 and i>=3 and i<=7) or (j==8 and i>=4 and i<=6) :
            print("*",end='')
        else:
            print(" ",end='')
      print()
      
      
    sleep(1)
    system('cls')
    print()
    for i in range(10):
      for j in range(11):
        if j==5 or i==4 or (i==5 and j>=1 and j<=9) or (i==6 and j>=2 and j<=8) or (i==7 and j>=3 and j<=7) or (i==8 and j>=4 and j<=6) :
            print("*",end='')
        else:
            print(" ",end='')
      print()
    

    sleep(1)
    system('cls')
    print()
    for i in range(11):
      for j in range(10):
        if i==5 or j==5 or (j==4 and i>=1 and i<=9) or (j==3 and i>=2 and i<=8) or (j==2 and i>=3 and i<=7) or (j==1 and i>=4 and i<=6) :
            print("*",end='')
        else:
            print(" ",end='')
      print()
      
    

    sleep(1)
    system('cls')
    print()
    for i in range(10):
      for j in range(11):
        if j==5 or i==5 or (i==4 and j>=1 and j<=9) or (i==3 and j>=2 and j<=8) or (i==2 and j>=3 and j<=7) or (i==1 and j>=4 and j<=6) :
            print("*",end='')
        else:
            print(" ",end='')
      print()
    sleep(1)
    system('cls')