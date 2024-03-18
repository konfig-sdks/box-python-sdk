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

from box_python_sdk.pydantic.shield_information_barrier_base import ShieldInformationBarrierBase
from box_python_sdk.pydantic.user_base import UserBase

class ShieldInformationBarrierSegment(BaseModel):
    # Description of the shield information barrier segment
    description: typing.Optional[str] = Field(None, alias='description')

    # The unique identifier for the shield information barrier segment
    id: typing.Optional[str] = Field(None, alias='id')

    # The type of the shield information barrier segment
    type: typing.Optional[Literal["shield_information_barrier_segment"]] = Field(None, alias='type')

    shield_information_barrier: typing.Optional[ShieldInformationBarrierBase] = Field(None, alias='shield_information_barrier')

    # Name of the shield information barrier segment
    name: typing.Optional[str] = Field(None, alias='name')

    # ISO date time string when this shield information barrier object was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    created_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='created_by')

    # ISO date time string when this shield information barrier segment was updated.
    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')

    updated_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='updated_by')
    class Config:
        arbitrary_types_allowed = True
