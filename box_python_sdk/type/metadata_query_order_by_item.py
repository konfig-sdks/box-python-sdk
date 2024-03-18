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


class RequiredMetadataQueryOrderByItem(TypedDict):
    pass

class OptionalMetadataQueryOrderByItem(TypedDict, total=False):
    # The metadata template field to order by.  The `field_key` represents the `key` value of a field from the metadata template being searched for.
    field_key: str

    # The direction to order by, either ascending or descending.  The `ordering` direction must be the same for each item in the array.
    direction: str

class MetadataQueryOrderByItem(RequiredMetadataQueryOrderByItem, OptionalMetadataQueryOrderByItem):
    pass
