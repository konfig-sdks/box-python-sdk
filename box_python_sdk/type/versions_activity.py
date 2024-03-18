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

from box_python_sdk.type.fa_file_version import FaFileVersion
from box_python_sdk.type.file_activity_user import FileActivityUser

class RequiredVersionsActivity(TypedDict):
    pass

class OptionalVersionsActivity(TypedDict, total=False):
    # Users who performed one of the `action_types` (`created`, `deleted` or `restored`)
    action_by: typing.List[FileActivityUser]

    action_type: str

    end: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    start: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    type: str

class VersionsActivity(RequiredVersionsActivity, OptionalVersionsActivity):
    pass
