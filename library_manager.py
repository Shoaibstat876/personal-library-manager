# 📚 Personal Library Manager
# Developed by Shoaib 💖

import json

LIBRARY_FILE = "library.txt"

# Load existing library or create new one
try:
    with open(LIBRARY_FILE, "r") as file:
        library = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    library = []

# Function to add a book
def add_book():
    title = input("📖 Enter the book title: ")
    author = input("✍️ Enter the author: ")
    year = input("📅 Enter the publication year: ")
    genre = input("🎭 Enter the genre: ")
    read_status = input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }

    library.append(book)
    print("✅ Book added successfully!\n")

# Function to display books
def display_books():
    if not library:
        print("📚 Your library is empty! Add some books first.\n")
        return

    print("\n📖 Your Library:")
    for index, book in enumerate(library, 1):
        read_status = "✅ Read" if book["read"] else "❌ Unread"
        print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    print("\n")

# Function to remove a book
def remove_book():
    display_books()
    if not library:
        return

    try:
        choice = int(input("❌ Enter the book number to remove: ")) - 1
        if 0 <= choice < len(library):
            removed_book = library.pop(choice)
            print(f"✅ Removed: {removed_book['title']} by {removed_book['author']}\n")
        else:
            print("⚠️ Invalid selection!")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Function to search for books by title or author
def search_book():
    query = input("🔍 Enter title or author name to search: ").strip().lower()
    results = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]

    if results:
        print("\n🔎 Search Results:")
        for book in results:
            read_status = "✅ Read" if book["read"] else "❌ Unread"
            print(f"📖 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("❌ No matching books found.\n")

# Function to save the library
def save_library():
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file)
    print("💾 Library saved successfully!\n")

# Main menu function
def main_menu():
    while True:
        print("\n📚 Welcome to Personal Library Manager!")
        print("1️⃣ Add a book")
        print("2️⃣ Display all books")
        print("3️⃣ Remove a book")
        print("4️⃣ Search for a book")
        print("5️⃣ Save and Exit")

        choice = input("👉 Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            save_library()
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please select a valid option.\n")

# Run the program
if __name__ == "__main__":
    main_menu()
