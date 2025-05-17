import streamlit as st
from auth import register_member, login
from librarian import librarian_dashboard
from member import member_dashboard

st.set_page_config(page_title="📚 Library Management System", layout="centered")

if "user" not in st.session_state:
    st.session_state.user = None

st.title("📚 Library Management System")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if st.session_state.user is None:
    if choice == "Login":
        st.subheader("🔐 Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        role = st.radio("Login as", ["Member", "Librarian"])
        if st.button("Login"):
            user = login(email, password)
            if user:
                st.session_state.user = user
                st.session_state.role = role
                st.success(f"Logged in as {user.Name} ({role})")
            else:
                st.error("Invalid credentials.")
    else:
        st.subheader("📝 Register")
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Register"):
            success, msg = register_member(name, email, password)
            if success:
                st.success(msg)
            else:
                st.error(msg)
else:
    role = st.session_state.role
    if role == "Librarian":
        librarian_dashboard()
    else:
        member_dashboard()

    if st.button("Logout"):
        st.session_state.user = None
        st.session_state.role = None
