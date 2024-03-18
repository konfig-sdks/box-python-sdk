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

from box_python_sdk.type.file_version_mini import FileVersionMini
from box_python_sdk.type.folder_mini import FolderMini
from box_python_sdk.type.user_mini import UserMini

class RequiredTrashFile(TypedDict):
    # The optional description of this file
    description: str

    # The unique identifier that represent a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.
    id: str

    # `file`
    type: str

    sequence_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The SHA1 hash of the file. This can be used to compare the contents of a file on Box with a local file.
    sha1: str

    # The file size in bytes. Be careful parsing this integer as it can get very large and cause an integer overflow.
    size: int

    path_collection: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The date and time when the file was created on Box.
    created_at: datetime

    # The date and time when the file was last updated on Box.
    modified_at: datetime

    modified_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    owned_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Defines if this item has been deleted or not.  * `active` when the item has is not in the trash * `trashed` when the item has been moved to the trash but not deleted * `deleted` when the item has been permanently deleted.
    item_status: str

class OptionalTrashFile(TypedDict, total=False):
    # The HTTP `etag` of this file. This can be used within some API endpoints in the `If-Match` and `If-None-Match` headers to only perform changes on the file if (no) changes have happened.
    etag: typing.Optional[str]

    # The name of the file
    name: str

    file_version: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The time at which this file was put in the trash.
    trashed_at: typing.Optional[datetime]

    # The time at which this file is expected to be purged from the trash.
    purged_at: typing.Optional[datetime]

    # The date and time at which this file was originally created, which might be before it was uploaded to Box.
    content_created_at: typing.Optional[datetime]

    # The date and time at which this file was last updated, which might be before it was uploaded to Box.
    content_modified_at: typing.Optional[datetime]

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The shared link for this file. This will be `null` if a file has been trashed, since the link will no longer be active.
    shared_link: typing.Optional[str]

    parent: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class TrashFile(RequiredTrashFile, OptionalTrashFile):
    pass
