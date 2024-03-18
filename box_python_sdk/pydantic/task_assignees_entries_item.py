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

from box_python_sdk.pydantic.file_activity_user import FileActivityUser
from box_python_sdk.pydantic.task_assignees_entries_item_permissions import TaskAssigneesEntriesItemPermissions

class TaskAssigneesEntriesItem(BaseModel):
    # When the task assigned was completed.
    completed_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='completed_at')

    id: typing.Optional[str] = Field(None, alias='id')

    # When the task assigned was modified.
    modified_at: typing.Optional[datetime] = Field(None, alias='modified_at')

    permissions: typing.Optional[TaskAssigneesEntriesItemPermissions] = Field(None, alias='permissions')

    role: typing.Optional[Literal["assignee", "creator"]] = Field(None, alias='role')

    status: typing.Optional[Literal["approved", "completed", "not_started", "rejected"]] = Field(None, alias='status')

    target: typing.Optional[FileActivityUser] = Field(None, alias='target')

    type: typing.Optional[Literal["task_collaborator"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
