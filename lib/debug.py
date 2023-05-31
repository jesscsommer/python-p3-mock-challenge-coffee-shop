#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    cf1 = Coffee("Tony's")
    cf2 = Coffee("Cafe Vita")
    cf3 = Coffee("Raven's Brew")

    cs1 = Customer("Herm")
    cs2 = Customer("Ron")
    cs3 = Customer("Jess")

    o1 = Order(cs1, cf1, 9.50)
    o2 = Order(cs3, cf1, 4.50)
    o3 = Order(cs2, cf2, 5.50)
    o4 = Order(cs1, cf1, 9.50)

    ipdb.set_trace()
