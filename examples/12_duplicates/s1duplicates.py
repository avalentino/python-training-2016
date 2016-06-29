#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import pprint
import logging

from argparse import ArgumentParser
from collections import defaultdict

import prettysize


class Result(object):
    def __init__(self, data, scanned_files):
        self.data = data
        self.scanned_files = scanned_files

    def duplicate_count(self):
        values = self.data.values()
        return sum(len(item) - 1 for item in values)

    def duplicate_size(self):
        size = 0
        for key in self.data:
            duplicates = self.data[key]
            filename = duplicates[0]  # first path
            size += os.path.getsize(filename) * (len(duplicates) - 1)

        return size


def scan_duplicates(dataroot):
    scanned_files = 0
    data = defaultdict(list)
    for root, dirs, files in os.walk(dataroot):
        scanned_files += len(files)
        for filename in files:
            fullpath = os.path.join(root, filename)
            if not os.path.islink(fullpath):
                data[filename].append(fullpath)

    # remove non duplicates
    for key in list(data.keys()):  # note: copy keys
        val = data[key]
        if len(val) < 2:
            del data[key]

    return Result(data, scanned_files)


def get_parser():
    parser = ArgumentParser(
        description='Search all duplicate files in the specified '
                    'directory tree')

    parser.add_argument(
        '--version', action='version', version='%(prog)s v1.0')
    parser.add_argument(
        '-s', '--compute-size', action='store_true', default=False,
        help='compute the total size of duplicate files '
             '(default: %(default)s)')
    parser.add_argument(
        '-l', '--list-files', action='store_true', default=False,
        help='dump the entire list of duplicate files (default: %(default)s)')
    parser.add_argument(
       '-v', '--verbose', action='store_true', default=False,
       help='print verbose help messages')
    parser.add_argument(
        'dataroot',
        help='the root of the directory tree to scan for duplicates')

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    result = scan_duplicates(args.dataroot)
    logging.info('%d duplicate files found' % result.duplicate_count())

    if args.compute_size:
        size = result.duplicate_size()
        sizestr = prettysize.pretty_file_size_str(size)
        logging.info('duplicate file size: %s' % sizestr)

    if args.list_files:
        logging.info('Duplicates in "%s"' % args.dataroot)
        pprint.pprint(result.data)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO, format='%(message)s', stream=sys.stdout)
    main()
