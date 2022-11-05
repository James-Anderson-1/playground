class Grocery_Item:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.has_discount = discount

    def display_info(self):
        print(self.name, "is $", self.price)



apple = Grocery_Item(name="apple", price=1, discount=False)
cheerios = Grocery_Item(name="cheerios", price=4, discount=True)

apple.display_info()
cheerios.display_info()

print("does", apple.name, "have a discount?", apple.has_discount)

