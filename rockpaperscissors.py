import random

def main():
    options = ["rock", "paper", "scissors"]

    print("Welcome to a game of rock paper scissors!")

    bull = True

    while bull == True:

        userOption = input("Please select one of the following (rock, paper, scissors): ").lower()

        while userOption not in options:
            userOption = input("Please select one of the following (rock, paper, scissors): ").lower()

        computerOption = random.choice(options)
        print("The computer chose " + computerOption)

        if userOption == "rock":
            if computerOption == "rock":
                print("It's a tie!")
            
            elif computerOption == "paper":
                print("You lost!")
            
            else:
                print("Congratulations, you won!")
            
        elif userOption == "paper":
            if computerOption == "rock":
                print("Congratulations, you won!")
          
            elif computerOption == "paper":
                print("It's a tie!")
            
            else:
                print("You lost!")
         
        else:
            if computerOption == "rock":
                print("You lost!")
          
            elif computerOption == "paper":
                print("Congratulations, you won!")
            
            else:
                print("It's a tie!")
           
        
        playAgain = input("Would you like to play again? (y/n): ").lower()
        if playAgain == "y":
            bull = True
        else:
            bull = False

    print("Thanks for playing rock paper scissors!")
    return

if __name__ == "__main__":
    main()