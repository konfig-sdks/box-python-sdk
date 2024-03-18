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


class RequiredTaskAssignmentsUpdateStateAssignedToUserRequest(TypedDict):
    pass

class OptionalTaskAssignmentsUpdateStateAssignedToUserRequest(TypedDict, total=False):
    # An optional message by the assignee that can be added to the task.
    message: str

    # The state of the task assigned to the user.  * For a task with an `action` value of `complete` this can be `incomplete` or `completed`. * For a task with an `action` of `review` this can be `incomplete`, `approved`, or `rejected`.
    resolution_state: str

class TaskAssignmentsUpdateStateAssignedToUserRequest(RequiredTaskAssignmentsUpdateStateAssignedToUserRequest, OptionalTaskAssignmentsUpdateStateAssignedToUserRequest):
    pass
