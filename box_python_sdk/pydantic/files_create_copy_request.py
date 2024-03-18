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

from box_python_sdk.pydantic.files_create_copy_request_parent import FilesCreateCopyRequestParent

class FilesCreateCopyRequest(BaseModel):
    parent: FilesCreateCopyRequestParent = Field(alias='parent')

    # An optional ID of the specific file version to copy.
    version: typing.Optional[str] = Field(None, alias='version')

    # An optional new name for the copied file.  There are some restrictions to the file name. Names containing non-printable ASCII characters, forward and backward slashes (`/`, `\\`), and protected names like `.` and `..` are automatically sanitized by removing the non-allowed characters.
    name: typing.Optional[str] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
