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

class FileRequest(BaseModel):
    # The unique identifier for this file request.
    id: str = Field(alias='id')

    # `file_request`
    type: Literal["file_request"] = Field(alias='type')

    folder: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='folder')

    # The date and time when the file request was created.
    created_at: datetime = Field(alias='created_at')

    # The date and time when the file request was last updated.
    updated_at: datetime = Field(alias='updated_at')

    # The title of file request. This is shown in the Box UI to users uploading files.  This defaults to title of the file request that was copied to create this file request.
    title: typing.Optional[str] = Field(None, alias='title')

    # The optional description of this file request. This is shown in the Box UI to users uploading files.  This defaults to description of the file request that was copied to create this file request.
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    # The status of the file request. This defaults to `active`.  When the status is set to `inactive`, the file request will no longer accept new submissions, and any visitor to the file request URL will receive a `HTTP 404` status code.  This defaults to status of file request that was copied to create this file request.
    status: typing.Optional[Literal["active", "inactive"]] = Field(None, alias='status')

    # Whether a file request submitter is required to provide their email address.  When this setting is set to true, the Box UI will show an email field on the file request form.  This defaults to setting of file request that was copied to create this file request.
    is_email_required: typing.Optional[bool] = Field(None, alias='is_email_required')

    # Whether a file request submitter is required to provide a description of the files they are submitting.  When this setting is set to true, the Box UI will show a description field on the file request form.  This defaults to setting of file request that was copied to create this file request.
    is_description_required: typing.Optional[bool] = Field(None, alias='is_description_required')

    # The date after which a file request will no longer accept new submissions.  After this date, the `status` will automatically be set to `inactive`.
    expires_at: typing.Optional[datetime] = Field(None, alias='expires_at')

    # The generated URL for this file request. This URL can be shared with users to let them upload files to the associated folder.
    url: typing.Optional[str] = Field(None, alias='url')

    # The HTTP `etag` of this file. This can be used in combination with the `If-Match` header when updating a file request. By providing that header, a change will only be performed on the  file request if the `etag` on the file request still matches the `etag` provided in the `If-Match` header.
    etag: typing.Optional[typing.Optional[str]] = Field(None, alias='etag')

    created_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='created_by')

    updated_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='updated_by')
    class Config:
        arbitrary_types_allowed = True
