class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    # Properties
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if ((type(price) == int 
            or type(price) == float) 
            and (1 <= price <= 10)): 
            self._price = price 
        else: 
            raise Exception("Price must be a number between 1 and 10")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter 
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else: 
            raise Exception("Customer must be an instance of Customer")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter 
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else: 
            raise Exception("Coffee must be an instance of Coffee")
        
from classes.customer import Customer 
from classes.coffee import Coffee