# stack_overflow code challenge
import random

word = "game"
count = 0
game = count + 1
player1_score = 0
player2_score = 0
with open('leaderboard.txt', 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                count=count+1
print("Occurrences of the word", word,"is", count)
print("Game number ", game)

def gameFunc():
    global player1_score, player2_score
    player1_roll = random.randint(0, 20)
    player2_roll = random.randint(0, 20)
    print("player 1 rolled", player1_roll)
    print("player 2 rolled", player2_roll)

    if player1_roll > player2_roll:
        print("Player 1 Wins!!" + "\n")
        player1_score += 1
    elif player1_roll < player2_roll:
        print("Player 2 Wins!!" + "\n")
        player2_score += 1
    else:
        print("It's a Tie!!" + "\n")

def Main():
    global player1_score, player2_score
    rounds_input = int(input('How many rounds do you want?: '))
    i = rounds_input
    n = 0
    while n < i:
        gameFunc()
        n += 1
    else:
        if player1_score > player1_score:
            print("Player 1 Wins Game", count)   
        elif player1_score < player1_score:
            print("Player 2 Wins Game", count) 

def Start():
    print("Do you want to begin?")
    beginPrompt = input('Type START to begin: ').lower()
    if beginPrompt == 'start':
        print("\n")
        Main()
    else:
        print("\n" + "Try Again" + "\n")
        Start()

Start()



    