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

from box_python_sdk.pydantic.group_mini import GroupMini
from box_python_sdk.pydantic.user_mini import UserMini

class GroupMembership(BaseModel):
    # The unique identifier for this group membership
    id: typing.Optional[str] = Field(None, alias='id')

    # `group_membership`
    type: typing.Optional[Literal["group_membership"]] = Field(None, alias='type')

    user: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='user')

    group: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='group')

    # The role of the user in the group.
    role: typing.Optional[Literal["member", "admin"]] = Field(None, alias='role')

    # The time this membership was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # The time this membership was last modified.
    modified_at: typing.Optional[datetime] = Field(None, alias='modified_at')
    class Config:
        arbitrary_types_allowed = True
