import random
n= random.randrange(1,1000)
guess = int (input("Guess the number:"))
while n!= guess:
    if guess<n:
        print("Too Low")
        guess = int (input("Guess the number:"))
    elif guess >n:
        print("Too High")
        guess = int (input("Guess the number:"))
    else:
        break
print("You Guessed it Right!!!!")