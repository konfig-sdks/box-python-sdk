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

from box_python_sdk.pydantic.uploads_small_file_request_attributes_parent import UploadsSmallFileRequestAttributesParent

class UploadsSmallFileRequestAttributes(BaseModel):
    # The name of the file
    name: str = Field(alias='name')

    parent: UploadsSmallFileRequestAttributesParent = Field(alias='parent')

    # Defines the time the file was originally created at.  If not set, the upload time will be used.
    content_created_at: typing.Optional[datetime] = Field(None, alias='content_created_at')

    # Defines the time the file was last modified at.  If not set, the upload time will be used.
    content_modified_at: typing.Optional[datetime] = Field(None, alias='content_modified_at')
    class Config:
        arbitrary_types_allowed = True
