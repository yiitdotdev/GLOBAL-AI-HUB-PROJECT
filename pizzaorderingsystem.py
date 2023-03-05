#SUPERCLASS

class pizza:
    def __init__(self,codeid,name,description,cost,):
        self.name=name
        self.description=description
        self.cost=cost
        self.codeid=codeid

    def get_description(self):
        return self.description
    
    def get_name(self):
        return self.name
    
    def get_codeid(self):
        return self.codeid
    
    def get_cost(self):
        return self.cost


#SUBCLASS

class klasik(pizza):
    def __init__(self):
        super().__init__(codeid="A1",name="Klasik pizza",description="KLASİK DESC",cost=12.00)

class margarita(pizza):
    def __init__(self):
        super().__init__(codeid="A2",name="Margarita",description="MARGARİTA DESC",cost=15.00)

class turkishpizza(pizza):
    def __init__(self):
        super().__init__(codeid="A3",name="Türk pizza",description="TÜRK PİZZA DESC",cost=16.00)

class sade(pizza):
    def __init__(self):
        super().__init__(codeid="A4",name="Sade",description="SADE PİZZA DESC",cost=12.00)


#DECORATOR SUPERCLASS

class ToppingDecorator(pizza):
    def __init__(self,pizza) :
        self.pizza=pizza
    
    def get_codeid(self):
        return f"{self.pizza.get_codeid()} + {self.codeid}"

    def get_name(self):
        return f"{self.pizza.get_name()} + {self.name}"
    
    def get_description(self):
        return f"{self.pizza.get_description()} + {self.description}"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost


#TOPPING SUBCLASS

class Zeytin(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.codeid="X1"
        self.name= "Zeytin"
        self.description = "ZEYTİN DESC"
        self.cost = 2.00

class Mantar(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.codeid="X2"
        self.name= "Mantar"
        self.description = "MANTAR DESC"
        self.cost = 1.00

class Kecipeyniri(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.codeid="X3"
        self.name= "Keçi Peyniri"
        self.description = "PEYNİR DESC"
        self.cost = 2.00

class Et(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.codeid="X4"
        self.name= "Et"
        self.description = "ET DESC"
        self.cost = 2.00

class Sogan(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.codeid="X5"
        self.name= "Soğan"
        self.description = "SOĞAN DESC"
        self.cost = 2.00

class Misir(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.codeid="X6"
        self.name= "Mısır"
        self.description = "MISIR DESC"
        self.cost = 2.00

# Order Class
class PizzaOrder:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza, toppings):
        pizza_with_toppings = (pizza, toppings)
        self.pizzas.append(pizza_with_toppings)

    def print_receipt(self):
        total_cost = 0
        for pizza_with_toppings in self.pizzas:
            pizza, toppings = pizza_with_toppings
            print(f"{pizza.get_name()} ({pizza.get_codeid()})")
            print(f"\tDescription: {pizza.get_description()}")
            print(f"\tCost: ${pizza.get_cost()}")

            for topping in toppings:
                print(f"\t{ToppingDecorator.get_name(topping)} ({ToppingDecorator.get_codeid(topping)})")
                print(f"\t\tDescription: {ToppingDecorator.get_description(topping)}")
                print(f"\t\tCost: ${ToppingDecorator.get_cost(topping)}")

            total_cost += pizza.get_cost() + sum([topping.get_cost() for topping in toppings])

        print(f"\nTotal cost: ${total_cost}")