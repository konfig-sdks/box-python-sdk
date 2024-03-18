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


class TaskLinksEntriesItemTarget(BaseModel):
    type: typing.Optional[str] = Field(None, alias='type')

    id: typing.Optional[str] = Field(None, alias='id')

    sequence_id: typing.Optional[str] = Field(None, alias='sequence_id')

    etag: typing.Optional[str] = Field(None, alias='etag')

    sha1: typing.Optional[str] = Field(None, alias='sha1')

    name: typing.Optional[str] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
