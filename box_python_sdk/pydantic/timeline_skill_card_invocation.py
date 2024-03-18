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


class TimelineSkillCardInvocation(BaseModel):
    # `skill_invocation`
    type: Literal["skill_invocation"] = Field(alias='type')

    # A custom identifier that represent the instance of the service that applied this metadata. For example, if your `image-recognition-service` runs on multiple nodes, this field can be used to identify the ID of the node that was used to apply the metadata.
    id: str = Field(alias='id')
    class Config:
        arbitrary_types_allowed = True
