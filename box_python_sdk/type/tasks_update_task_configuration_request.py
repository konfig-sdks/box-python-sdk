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


class RequiredTasksUpdateTaskConfigurationRequest(TypedDict):
    pass

class OptionalTasksUpdateTaskConfigurationRequest(TypedDict, total=False):
    # The action the task assignee will be prompted to do. Must be  * `review` defines an approval task that can be approved or rejected * `complete` defines a general task which can be completed
    action: str

    # The message included with the task.
    message: str

    # When the task is due at.
    due_at: datetime

    # Defines which assignees need to complete this task before the task is considered completed.  * `all_assignees` (default) requires all assignees to review or approve the the task in order for it to be considered completed. * `any_assignee` accepts any one assignee to review or approve the the task in order for it to be considered completed.
    completion_rule: str

class TasksUpdateTaskConfigurationRequest(RequiredTasksUpdateTaskConfigurationRequest, OptionalTasksUpdateTaskConfigurationRequest):
    pass
