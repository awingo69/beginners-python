#!/usr/bin/env python3

# message display
print("Registration Form")
print()

# input from user
firstName = input("First name:\t")
lastName = input("Last name:\t")
birthYear = input("Bitrh year:\t")
print()

#full message 
print(f"Welcome {firstName} {lastName}!")
print("Your registration is complete.")
print(f"Your temporary password is : {firstName}*{birthYear}.")