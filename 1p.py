import random
words = ["Python" , " Computer" , "Science" , "Machine" , "Developer"]
word = random.choice(words)
guessed = " "
chances = 6
print("Welcome to Hangman Game")
while chances > 0:
    failed = 0
    for ch in word :
        if ch in guessed :
            print(ch , end= " ")
        else:
            print("_",end=" ")
            failed +=1
    print()
    if failed ==0:
        print("Congratulation , You Won the Game")
        break
    guess = input("guess a letters:")
    guessed += guess
    if guess not in word:
        chances -=1
        print("Sorry ,You guess Wrong")
        print("Chances left " ,chances) 
if chances ==0:
    print("You Lost")
    print("word was: " ,word)                   