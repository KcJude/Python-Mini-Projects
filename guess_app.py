# A Guessing App
#SECRET GUESS NUMBER IS 42

# 1. Set SECRET = 42 at the top
# 2. Loop until the user guesses it, or uses up six attempts
# 3. Reject non-numeric guesses without using up an attempt
# 4. After each wrong guess say "Too high" or "Too low"
# 5. When they win, say how many attempts it took
# 6. If they run out, reveal the number

print("*************")
print("Hi, Welcome to your favourite guess app")
print("Let's play!")
print("*************")
guess_no = input("Please enter your guess number: ").strip()

while not guess_no.isdigit():
    print("Guess number must be a numeric value")
    guess_no = input("Enter your guess number: ")
    if guess_no.isdigit():
        continue

secret_number = int(guess_no)
max_attempts = 6
attempts = 0

while attempts < max_attempts or not ((secret_number) == 42):
    if int(secret_number) >42:
        print("Your guess is too high")
        secret_number = input("Enter your guess number: ")
        attempts += 1
    
    if int(secret_number) <42:
         print("Your guess is too low")
         secret_number = input("Enter your guess number: ")
         attempts += 1
    if int(secret_number) == 42:
         print(f" Congratulations to you, it took you {attempts +1}times to guess the secret number {secret_number} correctly")
         break
    if attempts == 5:
        print("You have run out of trials, the secret number is 42")
        break
        
    if int(secret_number) == 42:
        print("**********")
        print(f" Congratulations to you, it took you {attempts +1}times to guess the secret number {secret_number} correctly")
        print("**********")
        break


