#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        args_str = ', '.join(
            [repr(arg) for arg in args] +
            ['%s=%r' % (k, v) for k, v in kwargs.items()])
        logging.debug('%s(%s)' % (name, args_str))
        ret = func(*args, **kwargs)
        logging.debug('%s --> %r' % (name, ret))
        return ret
    return wrapper


logging.basicConfig(
    level=logging.DEBUG, format='%(levelname)s: %(message)s')


# equivalent to: do_something = trace(do_something)
@trace
def do_something():
    pass

do_something()

# DEBUG: do_something()
# DEBUG: do_something --> None
