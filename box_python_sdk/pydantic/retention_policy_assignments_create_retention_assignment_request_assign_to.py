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


class RetentionPolicyAssignmentsCreateRetentionAssignmentRequestAssignTo(BaseModel):
    # The type of item to assign the policy to.
    type: Literal["enterprise", "folder", "metadata_template"] = Field(alias='type')

    # The ID of item to assign the policy to. Set to `null` or omit when `type` is set to `enterprise`.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='id')
    class Config:
        arbitrary_types_allowed = True
