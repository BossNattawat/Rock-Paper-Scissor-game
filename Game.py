import random

def main():
    
    while True:
        print("_________ Rock Paper Scissor game _________")
        print()
        
        choice = ["Rock", "Paper", "Scissors"]
        
        while True:
            try:
                user_input = input("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors\n\nAnswer : ").capitalize()
                
                if user_input not in choice:
                    print("The answer must be Rock, Paper, or Scissors.")
                    pass
                else:
                    break
            except ValueError:
                pass
            
        computer_answer = random.choice(choice)
        print(f"Computer Answer : {computer_answer}")
        print()
        
        if user_input == "Rock" and computer_answer == "Scissors":
            print("\tYou Win!")
        elif user_input == "Paper" and computer_answer == "Rock":
            print("\tYou Win!")
        elif user_input == "Scissors" and computer_answer == "Paper":
            print("\tYou Win!")
        elif user_input == "Rock" and computer_answer == "Paper":
            print("\tComputer Win!")
        elif user_input == "Paper" and computer_answer == "Scissors":
            print("\tComputer Win!")
        elif user_input == "Scissors" and computer_answer == "Rock":
            print("\tComputer Win!")
        else:
            print("\tTie!")
        
        print()
        
        again = input("Want to play more? (y/n) : ").lower()
        
        if again == "n":
            break
        else:
            pass
    
if __name__ == "__main__":
    main()