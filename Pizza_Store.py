from Pizza_store.Pizza_types.Cheese_Pizza import CheesePizza
from Pizza_store.Pizza_types.Greek_Pizza import GreekPizza

class PizzaStore:
    def OrderPizza(type):

        if (type == "Cheese"):
            pizza = CheesePizza()
        elif (type == "Greek"):
            pizza = GreekPizza()
        else:
            print()
            print("DONT HAVE", type, '\n')
            return
        pizza.Prepare()
        pizza.Bake()
        pizza.Cut()
        pizza.Box()

