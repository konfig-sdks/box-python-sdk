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

class RequiredFileRequest(TypedDict):
    # The unique identifier for this file request.
    id: str

    # `file_request`
    type: str

    folder: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The date and time when the file request was created.
    created_at: datetime

    # The date and time when the file request was last updated.
    updated_at: datetime

class OptionalFileRequest(TypedDict, total=False):
    # The title of file request. This is shown in the Box UI to users uploading files.  This defaults to title of the file request that was copied to create this file request.
    title: str

    # The optional description of this file request. This is shown in the Box UI to users uploading files.  This defaults to description of the file request that was copied to create this file request.
    description: typing.Optional[str]

    # The status of the file request. This defaults to `active`.  When the status is set to `inactive`, the file request will no longer accept new submissions, and any visitor to the file request URL will receive a `HTTP 404` status code.  This defaults to status of file request that was copied to create this file request.
    status: str

    # Whether a file request submitter is required to provide their email address.  When this setting is set to true, the Box UI will show an email field on the file request form.  This defaults to setting of file request that was copied to create this file request.
    is_email_required: bool

    # Whether a file request submitter is required to provide a description of the files they are submitting.  When this setting is set to true, the Box UI will show a description field on the file request form.  This defaults to setting of file request that was copied to create this file request.
    is_description_required: bool

    # The date after which a file request will no longer accept new submissions.  After this date, the `status` will automatically be set to `inactive`.
    expires_at: datetime

    # The generated URL for this file request. This URL can be shared with users to let them upload files to the associated folder.
    url: str

    # The HTTP `etag` of this file. This can be used in combination with the `If-Match` header when updating a file request. By providing that header, a change will only be performed on the  file request if the `etag` on the file request still matches the `etag` provided in the `If-Match` header.
    etag: typing.Optional[str]

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    updated_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class FileRequest(RequiredFileRequest, OptionalFileRequest):
    pass
