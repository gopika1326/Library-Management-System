import json
import os

BOOKS_FILE = "books.json"


def load_books():
    """Load books from the JSON file."""
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_books(books):
    """Save books to the JSON file."""
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)


def add_book(books):
    """Add a new book to the library."""
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    save_books(books)

    print("\nBook added successfully!")


def view_books(books):
    """Display all books."""
    if not books:
        print("\nNo books found.")
        return

    print("\n========== LIBRARY BOOKS ==========")

    for book in books:
        status = "Available" if book["available"] else "Issued"

        print(f"ID     : {book['id']}")
        print(f"Title  : {book['title']}")
        print(f"Author : {book['author']}")
        print(f"Status : {status}")
        print("-----------------------------------")


def search_book(books):
    """Search for a book by title."""
    search = input("Enter book title to search: ").lower()

    found = False

    for book in books:
        if search in book["title"].lower():
            status = "Available" if book["available"] else "Issued"

            print("\nBook Found!")
            print(f"ID     : {book['id']}")
            print(f"Title  : {book['title']}")
            print(f"Author : {book['author']}")
            print(f"Status : {status}")

            found = True

    if not found:
        print("\nBook not found.")


def issue_book(books):
    """Issue a book."""
    book_id = input("Enter book ID to issue: ")

    for book in books:
        if book["id"] == book_id:

            if book["available"]:
                book["available"] = False
                save_books(books)
                print("\nBook issued successfully!")
            else:
                print("\nThis book is already issued.")

            return

    print("\nBook ID not found.")


def return_book(books):
    """Return a book."""
    book_id = input("Enter book ID to return: ")

    for book in books:
        if book["id"] == book_id:

            if not book["available"]:
                book["available"] = True
                save_books(books)
                print("\nBook returned successfully!")
            else:
                print("\nThis book was not issued.")

            return

    print("\nBook ID not found.")


def remove_book(books):
    """Remove a book from the library."""
    book_id = input("Enter book ID to remove: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books(books)
            print("\nBook removed successfully!")
            return

    print("\nBook ID not found.")


def main():
    """Main program."""
    books = load_books()

    while True:
        print("\n===================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Exit")
        print("===================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_book(books)

        elif choice == "2":
            view_books(books)

        elif choice == "3":
            search_book(books)

        elif choice == "4":
            issue_book(books)

        elif choice == "5":
            return_book(books)

        elif choice == "6":
            remove_book(books)

        elif choice == "7":
            print("\nThank you for using the Library Management System!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()