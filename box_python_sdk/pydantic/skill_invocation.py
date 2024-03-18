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

from box_python_sdk.pydantic.event import Event
from box_python_sdk.pydantic.file import File
from box_python_sdk.pydantic.folder import Folder
from box_python_sdk.pydantic.skill_invocation_status import SkillInvocationStatus
from box_python_sdk.pydantic.skill_invocation_token import SkillInvocationToken

class SkillInvocation(BaseModel):
    # `skill_invocation`
    type: typing.Optional[Literal["skill_invocation"]] = Field(None, alias='type')

    # Unique identifier for the invocation request.
    id: typing.Optional[str] = Field(None, alias='id')

    skill: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='skill')

    token: typing.Optional[SkillInvocationToken] = Field(None, alias='token')

    status: typing.Optional[SkillInvocationStatus] = Field(None, alias='status')

    # The time this invocation was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # Action that triggered the invocation
    trigger: typing.Optional[str] = Field(None, alias='trigger')

    enterprise: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='enterprise')

    source: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='source')

    event: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='event')
    class Config:
        arbitrary_types_allowed = True
