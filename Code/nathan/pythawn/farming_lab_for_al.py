class Farmer:
    def __init__(self, energy, filth, day_light, milk, eggs, bacon, money):
        self.energy = energy
        self.filth = filth
        self.day_light = day_light
        self.milk = milk
        self.eggs = eggs
        self.bacon = bacon
        self.money = money

    def farm(self):
        self.day_light = self.day_light - 2
        self.filth = self.filth + 1
        self.energy = self.energy - 1
        if self.energy <= 0 or self.day_light <= 0:
            print('You ran out of energy and died')
            exit()
        if self.filth > 5:
            print('You got so stinky all the animals left you')
            exit()
        else:
            return f'energy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def bathe(self):
        self.day_light = self.day_light - 1
        self.filth = 0
        if self.energy <= 0 or self.day_light <= 0:
            print('You ran out of energy and died')
            exit()
        else:
            return f'energy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def sleep(self):
        self.day_light = 10
        self.energy = 5
        return f'energy: {self.energy}, filth: {self.filth}, day light: {self.day_light}'

    def milk_cow(self):
        self.milk += 1
        return f'You have {self.milk} gallon of milk'

    def farm_chicken(self):
        self.eggs += 2
        return f'You have {self.eggs} eggs'

    def make_bacon(self):
        self.bacon += 4
        return f'You have {self.bacon} pounds of bacon'

    def make_money(self):
        self.milk *= 2
        self.bacon *= 3
        self.money += self.milk + self.eggs + self.bacon
        return f'you made {self.money} dollars'

    def check_wallet(self):
        return self.money

print('you are just a simple farmer and you heart is on the farm')
print('you can take a farmer from the farm but you can never take a farm from the farmer\n...')
farmer = Farmer(5, 0, 10, 0, 0, 0, 0)
while True:
    task = input('\nHowdy, what would you like to do?\n(farm)\n(bathe)\n(sleep)\n(sell)\n(check wallet)\n**type \'city boy\' to leave the farm\n>')
    if task == 'farm':
        print(farmer.farm())
        animal = input('which animal are you looking to farm?\n(cow)\n(chicken)\n(pig)\n>')
        if animal == 'cow':
            print(farmer.milk_cow())
        elif animal == 'chicken':
            print(farmer.farm_chicken())
        elif animal == 'pig':
            print(farmer.make_bacon())
    elif task == 'bathe':
        print(farmer.bathe())
    elif task == 'sleep':
        print(farmer.sleep())
    elif task == 'sell':
        print(farmer.make_money())
    elif task == 'city boy':
        print('Thank you, come again')
        break



