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

from box_python_sdk.pydantic.task_base import TaskBase
from box_python_sdk.pydantic.task_links_entries_item_permissions import TaskLinksEntriesItemPermissions
from box_python_sdk.pydantic.task_links_entries_item_target import TaskLinksEntriesItemTarget

class TaskLinksEntriesItem(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    id: typing.Optional[str] = Field(None, alias='id')

    permissions: typing.Optional[TaskLinksEntriesItemPermissions] = Field(None, alias='permissions')

    target: typing.Optional[TaskLinksEntriesItemTarget] = Field(None, alias='target')

    task: typing.Optional[TaskBase] = Field(None, alias='task')

    type: typing.Optional[Literal["task_link"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
