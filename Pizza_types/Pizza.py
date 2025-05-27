class Pizza:
    def __init__(self, name, dough, sauce, toppings, type):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.type = type 
    
    def Prepare(self):
        print("Preparing", self.name)
        print("Tossing dough")
        print("Adding sauce")
        print("Adding toppings:")
        for topping in self.toppings:
            print("      ", topping)
        

    def Bake(self):
        print("Baking", self.name, "in 30 miniutes")

    def Cut(self):
        print("Cutting", self.name)

    def Box(self):
        print("Boxing", self.name)
