"""Defining a Class!"""

class Pizza:
    # attributes
    # Think of these as the variables
    # each instance of my class will have
    # <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, inp_gf: bool):
        """My constructor"""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf

    def price(self) -> float:
        """Calculate price of pizza"""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += 0.75*self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    
    def add_toppings(self, num_toppings: int):
        """Add toppings to existing pizza"""
        self.toppings += num_toppings
