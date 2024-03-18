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

from box_python_sdk.type.metadata_base import MetadataBase

class RequiredMetadatas(TypedDict):
    pass

class OptionalMetadatas(TypedDict, total=False):
    # A list of metadata instances, as applied to this file or folder.
    entries: typing.List[MetadataBase]

    # The limit that was used for this page of results.
    limit: int

class Metadatas(RequiredMetadatas, OptionalMetadatas):
    pass
