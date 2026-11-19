# Library book management system •
# What it is: A digital sign-out sheet for books. What it does: It keeps track of books in a small library. 
# It lets users search for a book title and check it out. 
# Once checked out, it marks the book as "borrowed" so no one else can take it.

library_books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "isbn": "9780743273565",
        "status": "available"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "9780446310789",
        "status": "borrowed"
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "isbn": "9780451524935",
        "status": "available"
    },
    {
        "id": 4,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "isbn": "9780316769174",
        "status": "available"
    },
    {
        "id": 5,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "isbn": "9780547928227",
        "status": "borrowed"
    }
]

borrowed_cart = []

while True:
    print("Welcome, what would you want to do today? Borrow/Return ")
    reader_response = input("Please enter your choice:  ")
    
    if reader_response == "Borrow":
        available_books = []
        for book in library_books:
            if book["status"] == "available":
                available_books.append(book)
        
        for book in available_books:
            print("The below books are available")
            print()
            print(book["id"])
            print(book["title"])
            print(book["author"])
            print()

        while len(available_books) >0:
            reader_choice_book = input("Enter your choice of book id: ")
            borrowed_cart.append(reader_choice_book)
            available_books.pop.index[reader_choice_book]
            
            
