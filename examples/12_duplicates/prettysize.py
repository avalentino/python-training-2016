#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division


def pretty_file_size_str(size):
    '''String representation of file size

    Gets a size in bytes and return the its string representation
    using appropriate units.

    >>> pretty_file_size_str(1.3 * 1024**5)
    '1.30 PB'

    >>> pretty_file_size_str(1.3 * 1024)
    '1.30 KB'

    >>> pretty_file_size_str(18)
    '18.00 Bytes'

    >>> pretty_file_size_str(0.3)
    '0.30 Bytes'

    '''

    UNITS = ('Bytes', 'KB', 'MB', 'GB', 'TB', 'PB')

    for exponent, units_str in enumerate(UNITS):
        normalized_size = size / 1024**exponent
        if normalized_size < 1024:
            break

    return '%.2f %s' % (normalized_size, units_str)


if __name__ == '__main__':
    import os
    import hashlib

    # print the fill module path
    print('filename: {}'.format(os.path.abspath(__file__)))

    # print the module size
    size = os.path.getsize(__file__)
    print('size: {}'.format(pretty_file_size_str(size)))

    # compute the MD5 checksum
    md5 = hashlib.md5()
    with open(__file__, 'rb') as fd:
        for data in fd:
            md5.update(data)

    # pront the MD5 checksum of the module file
    basename = os.path.basename(__file__)
    print('{} *{}'.format(basename, md5.hexdigest()))
