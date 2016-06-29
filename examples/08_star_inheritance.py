#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function


class Root(object):
    def __init__(self, arg):
        print('Root(%r)' % arg)
        super().__init__()  # no args for object

class Base1(Root):
    def __init__(self, arg):
        print('Base1(%r)' % arg)
        super().__init__(arg)  # what if I comment this line?

class Base2(Root):
    def __init__(self, arg):
        print('Base2(%r)' % arg)
        super().__init__(arg)

class Derived(Base1, Base2):
    def __init__(self, arg):
        print('Derived(%r)' % arg)
        super().__init__(arg)


obj = Derived('arg')

print()
print('MRO')
import pprint
pprint.pprint(Derived.mro())
