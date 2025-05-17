import streamlit as st
from storage import load_books, load_loans
from models import Loan

def member_dashboard(user):
    st.subheader(f"👤 Welcome, {user.Name}")

    menu = ["Search Books", "My Loans"]
    choice = st.selectbox("Menu", menu)

    if choice == "Search Books":
        books = load_books()
        keyword = st.text_input("Enter title or author keyword")
        if keyword:
            results = [b for b in books if keyword.lower() in b.Title.lower() or keyword.lower() in b.Author.lower()]
            for b in results:
                st.text(f"{b.Title} by {b.Author} (Available: {b.CopiesAvailable})")

    elif choice == "My Loans":
        loans = load_loans()
        user_loans = [l for l in loans if l.MemberID == user.MemberID]
        for l in user_loans:
            st.write(f"Loan ID: {l.LoanID}, ISBN: {l.ISBN}, Issue: {l.IssueDate}, Due: {l.DueDate}, Returned: {l.ReturnDate or '❌'}")
