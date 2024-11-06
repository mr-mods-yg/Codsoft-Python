import random
import time

def playGame(user_score, computer_score, rounds):
    valid_choice = ['rock','paper','scissors']
    current_round = 1
    while user_score<=1 and computer_score<=1:
        wonTheGame = False
        isGameTied = False
        time.sleep(1)
        
        print(f"\nRound {current_round}")
        user_choice = input("enter your choice: (rock,paper,scissors) ")
        computer_choice = random.choice(valid_choice)
        if(user_choice not in valid_choice):
            print("error: invalid choice!")
            continue
        if(user_choice == "rock" and computer_choice == "scissors"):
            wonTheGame = True
        elif(user_choice == "scissors" and computer_choice == "paper"):
            wonTheGame = True
        elif(user_choice == "paper" and computer_choice == "rock"):
            wonTheGame = True
        elif(user_choice==computer_choice):
            isGameTied = True

        print(f"computer choice: {computer_choice}")
        if(wonTheGame):
            user_score+=1
            print("congrats! you won the round")
        else:
            # check if game is tied or not
            if(isGameTied):
                print("the game is tied")
                print("there will be one extra round to decide now!")
            else:
                computer_score+=1
                print("you lost the round!")
                
        time.sleep(1)
        print(f"\nRound {current_round} completed: \nUser Score: {user_score} \nComputer Score: {computer_score}")
        current_round +=1

    if(user_score>computer_score):
        print("\nCongrats! you have won the game")
    else:
        print("\nYou have lost the game! better luck next time")

if __name__ == "__main__":
    # variables
    
    # main
    print("Welcome to Rock Paper Scissors game!")
    print("Game Rules :")
    print("- Winner will be most scorer in three games")
    print("- If game is tied, extra round will be played for each tied round")
    wantToPlayGame = True
    while wantToPlayGame:
        playGame(user_score=0,computer_score=0,rounds=3)
        prompt = input("\nDo you want to continue the game: (Y/N)")
        if(prompt=='N'):
            wantToPlayGame = False
    print("Thanks for playing!! :)")