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


class SkillInvocationTokenRead(BaseModel):
    # The requested access token.
    access_token: typing.Optional[str] = Field(None, alias='access_token')

    # The time in seconds by which this token will expire.
    expires_in: typing.Optional[int] = Field(None, alias='expires_in')

    # The type of access token returned.
    token_type: typing.Optional[Literal["bearer"]] = Field(None, alias='token_type')

    # The permissions that this access token permits, providing a list of resources (files, folders, etc) and the scopes permitted for each of those resources.
    restricted_to: typing.Optional[str] = Field(None, alias='restricted_to')
    class Config:
        arbitrary_types_allowed = True
