# # Write your code here
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")
# print()
#
# water_per_cup = 200
# milk_per_cup = 50
# coffee_per_cup = 15
# print("Write how many cups of coffee you will need:")
# cups_needed = int(input("> "))
# print("For " + str(cups_needed) + " cups of coffee you will need:")
# print(str(cups_needed * water_per_cup) + " ml of water")
# print(str(cups_needed * milk_per_cup) + " ml of milk")
# print(str(cups_needed * coffee_per_cup) + " g of coffee beans")


class CoffeeMachine:
    # water = 400
    # milk = 540
    # beans = 120
    # cups = 9
    # money = 550
    # state = None

    def __init__(self, water, milk, beans, cups, money, state):
        self.water = water
        self.milk = milk
        self. beans = beans
        self.cups = cups
        self.money = money
        self.state = state

    def input_(self, state):
        self.state = state
        action = self.state
        while action != "exit":
            if action == "buy":
                choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")
                if choice == '1' and self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                    print("I have enough resources, making you a coffee!\n")
                    self.water -= 250
                    self.beans -= 16
                    self.money += 4
                    self.cups -= 1
                elif self.water < 250:
                    print("Sorry, not enough water!\n")
                elif self.beans < 16:
                    print("Sorry, not enough beans!\n")
                elif self.cups < 1:
                    print("Sorry, not enough cups!\n")
                elif choice == '2' and self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups > 1:
                    print("I have enough resources, making you a coffee!\n")
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.money += 7
                    self.cups -= 1
                elif self.water < 350:
                    print("Sorry, not enough water!\n")
                elif self.milk < 75:
                    print("Sorry, not enough milk!\n")
                elif self.beans < 20:
                    print("Sorry, not enough beans!\n")
                elif self.cups < 1:
                    print("Sorry, not enough cups!\n")
                elif choice == '3' and self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                    print("I have enough resources, making you a coffee!\n")
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.money += 6
                    self.cups -= 1
                elif self.water < 200:
                    print("Sorry, not enough water!\n")
                elif self.milk < 100:
                    print("Sorry, not enough milk!\n")
                elif self.beans < 12:
                    print("Sorry, not enough beans!\n")
                elif self.cups < 1:
                    print("Sorry, not enough cups!\n")
                elif choice == "back":
                    pass
            elif action == "fill":
                self.water += int(input("Write how many ml of water do you want to add:\n> "))
                self.milk += int(input("Write how many ml of milk do you want to add:\n> "))
                self.beans += int(input("Write how many grams of coffee beans do you want to add:\n> "))
                self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n> "))
            elif action == "take":
                print("I gave you $", self.money)
                self.money = 0
                print()
            elif action == "remaining":
                print("The coffee machine has:")
                print(self.water, "of water")
                print(self.milk, "of milk")
                print(self.beans, "of coffee beans")
                print(self.cups, "of disposable cups")
                print(self.money, "of money")
                print()
            else:
                break
            action = machine1.input_(input("Write action (buy, fill, take, remaining, exit):\n> ").strip().lower())


machine1 = CoffeeMachine(400, 540, 120, 9, 550, '')
machine1.input_(input("Write action (buy, fill, take, remaining, exit):\n> ").strip().lower())



