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


class RequiredUploadSession(TypedDict):
    pass

class OptionalUploadSession(TypedDict, total=False):
    # The unique identifier for this session
    id: str

    # `upload_session`
    type: str

    # The date and time when this session expires.
    session_expires_at: datetime

    # The  size in bytes that must be used for all parts of of the upload.  Only the last part is allowed to be of a smaller size.
    part_size: int

    # The total number of parts expected in this upload session, as determined by the file size and part size.
    total_parts: int

    # The number of parts that have been uploaded and processed by the server. This starts at `0`.  When committing a file files, inspecting this property can provide insight if all parts have been uploaded correctly.
    num_parts_processed: int

    session_endpoints: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class UploadSession(RequiredUploadSession, OptionalUploadSession):
    pass
