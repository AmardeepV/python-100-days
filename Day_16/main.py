from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    order = True
    money_machine = MoneyMachine()
    menu = Menu()
    coffee_maker = CoffeeMaker()

    while order:
        take_order = input(
            f"What would you like? {menu.get_items()}: ").lower()

        if take_order == 'report':
            coffee_maker.report()
            money_machine.report()
        elif take_order == 'off':
            order = False

        else:
            drink = menu.find_drink(take_order)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == '__main__':
    main()
