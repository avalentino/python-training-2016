#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pow_func_generator(base=10):

    def pow_func(n):
        return base ** n # base: parent scope

    return pow_func      # returns a function


# this is another way to define a function
pow2 = pow_func_generator(base=2)


# no 'base' variable defined in this scope
print(pow2(3))          # --> 8
