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


class UploadUrl(BaseModel):
    # A URL for an upload session that can be used to upload the file.
    upload_url: typing.Optional[str] = Field(None, alias='upload_url')

    # An optional access token to use to upload the file
    upload_token: typing.Optional[str] = Field(None, alias='upload_token')
    class Config:
        arbitrary_types_allowed = True
