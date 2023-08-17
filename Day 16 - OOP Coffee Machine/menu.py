class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, altname1, altname2, water, milk, coffee, cost):
        self.name = name
        self.altname1 = altname1
        self.altname2 = altname2
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="espresso",altname1="e",altname2="1", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="latte",altname1="l",altname2="2", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="cappuccino",altname1="c",altname2="3", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
            if item.altname1 == order_name:
                return item
            if item.altname2 == order_name:
                return item
        print("Sorry that item is not available.")
