# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

import unittest

import os
from pprint import pprint
from box_python_sdk import Box

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        box = Box(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(box)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
