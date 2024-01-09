#!/usr/bin/env python3

#title
print("Sales Tax Calculator")


#math time
choice = "y"
while choice.lower() == "y" :
    totalCost = 0
    
  
    
    def calc_sales_tax():
        tax = round(totalCost + tax_rate , 2)
        print("Total after tax:\t", tax)
        return tax    
    print()
    print("ENTER ITEMS (ENTER 0 TO END)")
    while True:
        itemCost = float(input("Cost of items:\t"))
        totalCost = itemCost + totalCost
        if itemCost == 0:
            break
    tax_rate = round(.06 * totalCost , 2)
    print(f"Total:  \t\t{totalCost}")
    print(f"Sales tax: \t\t{tax_rate}")
    calc_sales_tax()
    print()
    choice = input("Again? (y/n): ")
    
print()
print("Thanks, bye!")    



#ending
