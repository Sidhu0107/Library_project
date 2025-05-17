import streamlit as st
from storage import load_books, save_books
from models import Book

def librarian_dashboard():
    st.subheader("📚 Librarian Dashboard")

    menu = ["Add Book", "Remove Book", "View Books"]
    choice = st.selectbox("Menu", menu)

    if choice == "Add Book":
        isbn = st.text_input("ISBN")
        title = st.text_input("Title")
        author = st.text_input("Author")
        total = st.number_input("Copies", min_value=1, step=1)
        if st.button("Add"):
            books = load_books()
            books.append(Book(ISBN=isbn, Title=title, Author=author, CopiesTotal=total, CopiesAvailable=total))
            save_books(books)
            st.success("Book added.")

    elif choice == "Remove Book":
        isbn = st.text_input("Enter ISBN to Remove")
        if st.button("Remove"):
            books = load_books()
            books = [b for b in books if b.ISBN != isbn]
            save_books(books)
            st.success("Book removed.")

    elif choice == "View Books":
        books = load_books()
        for b in books:
            st.text(f"{b.Title} by {b.Author} (Available: {b.CopiesAvailable}/{b.CopiesTotal})")
