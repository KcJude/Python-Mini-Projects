# Registration and login system
users = []

while True:
    print("Do you want to login or register?")
    answer = input("Login or Register:  ")
    if answer == "register":
        print("Please enter your details below")
        name = input("Enter your name:  ")
        email = input("Enter your email:  ")
        password = input("Enter your password:  ")
        user_dict = {
            "name":name,
            "email": email,
            "password": password
        }
        users.append(user_dict)
        print("User registered successfully.")
        continue
    elif answer == "login":
        print("Please enter your email and password")
        user_email = input("Please enter your email address:  ").strip()

        for user in users:
            if user_email == user["email"]:

                user_password = input("Please enter your password:  ").strip()
                if user_password == user["password"]:
                    print("Login successful..")
                    break
                else:
                    print("Incorrect password.. please try again.")
            
            else:
                print("Email does not exist in our system")
                continue