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


class CollaborationAcceptanceRequirementsStatusTwoFactorAuthenticationRequirement(BaseModel):
    # Whether or not the enterprise that owns the content requires two-factor authentication to be enabled in order to collaborate on the content.
    enterprise_has_two_factor_auth_enabled: typing.Optional[bool] = Field(None, alias='enterprise_has_two_factor_auth_enabled')

    # Whether or not the user has two-factor authentication enabled. The field is `null` when two-factor authentication is not required.
    user_has_two_factor_authentication_enabled: typing.Optional[typing.Optional[bool]] = Field(None, alias='user_has_two_factor_authentication_enabled')
    class Config:
        arbitrary_types_allowed = True
