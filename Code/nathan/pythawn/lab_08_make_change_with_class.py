class Change_creator:

    def __init__(self, non_converted_pennies):
        self.non_converted_pennies = non_converted_pennies

    def quarters(self, non_converted_pennies):
        self.non_converted_pennies = non_converted_pennies // 25
        return self.non_converted_pennies % 25

    def dimes(self, non_converted_pennies):
        self.non_converted_pennies = non_converted_pennies // 10
        return self.non_converted_pennies % 10

    def nickels(self, non_converted_pennies):
        self.non_converted_pennies = non_converted_pennies // 5
        return self.non_converted_pennies % 5

    def pennies(self, non_converted_pennies):
        self.non_converted_pennies = non_converted_pennies // 1
        return self.non_converted_pennies % 1


non_converted_pennies = int(input('how many pennies do you have?\n >'))
change = Change_creator(non_converted_pennies)

print(f" you got {change.quarters(non_converted_pennies)} quarters, {change.dimes(non_converted_pennies)} dimes, {change.nickels(non_converted_pennies)} nickels, {change.pennies(non_converted_pennies)} pennies")