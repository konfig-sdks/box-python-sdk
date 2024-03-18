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

from box_python_sdk.type.file_full import FileFull
from box_python_sdk.type.folder_full import FolderFull
from box_python_sdk.type.web_link import WebLink

class RequiredRecentItem(TypedDict):
    pass

class OptionalRecentItem(TypedDict, total=False):
    # `recent_item`
    type: str

    item: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The most recent type of access the user performed on the item.
    interaction_type: str

    # The time of the most recent interaction.
    interacted_at: datetime

    # If the item was accessed through a shared link it will appear here, otherwise this will be null.
    interaction_shared_link: str

class RecentItem(RequiredRecentItem, OptionalRecentItem):
    pass
