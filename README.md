
# 📚 Personal Library Manager

A command-line Python program that helps users manage their personal book collection. Users can add, remove, search, and view book details, as well as track which books they’ve read. The library is saved to a file for persistence.

---

## ✅ Features

- 📖 Add a book (title, author, year, genre, read status)
- ❌ Remove a book by title
- 🔍 Search by title or author
- 📋 Display all books
- 📊 Show statistics (total books, % read)
- 💾 Automatically save/load to `library.txt`

---

## 💻 How to Run

1. Make sure Python is installed.
2. Save the code as `library_manager.py`.
3. Open terminal / command prompt.
4. Run the program:

```bash
python library_manager.py
```

---

## 🗂 Sample `library.txt` Format

Each line = 1 book:

```
The Great Gatsby | F. Scott Fitzgerald | 1925 | Fiction | Read
1984 | George Orwell | 1949 | Dystopian | Unread
```

---

## 📦 Requirements

- Python 3.x
- No external libraries needed

---

## ✨ Sample Output

```
Menu
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
Enter your choice:
```

---

## 🔐 Tips

- Edit `library.txt` to manually add books
- Back it up to keep your library safe!
