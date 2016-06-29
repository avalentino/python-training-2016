#!usr/bin/env python3
# -*- coding: utf-8 -*-

def trace(func, *args, **kwargs):
    # func is mandatory
    # type(args)   --> tuple - default ()
    # type(kwargs) --> dict  - default {}

    name = func.__name__         # functions are objects
    args_str = ', '.join(
            [repr(arg) for arg in args] +
            ['%s=%r' % (k, v) for k, v in kwargs.items()])

    print('TRACE: %s(%s)' % (name, args_str))

    ret = func(*args, **kwargs)  # argumnts unpacking

    print('TRACE: %s --> %r' % (name, ret))

    return ret


def simple_sum(a, b, c=0):
    print('This is "simple_sum"')

    return a + b + c

trace(simple_sum, 10, b=20, c=30)

# TRACE: simple_sum(10, c=30, b=20)
# This is "simple_sum"
# TRACE: simple_sum --> 60
