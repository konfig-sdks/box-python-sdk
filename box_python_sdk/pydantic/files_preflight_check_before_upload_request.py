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


class FilesPreflightCheckBeforeUploadRequest(BaseModel):
    # The name for the file
    name: typing.Optional[str] = Field(None, alias='name')

    # The size of the file in bytes
    size: typing.Optional[int] = Field(None, alias='size')

    parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='parent')
    class Config:
        arbitrary_types_allowed = True
