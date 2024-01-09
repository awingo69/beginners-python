#!/usr/bin/env python3

# display welcome message
print("Price Comparison")
print()

# get input from user
p64 = float(input("Price of 64 oz size:\t"))
p32 = float(input("Price of 32 oz size:\t"))

# calclate and round price per oz
price64oz = round(p64 / 64, 2)
price32oz = round(p32 /32, 2)

# display the result
print()
print(f"Price per oz (64 oz):\t{price64oz}")
print(f"Price per oz (32 oz):\t{price32oz}")