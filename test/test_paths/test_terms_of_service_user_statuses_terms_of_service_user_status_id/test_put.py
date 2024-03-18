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
from box_python_sdk.paths.terms_of_service_user_statuses_terms_of_service_user_status_id import put
from box_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTermsOfServiceUserStatusesTermsOfServiceUserStatusId(ApiTestMixin, unittest.TestCase):
    """
    TermsOfServiceUserStatusesTermsOfServiceUserStatusId unit test stubs
        Update terms of service status for existing user
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
