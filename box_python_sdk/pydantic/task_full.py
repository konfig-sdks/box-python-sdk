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
from box_python_sdk.pydantic.task_assignees import TaskAssignees
from box_python_sdk.pydantic.task_base import TaskBase
from box_python_sdk.pydantic.task_links import TaskLinks

TaskFull = typing.Union[TaskBase,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
TaskFull = object
