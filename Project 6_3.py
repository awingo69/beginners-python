#!/usr/bin/env python3

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
def list(contact_name):
    for i, name in enumerate(contact_name, start=1):
        print(f"{i}. {name}")
    print()
    
#view a contact
def view(contact_name, contact_email, contact_phone):
    number = int(input("Number: "))
    if number < 1 or number > len(contact_name):
        print("Invalid contact number, please try again. \n")
    else:
        name = contact_name[number-1]
        email = contact_email[number-1]
        phone = contact_phone[number-1]

        print("Name: ", name)
        print("Email: ", email)
        print("Phone: ", phone)
        print()
    
#add the contact
def add(contact_name, contact_email, contact_phone):
    name = input("Name: ")
    email = input("Email: ")
    phonen = input("Phone: ")
    contact = []
   
    contact_name.append(name)
    contact_email.append(email)
    contact_phone.append(phonen)    
    
    
    print(f"{name} was added.") 
    print()
    

#remove contact
def delete(contact_name):
    number = int(input("Number: "))
    if number < 1 or number > len(contact_name):
        print("Invalid contact number, please try again. \n")
    else:
        name = contact_name.pop(number-1)
        print(f"{name} was deleted.")
    print()
    return contact_name

def main():

    contact_name = ['Guido van Rossum', 'Eric Idle']
    contact_email = ['kokoko@ggmil.com','eric@ericidle.com']
    contact_phone = ['+11 32 1235 1247','+44 20 7946 0958']
   
    
    display_title()
    print()
    command_menu()
    


#make the list/commands


    i = 1
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list(contact_name)
        elif command.lower() == "view":
            view(contact_name, contact_email, contact_phone)
        elif command.lower() == "add":
            add(contact_name, contact_email, contact_phone)
        elif command.lower() == "del":
            delete(contact_name)
        elif command.lower() == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command, please try again. \n")

       
            

if __name__ == "__main__":
    main()
    