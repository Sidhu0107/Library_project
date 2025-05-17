import streamlit as st
from auth import login, register_member
from member import member_dashboard
from librarian import librarian_dashboard

st.set_page_config(page_title="Library System", layout="centered")

if "user" not in st.session_state:
    st.session_state.user = None
if "role" not in st.session_state:
    st.session_state.role = None

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if st.session_state.user:
    if st.session_state.role == "librarian":
        librarian_dashboard()
    else:
        member_dashboard(st.session_state.user)

elif choice == "Login":
    st.subheader("🔐 Login")
    role = st.selectbox("Role", ["Member", "Librarian"])
    id_or_email = st.text_input("Member ID" if role == "Member" else "Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if role == "Member":
            user = login(id_or_email, password)
            if user:
                st.session_state.user = user
                st.session_state.role = "member"
                st.success(f"Welcome, {user.Name}!")
                st.experimental_rerun()
            else:
                st.error("Invalid credentials.")
        elif role == "Librarian":
            if id_or_email == "admin@mail.com" and password == "admin123":
                st.session_state.user = {"Name": "Admin"}
                st.session_state.role = "librarian"
                st.success("Welcome Librarian!")
                st.experimental_rerun()
            else:
                st.error("Invalid librarian credentials.")

elif choice == "Register":
    st.subheader("📝 Member Registration")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        success, msg = register_member(name, email, password)
        if success:
            st.success(msg)
        else:
            st.error(msg)
