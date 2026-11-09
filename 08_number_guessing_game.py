import random

def main():
    secret = random.randint(1, 100)
    max_attempts = 7
    print("Guess the number from 1 to 100. You have 7 attempts.")
    for attempt in range(1, max_attempts + 1):
        while True:
            try:
                guess = int(input(f"Attempt {attempt}: "))
                if 1 <= guess <= 100: break
                print("Enter a number between 1 and 100.")
            except ValueError: print("Enter a valid whole number.")
        if guess == secret:
            print(f"Correct! You guessed it in {attempt} attempt(s).")
            break
        elif guess < secret: print("Too low.")
        else: print("Too high.")
    else:
        print("You have used all attempts. The number was", secret)

if __name__ == "__main__": main()
