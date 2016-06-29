#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function


class UserType(object):
    def __repr__(self):
        return 'bla bla bla'

    def __enter__(self):
        print('acquiring resources')
        return self   # used by the 'as' clause

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('releasing resources')


obj = UserType()

# __repr__
print(repr(obj))        # --> bla bla bla


# __enter__, __exit__
with obj:
    print('do job')

# acquiring resources
# do job
# releasing resources
