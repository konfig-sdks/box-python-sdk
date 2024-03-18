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


class CollaborationAcceptanceRequirementsStatusStrongPasswordRequirement(BaseModel):
    # Whether or not the enterprise that owns the content requires a strong password to collaborate on the content.
    enterprise_has_strong_password_required_for_external_users: typing.Optional[bool] = Field(None, alias='enterprise_has_strong_password_required_for_external_users')

    # Whether or not the user has a strong password set for their account. The field is `null` when a strong password is not required.
    user_has_strong_password: typing.Optional[typing.Optional[bool]] = Field(None, alias='user_has_strong_password')
    class Config:
        arbitrary_types_allowed = True
