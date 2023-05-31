#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    cf1 = Coffee("Tony's")
    cs1 = Customer("Herm")
    # o1 = Order(cf1, cs1, 9.50)

    # coffee = Coffee("Vanilla Latte")
    # customer = Customer('Steve')
    # order_1 = Order(customer, coffee, 2)
    # order_2 = Order(customer, coffee, 5)


    ipdb.set_trace()
