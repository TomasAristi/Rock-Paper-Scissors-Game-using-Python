import random

Games = 0
You = 0
PC = 0

while Games <= 10:
    print("You:", You)
    print("PC:", PC)
    print("Games played: ", Games )

    you = input("Select Rock, Paper, or Scissor :").lower()
    pc = random.choice(["Rock", "Paper", "Scissor"]).lower()
    print("PC:", pc)

    if you == "rock" and pc == "paper":
        print("PC won, better luck next time.")
        PC = PC + 1
        Games = Games +1
    elif you == "paper" and pc == "scissor":
        print("PC won, better luck next time.")
        PC = PC + 1
        Games = Games +1
    elif you == "scissor" and pc == "rock":
        print("PC won, better luck next time.")
        PC = PC + 1
        Games = Games +1
    elif you == pc:
        print("Tie")
        Games = Games +1

    elif you != "rock"or"paper"or"scissor":
        print("Invalid match.")
        Games = Games +1

    else:       
        print("You win.")
        You = You + 1
        Games = Games +1


