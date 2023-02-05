import random

You = input("Select Rock, Paper, or Scissor :").lower()
PC = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("PC selected: ", PC)

if You == "rock" and PC == "paper":
    print("PC Won")
elif You == "paper" and PC == "scissor":
    print("PC Won")
elif You == "scissor" and PC == "rock":
    print("PC Won")
elif You == PC:
    print("Tie")
elif You != "rock" or"paper" or"scissor":
    print("Cheater, pc wins")
else:
    print("You Won")

    
    