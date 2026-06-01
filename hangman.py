import random

word = random.choice(["python", "intern", "coding", "alpha", "software"])
guessed = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    # Word status check
    status = "".join([ltr if ltr in guessed else "_" for ltr in word])
    print("\nWord:", " ".join(status))
    
    if "_" not in status:
        print("🎉 You Won!")
        break
        
    guess = input("Guess a letter: ").lower()
    guessed.append(guess)
    
    if guess not in word:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")
else:
    print(f"😭 Game Over! The word was: {word}")