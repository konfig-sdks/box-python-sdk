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

from box_python_sdk.type.web_links_create_object_request_parent import WebLinksCreateObjectRequestParent

class RequiredWebLinksCreateObjectRequest(TypedDict):
    # The URL that this web link links to. Must start with `\"http://\"` or `\"https://\"`.
    url: str

    parent: WebLinksCreateObjectRequestParent

class OptionalWebLinksCreateObjectRequest(TypedDict, total=False):
    # Description of the web link.
    description: str

    # Name of the web link. Defaults to the URL if not set.
    name: str

class WebLinksCreateObjectRequest(RequiredWebLinksCreateObjectRequest, OptionalWebLinksCreateObjectRequest):
    pass
