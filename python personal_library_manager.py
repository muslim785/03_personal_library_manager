import os

FILENAME = "library.txt"
library = []

def load_library():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 5:
                    title, author, year, genre, read_str = parts
                    read = read_str.lower() == "read"
                    library.append({
                        "title": title,
                        "author": author,
                        "year": int(year),
                        "genre": genre,
                        "read": read
                    })

def save_library():
    with open(FILENAME, "w") as file:
        for book in library:
            read_status = "Read" if book["read"] else "Unread"
            file.write(f"{book['title']} | {book['author']} | {book['year']} | {book['genre']} | {read_status}\n")
    print("Library saved to file. Goodbye!")

def add_book():
    print("\nAdd a Book")
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: ").strip())
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_input == "yes"

    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read}
    library.append(book)
    print("Book added successfully!")

def remove_book():
    print("\nRemove a Book")
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_book():
    print("\nSearch for a Book")
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    keyword = input("Enter the title/author: ").strip().lower()

    matches = []
    for book in library:
        if (choice == '1' and keyword in book["title"].lower()) or \
           (choice == '2' and keyword in book["author"].lower()):
            matches.append(book)

    if matches:
        print("Matching Books:")
        for idx, b in enumerate(matches, 1):
            status = "Read" if b["read"] else "Unread"
            print(f"{idx}. {b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {status}")
    else:
        print("No matching books found.")

def display_books():
    print("\nDisplay All Books")
    if not library:
        print("Your library is empty.")
    else:
        print("Your Library:")
        for idx, book in enumerate(library, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_stats():
    print("\nDisplay Statistics")
    total = len(library)
    if total == 0:
        print("No books in the library.")
        return
    read_count = sum(1 for book in library if book["read"])
    print(f"Total books: {total}")
    print(f"Percentage read: {read_count / total * 100:.1f}%")

def menu():
    print("Welcome to your Personal Library Manager!")
    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_books()
        elif choice == '5':
            display_stats()
        elif choice == '6':
            save_library()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    load_library()
    menu()
