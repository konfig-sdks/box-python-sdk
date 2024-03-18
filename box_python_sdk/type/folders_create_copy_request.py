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

from box_python_sdk.type.folders_create_copy_request_parent import FoldersCreateCopyRequestParent

class RequiredFoldersCreateCopyRequest(TypedDict):
    parent: FoldersCreateCopyRequestParent

class OptionalFoldersCreateCopyRequest(TypedDict, total=False):
    # An optional new name for the copied folder.  There are some restrictions to the file name. Names containing non-printable ASCII characters, forward and backward slashes (`/`, `\\`), as well as names with trailing spaces are prohibited.  Additionally, the names `.` and `..` are not allowed either.
    name: str

class FoldersCreateCopyRequest(RequiredFoldersCreateCopyRequest, OptionalFoldersCreateCopyRequest):
    pass
