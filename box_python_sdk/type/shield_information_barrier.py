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

from box_python_sdk.type.enterprise_base import EnterpriseBase
from box_python_sdk.type.user_base import UserBase

class RequiredShieldInformationBarrier(TypedDict):
    pass

class OptionalShieldInformationBarrier(TypedDict, total=False):
    # The unique identifier for the shield information barrier
    id: str

    # The type of the shield information barrier
    type: str

    # The `type` and `id` of enterprise this barrier is under.
    enterprise: EnterpriseBase

    # Status of the shield information barrier
    status: str

    # ISO date time string when this shield information barrier object was created.
    created_at: datetime

    # The user who created this shield information barrier.
    created_by: UserBase

    # ISO date time string when this shield information barrier was updated.
    updated_at: datetime

    # The user that updated this shield information barrier.
    updated_by: UserBase

    # ISO date time string when this shield information barrier was enabled.
    enabled_at: datetime

    enabled_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class ShieldInformationBarrier(RequiredShieldInformationBarrier, OptionalShieldInformationBarrier):
    pass
