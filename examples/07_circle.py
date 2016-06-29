#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi


class Circle(object):
    def  __init__(self, r):
         self.r = r

    def area(self):
        # pi * r**2 --> error
        return pi * self.r**2

c = Circle(r=1)
area = c.area()
print(area)             # --> 3.141592653589793

# also possible
area = Circle.area(c)
print(area)             # --> 3.141592653589793
