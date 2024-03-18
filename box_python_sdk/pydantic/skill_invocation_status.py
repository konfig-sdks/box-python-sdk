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


class SkillInvocationStatus(BaseModel):
    # The state of this event.  * `invoked` - Triggered the skill with event details to start   applying skill on the file. * `processing` - Currently processing. * `success` - Completed processing with a success. * `transient_failure` - Encountered an issue which can be   retried. * `permanent_failure` -  Encountered a permanent issue and   retry would not help.
    state: typing.Optional[Literal["invoked", "processing", "success", "transient_failure", "permanent_failure"]] = Field(None, alias='state')

    # Status information
    message: typing.Optional[str] = Field(None, alias='message')

    # Error code information, if error occurred.
    error_code: typing.Optional[str] = Field(None, alias='error_code')

    # Additional status information.
    additional_info: typing.Optional[str] = Field(None, alias='additional_info')
    class Config:
        arbitrary_types_allowed = True
