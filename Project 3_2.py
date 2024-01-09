#!/usr/bin/env python3

#Banner

print("Tip Calculator")
print()

#input cost
mealCost = float(input("Cost of Meal: \t"))
print()

#calculate percenage
cp15 = round(.15 * mealCost, 2)
cp20 = round(.20 * mealCost, 2)
cp25 = round(.25 * mealCost, 2)
cp15a = round(mealCost + cp15, 2)
cp20a = round(mealCost + cp20, 2)
cp25a = round(mealCost + cp25, 2)

#tipping at 15%
print("15%")
print(f"Tip amount: \t{cp15}")
print(f"Total amount: \t{cp15a}")
print()

#tipping at 20%
print("20%")
print(f"Tip amount: \t{cp20}")
print(f"Total amount: \t{cp20a}")
print()

#tiping at 25%
print("25%")
print(f"Tip amount: \t{cp25}")
print(f"Total amount: \t{cp25a}")