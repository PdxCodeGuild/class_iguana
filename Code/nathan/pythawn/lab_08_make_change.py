non_converted_pennies = int(input('how many pennies do you have?\n >'))

quarters = non_converted_pennies // 25
non_converted_pennies %= 25

dimes = non_converted_pennies // 10
non_converted_pennies = non_converted_pennies % 10

nickels = non_converted_pennies // 5
non_converted_pennies = non_converted_pennies % 5

pennies = non_converted_pennies // 1
non_converted_pennies = non_converted_pennies % 1

print(f" you got {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")

