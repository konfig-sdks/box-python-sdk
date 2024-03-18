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

from box_python_sdk.pydantic.terms_of_service_base import TermsOfServiceBase
from box_python_sdk.pydantic.user_mini import UserMini

class TermsOfServiceUserStatus(BaseModel):
    # The unique identifier for this terms of service user status
    id: str = Field(alias='id')

    # `terms_of_service_user_status`
    type: Literal["terms_of_service_user_status"] = Field(alias='type')

    tos: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='tos')

    user: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='user')

    # If the user has accepted the terms of services
    is_accepted: typing.Optional[bool] = Field(None, alias='is_accepted')

    # When the legal item was created
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # When the legal item was modified.
    modified_at: typing.Optional[datetime] = Field(None, alias='modified_at')
    class Config:
        arbitrary_types_allowed = True
