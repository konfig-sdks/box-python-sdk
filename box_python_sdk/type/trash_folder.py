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

from box_python_sdk.type.folder_mini import FolderMini
from box_python_sdk.type.user_mini import UserMini

class RequiredTrashFolder(TypedDict):
    description: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The unique identifier that represent a folder.  The ID for any folder can be determined by visiting a folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folders/123` the `folder_id` is `123`.
    id: str

    # `folder`
    type: str

    # The name of the folder.
    name: str

    # The folder size in bytes.  Be careful parsing this integer as its value can get very large.
    size: int

    path_collection: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    modified_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    owned_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Defines if this item has been deleted or not.  * `active` when the item has is not in the trash * `trashed` when the item has been moved to the trash but not deleted * `deleted` when the item has been permanently deleted.
    item_status: str

class OptionalTrashFolder(TypedDict, total=False):
    # The HTTP `etag` of this folder. This can be used within some API endpoints in the `If-Match` and `If-None-Match` headers to only perform changes on the folder if (no) changes have happened.
    etag: typing.Optional[str]

    sequence_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The date and time when the folder was created. This value may be `null` for some folders such as the root folder or the trash folder.
    created_at: typing.Optional[datetime]

    # The date and time when the folder was last updated. This value may be `null` for some folders such as the root folder or the trash folder.
    modified_at: typing.Optional[datetime]

    # The time at which this folder was put in the trash.
    trashed_at: typing.Optional[datetime]

    # The time at which this folder is expected to be purged from the trash.
    purged_at: typing.Optional[datetime]

    # The date and time at which this folder was originally created.
    content_created_at: typing.Optional[datetime]

    # The date and time at which this folder was last updated.
    content_modified_at: typing.Optional[datetime]

    # The shared link for this folder. This will be `null` if a folder has been trashed, since the link will no longer be active.
    shared_link: typing.Optional[str]

    # The folder upload email for this folder. This will be `null` if a folder has been trashed, since the upload will no longer work.
    folder_upload_email: typing.Optional[str]

    parent: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class TrashFolder(RequiredTrashFolder, OptionalTrashFolder):
    pass
