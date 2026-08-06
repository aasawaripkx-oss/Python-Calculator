#Number Guessing Game

import random
Best_score = None
Play_again = "Y"

while Play_again == "Y" :
############################LET US GUESS THE NUMBERS(Name of the Game)#################
    print("*******************************")

    print("LET US GUESS THE NUMBERS")

    print("*******************************")

    print("1.Easy 1-100")
    print("2.Medium 1-500")
    print("3.Hard 1-1000")
    
    try:
      Choice = int(input("Enter your Choice:"))
    except ValueError :
        print("Invalid Choice ")
        continue
   
    if Choice == 1 :
        maximum_number = 100
        print("Easy mode selected")
    elif Choice == 2 :
        maximum_number = 500
        print("Medium mode selected") 
    elif Choice == 3 :
        maximum_number = 1000
        print("Hard mode selected:") 
    else: 
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue
     
    Secret_number = random.randint(1, maximum_number)

    Attempts = 0
    try:
        Guess_the_number = int(input("Enter your guessing number:"))
    except ValueError:
        print("Invalid Guess")
        continue
    Attempts += 1

    while Secret_number != Guess_the_number:
    
        if Guess_the_number > Secret_number:
            print("Greater than the secret number")
        elif  Secret_number > Guess_the_number:
            print("Smaller than the secret number")
        try :
            Guess_the_number = int(input("Enter your guessing number:"))
        except ValueError:
            print("Invalid input")
            continue
            
        Attempts+= 1
        

    if Secret_number == Guess_the_number:
        print("You Win\nYou guessed the number right")

    print("Attempts :",Attempts)



    if Best_score is None : 
        Best_score = Attempts
    elif Attempts < Best_score:
        Best_score = Attempts
    
    print("Best_score :",Best_score ) 
    
    Play_again = input("Do you want to play again :? ").upper()
    
    
    