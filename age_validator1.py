# My Age Validator App

# To collector age of not more than 100 or less than 14
# And strike out inputs that are not whole numbers

age_text = input("Please enter your age: ").strip()

while not age_text.isdigit():
    print("Your entry is not a whole number, please try again")
    age_text = input("Please re-enter your age: ").strip()

age = int(age_text)
while not (14 <= int(age) <= 100):
    print("Please you must be between the ages of 14 and 100")
    age = int(input("Please re-enter your age again now: "))

print("************")
print(f"You are {age}years old, congratulations you will be {age + 10}years old in the next decade.")
print("************")
print()