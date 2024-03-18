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

from box_python_sdk.type.file_mini import FileMini
from box_python_sdk.type.user_mini import UserMini

class RequiredTaskAssignment(TypedDict):
    pass

class OptionalTaskAssignment(TypedDict, total=False):
    # The unique identifier for this task assignment
    id: str

    # `task_assignment`
    type: str

    item: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    assigned_to: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # A message that will is included with the task assignment. This is visible to the assigned user in the web and mobile UI.
    message: str

    # The date at which this task assignment was completed. This will be `null` if the task is not completed yet.
    completed_at: datetime

    # The date at which this task was assigned to the user.
    assigned_at: datetime

    # The date at which the assigned user was reminded of this task assignment.
    reminded_at: datetime

    # The current state of the assignment. The available states depend on the `action` value of the task object.
    resolution_state: str

    assigned_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class TaskAssignment(RequiredTaskAssignment, OptionalTaskAssignment):
    pass
