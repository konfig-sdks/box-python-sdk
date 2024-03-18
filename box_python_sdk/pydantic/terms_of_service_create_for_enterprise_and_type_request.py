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


class TermsOfServiceCreateForEnterpriseAndTypeRequest(BaseModel):
    # Whether this terms of service is active.
    status: Literal["enabled", "disabled"] = Field(alias='status')

    # The terms of service text to display to users.  The text can be set to empty if the `status` is set to `disabled`.
    text: str = Field(alias='text')

    # The type of user to set the terms of service for.
    tos_type: typing.Optional[Literal["external", "managed"]] = Field(None, alias='tos_type')
    class Config:
        arbitrary_types_allowed = True
