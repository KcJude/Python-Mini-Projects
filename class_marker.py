

quiz_questions = [
    {
        "text": "Which data type is used to store text in Python?",
        "options": ["A) int", "B) float", "C) str", "D) bool"],
        "correct_answer": "C"
    },

    {
        "text": "What is the correct way to start a function definition in Python?",
        "options": ["A) def myFunction():", "B) function myFunction():", "C) create myFunction():", "D) define myFunction():"],
        "correct_answer": "A"
    },
    {
        "text": "Which of the following is an immutable data type?",
        "options": ["A) list", "B) dictionary", "C) tuple", "D) set"],
        "correct_answer": "C"
    },
    {
        "text": "What keyword is used to skip the rest of the current loop iteration and jump to the top?",
        "options": ["A) break", "B) continue", "C) pass", "D) exit"],
        "correct_answer": "B"
    },
    {
        "text": "Which collection data type does NOT allow duplicate elements?",
        "options": ["A) list", "B) tuple", "C) set", "D) dictionary keys"],
        "correct_answer": "C"
    },
    {
        "text": "What will print(type(4.5)) output?",
        "options": ["A) <class 'int'>", "B) <class 'str'>", "C) <class 'float'>", "D) <class 'bool'>"],
        "correct_answer": "C"
    },
    {
        "text": "How do you add an element to the end of a list in Python?",
        "options": ["A) list.add()", "B) list.append()", "C) list.insert()", "D) list.push()"],
        "correct_answer": "B"
    },
    {
        "text": "What does a while loop do if its condition is always True?",
        "options": ["A) Runs exactly once", "B) Throws a SyntaxError", "C) Loops infinitely", "D) Skips the code entirely"],
        "correct_answer": "C"
    },
    {
        "text": "Which operator is used for calculating the remainder of a division?",
        "options": ["A) /", "B) //", "C) %", "D) **"],
        "correct_answer": "C"
    },
    {
        "text": "What is the value of the expression: True and False?",
        "options": ["A) True", "B) False", "C) None", "D) Error"],
        "correct_answer": "B"
    },
    {
        "text": "How do you access the value associated with a key in a dictionary named 'user'?",
        "options": ["A) user(key)", "B) user[key]", "C) user.key", "D) user.get_index(key)"],
        "correct_answer": "B"
    },
    {
        "text": "Which loop is best used when you know exactly how many times you want to iterate?",
        "options": ["A) while loop", "B) for loop", "C) infinite loop", "D) nested loop"],
        "correct_answer": "B"
    },
    {
        "text": "What value does a function return by default if it has no return statement?",
        "options": ["A) 0", "B) False", "C) None", "D) str"],
        "correct_answer": "C"
    },
    {
        "text": "What is the output of print('Python'[0])?",
        "options": ["A) P", "B) y", "C) n", "D) Error"],
        "correct_answer": "A"
    },
    {
        "text": "Which data type can only hold the values True or False?",
        "options": ["A) string", "B) boolean", "C) integer", "D) float"],
        "correct_answer": "B"
    },
    {
        "text": "How do you find the total number of items in a list named 'my_list'?",
        "options": ["A) len(my_list)", "B) my_list.count()", "C) size(my_list)", "D) my_list.length()"],
        "correct_answer": "A"
    },
    {
        "text": "What does the 'break' keyword do inside a loop?",
        "options": ["A) Pauses the loop", "B) Skips to the next round", "C) Exits the loop completely", "D) Restarts the script"],
        "correct_answer": "C"
    },
    {
        "text": "What is the result of 2 ** 3 in Python?",
        "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
        "correct_answer": "B"
    },
    {
        "text": "Which symbol is used to add a comment in Python code?",
        "options": ["A) //", "B) /*", "C) #", "D) <!--"],
        "correct_answer": "C"
    },
    {
        "text": "What will be the result of bool([])?",
        "options": ["A) True", "B) False", "C) None", "D) ValueError"],
        "correct_answer": "B"
    }
]


# Question and Answers

# user_name = input("Please enter your name: ")

count = 0

for question in quiz_questions:
    print(question["text"])
    for option in question["options"]:
        print(option)
    while True:
        answer = input("Enter answer: ").strip()
        if len(answer) >1:
            print("Invalid answer format, must a one character answer")
            continue
        if type(answer) != str:
            print("Answer must an alphabet A, B, C, D")
            continue
        if answer == question["correct_answer"]:
            print("Congratulations!")
            count += 1
            break
        else:
            print("The answer is incorrect, try again")
            continue



    
    
    