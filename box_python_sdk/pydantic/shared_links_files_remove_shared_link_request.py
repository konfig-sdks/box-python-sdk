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


class SharedLinksFilesRemoveSharedLinkRequest(BaseModel):
    # By setting this value to `null`, the shared link is removed from the file.
    shared_link: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='shared_link')
    class Config:
        arbitrary_types_allowed = True
