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

from box_python_sdk.type.event import Event

class RequiredEvents(TypedDict):
    pass

class OptionalEvents(TypedDict, total=False):
    # The number of events returned in this response.
    chunk_size: int

    # The stream position of the start of the next page (chunk) of events.
    next_stream_position: str

    # A list of events
    entries: typing.List[Event]

class Events(RequiredEvents, OptionalEvents):
    pass
