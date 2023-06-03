import random

def guessgame(a,b,actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess< actual:
            guess = int(input(f"Enter a bigger number\n"))

        else:
            guess = int(input(f"Enter a smaller number\n"))
            guess += 1
    print(f"You guessed the number in {guess} guesses\n")            
    return nguess

if __name__ ==  "__main__":
    a = int(input("Enter the value of a\n"))
    b = int(input("Enter the value of b\n"))
    actual = random.randint(a,b)
    print("player 1's turn")
    g1 = guessgame(a,b,actual)
    print("player 2's turn")
    g2 = guessgame(a,b,actual)

    if g1 < g2:
        print("player 1 won the match!\n")

    elif g1 > g2:
        print("player 2 won the match\n")

    else:
        print("It's a tie!")        