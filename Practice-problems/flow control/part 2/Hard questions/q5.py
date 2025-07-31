# Rock-Paper-Scissors: Determine winner based on players' inputs.
p1 = input("Player 1, enter rock/paper/scissors: ").lower()
p2 = input("Player 2, enter rock/paper/scissors: ").lower()

if p1 == p2:
    print("Tie")
elif (p1 == "rock" and p2 == "scissors") or \
     (p1 == "scissors" and p2 == "paper") or \
     (p1 == "paper" and p2 == "rock"):
    print("Player 1 wins")
else:
    print("Player 2 wins")