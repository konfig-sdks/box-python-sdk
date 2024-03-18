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


class StatusSkillCardStatus(BaseModel):
    # A code for the status of this Skill invocation. By default each of these will have their own accompanied messages. These can be adjusted by setting the `message` value on this object.
    code: Literal["invoked", "processing", "success", "transient_failure", "permanent_failure"] = Field(alias='code')

    # A custom message that can be provided with this status. This will be shown in the web app to the end user.
    message: typing.Optional[str] = Field(None, alias='message')
    class Config:
        arbitrary_types_allowed = True
