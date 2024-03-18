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

from box_python_sdk.pydantic.event_source_classification import EventSourceClassification
from box_python_sdk.pydantic.folder_mini import FolderMini
from box_python_sdk.pydantic.user_mini import UserMini

class EventSource(BaseModel):
    # The type of the item that the event represents. Can be `file` or `folder`. 
    item_type: Literal["file", "folder"] = Field(alias='item_type')

    # The unique identifier that represents the item. 
    item_id: str = Field(alias='item_id')

    # The name of the item. 
    item_name: str = Field(alias='item_name')

    classification: typing.Optional[EventSourceClassification] = Field(None, alias='classification')

    parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='parent')

    owned_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='owned_by')
    class Config:
        arbitrary_types_allowed = True
