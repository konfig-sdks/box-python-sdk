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

from box_python_sdk.pydantic.file_mini import FileMini
from box_python_sdk.pydantic.file_version_mini import FileVersionMini
from box_python_sdk.pydantic.retention_policy_mini import RetentionPolicyMini

class FileVersionRetention(BaseModel):
    # The unique identifier for this file version retention.
    id: typing.Optional[str] = Field(None, alias='id')

    # `file_version_retention`
    type: typing.Optional[Literal["file_version_retention"]] = Field(None, alias='type')

    file_version: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='file_version')

    file: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='file')

    # When this file version retention object was created
    applied_at: typing.Optional[datetime] = Field(None, alias='applied_at')

    # When the retention expires on this file version retention
    disposition_at: typing.Optional[datetime] = Field(None, alias='disposition_at')

    winning_retention_policy: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='winning_retention_policy')
    class Config:
        arbitrary_types_allowed = True
