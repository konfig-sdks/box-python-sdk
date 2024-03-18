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

from box_python_sdk.type.web_links_update_object_request_shared_link import WebLinksUpdateObjectRequestSharedLink

class RequiredWebLinksUpdateObjectRequest(TypedDict):
    pass

class OptionalWebLinksUpdateObjectRequest(TypedDict, total=False):
    # A new description of the web link.
    description: str

    # The new URL that the web link links to. Must start with `\"http://\"` or `\"https://\"`.
    url: str

    parent: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # A new name for the web link. Defaults to the URL if not set.
    name: str

    shared_link: WebLinksUpdateObjectRequestSharedLink

class WebLinksUpdateObjectRequest(RequiredWebLinksUpdateObjectRequest, OptionalWebLinksUpdateObjectRequest):
    pass
