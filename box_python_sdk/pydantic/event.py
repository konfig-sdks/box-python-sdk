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

from box_python_sdk.pydantic.event_source import EventSource
from box_python_sdk.pydantic.file import File
from box_python_sdk.pydantic.folder import Folder
from box_python_sdk.pydantic.generic_source import GenericSource
from box_python_sdk.pydantic.user import User
from box_python_sdk.pydantic.user_mini import UserMini

class Event(BaseModel):
    # `event`
    type: typing.Optional[str] = Field(None, alias='type')

    # When the event object was created
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # When the event object was recorded in database
    recorded_at: typing.Optional[datetime] = Field(None, alias='recorded_at')

    # The ID of the event object. You can use this to detect duplicate events
    event_id: typing.Optional[str] = Field(None, alias='event_id')

    created_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='created_by')

    event_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='event_type')

    # The session of the user that performed the action. Not all events will populate this attribute.
    session_id: typing.Optional[str] = Field(None, alias='session_id')

    source: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='source')

    # This object provides additional information about the event if available.  This can include how a user performed an event as well as additional information to correlate an event to external KeySafe logs. Not all events have an `additional_details` object.  This object is only available in the Enterprise Events.
    additional_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='additional_details')
    class Config:
        arbitrary_types_allowed = True
