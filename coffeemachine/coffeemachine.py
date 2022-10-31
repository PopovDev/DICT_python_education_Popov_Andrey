"""Coffee machine simulator by Popov Andrey"""

from enum import Enum
from time import sleep
from coffee import CoffeeType
from machine_store import MachineStore, NotEnoughResources


class MachineState(Enum):
    """Enum of coffee machine states."""
    OFF = 0
    WAITING_FOR_ACTION = 1
    ACTION_BUY = 2
    ACTION_SELECT_COFFEE = 3
    ACTION_FILL_WATER = 4
    ACTION_FILL_MILK = 5
    ACTION_FILL_COFFEE_BEANS = 6
    ACTION_FILL_CUPS = 7


class CoffeeMachine:
    """Coffee machine simulator."""

    def __init__(self):
        """Initialize the coffee machine."""
        self.store = MachineStore()
        self.state = MachineState.OFF

    def start(self):
        """Start the coffee machine."""
        print("Loading the machine...")
        sleep(1)
        self.state = MachineState.WAITING_FOR_ACTION
        print("The machine is ready to work!")

    def print_ui(self) -> None:
        """Print the UI of the coffee machine."""

        match self.state:
            case MachineState.WAITING_FOR_ACTION:
                print("Write action (buy, fill, take, remaining, exit):")
            case MachineState.ACTION_BUY:
                print("What do you want to buy?")
                print("1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            case MachineState.ACTION_SELECT_COFFEE:
                print("Write how many ml of water the coffee machine has:")
            case MachineState.ACTION_FILL_WATER:
                print("Write how many ml of water do you want to add:")
            case MachineState.ACTION_FILL_MILK:
                print("Write how many ml of milk do you want to add:")
            case MachineState.ACTION_FILL_COFFEE_BEANS:
                print("Write how many grams of coffee beans do you want to add:")
            case MachineState.ACTION_FILL_CUPS:
                print("Write how many disposable cups of coffee do you want to add:")
            case MachineState.OFF:
                print("The machine is off")

    def process_input(self, input_val: str):
        """Process the input from the user."""
        match self.state:
            case MachineState.WAITING_FOR_ACTION:
                self.__process_action(input_val)
            case MachineState.ACTION_BUY:
                self.__process_buy(input_val)
            case MachineState.ACTION_FILL_WATER:
                self.__process_fill_water(input_val)
            case MachineState.ACTION_FILL_MILK:
                self.__process_fill_milk(input_val)
            case MachineState.ACTION_FILL_COFFEE_BEANS:
                self.__process_fill_coffee_beans(input_val)
            case MachineState.ACTION_FILL_CUPS:
                self.__process_fill_cups(input_val)

    def __process_action(self, input_val: str) -> None:
        """Process the action input from the user."""
        match input_val:
            case "buy":
                self.state = MachineState.ACTION_BUY
            case "fill":
                self.state = MachineState.ACTION_FILL_WATER
            case "take":
                print(f"I gave you {self.store.take_all_money()} UAH")
                self.state = MachineState.WAITING_FOR_ACTION
            case "remaining":
                print(self.store)
                self.state = MachineState.WAITING_FOR_ACTION
            case "exit":
                self.state = MachineState.OFF
            case _:
                print("Unknown action")

    def __buy_coffee(self, coffee_type: CoffeeType) -> None:
        """Buy a coffee."""
        try:
            self.store.buy_coffee(coffee_type.value)
            print(f"I have enough resources, making a {coffee_type} for you!")
            sleep(1)
            print("Done!")
        except NotEnoughResources as error:
            print(error)
        self.state = MachineState.WAITING_FOR_ACTION

    def __process_buy(self, input_val: str) -> None:
        """Process the buy input from the user."""
        match input_val:
            case "1":
                self.__buy_coffee(CoffeeType.ESPRESSO)
            case "2":
                self.__buy_coffee(CoffeeType.LATTE)
            case "3":
                self.__buy_coffee(CoffeeType.CAPPUCCINO)
            case "back":
                self.state = MachineState.WAITING_FOR_ACTION
            case _:
                print("Unknown coffee type")

    def __process_fill_water(self, input_val: str) -> None:
        """Process the fill water input from the user."""
        try:
            self.store.add_water(int(input_val))
            self.state = MachineState.ACTION_FILL_MILK
        except ValueError:
            print("Invalid input")

    def __process_fill_milk(self, input_val: str) -> None:
        """Process the fill milk input from the user."""
        try:
            self.store.add_milk(int(input_val))
            self.state = MachineState.ACTION_FILL_COFFEE_BEANS
        except ValueError:
            print("Invalid input")

    def __process_fill_coffee_beans(self, input_val: str) -> None:
        """Process the fill coffee beans input from the user."""
        try:
            self.store.add_coffee_beans(int(input_val))
            self.state = MachineState.ACTION_FILL_CUPS
        except ValueError:
            print("Invalid input")

    def __process_fill_cups(self, input_val: str) -> None:
        """Process the fill cups input from the user."""
        try:
            self.store.add_cups(int(input_val))
            self.state = MachineState.WAITING_FOR_ACTION
        except ValueError:
            print("Invalid input")

    @property
    def enabled(self) -> bool:
        """Return if the machine is enabled."""
        return self.state != MachineState.OFF


def main() -> None:
    """Main function."""
    machine = CoffeeMachine()
    try:
        machine.start()
        while True:
            machine.print_ui()
            input_value = input("> ").strip()
            machine.process_input(input_value)
            if not machine.enabled:
                break
    except KeyboardInterrupt:
        print("\nThrowing the coffee machine out of the window...")
        sleep(1)
        print("The machine is broken!")
    print("Bye!")


if __name__ == "__main__":
    main()
