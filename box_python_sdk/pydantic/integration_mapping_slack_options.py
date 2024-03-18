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


class IntegrationMappingSlackOptions(BaseModel):
    # Indicates whether or not channel member access to the underlying box item should be automatically managed. Depending on type of channel, access is managed through creating collaborations or shared links.
    is_access_management_disabled: typing.Optional[bool] = Field(None, alias='is_access_management_disabled')
    class Config:
        arbitrary_types_allowed = True
