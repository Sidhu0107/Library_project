from librarian import add_book, issue_book, return_book

# Add a test book
add_book("12345", "Test Driven Dev", "Kent Beck", "5")

# Issue the book to a test member
issue_book("test-member", "12345")

# (You’ll need to manually fetch the LoanID from loans.csv and call return_book(loan_id))
