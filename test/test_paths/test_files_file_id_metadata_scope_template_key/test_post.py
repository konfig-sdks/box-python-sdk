# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

import unittest
from unittest.mock import patch

import urllib3

import box_python_sdk
from box_python_sdk.paths.files_file_id_metadata_scope_template_key import post
from box_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestFilesFileIdMetadataScopeTemplateKey(ApiTestMixin, unittest.TestCase):
    """
    FilesFileIdMetadataScopeTemplateKey unit test stubs
        Create metadata instance on file
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()
