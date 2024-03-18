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

from box_python_sdk.pydantic.folder_mini import FolderMini
from box_python_sdk.pydantic.user_mini import UserMini

class TrashFolder(BaseModel):
    description: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='description')

    # The unique identifier that represent a folder.  The ID for any folder can be determined by visiting a folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folders/123` the `folder_id` is `123`.
    id: str = Field(alias='id')

    # `folder`
    type: Literal["folder"] = Field(alias='type')

    # The name of the folder.
    name: str = Field(alias='name')

    # The folder size in bytes.  Be careful parsing this integer as its value can get very large.
    size: int = Field(alias='size')

    path_collection: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='path_collection')

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='created_by')

    modified_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='modified_by')

    owned_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='owned_by')

    # Defines if this item has been deleted or not.  * `active` when the item has is not in the trash * `trashed` when the item has been moved to the trash but not deleted * `deleted` when the item has been permanently deleted.
    item_status: Literal["active", "trashed", "deleted"] = Field(alias='item_status')

    # The HTTP `etag` of this folder. This can be used within some API endpoints in the `If-Match` and `If-None-Match` headers to only perform changes on the folder if (no) changes have happened.
    etag: typing.Optional[typing.Optional[str]] = Field(None, alias='etag')

    sequence_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='sequence_id')

    # The date and time when the folder was created. This value may be `null` for some folders such as the root folder or the trash folder.
    created_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='created_at')

    # The date and time when the folder was last updated. This value may be `null` for some folders such as the root folder or the trash folder.
    modified_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='modified_at')

    # The time at which this folder was put in the trash.
    trashed_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='trashed_at')

    # The time at which this folder is expected to be purged from the trash.
    purged_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='purged_at')

    # The date and time at which this folder was originally created.
    content_created_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='content_created_at')

    # The date and time at which this folder was last updated.
    content_modified_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='content_modified_at')

    # The shared link for this folder. This will be `null` if a folder has been trashed, since the link will no longer be active.
    shared_link: typing.Optional[typing.Optional[str]] = Field(None, alias='shared_link')

    # The folder upload email for this folder. This will be `null` if a folder has been trashed, since the upload will no longer work.
    folder_upload_email: typing.Optional[typing.Optional[str]] = Field(None, alias='folder_upload_email')

    parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='parent')
    class Config:
        arbitrary_types_allowed = True
