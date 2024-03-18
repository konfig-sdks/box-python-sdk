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

from box_python_sdk.pydantic.event import Event

class Events(BaseModel):
    # The number of events returned in this response.
    chunk_size: typing.Optional[int] = Field(None, alias='chunk_size')

    # The stream position of the start of the next page (chunk) of events.
    next_stream_position: typing.Optional[str] = Field(None, alias='next_stream_position')

    # A list of events
    entries: typing.Optional[typing.List[Event]] = Field(None, alias='entries')
    class Config:
        arbitrary_types_allowed = True
