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

from box_python_sdk.type.file_activity_user import FileActivityUser
from box_python_sdk.type.task_assignees_entries_item_permissions import TaskAssigneesEntriesItemPermissions

class RequiredTaskAssigneesEntriesItem(TypedDict):
    pass

class OptionalTaskAssigneesEntriesItem(TypedDict, total=False):
    # When the task assigned was completed.
    completed_at: typing.Optional[datetime]

    id: str

    # When the task assigned was modified.
    modified_at: datetime

    permissions: TaskAssigneesEntriesItemPermissions

    role: str

    status: str

    target: FileActivityUser

    type: str

class TaskAssigneesEntriesItem(RequiredTaskAssigneesEntriesItem, OptionalTaskAssigneesEntriesItem):
    pass
