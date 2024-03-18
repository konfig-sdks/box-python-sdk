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
from box_python_sdk.pydantic.user_mini import UserMini

class TaskAssignment(BaseModel):
    # The unique identifier for this task assignment
    id: typing.Optional[str] = Field(None, alias='id')

    # `task_assignment`
    type: typing.Optional[Literal["task_assignment"]] = Field(None, alias='type')

    item: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='item')

    assigned_to: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='assigned_to')

    # A message that will is included with the task assignment. This is visible to the assigned user in the web and mobile UI.
    message: typing.Optional[str] = Field(None, alias='message')

    # The date at which this task assignment was completed. This will be `null` if the task is not completed yet.
    completed_at: typing.Optional[datetime] = Field(None, alias='completed_at')

    # The date at which this task was assigned to the user.
    assigned_at: typing.Optional[datetime] = Field(None, alias='assigned_at')

    # The date at which the assigned user was reminded of this task assignment.
    reminded_at: typing.Optional[datetime] = Field(None, alias='reminded_at')

    # The current state of the assignment. The available states depend on the `action` value of the task object.
    resolution_state: typing.Optional[Literal["completed", "incomplete", "approved", "rejected"]] = Field(None, alias='resolution_state')

    assigned_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='assigned_by')
    class Config:
        arbitrary_types_allowed = True
