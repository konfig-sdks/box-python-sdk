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


class RequiredCollection(TypedDict):
    pass

class OptionalCollection(TypedDict, total=False):
    # The unique identifier for this collection.
    id: str

    # `collection`
    type: str

    # The name of the collection.
    name: str

    # The type of the collection. This is used to determine the proper visual treatment for collections.
    collection_type: str

class Collection(RequiredCollection, OptionalCollection):
    pass
