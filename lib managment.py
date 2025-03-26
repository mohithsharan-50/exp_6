class Library:
    def __init__(self):
        self.inventory = {}
        self.borrowed_books = {}

    def add_book(self, title, copies):
        self.inventory[title] = self.inventory.get(title, 0) + copies
        print(f"{copies} copies of '{title}' added to inventory.")

    def view_books(self):
        print("\nAvailable Books:")
        for title, copies in self.inventory.items():
            if copies > 0:
                print(f"{title} ({copies} copies)")

    def loan_book(self, title, user):
        if self.inventory.get(title, 0) > 0:
            self.inventory[title] -= 1
            self.borrowed_books[user] = self.borrowed_books.get(user, []) + [title]
            print(f"{user} borrowed '{title}'.")
        else:
            print(f"Sorry, '{title}' is not available.")

    def return_book(self, title, user):
        if user in self.borrowed_books and title in self.borrowed_books[user]:
            self.borrowed_books[user].remove(title)
            self.inventory[title] += 1
            print(f"{user} returned '{title}'.")
        else:
            print(f"Error: '{title}' was not borrowed by {user}.")

    def borrowed_books_list(self):
        print("\nBorrowed Books:")
        for user, books in self.borrowed_books.items():
            print(f"{user}: {', '.join(books)}")

library = Library()
library.add_book("Python Basics", 3)
library.add_book("Data Science", 2)
library.view_books()

library.loan_book("Python Basics", "Alice")
library.loan_book("Data Science", "Bob")
library.borrowed_books_list()

library.return_book("Python Basics", "Alice")
library.view_books()
library.borrowed_books_list()
