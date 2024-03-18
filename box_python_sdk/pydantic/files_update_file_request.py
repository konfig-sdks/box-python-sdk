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

from box_python_sdk.pydantic.files_update_file_request_collections import FilesUpdateFileRequestCollections
from box_python_sdk.pydantic.files_update_file_request_lock import FilesUpdateFileRequestLock
from box_python_sdk.pydantic.files_update_file_request_permissions import FilesUpdateFileRequestPermissions
from box_python_sdk.pydantic.files_update_file_request_tags import FilesUpdateFileRequestTags

class FilesUpdateFileRequest(BaseModel):
    tags: typing.Optional[FilesUpdateFileRequestTags] = Field(None, alias='tags')

    # The description for a file. This can be seen in the right-hand sidebar panel when viewing a file in the Box web app. Additionally, this index is used in the search index of the file, allowing users to find the file by the content in the description.
    description: typing.Optional[str] = Field(None, alias='description')

    # An optional different name for the file. This can be used to rename the file.
    name: typing.Optional[str] = Field(None, alias='name')

    parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='parent')

    shared_link: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='shared_link')

    lock: typing.Optional[FilesUpdateFileRequestLock] = Field(None, alias='lock')

    # The retention expiration timestamp for the given file. This date cannot be shortened once set on a file.
    disposition_at: typing.Optional[datetime] = Field(None, alias='disposition_at')

    permissions: typing.Optional[FilesUpdateFileRequestPermissions] = Field(None, alias='permissions')

    collections: typing.Optional[FilesUpdateFileRequestCollections] = Field(None, alias='collections')
    class Config:
        arbitrary_types_allowed = True
