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


class UploadSession(BaseModel):
    # The unique identifier for this session
    id: typing.Optional[str] = Field(None, alias='id')

    # `upload_session`
    type: typing.Optional[Literal["upload_session"]] = Field(None, alias='type')

    # The date and time when this session expires.
    session_expires_at: typing.Optional[datetime] = Field(None, alias='session_expires_at')

    # The  size in bytes that must be used for all parts of of the upload.  Only the last part is allowed to be of a smaller size.
    part_size: typing.Optional[int] = Field(None, alias='part_size')

    # The total number of parts expected in this upload session, as determined by the file size and part size.
    total_parts: typing.Optional[int] = Field(None, alias='total_parts')

    # The number of parts that have been uploaded and processed by the server. This starts at `0`.  When committing a file files, inspecting this property can provide insight if all parts have been uploaded correctly.
    num_parts_processed: typing.Optional[int] = Field(None, alias='num_parts_processed')

    session_endpoints: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='session_endpoints')
    class Config:
        arbitrary_types_allowed = True
