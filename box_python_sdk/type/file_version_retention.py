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

from box_python_sdk.type.file_mini import FileMini
from box_python_sdk.type.file_version_mini import FileVersionMini
from box_python_sdk.type.retention_policy_mini import RetentionPolicyMini

class RequiredFileVersionRetention(TypedDict):
    pass

class OptionalFileVersionRetention(TypedDict, total=False):
    # The unique identifier for this file version retention.
    id: str

    # `file_version_retention`
    type: str

    file_version: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    file: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # When this file version retention object was created
    applied_at: datetime

    # When the retention expires on this file version retention
    disposition_at: datetime

    winning_retention_policy: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class FileVersionRetention(RequiredFileVersionRetention, OptionalFileVersionRetention):
    pass
