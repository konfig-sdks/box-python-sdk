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

from box_python_sdk.pydantic.user_mini import UserMini

class CollaborationAllowlistExemptTarget(BaseModel):
    # The unique identifier for this exemption
    id: typing.Optional[str] = Field(None, alias='id')

    # `collaboration_whitelist_exempt_target`
    type: typing.Optional[Literal["collaboration_whitelist_exempt_target"]] = Field(None, alias='type')

    enterprise: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='enterprise')

    user: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='user')

    # The time the entry was created
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # The time the entry was modified
    modified_at: typing.Optional[datetime] = Field(None, alias='modified_at')
    class Config:
        arbitrary_types_allowed = True