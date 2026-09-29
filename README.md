# Library Management System

## About the Project

The **Library Management System** is a simple Python-based console application created as part of my Python Essentials project.

I wanted to build something practical rather than just a small program that performs one calculation. This project allows a user to manage books in a small library through a simple menu. Books can be added, viewed, searched, issued, returned, and removed.

The project stores the book information in a JSON file, so the data is available even after the program is closed.

## Features

The application provides the following options:

1. **Add Book** – Add a new book with its ID, title, and author.
2. **View All Books** – Display all books currently stored in the library.
3. **Search Book** – Search for a book using its title.
4. **Issue Book** – Change a book's status from available to issued.
5. **Return Book** – Mark an issued book as available again.
6. **Remove Book** – Remove a book from the library.
7. **Exit** – Close the application safely.

The program also includes basic input validation, such as checking for empty details and duplicate book IDs.

## Technologies Used

- Python 3.14
- JSON for storing data
- VS Code for development
- Git and GitHub for version control and submission

No external Python packages are required.

## Project Structure

```text
Library-Management-System/
│
├── library_management.py
├── books.json
├── README.md
└── requirements.txt
```

### File Description

- `library_management.py` – Main Python program.
- `books.json` – Stores the library's book data.
- `README.md` – Project documentation.
- `requirements.txt` – Lists external dependencies. This project does not require any external packages.

## How to Run the Project

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installation with:

```bash
python --version
```

### 2. Open the project folder

Open the `Library-Management-System` folder in VS Code or a terminal.

### 3. Run the program

Use:

```bash
python library_management.py
```

The main menu will appear in the terminal.

## Example

```text
===================================
       LIBRARY MANAGEMENT SYSTEM
===================================
1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Remove Book
7. Exit
===================================
Enter your choice (1-7):
```

## What I Learned

While developing this project, I practiced several important Python concepts:

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- File handling
- JSON data storage
- Exception handling
- User input validation
- Organizing a program into reusable functions

The project also helped me understand how a Python program can work with stored data instead of losing everything when the program closes.

## Future Improvements

If I continue developing this project, I would like to add:

- Student/member registration
- Due dates for issued books
- Fine calculation for late returns
- Login for librarian and students
- A graphical user interface
- Better reports and statistics
- Database support such as SQLite

## Author

**Name:** GOPIKA SRI A  
**Course:** Python Essentials  
**Project:** Library Management System