import re, sys, time
import database_manager as dbm



def get_id():
    # recevoir l'email comme certificat

    pattern = r"\b[A-Za-z0-9.-_]+@[A-Za-z0-9]+\.[a-z]{2,7}\b"
    try:
        email = input("Enter your email: ")
        assert re.match(pattern, email)
    except: 
        print("Invalid email. Try again")
        return get_id()
    else:
        return email
    
    
def get_password():
    # recevoir le mot de passe comme certificat
    try:
        password = input("Enter your password (min 8): ")
        assert len(password) >= 8
    except: 
        print("Invalid password. Try again")
        return get_password()
    else:
        return password    


def create_user():
    id = get_id()
    while dbm.check_user('users', id):
        print("User already exists. Try again")
        id = get_id()
    password = get_password()
    current_time = time.time()
    values = {'index': current_time, 'password': dbm.encrypt_password(password)}
    # add to database
    dbm.add_user('users', id, values)


def login():
    id = get_id()
    while not dbm.check_user('users', id):
        print("User does not exist. Try again")
        id = get_id()
    password = get_password()
    while dbm.load_database('users')[id]['password'] != dbm.encrypt_password(password):
        print("Wrong password. Try again")
        password = get_password()
    print("Login successful")
    return id