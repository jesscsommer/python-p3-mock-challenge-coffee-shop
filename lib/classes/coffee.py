class Coffee: 

    def __init__(self, name):
        self.name = name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        all_prices = [order.price for order in self.orders()]
        if all_prices:
            return round((sum(all_prices) / len(all_prices)), 2)

    # Properties 
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (not hasattr(self, "_name") 
            and type(name) == str 
            and (1 <= len(name.replace(" ", "")) <= 15)):
            self._name = name
        elif (not hasattr(self, "name")): 
            raise Exception("Coffee name must be a string between 1-15 chs")
        else: 
            raise Exception("Coffee name cannot be changed")
        
from classes.order import Order