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
from pydantic import BaseModel, Field, RootModel

from box_python_sdk.pydantic.file_version_mini import FileVersionMini
from box_python_sdk.pydantic.folder_mini import FolderMini
from box_python_sdk.pydantic.user_mini import UserMini

class TrashFileRestored(BaseModel):
    # The optional description of this file
    description: str = Field(alias='description')

    # The unique identifier that represent a file.  The ID for any file can be determined by visiting a file in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/files/123` the `file_id` is `123`.
    id: str = Field(alias='id')

    # `file`
    type: Literal["file"] = Field(alias='type')

    sequence_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='sequence_id')

    # The SHA1 hash of the file. This can be used to compare the contents of a file on Box with a local file.
    sha1: str = Field(alias='sha1')

    # The file size in bytes. Be careful parsing this integer as it can get very large and cause an integer overflow.
    size: int = Field(alias='size')

    path_collection: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='path_collection')

    # The date and time when the file was created on Box.
    created_at: datetime = Field(alias='created_at')

    # The date and time when the file was last updated on Box.
    modified_at: datetime = Field(alias='modified_at')

    modified_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='modified_by')

    owned_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='owned_by')

    # Defines if this item has been deleted or not.  * `active` when the item has is not in the trash * `trashed` when the item has been moved to the trash but not deleted * `deleted` when the item has been permanently deleted.
    item_status: Literal["active", "trashed", "deleted"] = Field(alias='item_status')

    # The HTTP `etag` of this file. This can be used within some API endpoints in the `If-Match` and `If-None-Match` headers to only perform changes on the file if (no) changes have happened.
    etag: typing.Optional[typing.Optional[str]] = Field(None, alias='etag')

    # The name of the file
    name: typing.Optional[str] = Field(None, alias='name')

    file_version: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='file_version')

    # The time at which this file was put in the trash - becomes `null` after restore.
    trashed_at: typing.Optional[typing.Optional[str]] = Field(None, alias='trashed_at')

    # The time at which this file is expected to be purged from the trash  - becomes `null` after restore.
    purged_at: typing.Optional[typing.Optional[str]] = Field(None, alias='purged_at')

    # The date and time at which this file was originally created, which might be before it was uploaded to Box.
    content_created_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='content_created_at')

    # The date and time at which this file was last updated, which might be before it was uploaded to Box.
    content_modified_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='content_modified_at')

    created_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='created_by')

    # The shared link for this file. This will be `null` if a file had been trashed, even though the original shared link does become active again.
    shared_link: typing.Optional[typing.Optional[str]] = Field(None, alias='shared_link')

    parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='parent')
    class Config:
        arbitrary_types_allowed = True
