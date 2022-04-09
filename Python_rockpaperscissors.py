from random import randint

# List to store Rock,Paper and Scissors
t = ["r", "p", "s"]
#     0    1    2

# keeping highscore
playerHighScore = 0
computerHighScore = 0

# to make computer chooses a random value from t
computer = t[randint(0, 2)]

# Setting to false allows the loop to repeat
# as once the variable have a value it changes to "True"
player = False

# title
print("junie's RPS 1.0")
print("w/ Highscore and randomized 2d values")
print()

# start of program
while player == False:
    player = input("[R]ock, [P]aper or [S]cissors?: ").lower()
    # by now computer already has a random value

    # tie situation
    if player == computer:
        print(f"Computer picked {computer}, so its a tie!")
        print(f"Player = {playerHighScore}, Computer = {computerHighScore}")
        print()

    # if player chooses Rock and computer chooses Paper
    elif player == "r":
        if computer == "p":
            print("You lose! Paper covers Rock")
            playerHighScore += 0
            computerHighScore += 1
            print(f"Player = {playerHighScore}, Computer = {computerHighScore}")
            print()
        elif computer == "s":
            print("You win! Rock smashes Scissors")
            playerHighScore += 1
            computerHighScore += 0
            print(f"Player = {playerHighScore}, Computer = {computerHighScore}")
            print()

    # if player chooses Paper and computer chooses Scissors
    elif player == "p":
        if computer == "s":
            print("You lose! Scissors cuts Paper")
            playerHighScore += 0
            computerHighScore += 1
            print(f"Player = {playerHighScore}, Computer = {computerHighScore}")
            print()
        elif computer == "r":
            print("You win! Paper covers Rock")
            playerHighScore += 1
            computerHighScore += 0
            print(f"Player = {playerHighScore}, Computer = {computerHighScore}")
            print()

    # if player chooses Scissors and computer chooses Rock
    elif player == "s":
        if computer == "r":
            print("You lose! Rock smashes Scissors")
            playerHighScore += 0
            computerHighScore += 1
            print(f"Player = {playerHighScore}, Computer = {computerHighScore}")
            print()
        elif computer == "p":
            print("You win! Scissors cuts Paper")
            playerHighScore += 1
            computerHighScore += 0
            print(f"Player = {playerHighScore}, Computer = {computerHighScore}")

    # if non of value included this is final
    else:
        print("You have inserted an invalid value.")
        print("Make sure to use either [R], [P] or [S]!")
        print()



    # since player = True now, we need to set it back to False
    # so that the program loops
    player = False
    computer = t[randint(0, 2)]
