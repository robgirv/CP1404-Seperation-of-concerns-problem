"""Product module"""


class Product:
    def __init__(self, name, price):
        """Construct a product object."""
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """Return a string representation of product object."""
        return f"{self.name}, ${self.price}"

    def __repr__(self) -> str:
        """Return a developer-friendly string representation of a Guitar."""
        return f"{vars(self)}"
