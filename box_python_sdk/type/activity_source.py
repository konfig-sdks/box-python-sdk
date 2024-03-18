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

from box_python_sdk.type.annotation import Annotation
from box_python_sdk.type.app_activity import AppActivity
from box_python_sdk.type.fa_comment_full import FaCommentFull
from box_python_sdk.type.task_full import TaskFull
from box_python_sdk.type.versions_activity import VersionsActivity

class RequiredActivitySource(TypedDict):
    pass

class OptionalActivitySource(TypedDict, total=False):
    annotation: Annotation

    app_activity: AppActivity

    comment: FaCommentFull

    task: TaskFull

    versions: VersionsActivity

class ActivitySource(RequiredActivitySource, OptionalActivitySource):
    pass
