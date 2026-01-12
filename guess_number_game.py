import random

def getRandomNumber(maxrange):
    return random.randint(1,maxrange)

def giveHint(number, guess):
    if guess > (number + 10) or guess < (number - 10):
        return "COLD"
    elif number == guess:
        return "RIGHT"
    else:
        return "HOT"

def runGuess():
    level=input("Choose a level \nEasy: E, Midium: M, Hard: H \nAnswer : ")
    if level.upper()=="E":
        maxrange=50
    elif level.upper()=="M":
        maxrange=100
    else :
        maxrange=150
    secretNumber = getRandomNumber(maxrange)
    a=0
    while True:
        user_guess = int(input(f"Enter a number between 1 and {maxrange} : "))
        hint = giveHint(secretNumber, user_guess)
        a +=1
        if hint == "RIGHT":
            print("You guessed it Right! Attempts: ",a)
            break
        else:
            print(hint)

def main():
    while True:
        runGuess()
        ask=input("Want to play again? (Yes/No) :")
        if ask.lower()=="no":
            break

print("!!! RULES !!!")
print("i) If the guess matches the secret number  - RIGHT")
print("ii) If the guess is within ±10 of the secret number  - HOT")
print("iii) If the guess is greater by 10 or lesser by 10  - COLD")
print("\n")

if __name__ == '__main__':
    main()
