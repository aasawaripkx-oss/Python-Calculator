#Number Guessing Game

import random
best_score = None
play_again = "Y"

while play_again == "Y" :
############################LET US GUESS THE NUMBERS(Name of the Game)#################
    print("*******************************")

    print("LET US GUESS THE NUMBERS")

    print("*******************************")

    print("1.Easy 1-100")
    print("2.Medium 1-500")
    print("3.Hard 1-1000")
    
    try:
      choice = int(input("Enter your Choice:"))
    except ValueError :
        print("Invalid Choice ")
        continue
   
    if choice == 1 :
        maximum_number = 100
        print("Easy mode selected\nGuess number from 1 - 100")
    elif choice == 2 :
        maximum_number = 500
        print("Medium mode selected\n Guess number from 1 - 500") 
    elif choice == 3 :
        maximum_number = 1000
        print("Hard mode selected\n Guess numbers from 1 - 1000") 
    else: 
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue
     
    secret_number = random.randint(1, maximum_number)

    attempts = 0
    while True:
        try:
            guess_the_number = int(input("Enter your guessing number:"))
            break
        except ValueError:
            print("Invalid Guess")
        
    attempts += 1

    while secret_number != guess_the_number:
    
        if guess_the_number > secret_number:
            print("Greater than the secret number")
        elif  secret_number > guess_the_number:
            print("Smaller than the secret number")
            
            
        while True :
            try :
                guess_the_number = int(input("Enter your guessing number:"))
                break
            except ValueError:
                
                print("Invalid input")

            
        attempts+= 1
        

    if secret_number == guess_the_number:
        print("You Win\nYou guessed the number right")

    print("Attempts :",attempts)



    if best_score is None : 
        best_score = attempts
    elif attempts < best_score:
        best_score = attempts
    
    print("best_score :",best_score ) 
    
    play_again = input("Do you want to play again ? ").upper()
    
    
    