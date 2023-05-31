from classes.order import Order

class Coffee: 

    def __init__(self, name):
        self.name = name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return {order.customer for order in self.orders()}

    # Properties 
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (not hasattr(self, "name") 
            and type(name) == str 
            and (1 <= len(name) <= 15)):
            self._name = name
        elif (not hasattr(self, "name")): 
            raise Exception("Coffee name must be a string between 1-15 chs")
        else: 
            raise Exception("Coffee name cannot be changed")