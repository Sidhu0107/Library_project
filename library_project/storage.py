import csv
import os
from models import Book, Member, Loan

DATA_DIR = "data"

def load_books():
    path = os.path.join(DATA_DIR, "books.csv")
    with open(path, newline='') as f:
        return [Book(row['ISBN'], row['Title'], row['Author'], int(row['CopiesTotal']), int(row['CopiesAvailable']))
                for row in csv.DictReader(f)]

def save_books(books):
    path = os.path.join(DATA_DIR, "books.csv")
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Book.__annotations__.keys())
        writer.writeheader()
        for book in books:
            writer.writerow(book.__dict__)

def load_members():
    path = os.path.join(DATA_DIR, "members.csv")
    with open(path, newline='') as f:
        return [Member(**row) for row in csv.DictReader(f)]

def save_members(members):
    path = os.path.join(DATA_DIR, "members.csv")
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Member.__annotations__.keys())
        writer.writeheader()
        for member in members:
            writer.writerow(member.__dict__)

def load_loans():
    path = os.path.join(DATA_DIR, "loans.csv")
    with open(path, newline='') as f:
        return [Loan(**row) for row in csv.DictReader(f)]

def save_loans(loans):
    path = os.path.join(DATA_DIR, "loans.csv")
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Loan.__annotations__.keys())
        writer.writeheader()
        for loan in loans:
            writer.writerow(loan.__dict__)
