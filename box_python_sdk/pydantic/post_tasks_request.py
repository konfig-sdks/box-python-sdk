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

from box_python_sdk.pydantic.post_tasks_request_item import PostTasksRequestItem

class PostTasksRequest(BaseModel):
    item: PostTasksRequestItem = Field(alias='item')

    # The action the task assignee will be prompted to do. Must be  * `review` defines an approval task that can be approved or rejected * `complete` defines a general task which can be completed
    action: typing.Optional[Literal["review", "complete"]] = Field(None, alias='action')

    # An optional message to include with the task.
    message: typing.Optional[str] = Field(None, alias='message')

    # Defines when the task is due. Defaults to `null` if not provided.
    due_at: typing.Optional[datetime] = Field(None, alias='due_at')

    # Defines which assignees need to complete this task before the task is considered completed.  * `all_assignees` (default) requires all assignees to review or approve the the task in order for it to be considered completed. * `any_assignee` accepts any one assignee to review or approve the the task in order for it to be considered completed.
    completion_rule: typing.Optional[Literal["all_assignees", "any_assignee"]] = Field(None, alias='completion_rule')
    class Config:
        arbitrary_types_allowed = True
