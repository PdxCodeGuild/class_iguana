#lab_8_make_change.py
#Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136. Then #break that 136 into quarters (5), dimes (1), nickles (0) and pennies (1).
unconverted_pennies = input("How many pennies are you bringing in? >")
unconverted_pennies = int(unconverted_pennies)
quarters = unconverted_pennies // 25
quarters_removed = quarters * 25
unconverted_pennies = unconverted_pennies - quarters_removed
dimes = unconverted_pennies // 10
dimes_removed = dimes * 10
unconverted_pennies = unconverted_pennies - dimes_removed
nickels = unconverted_pennies // 5
nickels_removed = nickels * 5
unconverted_pennies = unconverted_pennies - nickels_removed
print(f"Here you go, \n{quarters} quarters, and \n{dimes} dimes and \n{nickels} nickels and \n{unconverted_pennies} pennies")
