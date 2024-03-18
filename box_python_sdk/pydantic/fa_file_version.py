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

from box_python_sdk.pydantic.file_activity_user import FileActivityUser

class FaFileVersion(BaseModel):
    # The unique identifier that represent a file version.
    id: str = Field(alias='id')

    # When the `file_version` object was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    created_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='created_by')

    # Version number.
    number: typing.Optional[int] = Field(None, alias='number')

    # When the `file_version` object was restored.
    restored_at: typing.Optional[datetime] = Field(None, alias='restored_at')

    restored_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='restored_by')

    # When the `file_version` object was trashed.
    trashed_at: typing.Optional[datetime] = Field(None, alias='trashed_at')

    trashed_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='trashed_by')

    # `file_version`
    type: typing.Optional[Literal["file_version"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
