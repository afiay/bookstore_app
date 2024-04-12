import json
from pymongo import MongoClient

# Connect to MongoDB (ensure MongoDB is running locally)
client = MongoClient('mongodb://localhost:27017/')
db = client.bookstore
books = db.books

# Load initial data into the database


def load_initial_data():
    with open('initial_books.json', 'r') as file:
        book_data = json.load(file)
    books.insert_many(book_data)


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    book = {"title": title, "author": author, "price": price, "stock": stock}
    books.insert_one(book)
    print("Book added successfully!")


def view_all_books():
    for book in books.find():
        print(book)


def list_books_and_select():
    books_cursor = books.find()
    book_list = list(books_cursor)
    if not book_list:
        print("No books available.")
        return None
    for index, book in enumerate(book_list):
        print(f"{index + 1}. {book['title']} by {book['author']
                                                 } - ${book['price']} (Stock: {book['stock']})")
    choice = input("Enter the number of the book you want to select: ")
    try:
        selected_index = int(choice) - 1
        if 0 <= selected_index < len(book_list):
            return book_list[selected_index]
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
    return None


def search_book_by_title():
    title = input("Enter title to search for: ")
    # 'i' for case-insensitive
    # Regex query, which will allow partial matches like searching "hello" in "hello book" or "book hello".
    regex_pattern = {'$regex': title, '$options': 'i'}
    for book in books.find({"title": regex_pattern}):
        print(book)


def update_book_price():
    print("Select a book to update its price:")
    selected_book = list_books_and_select()
    if selected_book:
        new_price = float(input("Enter new price: "))
        books.update_one({'_id': selected_book['_id']}, {
                         '$set': {'price': new_price}})
        print(f"Price updated successfully for {selected_book['title']}!")


def delete_book():
    print("Select a book to delete:")
    selected_book = list_books_and_select()
    if selected_book:
        books.delete_one({'_id': selected_book['_id']})
        print(f"Book deleted successfully: {selected_book['title']}")



def view_books_by_author():
    author = input("Enter author's name: ")
    for book in books.find({"author": author}):
        print(book)


def view_books_in_stock():
    for book in books.find({"stock": {"$gt": 0}}):
        print(book)


def reverse_engineer_schema():
    print("Analyzing collection schema...")
    schema = {}
    sample_size = 100
    for book in books.find().limit(sample_size):
        for key, value in book.items():
            if key not in schema:
                schema[key] = set()
            schema[key].add(type(value).__name__)
    for key, types in schema.items():
        print(f"{key}: {', '.join(types)}")

# Main menu function


def main_menu():
    while True:
        print("\n--- Hello and welcome to the awesome Lexicon bookstore! ---")
        print("1. Add a book")
        print("2. View all books")
        print("3. Search a book by title")
        print("4. Update a book price")
        print("5. Delete a book")
        print("6. View books by author")
        print("7. View books in Stock")
        print("8. Reverse Engineer Schema")
        print("9. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            view_all_books()
        elif choice == '3':
            search_book_by_title()
        elif choice == '4':
            update_book_price()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            view_books_by_author()
        elif choice == '7':
            view_books_in_stock()
        elif choice == '8':
            reverse_engineer_schema()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")


if __name__ == "__main__":
    main_menu()
