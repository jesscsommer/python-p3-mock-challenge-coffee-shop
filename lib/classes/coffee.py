class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer and isinstance(new_customer, Customer):
            self._customers.append(new_customer)
        return list(set(self._customers))
    
    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        all_prices = [order.price for order in self._orders]
        if all_prices:
            return sum(all_prices) / len(all_prices)
    
    # Properties
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name"):
            self._name = name 
        else: 
            raise AttributeError("Coffee name cannot be reset")