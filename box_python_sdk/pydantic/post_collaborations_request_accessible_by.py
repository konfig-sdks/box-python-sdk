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


class PostCollaborationsRequestAccessibleBy(BaseModel):
    # The type of collaborator to invite.
    type: Literal["user", "group"] = Field(alias='type')

    # The ID of the user or group.  Alternatively, use `login` to specify a user by email address.
    id: typing.Optional[str] = Field(None, alias='id')

    # The email address of the user to grant access to the item.  Alternatively, use `id` to specify a user by user ID.
    login: typing.Optional[str] = Field(None, alias='login')
    class Config:
        arbitrary_types_allowed = True
