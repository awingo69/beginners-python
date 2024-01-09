#!/usr/bin/env python3

#title with lines
print("============================================================")
print("Shipping Calculator")
print("============================================================")
#cost and shipping input
choice = "y"
while choice.lower() == "y" : 
    
    itemCost = float(input("Cost of items ordered: \t"))
    if itemCost < 0:
        print("You must enter a postive number. Please try again.") 
        continue
    
    if itemCost < 30.00 :
        shipCost = 5.95
    elif itemCost <= 49.99 :
        shipCost = 7.95
    elif itemCost <= 74.99 :
        shipCost = 9.95
    else:
        shipCost = 0
    
        
    
    print(f"Shipping cost: \t\t{shipCost}")
    totalCost = round(itemCost + shipCost , 2)
    print(f"Total cost: \t\t{totalCost}")

    print()
    choice = input("Continue? (y/n): ")
    
    print("============================================================")
#ending

print("Bye!")