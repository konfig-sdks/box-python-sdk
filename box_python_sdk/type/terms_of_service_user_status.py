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

from box_python_sdk.type.terms_of_service_base import TermsOfServiceBase
from box_python_sdk.type.user_mini import UserMini

class RequiredTermsOfServiceUserStatus(TypedDict):
    # The unique identifier for this terms of service user status
    id: str

    # `terms_of_service_user_status`
    type: str

class OptionalTermsOfServiceUserStatus(TypedDict, total=False):
    tos: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    user: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # If the user has accepted the terms of services
    is_accepted: bool

    # When the legal item was created
    created_at: datetime

    # When the legal item was modified.
    modified_at: datetime

class TermsOfServiceUserStatus(RequiredTermsOfServiceUserStatus, OptionalTermsOfServiceUserStatus):
    pass
