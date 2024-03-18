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

from box_python_sdk.pydantic.invite_invited_to import InviteInvitedTo
from box_python_sdk.pydantic.user_mini import UserMini

class Invite(BaseModel):
    # The unique identifier for this invite
    id: str = Field(alias='id')

    # `invite`
    type: Literal["invite"] = Field(alias='type')

    invited_to: typing.Optional[InviteInvitedTo] = Field(None, alias='invited_to')

    actionable_by: typing.Optional[UserMini] = Field(None, alias='actionable_by')

    invited_by: typing.Optional[UserMini] = Field(None, alias='invited_by')

    # The status of the invite
    status: typing.Optional[str] = Field(None, alias='status')

    # When the invite was created
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # When the invite was modified.
    modified_at: typing.Optional[datetime] = Field(None, alias='modified_at')
    class Config:
        arbitrary_types_allowed = True
