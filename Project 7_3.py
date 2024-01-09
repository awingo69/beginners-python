#!/usr/bin/env python3
#totally didn't just copy 6.3 lab

import csv

FILENAME = "contacts.csv"

def write_contacts(contactz):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contactz)
        
def read_contacts():
    contactz = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contactz.append(row)
    return contactz



def display_title():
    print("Contact Manager")

def command_menu():
    print("COMMAND MENNU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()
    
#list the contacts
def list_contacts(contactz):
    for i, contacts in enumerate(contactz, start=1):
        print(f"{i}. {contacts[0]}")
    print()

    
#view a contact
def view(contactz):
    number = int(input("Number: "))
    if number < 1 or number > len(contactz):
        print("Invalid contact number, please try again. \n")
    else:
        name = contactz[number-1][0]
        email = contactz[number-1][1]
        phone = contactz[number-1][2]

        print("Name: ", name)
        print("Email: ", email)
        print("Phone: ", phone)
        print()
    
#add the contact
def add(contactz):
    addcontactz = []
    name = input("Name: ")
    email = input("Email: ")
    phonen = input("Phone: ")
    
    addcontactz.append(name)
    addcontactz.append(email)
    addcontactz.append(phonen)
    
    contactz.append(addcontactz)
    write_contacts(contactz)

    
    print(f"{name} was added.") 
    print()
    

#remove contact
def delete(contactz):
    number = int(input("Number: "))
    if number < 1 or number > len(contactz):
        print("Invalid contact number, please try again. \n")
    else:
        name = contactz.pop(number-1)
        write_contacts(contactz)
        print(f"{name[0]} was deleted.")
    print()
    return contactz

def main():

    
    display_title()
    contacts = read_contacts()
    command_menu()
    


#make the list/commands


    i = 1
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_contacts(contacts)
        elif command.lower() == "view":
            view(contacts)
        elif command.lower() == "add":
            add(contacts)
        elif command.lower() == "del":
            delete(contacts)
        elif command.lower() == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command, please try again. \n")

       
            

if __name__ == "__main__":
    main()
