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

from box_python_sdk.type.shield_information_barrier_base import ShieldInformationBarrierBase
from box_python_sdk.type.user_base import UserBase

class RequiredShieldInformationBarrierSegment(TypedDict):
    pass

class OptionalShieldInformationBarrierSegment(TypedDict, total=False):
    # Description of the shield information barrier segment
    description: str

    # The unique identifier for the shield information barrier segment
    id: str

    # The type of the shield information barrier segment
    type: str

    shield_information_barrier: ShieldInformationBarrierBase

    # Name of the shield information barrier segment
    name: str

    # ISO date time string when this shield information barrier object was created.
    created_at: datetime

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # ISO date time string when this shield information barrier segment was updated.
    updated_at: datetime

    updated_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class ShieldInformationBarrierSegment(RequiredShieldInformationBarrierSegment, OptionalShieldInformationBarrierSegment):
    pass
