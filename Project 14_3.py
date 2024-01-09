#!/usr/bin/env python3

import csv
from dataclasses import dataclass


FILENAME = "customers.csv"

customerz = []
def read_csv():
    
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            customerz.append(row)
        customerz.pop(0)
    return customerz   

class Customer:
    def __init__(self, cust_id,
                 first_name, last_name,
                 company_name, address,
                 city, state, zip):
        self.id = cust_id
        self.firstName = first_name
        self.lastName = last_name
        self.company = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

def getFullName(self):
    fullName = self.firstName + " " + self.lastName
    return fullName

def getFullAddress(self):
    a = self.getFullName() + "\n"
    if self.company != "":
        a += self.company + "\n"
        a += self.address + "\n"
        a += self.city + ", " + self.state + " " + self.zip
        return a

def dispaly_title():
    print("Customer Viewer")
    print()
    
def input_id(customerz):
    
    c_id = input("Enter customer ID: ")
    for customers in customerz:
        if c_id == customers[0]:
            print(f"{customers[1]} {customers[2]}")
            if customers[3] == "":
                pass
            else:
                print(f"{customers[3]}")
            print(f"{customers[4]}")
            print(f"{customers[5]}, {customers[6]} {customers[7]}")
            print()
            break
    else:
        print()
        print("No customer with that ID")
        print()

def main():
    dispaly_title()
    read_csv()
    choice = "y"
    while choice.lower() == "y":
        input_id(customerz)
        
        
        choice = input("Continue? (y/n): ")
        print()
    print("Bye!")
    
if __name__ == "__main__":
    main()    