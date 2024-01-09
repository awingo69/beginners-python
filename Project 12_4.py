#!/usr/bin/env python3

FILENAME = "monthly_sales.txt"

def write_months(sales):
    with open(FILENAME, "w") as file:
        for month, amount in sales.items():
            file.write(month + "\t" + str(amount) + "\n")
sales = {}

def read_months():
    with open (FILENAME, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            row = line.split("\t")
            sales[row[0]] = int(row[1]) 
        return sales

def display_title():
    print ("Monthly Sales Program")
    print()
    
def command_list():
    print ("COMMAND MENU")
    print ("view - View sales for specified month")
    print ("edit - Edit sales for specified month")
    print ("totals - View sales summary for year")
    print ("exit - Exit program")
    print()
    
def edit(sales):
    month = input("Three-letter Month: ")
    month = month.title()
    if month in sales.keys():
        amount = int(input("Sales Amount: "))
        sales[month] = amount
        write_months(sales)
        print("Sales amount for {:s} is {:,.2f}.".format(month, amount))
        print()
    else:
        print("Invalid three-letter month.") 
        print()
    
        
def view(sales):
    month = input("Three-letter Month: ")
    month = month.title()
    if month in sales.keys():
        print("Sales amount for {:s} is {:,.2f}.".format(month, sales[month]))
        print()
    else:
        print(" Invalid three-letter month.")    
        print()
    
def totals(sales):
    for amount in sales.values():
       total = int(sum(sales.values()))
        
    year_tot = total    
    month_av = (year_tot)/12    
    
    print(f"Yearly total: {year_tot:,.2f}")
    print(f"Monthly average: {month_av:,.2f}")
    print()
    
def main():
    display_title()
    command_list()
    read_months()
    
    while True:
        command = input("Command: ")
        if command.lower() == "view":
            view(sales)
        elif command.lower() == "edit":
            edit(sales)
        elif command.lower() == "totals":
            totals(sales)
        elif command.lower() == "exit":
            print("Bye!")
            break    
    
    
if __name__ == "__main__":
    main()    