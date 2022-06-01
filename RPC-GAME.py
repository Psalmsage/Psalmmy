print("Let play!!!""\U0001F601")
print ("Instruction")
print("----------")
print("Rock beats Scissors")
print("Paper Beats Rock")
print("Scissors beats Paper")
print("R=Rock")
print("P=Paper")
print("S=Scissors")
print("------------")
import random

while True:


    User_action = input("Enter any choice(R,P,S):")
 
    p_actions = ["R","P","S"]
    computer_action =random.choice(p_actions)
    R="Rock"
    P="Paper"
    S="Scissors"
     
 

    print(f"\nYou chose {User_action}, computer chose{computer_action}.\n")

    if User_action == computer_action:
        print(f"Both players selected {User_action}. It's a tie!" "\U0001F612")
        continue
    
    elif User_action == "R":
        if computer_action == "S":
            print("Rock smashes Scissors! You win!" "\U0001F601")
            break
        else :
            print("Paper cover Rock, you lose." "\U0001F602")

    elif User_action == "P":
        if computer_action =="R":
            print("Paper cover Rock, You WIn!." "\U0001F601")
            break
        else:
            print("Scissors cuts paper! You Lose" "\U0001F602")

    elif User_action =="S":
        if computer_action =="P":
            print("Scissors cut Paper, You Win!" "\U0001F601")
            break
        else:
            print("Rock smashes Scissors, You lose" "\U0001F602")
    else:
        print("Wrong input, Check")
     

    print("Are you still playing (Y/N)")
    playing_again= input("Playing again:")
    if playing_again.lower()!="y":
        break

print("\nThanks for playing")

