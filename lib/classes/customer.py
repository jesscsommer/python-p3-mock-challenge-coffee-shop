class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._coffees = []
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee and isinstance(new_coffee, Coffee):
            self._coffees.append(new_coffee)
        return set(self._coffees)

    def create_order(self, coffee, price):
        from classes.coffee import Coffee
        from classes.order import Order
        if isinstance(coffee, Coffee) and type(price) == int: 
            Order(self, coffee, price)

    # Properties 
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name): 
        if (type(name) == str) and (1 <= len(name) <= 15):
            self._name = name
        else: 
            raise TypeError("Name must be a string between 1 and 15 chars")