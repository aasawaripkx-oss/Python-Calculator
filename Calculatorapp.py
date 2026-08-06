#Calculator App 1
import math

while True :
    
    
    print ("______________________-------------------------------------Menu-------------------------------------------______________________________________")

    Choice = int(input("Entre your choice :"))

#####ADDITION#####
    if  Choice == 1  :
        try:
            NUM1 = (int(input("Entre First Number :")))
            NUM2 =(int(input("Entre Second Number :")))
            print("ADDITION:",NUM1 + NUM2)
        except:
            print("Invaild Syntax :takee input as int")
#####SUBTRACTION#####   
    elif Choice == 2 :
        try: 
           NUM1 =  (int(input("Enter First number:")))
           NUM2 = (int (input("Enter Second number:")))
           print("SUBTRACTION:",NUM1 - NUM2)
        except:
           print("Invaild Syntax :takee input as int")
#####MULTIPLICATION#####         
    elif Choice == 3 :
        try:
            NUM1 = int (input("Enter First Number:"))
            NUM2 = int (input("Enter Second Number:"))
            print("MULTIPLICATION:",NUM1 * NUM2 )
        except:
            print("Invaild Syntax :takee input as int")
#####DIVISION#####
    elif Choice == 4:
        try:
            NUM1 = int (input("Enter First Number:"))
            NUM2 = int (input("EnterSecond Number:"))
            if NUM2 == 0 :
                print("Cannot divided by zero")
            else:
                print("DIVISION:",NUM1 / NUM2 )
        except:
            print("Invaild Syntax :takee input as int")
#####FLOOR DIVISION#####
    elif Choice == 5 :
        try :
            NUM1 = int (input("Enter First Number :"))
            NUM2 = int(input("Enter Second Number :"))
            print("FLOOR DIVISON:",NUM1 // NUM2)
        except:
           print("Invaild Syntax :takee input as int") 
#####MODULUS#####
    elif Choice == 6 :
        try:
            NUM1 = int (input("Enter First Number :"))
            NUM2 = int(input("EnterSecond Number :"))
            print("Modulus",NUM1 % NUM2)  
        except:
            print("Invaild Syntax :takee input as int")
#####EXPONENT#####    
    elif Choice == 7 :
        try:
            NUM1 = int (input("Enter First Number :"))
            NUM2 = int(input("Enter Second Number :"))
            print("EXPONENT:",NUM1 ** NUM2)
        except:
            print("Invaild Syntax :takee input as int")
#####PERCENTAGE#####
    elif Choice == 8 :
        try :
           NUMBER = int (input("Enter First Number :"))
           PERCENTAGE= int(input("Enter Second Number :"))
           print(NUMBER*PERCENTAGE / 100)
        except:
            print("Invaild Syntax :takee input as int")
#####SQUARE #####     
    elif Choice == 9 :
        try :
            NUMBER = int(input("Entre a number:"))
            print(NUMBER ** 2)
        except:
            print("Invaild Syntax :takee input as int")
#####SQUARE ROOT #####
    elif Choice == 10 :
        try:
           NUMBER = int(input("Entre a number:"))
           print(math.sqrt(NUMBER))
        except:
            print("Invaild Syntax :takee input as int")
        break
else :
    print("INVALID OPERATION")


# #calculator App 2 

# a = float(input("Entre a number1:"))
# b= float(input("Entre a number2:"))
# op = input("Entre a Operator :(+,-,*,/,//,%,**):")

# if op == "+":
#     print(a+b)
# elif op == "-":
#     print(a-b)
# elif op == "*":
#     print(a*b)
# elif op == "/":
#     print(a/b)
# elif op == "//":
#     print(a//b)
# elif op == "%" :
#     print(a%b)
# elif op == "**":
#     print(a**b)
# else:
#     print("Invalid output")