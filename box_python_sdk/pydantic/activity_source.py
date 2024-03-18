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

from box_python_sdk.pydantic.annotation import Annotation
from box_python_sdk.pydantic.app_activity import AppActivity
from box_python_sdk.pydantic.fa_comment_full import FaCommentFull
from box_python_sdk.pydantic.task_full import TaskFull
from box_python_sdk.pydantic.versions_activity import VersionsActivity

class ActivitySource(BaseModel):
    annotation: typing.Optional[Annotation] = Field(None, alias='annotation')

    app_activity: typing.Optional[AppActivity] = Field(None, alias='app_activity')

    comment: typing.Optional[FaCommentFull] = Field(None, alias='comment')

    task: typing.Optional[TaskFull] = Field(None, alias='task')

    versions: typing.Optional[VersionsActivity] = Field(None, alias='versions')
    class Config:
        arbitrary_types_allowed = True
