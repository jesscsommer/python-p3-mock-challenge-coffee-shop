class Customer: 

    def __init__(self, name):
        self.name = name 

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return {order.coffee for order in self.orders()}
    
    def create_order(self, coffee, price):
        from classes.coffee import Coffee 
        if (isinstance(coffee, Coffee)
            and type(price) == int): 
            Order(self, coffee, price)
        else: 
            raise Exception("Could not create order")

    # Properties 
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if type(name) == str and (1 <= len(name) <= 15):
            self._name = name
        else: 
            raise Exception("Customer name must be a string between 1-15 chars")
        
from classes.order import Order