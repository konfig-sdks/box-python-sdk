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

from box_python_sdk.type.group_mini import GroupMini
from box_python_sdk.type.user_mini import UserMini

class RequiredGroupMembership(TypedDict):
    pass

class OptionalGroupMembership(TypedDict, total=False):
    # The unique identifier for this group membership
    id: str

    # `group_membership`
    type: str

    user: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    group: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The role of the user in the group.
    role: str

    # The time this membership was created.
    created_at: datetime

    # The time this membership was last modified.
    modified_at: datetime

class GroupMembership(RequiredGroupMembership, OptionalGroupMembership):
    pass
