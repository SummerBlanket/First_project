from Pizza import Pizza

class GreekPizza(Pizza):
    def __init__(self):
        self.name = "greek pizza"
        self.dough = "super thin"
        self.sauce = "sweet and sour"
        self.toppings = ["mushroom", "cheese", "onion"]