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
from box_python_sdk.pydantic.reply_parent import ReplyParent

class Reply(BaseModel):
    # reply object id.
    id: typing.Optional[str] = Field(None, alias='id')

    # When the reply object was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    created_by: typing.Optional[FileActivityUser] = Field(None, alias='created_by')

    # Reply message
    message: typing.Optional[str] = Field(None, alias='message')

    parent: typing.Optional[ReplyParent] = Field(None, alias='parent')

    # Reply type
    type: typing.Optional[Literal["comment"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
