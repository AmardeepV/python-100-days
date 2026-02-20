MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def show_report(total_money):
    for i in resources:
        print(f"{i}: {resources[i]}")
    print(f"Money: ${total_money}")


def main():
    total_money = 0
    order = True
    coffee_types = ['espresso', 'latte', 'cappuccino']
    while order:
        take_order = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()

        if take_order == 'report':
            show_report(total_money)
        elif take_order in coffee_types:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))  # 25cents
            dimes = int(input("How many dimes?: "))  # 10cents
            nickles = int(input("How many nickles?: "))  # 5 cents
            pennies = int(input("How many pennies?: "))  # 1 cent
            total_input_coins = quarters * 0.25 + dimes * \
                0.10 + nickles * 0.05 + pennies * 0.01

            ################ Espresso order ######################
            if take_order == 'espresso':  # water 50 coffee 18
                # print(MENU["cappuccino"]["ingredients"]["water"])
                if total_input_coins >= MENU["espresso"]["cost"]:
                    if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
                        if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                            total_money = total_input_coins - \
                                MENU["espresso"]["cost"]
                            resources["water"] = resources["water"] - \
                                MENU["espresso"]["ingredients"]["water"]
                            resources['coffee'] = resources["coffee"] - \
                                MENU["espresso"]["ingredients"]["coffee"]

                            if total_money == 0:
                                print(f"Here is your espresso ☕️ Enjoy!")
                            else:
                                print(f"Here is ${total_money:.2f} in change")
                                print(f"Here is your espresso ☕️ Enjoy!")
                        else:
                            print(
                                "Sorry there is not enough coffee. Money refunded.")
                            order = False
                            return
                    else:
                        print("Sorry there is not enough water.")
                        order = False
                        return
                else:
                    print("Sorry not enough money for expresso")

            ################ Latte order ######################
            elif take_order == 'latte':
                if total_input_coins >= MENU["latte"]["cost"]:
                    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
                        if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                            if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                                total_money = total_input_coins - \
                                    MENU["latte"]["cost"]
                                resources["water"] = resources["water"] - \
                                    MENU["latte"]["ingredients"]["water"]
                                resources['coffee'] = resources["coffee"] - \
                                    MENU["latte"]["ingredients"]["coffee"]
                                resources["milk"] = resources["milk"] - \
                                    MENU["latte"]["ingredients"]["milk"]

                                if total_money == 0:
                                    print(f"Here is your latte ☕️ Enjoy!")
                                else:
                                    print(
                                        f"Here is ${total_money:.2f} in change")
                                    print(f"Here is your latte ☕️ Enjoy!")
                            else:
                                print("Sorry there is not enough coffee.")
                                order = False
                                return
                        else:
                            print("Sorry there is not enough milk.")
                            order = False
                            return
                    else:
                        print("Sorry there is not enough water.")
                        order = False
                        return
                else:
                    print("Sorry not enough money for latte. Money refunded. ")

            ################ Cappuccino order ######################
            # elif take_order == 'cappuccino':
            else:
                if total_input_coins >= MENU["cappuccino"]["cost"]:
                    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
                        if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                            if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                                total_money = total_input_coins - \
                                    MENU["cappuccino"]["cost"]
                                resources["water"] = resources["water"] - \
                                    MENU["cappuccino"]["ingredients"]["water"]
                                resources['coffee'] = resources["coffee"] - \
                                    MENU["cappuccino"]["ingredients"]["coffee"]
                                resources["milk"] = resources["milk"] - \
                                    MENU["cappuccino"]["ingredients"]["milk"]

                                if total_money == 0:
                                    print(f"Here is your cappuccino ☕️ Enjoy!")
                                else:
                                    print(
                                        f"Here is ${total_money:.2f} in change")
                                    print(f"Here is your cappuccino ☕️ Enjoy!")
                            else:
                                print("Sorry there is not enough coffee.")
                                order = False
                                return
                        else:
                            print("Sorry there is not enough milk.")
                            order = False
                            return
                    else:
                        print("Sorry there is not enough water.")
                        order = False
                        return
                else:
                    print("Sorry not enough money for cappuccino. Money refunded.")

        elif take_order == 'off':
            order = False
            return

        else:
            print(
                "Wrong order type, please select one from espresso/latte/cappuccino")


if __name__ == '__main__':
    main()
