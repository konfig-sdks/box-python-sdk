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

from box_python_sdk.type.file_activity_user import FileActivityUser

class RequiredFaFileVersion(TypedDict):
    # The unique identifier that represent a file version.
    id: str

class OptionalFaFileVersion(TypedDict, total=False):
    # When the `file_version` object was created.
    created_at: datetime

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Version number.
    number: int

    # When the `file_version` object was restored.
    restored_at: datetime

    restored_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # When the `file_version` object was trashed.
    trashed_at: datetime

    trashed_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # `file_version`
    type: str

class FaFileVersion(RequiredFaFileVersion, OptionalFaFileVersion):
    pass
