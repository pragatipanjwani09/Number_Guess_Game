import random

def getRandomNumber():
    return random.randrange(1, 100)

def giveHint(number, guess):
    if guess > (number + 10) or guess < (number - 10):
        return "COLD"
    elif number == guess:
        return "RIGHT"
    else:
        return "HOT"

def runGuess():
    secretNumber = getRandomNumber()
  
    while True:
        user_guess = int(input("Enter a number between 1 and 100: "))
        hint = giveHint(secretNumber, user_guess)
        if hint == "Right":
            print("You guessed it Right!")
            break
        else:
            print(hint)

print("!!! RULES !!!")
print("i) If the guess matches the secret number  - RIGHT")
print("ii) If the guess is within ±10 of the secret number  - HOT")
print("iii) If the guess is greater by 10 or lesser by 10  - COLD")
print("\n")

if __name__ == '__main__':
    runGuess()
