import random

class Survival:
    def __init__(self, food, water, gasoline, meds, crew, ammo, grenade, days, daily_food, daily_water):
        self.food = food #amount of food
        self.water = water #amount of water
        self.gasoline = gasoline #amoung of gasoline
        self.meds = meds #amount of med kits
        self.ammo = ammo #amount of ammo
        self.crew = crew #number of crew members
        self.grenade = grenade #number of grenades
        self.days = days #number of days surivied
        self.situations = [1, 2, 3, 4, 5, 6, 7, 8] #list of possible situations
        self.fifty_percent = [1, 2] #coin toss
        self.one_in_three = [1, 2, 3] #rock paper scissors
        self.russian_roulette = [1, 2, 3, 4, 5, 6] #russian roulette
        self.daily_food = daily_food #daily food ration
        self.daily_water = daily_water #daily water ration

    # 'Encounter Another Crew', 'Abandoned Vehicle'
    def display_stats(self):
        return f"You currently have {self.food}-lb of food, {self.water} gallons of water, {self.gasoline} gallons of gasoline, {self.meds} medical kits, {self.crew} crew members, {self.ammo} rounds of ammunition, and {self.grenade} grenade(s)..."

    def situation(self):
        current_situation = random.choice(self.situations)
        if current_situation == 1:
            print('A Level 1 Zombie has appeared, it takes 5 rounds of ammo to kill')
            kill = input('would you like to kill the zombie')
            if kill == 'yes':
                if current_situation == 1:
                    print('\na crew member was killed by the zombie...')
                    self.crew -= 1
                    self.ammo -= 5
                    self.daily_food -= 2
                    self.daily_water -= 1
                    return f'you killed the zombie, you have {self.ammo} rounds of ammo'
                elif random.choice(self.one_in_three) == 2 or 3:
                    self.ammo -= 5
                    return f'you killed the zombie, you have {self.ammo} rounds of ammo'
        elif current_situation == 2:
            print('A Level 2 Zombie has appeared, it takes 10 rounds of ammo to kill')
            kill = input('would you like to kill the zombie')
            if kill == 'yes':
                if random.choice(self.one_in_three) == 1:
                    print('\na crew member was killed by the zombie...')
                    self.crew -= 1
                    self.ammo -= 10
                    self.daily_food -= 2
                    self.daily_water -= 1
                    return f'you killed the zombie, you have {self.ammo} rounds of ammo'
                elif random.choice(self.one_in_three) == 2 or 3:
                    self.ammo -= 10
                    return f'you killed the zombie, you have {self.ammo} rounds of ammo'
        elif current_situation == 3:
            print('A Level 3 Zombie has appeared, it takes 15 rounds of ammo to kill')
            kill = input('would you like to kill the zombie')
            if kill == 'yes':
                if random.choice(self.one_in_three) == 1:
                    print('a crew member was killed by the zombie...')
                    self.crew -= 1
                    self.ammo -= 15
                    self.daily_food -= 2
                    self.daily_water -= 1
                    return f'you killed the zombie, you have {self.ammo} rounds of ammo'
                elif random.choice(self.one_in_three) == 2 or 3:
                    self.ammo -= 15
                    return f'you killed the zombie, you have {self.ammo} rounds of ammo'
        elif current_situation == 4:
            print('A Zombie Pack has appeared, it takes 1 grenade to kill')
            kill = input('\nwould you like to kill the zombie pack')
            if kill == 'yes':
                if random.choice(self.one_in_three) == 1:
                    print('a crew member was killed by the zombie pack...')
                    self.crew -= 1
                    self.grenade -= 1
                    self.daily_food -= 2
                    self.daily_water -= 1
                    return f'you killed the zombie pack, you have {self.grenade} grenade(s)'
                elif random.choice(self.one_in_three) == 2 or 3:
                    self.grenade -= 1
                    return f'you killed the zombie pack, you have {self.grenade} grenade(s)'
        elif current_situation == 5:
            print('A crew member has been injured, you need two medical kits to save them')
            save = input('would you like to save your crew member')
            if save == 'yes':
                self.meds -= 2
                return 'you saved the crew member'
            elif save == 'no':
                self.crew -= 1
                self.daily_food -= 2
                self.daily_water -= 1
                return 'your crew member died'
        elif current_situation == 6:
            self.crew += 1
            self.daily_food += 2
            self.daily_water += 1
            return f'You recruited a rogue survivor, you now have {self.crew} crew members'
        elif current_situation == 7:
            self.food //= 2
            self.water //= 2
            self.gasoline //= 2
            self.meds //= 2
            self.ammo //= 2
            self.grenade //= 2
            return f'A thief stole half of your supplies, You now have {self.food}-lb of food, {self.water} gallons of water, {self.gasoline} gallons of gasoline, {self.meds} medical kits, {self.ammo} rounds of ammunition, and {self.grenade} grenade(s)...'
        elif current_situation == 8:
            self.crew -= 1
            self.food //= 2
            self.water //= 2
            self.gasoline //= 2
            self.meds -= self.meds
            self.ammo //= 2
            self.grenade -= self.grenade
            self.daily_food -= 2
            self.daily_water -= 1
            return f'A crew member has gone missing, You now have {self.food}-lb of food, {self.water} gallons of water, {self.gasoline} gallons of gasoline, {self.meds} medical kits, {self.ammo} rounds of ammunition, and {self.grenade} grenade(s)...'


    def search_for_supplies(self):
        self.gasoline -= 5
        if random.choice(self.russian_roulette) == 1:
            self.food += 35
            self.water += 5
            self.gasoline += 5
            self.meds += 0
            self.ammo += 0
            self.grenade += 1
        elif random.choice(self.russian_roulette) == 2:
            self.food += 10
            self.water += 15
            self.gasoline += 0
            self.meds += 2
            self.ammo += 5
            self.grenade += 0
        elif random.choice(self.russian_roulette) == 3:
            self.food += 0
            self.water += 5
            self.gasoline += 15
            self.meds += 0
            self.ammo += 0
            self.grenade += 0
        elif random.choice(self.russian_roulette) == 4:
            self.food += 0
            self.water += 5
            self.gasoline += 0
            self.meds += 20
            self.ammo += 5
            self.grenade += 1
        elif random.choice(self.russian_roulette) == 5:
            self.food += 5
            self.water += 5
            self.gasoline += 0
            self.meds += 0
            self.ammo += 30
            self.grenade += 0
        elif random.choice(self.russian_roulette) == 6:
            self.food += 5
            self.water += 0
            self.gasoline += 0
            self.meds += 2
            self.ammo += 5
            self.grenade += 2
        return f"After gathering supplies, you have: {self.food}-lb of food, {self.water} gallons of water, {self.gasoline} gallons of gasoline, {self.meds} medical kits, {self.ammo} rounds of ammunition, and {self.grenade} grenade(s)..."



    def end_of_day(self):
        self.food -= self.daily_food
        self.water -= self.daily_water
        self.days += 1
        # if self.food or self.water == 0:
        # if self.crew == 0:
        #     exit()
        # if self.ammo == 0:
        #     exit()
        # if self.meds == 0:
        #     exit()
        return f"\nIt is now day {self.days}.\nYou have {self.crew} crew members.\nFood:{self.food}-lb.\nWater:{self.water} gallons."

survival = Survival(100, 50, 50, 10, 5, 50, 2, 1, 10, 5)

input('Something has gone horribly wrong...\n(press enter)')
input('A zombie outbreak has occured, the world has been without power for 1 month now.\n(press enter)')
input('You joined a crew of 4 other survivers. They seem fairly trustworthy.\n(press enter)')

while True:

    make_choice = int(input('\nWhat would you like to do?\n\t[1]check stats\n\t[2]search for supplies\n\t[3]trade\n'))
    if make_choice == 1:
        print(survival.display_stats())
    if make_choice == 2:
        print(survival.situation())
        print(survival.search_for_supplies())
        print(survival.end_of_day())





