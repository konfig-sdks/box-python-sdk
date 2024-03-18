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


class RequiredTaskAssignmentsAssignMultipleUsersRequestAssignTo(TypedDict):
    pass

class OptionalTaskAssignmentsAssignMultipleUsersRequestAssignTo(TypedDict, total=False):
    # The ID of the user to assign to the task.  To specify a user by their email address use the `login` parameter.
    id: str

    # The email address of the user to assign to the task. To specify a user by their user ID please use the `id` parameter.
    login: str

class TaskAssignmentsAssignMultipleUsersRequestAssignTo(RequiredTaskAssignmentsAssignMultipleUsersRequestAssignTo, OptionalTaskAssignmentsAssignMultipleUsersRequestAssignTo):
    pass
