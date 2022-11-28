"""Store for the coffee machine."""

from coffee import CoffeeData


class NotEnoughResources(Exception):
    """Exception for not enough resources."""

    def __init__(self, resource: str):
        self.resource = resource

    def __str__(self):
        return f"Sorry, not enough {self.resource}!"


class MachineStore:
    """Store for the coffee machine."""

    def __init__(self):
        """Initialize the store with default values."""
        self.money = 550
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9

    def __str__(self) -> str:
        """Return the store as a string."""
        return f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money"""

    def take_all_money(self) -> int:
        """Take all the money from the store.

        Returns:
            The amount of money taken.
        """
        money = self.money
        self.money = 0
        return money

    def add_water(self, water: int) -> None:
        """Add water to the store."""
        self.water += water

    def add_milk(self, milk: int) -> None:
        """Add milk to the store."""
        self.milk += milk

    def add_coffee_beans(self, coffee_beans: int) -> None:
        """Add coffee beans to the store."""
        self.coffee_beans += coffee_beans

    def add_cups(self, cups: int) -> None:
        """Add cups to the store."""
        self.cups += cups

    def __check_resources(self, coffee_data: CoffeeData):
        """Check if there are enough resources to make a coffee."""
        if self.water < coffee_data.water:
            raise NotEnoughResources("water")
        if self.milk < coffee_data.milk:
            raise NotEnoughResources("milk")
        if self.coffee_beans < coffee_data.coffee_beans:
            raise NotEnoughResources("coffee beans")
        if self.cups < 1:
            raise NotEnoughResources("disposable cups")

    def __spent_resources(self, coffee_data: CoffeeData) -> None:
        """Subtract the resources spent for making a coffee."""
        self.water -= coffee_data.water
        self.milk -= coffee_data.milk
        self.coffee_beans -= coffee_data.coffee_beans
        self.cups -= 1
        

    def buy_coffee(self, coffee_type: CoffeeData):
        """Buy a coffee of the given type.

        Raises:
            NotEnoughResources: If there are not enough resources.
        """
        self.__check_resources(coffee_type)
        self.__spent_resources(coffee_type)
        self.money += coffee_type.price
