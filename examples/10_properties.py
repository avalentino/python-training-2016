#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

from math import pi, sqrt


class Shape(object):
    pass


class Circle(Shape):
    def __init__(self, r=0):
        self._r = r                 # one protected attribute

    @property                       # decorator
    def radius(self):               # getter
        return self._r

    @radius.setter
    def radius(self, value):        # setter
        self._r = value

    @property
    def diameter(self):             # getter
        return 2 * self._r

    @diameter.setter
    def diameter(self, value):      # setter: if omitted then
        self._r = value / 2.        # the property is read-only

    @property
    def circumference(self):
        return 2. * pi * self._r

    @circumference.setter
    def circumference(self, value):
        self._r = value / 2. / pi

    @property
    def area(self):
        return pi * self._r ** 2

    @area.setter
    def ares(self, value):
        self._r = sqrt(value / pi)

c = Circle()

# set the redius
c.radius = 3

# the diameter stay consistent
print('diameter', c.diameter)               # --> 6

# ... and the area too
print('area', c.area)                       # --> 28.274333882308138

c.diameter = 5                              # now the diameter is changed

# hey, the radius has been updated as well!
print('radius', c.radius)                   # --> 2.5

# and the circumference too
print('circumference', c.circumference)     # --> 15.707963267948966
