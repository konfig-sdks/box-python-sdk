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

from box_python_sdk.type.event_source import EventSource
from box_python_sdk.type.file import File
from box_python_sdk.type.folder import Folder
from box_python_sdk.type.generic_source import GenericSource
from box_python_sdk.type.user import User
from box_python_sdk.type.user_mini import UserMini

class RequiredEvent(TypedDict):
    pass

class OptionalEvent(TypedDict, total=False):
    # `event`
    type: str

    # When the event object was created
    created_at: datetime

    # When the event object was recorded in database
    recorded_at: datetime

    # The ID of the event object. You can use this to detect duplicate events
    event_id: str

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    event_type: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The session of the user that performed the action. Not all events will populate this attribute.
    session_id: str

    source: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # This object provides additional information about the event if available.  This can include how a user performed an event as well as additional information to correlate an event to external KeySafe logs. Not all events have an `additional_details` object.  This object is only available in the Enterprise Events.
    additional_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class Event(RequiredEvent, OptionalEvent):
    pass
