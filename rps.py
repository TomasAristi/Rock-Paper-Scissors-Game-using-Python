import random
while 1==1:
    player1 = input("Select Rock, Paper, or Scissor :").lower()
    player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
    print("Player 2 selected: ", player2)

    if player1 == "rock" and player2 == "paper":
        print("Player 2 Won, better luck next time")
    elif player1 == "paper" and player2 == "scissor":
        print("Player 2 Won, better luck next time")
    elif player1 == "scissor" and player2 == "rock":
        print("Player 2 Won, better luck next time")
    elif player1 == player2:
        print("Tie")
    elif player1 != "scissor" or "paper" or "rock":
        print("Cheater! Player 2 wins")
    else:
        print("Player 1 Won")
    input("Thanks for playing. Press any key to start again.")