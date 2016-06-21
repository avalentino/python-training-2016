#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pretty_file_size_str(size):
    '''String representation of file size

    Get the size in bytes and return the string
    representation using appropriate units.

    '''

    if size >= 2**20:
        size /= 2**20
        units = 'MB'
    elif size >= 2**10:
        size /= 2**10
        units = 'KB'
    else:
        units = 'Bytes'

    return '%.3f %s' % (size, units)


if __name__ == '__main__':
    import os

    filename = os.path.join(os.pardir, 'src', 'python-training.lyx')
    size = os.path.getsize(filename)
    # 198431

    print(pretty_file_size_str(size))
    # 193.780 KB
