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
from box_python_sdk.type.task_assignments import TaskAssignments
from box_python_sdk.type.user_mini import UserMini

class RequiredTask(TypedDict):
    pass

class OptionalTask(TypedDict, total=False):
    # The unique identifier for this task
    id: str

    # `task`
    type: str

    item: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # When the task is due
    due_at: datetime

    # The type of task the task assignee will be prompted to perform.
    action: str

    # A message that will be included with the task
    message: str

    task_assignment_collection: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Whether the task has been completed
    is_completed: bool

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # When the task object was created
    created_at: datetime

    # Defines which assignees need to complete this task before the task is considered completed.  * `all_assignees` requires all assignees to review or approve the the task in order for it to be considered completed. * `any_assignee` accepts any one assignee to review or approve the the task in order for it to be considered completed.
    completion_rule: str

class Task(RequiredTask, OptionalTask):
    pass
