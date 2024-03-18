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

from box_python_sdk.pydantic.enterprise_base import EnterpriseBase
from box_python_sdk.pydantic.user_base import UserBase

class ShieldInformationBarrier(BaseModel):
    # The unique identifier for the shield information barrier
    id: typing.Optional[str] = Field(None, alias='id')

    # The type of the shield information barrier
    type: typing.Optional[Literal["shield_information_barrier"]] = Field(None, alias='type')

    # The `type` and `id` of enterprise this barrier is under.
    enterprise: typing.Optional[EnterpriseBase] = Field(None, alias='enterprise')

    # Status of the shield information barrier
    status: typing.Optional[Literal["draft", "pending", "disabled", "enabled", "invalid"]] = Field(None, alias='status')

    # ISO date time string when this shield information barrier object was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # The user who created this shield information barrier.
    created_by: typing.Optional[UserBase] = Field(None, alias='created_by')

    # ISO date time string when this shield information barrier was updated.
    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')

    # The user that updated this shield information barrier.
    updated_by: typing.Optional[UserBase] = Field(None, alias='updated_by')

    # ISO date time string when this shield information barrier was enabled.
    enabled_at: typing.Optional[datetime] = Field(None, alias='enabled_at')

    enabled_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='enabled_by')
    class Config:
        arbitrary_types_allowed = True
