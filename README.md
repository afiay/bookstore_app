# Awesome Lexicon Bookstore Application

This Python application provides a simple console-based interface for managing a bookstore database using MongoDB. It supports basic CRUD operations and is designed for educational purposes to demonstrate how to interact with MongoDB using Python.

## Features

- Add books to the bookstore database.
- View all books in the database.
- Search for books by title using partial matching.
- Update the price of a book.
- Delete a book from the database.
- View books by a specific author.
- List books that are currently in stock.
- Reverse engineer the database schema to understand the structure of data.
- Exit the program.

## Prerequisites

Before you run the application, make sure you have the following installed:
- Python 3.x
- MongoDB
- pymongo (MongoDB driver for Python)

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/afiay/bookstore_app
    cd <repository-folder>
    ```

2. Set up a virtual environment (Optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install pymongo
    ```

4. Ensure MongoDB is running locally on your machine.

5. Start the application:
    ```bash
    python bookstore.py
    ```

## Usage

Run the script, and you will be greeted with a menu of options. Follow the on-screen prompts to interact with the bookstore database:
