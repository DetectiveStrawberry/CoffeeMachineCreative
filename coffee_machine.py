class CoffeeMachine:
    revenue = 0
    products_sold = 0
    water = 0
    milk = 0
    coffee_beans = 0
    cups = 0
    money = 0
    functions_list = ["buy", "fill", "take", "remaining", "stats", "exit"]
    coffee_types = ["1", "2", "3", "back"]

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def make_coffee(self, coffee_type):
        if coffee_type == "1":
            if self.water - 250 <= 0:
                print("Sorry, not enough water!")
                return
            if self.coffee_beans - 16 <= 0:
                print("Sorry, not enough coffee beans!")
                return
            if self.cups - 1 <= 0:
                print("Sorry, not enough cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water = self.water - 250 if self.water > 249 else 0
            self.coffee_beans = self.coffee_beans - 16 if self.coffee_beans > 15 else 0
            self.cups = self.cups - 1 if self.cups > 0 else 0
            self.money = self.money + 4
            self.revenue = self.revenue + 4
        elif coffee_type == "2":
            if self.water - 350 <= 0:
                print("Sorry, not enough water!")
                return
            if self.milk - 75 <= 0:
                print("Sorry, not enough milk!")
                return
            if self.coffee_beans - 20 <= 0:
                print("Sorry, not enough coffee beans!")
                return
            if self.cups - 1 <= 0:
                print("Sorry, not enough cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water = self.water - 350 if self.water > 349 else 0
            self.milk = self.milk - 75 if self.milk > 74 else 0
            self.coffee_beans = self.coffee_beans - 20 if self.coffee_beans > 19 else 0
            self.cups = self.cups - 1 if self.cups > 0 else 0
            self.money = self.money + 7
            self.revenue = self.revenue + 7
        else:
            if self.water - 200 <= 0:
                print("Sorry, not enough water!")
                return
            if self.milk - 100 <= 0:
                print("Sorry, not enough milk!")
                return
            if self.coffee_beans - 12 <= 0:
                print("Sorry, not enough coffee beans!")
                return
            if self.cups - 1 <= 0:
                print("Sorry, not enough cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water = self.water - 200 if self.water > 199 else 0
            self.milk = self.milk - 100 if self.milk > 99 else 0
            self.coffee_beans = self.coffee_beans - 12 if self.coffee_beans > 11 else 0
            self.cups = self.cups - 1 if self.cups > 0 else 0
            self.money = self.money + 6
            self.revenue = self.revenue + 6
        self.products_sold = self.products_sold + 1

    def brewed_coffees(self, user_input, cups_brewed):
        if cups_brewed == user_input:
            print("Yes, I can make that amount of coffee")
        elif cups_brewed > user_input:
            print(f"Yes, I can make that amount of coffee (and even {cups_brewed - user_input} more than that)")
        else:
            print(f"No, I can only make {cups_brewed} cups of coffee")

    def start_up(self):
        exit_machine = False
        while not exit_machine:
            user_input = ""
            while user_input not in self.functions_list:
                user_input = input("Write action (buy, fill, take, remaining, stats, exit):\n")
            exit_machine = self.functions(user_input)

    def functions(self, choice):
        if choice == "buy":
            self.buy_coffee()
        elif choice == "fill":
            self.fill_machine()
        elif choice == "take":
            self.cash_out()
        elif choice == "remaining":
            self.status()
        elif choice == "stats":
            self.stats()
        else:
            return True
        return False

    def stats(self):
        print()
        print(f"This coffee machine has sold")
        print(f"{self.products_sold} beverages.")
        print(f"And has generated a total of")
        print(f"{self.revenue}$ of revenue.")
        print()

    def buy_coffee(self):
        user_input = 0
        while user_input not in self.coffee_types:
            user_input = input("What do you want to buy? "
                               "1 - espresso, "
                               "2 - latte, "
                               "3 - cappuccino, "
                               "back - to main menu:\n")
        if user_input == "back":
            return
        else:
            self.make_coffee(user_input)

    def fill_machine(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def cash_out(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def status(self):
        print()
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
        print()


def __main__():
    machine = CoffeeMachine(400, 540, 120, 9, 550)
    machine.start_up()


__main__()
