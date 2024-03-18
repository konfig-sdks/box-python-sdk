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

from box_python_sdk.pydantic.file_full import FileFull
from box_python_sdk.pydantic.folder_full import FolderFull
from box_python_sdk.pydantic.web_link import WebLink

class RecentItem(BaseModel):
    # `recent_item`
    type: typing.Optional[str] = Field(None, alias='type')

    item: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='item')

    # The most recent type of access the user performed on the item.
    interaction_type: typing.Optional[Literal["item_preview", "item_upload", "item_comment", "item_open", "item_modify"]] = Field(None, alias='interaction_type')

    # The time of the most recent interaction.
    interacted_at: typing.Optional[datetime] = Field(None, alias='interacted_at')

    # If the item was accessed through a shared link it will appear here, otherwise this will be null.
    interaction_shared_link: typing.Optional[str] = Field(None, alias='interaction_shared_link')
    class Config:
        arbitrary_types_allowed = True
