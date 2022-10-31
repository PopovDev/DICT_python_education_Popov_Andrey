"""Coffee types and their properties."""

from enum import Enum
from typing import NamedTuple

class CoffeeData(NamedTuple):
    """Coffee type and its properties."""
    water: int
    milk: int
    coffee_beans: int
    price: int


class CoffeeType(Enum):
    """Coffee types and their properties."""

    ESPRESSO = CoffeeData(250, 0, 16, 4)
    LATTE = CoffeeData(350, 75, 20, 7)
    CAPPUCCINO = CoffeeData(200, 100, 12, 6)

    def __str__(self) -> str:
        """Return the coffee type as a string."""
        return self.name.capitalize()
