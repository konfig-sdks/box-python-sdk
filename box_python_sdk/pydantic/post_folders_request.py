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

from box_python_sdk.pydantic.post_folders_request_parent import PostFoldersRequestParent

class PostFoldersRequest(BaseModel):
    # The name for the new folder.  There are some restrictions to the file name. Names containing non-printable ASCII characters, forward and backward slashes (`/`, `\\`), as well as names with trailing spaces are prohibited.  Additionally, the names `.` and `..` are not allowed either.
    name: str = Field(alias='name')

    parent: PostFoldersRequestParent = Field(alias='parent')

    folder_upload_email: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='folder_upload_email')

    # Specifies whether a folder should be synced to a user's device or not. This is used by Box Sync (discontinued) and is not used by Box Drive.
    sync_state: typing.Optional[Literal["synced", "not_synced", "partially_synced"]] = Field(None, alias='sync_state')
    class Config:
        arbitrary_types_allowed = True
