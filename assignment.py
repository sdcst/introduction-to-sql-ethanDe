#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""

import sqlite3

file = "data_vet.db"
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()

query = """
create table if not exists customers (
    id integer primary key autoincrement,
    pet_name tinytext,
    pet_species tinytext,
    pet_breed tinytext,
    owner_name tinytext,
    owner_phone_number tinytext,
    owner_email tinytext,
    owner_balance float,
    date_of_first_visit tinytext);
    """
cursor.execute(query)

def customer():
    id = int(input("Unique Integer Identifier: "))
    pet_name = str(input("Pet's Name: "))
    pet_species = str(input("Pet's Species: "))
    pet_breed = str(input("Pet's Breed: "))
    owner_name = str(input("Owner's Name: "))
    owner_phone_number = str(input("Phone Number: "))
    owner_email = str(input("Email: "))
    owner_balance = float(input("Balance: "))
    date_of_first_visit = str(input("First visit (MM/DD/YYYY): "))
    query = f"""
    insert into customers (id, pet_name, pet_species, pet_breed, owner_name, owner_phone_number, owner_email, owner_balance, date_of_first_visit) values ('{id}', '{pet_name}', '{pet_species}','{pet_breed}', '{owner_name}','{owner_phone_number}', '{owner_email}','{owner_balance}','{date_of_first_visit}');
    """
    cursor = connection.cursor()
    cursor.execute(query)

def datascanbyid():
    id = input("Enter ID: ")
    query = f'select * from customers where id = "{id}"'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    
def datascanbyemail():
    email = input("Enter email: ")
    query = f'select * from customers where owner_email = "{email}"'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

def datascanbyphone():
    phone = input("Enter phone: ")
    query = f'select * from customers where owner_phone_number = {phone}'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

def useroption():
    opt = input("Enter 'e' to access existing information; enter 'n' to submit new information; or 'c' to close the program: ")
    if opt == 'e':
        funct = input("Retrieve data by\n('a') - ID \n('b') - phone \n('c') - email \nYour selection: ")
        if funct == "a":
            datascanbyid()
        elif funct == "b":
            datascanbyphone()
        elif funct == "c":
            datascanbyemail()
    elif opt == 'n':
        customer()
    elif opt == 'c':
        exit()

if __name__ == "__main__":
    while True:
        useroption()
    