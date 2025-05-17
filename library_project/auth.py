import bcrypt
from storage import load_members, save_members
from models import Member
import datetime

def register_member(name, email, password):
    members = load_members()
    if any(m.Email == email for m in members):
        return False, "Email already registered."
    member_id = str(1000 + len(members) + 1)
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    new_member = Member(MemberID=member_id, Name=name, Email=email, PasswordHash=password_hash, JoinDate=str(datetime.date.today()))
    members.append(new_member)
    save_members(members)
    return True, "Registration successful. Your Member ID is " + member_id

def login(member_id, password):
    members = load_members()
    for m in members:
        if m.MemberID == member_id and bcrypt.checkpw(password.encode(), m.PasswordHash.encode()):
            return m
    return None
