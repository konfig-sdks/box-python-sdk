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

from box_python_sdk.type.folder_lock import FolderLock

class RequiredFolderLocks(TypedDict):
    pass

class OptionalFolderLocks(TypedDict, total=False):
    # A list of folder locks
    entries: typing.List[FolderLock]

    # The limit that was used for these entries. This will be the same as the `limit` query parameter unless that value exceeded the maximum value allowed. The maximum value varies by API.
    limit: str

    # The marker for the start of the next page of results.
    next_marker: typing.Optional[str]

class FolderLocks(RequiredFolderLocks, OptionalFolderLocks):
    pass
