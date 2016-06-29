#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import shutil
import tempfile
import unittest
import subprocess
import collections

import s1duplicates
from prettysize import pretty_file_size_str


def create_dummy_file(filename, size=None):
    with open(filename, 'wb') as fd:
        if size:
            fd.seek(size-1)
            fd.write(b'\0')


class CreateTestDirMixin(object):
    ROOT = 'dataIN'
    DATASET = (
        'S1A/S1A_IW/S1A_IW_RAW__0A/S1A_IW_RAW__0ADV_20160619T053500_20160619T053641_000792_000504_DC7F.SAFE',
        'S1A/S1A_IW/S1A_IW_RAW__0S/S1A_IW_RAW__0SDV_20160619T053500_20160619T053641_000792_000504_F7CD.SAFE',
    )

    REPLICA_DIR = 'S1A/DT_SITE'
    DEFAULTSIZE = 1024

    def _setup_test_dataset(self):
        replicadir = os.path.join(self.root, self.REPLICA_DIR)
        os.makedirs(replicadir)

        for path in self.DATASET:
            dirname, basename = os.path.split(path)
            dirname = os.path.join(self.root, dirname)
            os.makedirs(dirname)
            filename = os.path.join(dirname, basename)
            create_dummy_file(filename, self.DEFAULTSIZE)

            replica = os.path.join(replicadir, basename)
            create_dummy_file(replica, self.DEFAULTSIZE)

    def setUp(self):
        self.testdir = tempfile.mkdtemp()
        self.root = os.path.join(self.testdir, self.ROOT)
        self._setup_test_dataset()

    def tearDown(self):
        shutil.rmtree(self.testdir)


class ScanDuplicatesTestCase(CreateTestDirMixin, unittest.TestCase):
    def test_scan_result(self):
        result = s1duplicates.scan_duplicates(self.root)
        self.assertTrue(hasattr(result, 'data'))

    def test_scan_result_data(self):
        result = s1duplicates.scan_duplicates(self.root)
        self.assertTrue(isinstance(result.data, collections.Mapping))

    def test_duplicate_number(self):
        result = s1duplicates.scan_duplicates(self.root)
        self.assertEqual(result.duplicate_count(), len(self.DATASET))

    def test_duplicate_size(self):
        result = s1duplicates.scan_duplicates(self.root)
        size = self.DEFAULTSIZE * len(self.DATASET)
        self.assertEqual(result.duplicate_size(), size)


class UiTestCase(CreateTestDirMixin, unittest.TestCase):
    VERSION = '1.0'
    BASEARGS = [sys.executable, '-u', 's1duplicates.py']
    ITEM_RE = re.compile(
        "'(?P<key>.*\.SAFE)': \[(?P<values>'.*\.SAFE'(,\s+'.*\.SAFE')*\])",
        re.MULTILINE)

    def test_version(self):
        args = self.BASEARGS + ['--version']
        outbytes = subprocess.check_output(args)
        out = outbytes.decode('utf-8')
        self.assertTrue(self.VERSION in out)

    def test_help(self):
        args = self.BASEARGS + ['--help']
        outbytes = subprocess.check_output(args)
        out = outbytes.decode('utf-8')
        self.assertTrue(out.startswith('usage:'))

    def test_duplicate_number(self):
        args = self.BASEARGS + [self.root]
        outbytes = subprocess.check_output(args)
        out = outbytes.decode('utf-8')
        self.assertEqual(
            out.strip(), '%d duplicate files found' % len(self.DATASET))

    def test_duplicate_size(self):
        args = self.BASEARGS + ['-s', self.root]
        outbytes = subprocess.check_output(args)
        out = outbytes.decode('utf-8')
        count_line, size_line = out.strip().splitlines()
        size = self.DEFAULTSIZE * len(self.DATASET)
        self.assertEqual(
            size_line,
            'duplicate file size: %s' % pretty_file_size_str(size))

    def test_duplicate_list(self):
        args = self.BASEARGS + ['-l', self.root]
        outbytes = subprocess.check_output(args)
        out = outbytes.decode('utf-8')

        keys = set(os.path.basename(item) for item in self.DATASET)
        found_keys = []

        for i, mobj in enumerate(self.ITEM_RE.finditer(out)):
            key = mobj.group('key')
            self.assertTrue(key in keys)
            found_keys.append(key)

            values = mobj.group('values')
            self.assertEqual(len(values.split(',')), 2)

        self.assertEqual(len(found_keys), len(keys))


if __name__ == '__main__':
    unittest.main()
