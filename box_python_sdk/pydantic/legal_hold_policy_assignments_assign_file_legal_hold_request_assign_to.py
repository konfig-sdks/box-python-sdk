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


class LegalHoldPolicyAssignmentsAssignFileLegalHoldRequestAssignTo(BaseModel):
    # The type of item to assign the policy to
    type: Literal["file", "file_version", "folder", "user"] = Field(alias='type')

    # The ID of item to assign the policy to
    id: str = Field(alias='id')
    class Config:
        arbitrary_types_allowed = True
