# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from box_python_sdk.type.client_error_context_info import ClientErrorContextInfo

class RequiredClientError(TypedDict):
    pass

class OptionalClientError(TypedDict, total=False):
    # error
    type: str

    # The HTTP status of the response.
    status: int

    # A Box-specific error code
    code: str

    # A short message describing the error.
    message: str

    context_info: ClientErrorContextInfo

    # A URL that links to more information about why this error occurred.
    help_url: str

    # A unique identifier for this response, which can be used when contacting Box support.
    request_id: str

class ClientError(RequiredClientError, OptionalClientError):
    pass
