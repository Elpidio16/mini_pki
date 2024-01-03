import os
import json
import hashlib

def create_database(db_name):
    if not os.path.exists('databases'):
        os.mkdir('databases')
    if os.path.exists(f'databases/{db_name}.json'):
        return
    
    with open(f'databases/{db_name}.json', 'w') as file:
        json.dump({}, file, indent=4)

       
def load_database(db_name):
    if not os.path.exists(f'databases/{db_name}.json'):
        create_database(db_name)

    with open(f'databases/{db_name}.json', 'r') as file:
        return json.load(file)
    

def check_user(db_name, email):
    db = load_database(db_name)
    return email in db


def add_user(db_name, email, password):
    db = load_database(db_name)
    db[email] = password
    with open(f'databases/{db_name}.json', 'w') as file:
        json.dump(db, file, indent=4)


def update_user(db_name, email, password):
    db = load_database(db_name)
    db[email] = password
    with open(f'databases/{db_name}.json', 'w') as file:
        json.dump(db, file, indent=4)



def delete_user(db_name, email):
    db = load_database(db_name)
    del db[email]
    with open(f'databases/{db_name}.json', 'w') as file:
        json.dump(db, file, indent=4)


def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


