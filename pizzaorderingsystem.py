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
            print(f"\tAçıklama: {pizza.get_description()}")
            print(f"\tTutar: {pizza.get_cost()} ₺")

            for topping in toppings:
                print(f"\t{ToppingDecorator.get_name(topping)} ({ToppingDecorator.get_codeid(topping)})")
                print(f"\t\tAçıklama: {ToppingDecorator.get_description(topping)}")
                print(f"\t\tTutar: {ToppingDecorator.get_cost(topping)} ₺")

            total_cost += pizza.get_cost() + sum([topping.get_cost() for topping in toppings])

        print(f"\nTOTAL: {total_cost} ₺")

# pizzaları listelemek için boş liste oluşturuyoruz.
pizzas = []

# Kullanıcıdan değer alma işlemi
while True:
    choice = input("Pizza Kodunu giriniz!(a1-a4) (Sepete gitmek için: 'done'): ")
    if choice.lower() == 'done':
        break
    elif choice.lower() == 'a1':
        new_pizza = klasik()
    elif choice.lower() == 'a2':
        new_pizza = margarita()
    elif choice.lower() == 'a3':
        new_pizza = turkishpizza()
    elif choice.lower() == 'a4':
        new_pizza = sade()
    else:
        print("Geçersiz kod. Tekrar deneyin.")
        continue

    # Pizzaya sos ekleme işlemi - input
    while True:
        topping_choice = input(f" Seçtin:  {new_pizza.get_name()}. \n Sos eklemek ister misin? (y/n): ")
        if topping_choice.lower() == 'y':
            topping_code = input("Sos Kodu giriniz (x1 - x6): ")
            if topping_code.lower() == 'x1':
                new_pizza = Zeytin(new_pizza)
            elif topping_code.lower() == 'x2':
                new_pizza = Mantar(new_pizza)
            elif topping_code.lower() == 'x3':
                new_pizza = Kecipeyniri(new_pizza)
            elif topping_code.lower() == 'x4':
                new_pizza = Et(new_pizza)
            elif topping_code.lower() == 'x5':
                new_pizza = Sogan(new_pizza)
            elif topping_code.lower() == 'x6':
                new_pizza = Misir(new_pizza)
            else:
                print("Geçersiz kod. Tekrar deneyin")
                continue
        elif topping_choice.lower() == 'n':
            break
        else:
            print("Geçersiz kod. Evet için 'y', Hayır için 'n'.")
            continue

    # oluşturulan pizzayı listeye ekleme
    pizzas.append(new_pizza)

    # onay mesajı
    print(f"{new_pizza.get_name()} Sepete eklendi.")

order = PizzaOrder()
for pizza in pizzas:
    order.add_pizza(pizza, [])

# fiş yazdırma
order.print_receipt()
