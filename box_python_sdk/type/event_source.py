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

from box_python_sdk.type.event_source_classification import EventSourceClassification
from box_python_sdk.type.folder_mini import FolderMini
from box_python_sdk.type.user_mini import UserMini

class RequiredEventSource(TypedDict):
    # The type of the item that the event represents. Can be `file` or `folder`. 
    item_type: str

    # The unique identifier that represents the item. 
    item_id: str

    # The name of the item. 
    item_name: str

class OptionalEventSource(TypedDict, total=False):
    classification: EventSourceClassification

    parent: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    owned_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class EventSource(RequiredEventSource, OptionalEventSource):
    pass
