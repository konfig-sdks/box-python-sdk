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

from box_python_sdk.pydantic.file_mini import FileMini
from box_python_sdk.pydantic.task_assignments import TaskAssignments
from box_python_sdk.pydantic.user_mini import UserMini

class Task(BaseModel):
    # The unique identifier for this task
    id: typing.Optional[str] = Field(None, alias='id')

    # `task`
    type: typing.Optional[Literal["task"]] = Field(None, alias='type')

    item: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='item')

    # When the task is due
    due_at: typing.Optional[datetime] = Field(None, alias='due_at')

    # The type of task the task assignee will be prompted to perform.
    action: typing.Optional[Literal["review", "complete"]] = Field(None, alias='action')

    # A message that will be included with the task
    message: typing.Optional[str] = Field(None, alias='message')

    task_assignment_collection: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='task_assignment_collection')

    # Whether the task has been completed
    is_completed: typing.Optional[bool] = Field(None, alias='is_completed')

    created_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='created_by')

    # When the task object was created
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # Defines which assignees need to complete this task before the task is considered completed.  * `all_assignees` requires all assignees to review or approve the the task in order for it to be considered completed. * `any_assignee` accepts any one assignee to review or approve the the task in order for it to be considered completed.
    completion_rule: typing.Optional[Literal["all_assignees", "any_assignee"]] = Field(None, alias='completion_rule')
    class Config:
        arbitrary_types_allowed = True
