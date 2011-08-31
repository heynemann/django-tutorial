#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import join

import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase


class Simple(FunkLoadTestCase):
    def setUp(self):
        self.server_url = self.conf_get('main', 'url').rstrip('/')

    def test_simple(self):
        server_url = join(self.server_url, 'polls')
        self.get(server_url, description='Get polls')

if __name__ in ('main', '__main__'):
    unittest.main()
