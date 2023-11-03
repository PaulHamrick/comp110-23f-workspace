from lessons.classes.pizza import Pizza


#my_pizza: Pizza = Pizza("Large")
#print(my_pizza.gluten_free)
# my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

sals_pizza: Pizza = Pizza("medium", 5, False)

x: int = int()
print(x)
y: str = str()
print(y)

def price(input_pizza: Pizza) -> float:
    if input_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += 0.75*input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price

print(sals_pizza.price())