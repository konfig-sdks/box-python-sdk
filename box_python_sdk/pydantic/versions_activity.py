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

from box_python_sdk.pydantic.fa_file_version import FaFileVersion
from box_python_sdk.pydantic.file_activity_user import FileActivityUser

class VersionsActivity(BaseModel):
    # Users who performed one of the `action_types` (`created`, `deleted` or `restored`)
    action_by: typing.Optional[typing.List[FileActivityUser]] = Field(None, alias='action_by')

    action_type: typing.Optional[Literal["created", "restored", "trashed"]] = Field(None, alias='action_type')

    end: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='end')

    start: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='start')

    type: typing.Optional[Literal["versions"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
