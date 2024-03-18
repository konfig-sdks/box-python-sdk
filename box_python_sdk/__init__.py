# coding: utf-8

# flake8: noqa

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

__version__ = "2.0.0"

# import ApiClient
from box_python_sdk.api_client import ApiClient

# import Configuration
from box_python_sdk.configuration import Configuration

# import exceptions
from box_python_sdk.exceptions import OpenApiException
from box_python_sdk.exceptions import ApiAttributeError
from box_python_sdk.exceptions import ApiTypeError
from box_python_sdk.exceptions import ApiValueError
from box_python_sdk.exceptions import ApiKeyError
from box_python_sdk.exceptions import ApiException

from box_python_sdk.client import Box
