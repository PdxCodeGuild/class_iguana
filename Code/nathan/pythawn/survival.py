import random

class Survival:
    def __init__(self, food, water, gasoline, meds, crew, ammo, grenade, days):
        self.food = food
        self.water = water
        self.gasoline = gasoline
        self.meds = meds
        self.ammo = ammo
        self.crew = crew
        self.grenade = grenade
        self.days = days
        self.situations = ['Level 1 Zombie', 'Level 2 Zombie', 'Level 3 Zombie', 'Zombie Pack', 'Crew Member Hurt']
        self.fifty_percent = [1, 2]
        self.one_in_three = [1, 2, 3]

    # 'Encounter Another Crew', 'Abandoned Vehicle'
    def display_stats(self):
        return f"You currently have {self.food}-lb of food, {self.water} gallons of water, {self.gasoline} gallons of gasoline, {self.meds} medical kits, {self.crew} crew members, {self.ammo} rounds of ammunition, and {self.grenade} grenade(s)..."

    def search_for_supplies(self):
        if random.choice(self.situations) == 'Level 1 Zombie':
            print('A Level 1 Zombie has appeared, it takes 5 rounds of ammo to kill')
            kill = input('would you like to kill the zombie')
            if kill == 'yes':
                if random.choice(self.one_in_three) == 1:
                    print('\na crew member was killed by the zombie...\n')
                    self.crew -= 1
                    self.ammo -= 5
                    return f'\nyou killed the zombie, you have {self.ammo} rounds of ammo'
                elif random.choice(self.one_in_three) == 2 or 3:
                    self.ammo -= 5
                    return f'\nyou killed the zombie, you have {self.ammo} rounds of ammo'
        elif random.choice(self.situations) == 'Level 2 Zombie':
            print('A Level 2 Zombie has appeared, it takes 10 rounds of ammo to kill')
            kill = input('\nwould you like to kill the zombie')
            if kill == 'yes':
                if random.choice(self.one_in_three) == 1:
                    print('a crew member was killed by the zombie...\n')
                    self.crew -= 1
                    self.ammo -= 10
                    return f'\nyou killed the zombie, you have {self.ammo} rounds of ammo'
                elif random.choice(self.one_in_three) == 2 or 3:
                    self.ammo -= 10
                    return f'\nyou killed the zombie, you have {self.ammo} rounds of ammo'
        elif random.choice(self.situations) == 'Level 3 Zombie':
            print('A Level 3 Zombie has appeared, it takes 15 rounds of ammo to kill')
            kill = input('would you like to kill the zombie')
            if kill == 'yes':
                if random.choice(self.one_in_three) == 1:
                    print('\na crew member was killed by the zombie...\n')
                    self.crew -= 1
                    self.ammo -= 15
                    return f'\nyou killed the zombie, you have {self.ammo} rounds of ammo'
                elif random.choice(self.one_in_three) == 2 or 3:
                    self.ammo -= 15
                    return f'\nyou killed the zombie, you have {self.ammo} rounds of ammo'
        elif random.choice(self.situations) == 'Zombie Pack':
            print('A Zombie Pack has appeared, it takes 1 grenade to kill')
            kill = input('\nwould you like to kill the zombie pack')
            if kill == 'yes':
                if random.choice(self.one_in_three) == 1:
                    print('\na crew member was killed by the zombie pack...\n')
                    self.crew -= 1
                    self.grenade -= 1
                    return f'\nyou killed the zombie pack, you have {self.grenade} grenade(s)'
                elif random.choice(self.one_in_three) == 2 or 3:
                    self.grenade -= 1
                    return f'\nyou killed the zombie pack, you have {self.grenade} grenade(s)'
        elif random.choice(self.situations) == 'Crew Member Hurt':
            print('A crew member has been injured, you need two medical kits to save them')
            save = input('\nwould you like to save your crew member')
            if save == 'yes':
                self.meds -= 2
                return '\nyou saved the crew member'
            elif save == 'no':
                self.crew -= 1
                return '\nyour crew member died'



    def end_of_day(self):
        self.food -= 10
        self.water -= 5
        self.days += 1
        # if self.food or self.water == 0:
        # if self.crew == 0:
        #     exit()
        # if self.ammo == 0:
        #     exit()
        # if self.meds == 0:
        #     exit()
        return f"\nFood:{self.food}-lb.\nWater:{self.water} gallons.\nIt is now day {self.days}."




survival = Survival(100, 50, 50, 20, 5, 50, 2, 1)

fifty_percent = [1, 2]
one_in_three = [1, 2, 3]



input('Something has gone horribly wrong...\n(press enter)')
input('A zombie outbreak has occured, the world has been without power for 1 month now.\n(press enter)')
input('You joined a crew of 4 other survivers. They seem fairly trustworthy.\n(press enter)')

while True:

    make_choice = input('\nWhat would you like to do?\n\t(check stats)\n\t(search for supplies)\n')
    if make_choice == 'check stats':
        print(survival.display_stats())
    if make_choice == 'search for supplies':
        print(survival.search_for_supplies())
        print(survival.end_of_day())





