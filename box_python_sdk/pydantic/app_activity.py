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

from box_python_sdk.pydantic.app_activity_activity_template import AppActivityActivityTemplate
from box_python_sdk.pydantic.app_group_mini import AppGroupMini
from box_python_sdk.pydantic.app_mini import AppMini
from box_python_sdk.pydantic.file_activity_user import FileActivityUser

class AppActivity(BaseModel):
    id: str = Field(alias='id')

    activity_template: typing.Optional[AppActivityActivityTemplate] = Field(None, alias='activity_template')

    app: typing.Optional[AppMini] = Field(None, alias='app')

    app_group: typing.Optional[AppGroupMini] = Field(None, alias='app_group')

    created_by: typing.Optional[FileActivityUser] = Field(None, alias='created_by')

    # When the `app_activity` object was created.
    occurred_at: typing.Optional[datetime] = Field(None, alias='occurred_at')

    rendered_text: typing.Optional[str] = Field(None, alias='rendered_text')

    type: typing.Optional[Literal["app_activity"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
