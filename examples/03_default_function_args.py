#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hello(name='World'):
    print('Hello, %s!' % name)

hello()                     # --> Hello, World!

import os
name = os.getenv('USER')    # antonio
hello(name.capitalize())    # --> Hello, Antonio!
