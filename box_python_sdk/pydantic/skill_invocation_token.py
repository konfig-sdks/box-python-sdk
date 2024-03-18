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

from box_python_sdk.pydantic.skill_invocation_token_read import SkillInvocationTokenRead
from box_python_sdk.pydantic.skill_invocation_token_write import SkillInvocationTokenWrite

class SkillInvocationToken(BaseModel):
    read: typing.Optional[SkillInvocationTokenRead] = Field(None, alias='read')

    write: typing.Optional[SkillInvocationTokenWrite] = Field(None, alias='write')
    class Config:
        arbitrary_types_allowed = True
