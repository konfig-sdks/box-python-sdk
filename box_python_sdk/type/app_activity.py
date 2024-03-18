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

from box_python_sdk.type.app_activity_activity_template import AppActivityActivityTemplate
from box_python_sdk.type.app_group_mini import AppGroupMini
from box_python_sdk.type.app_mini import AppMini
from box_python_sdk.type.file_activity_user import FileActivityUser

class RequiredAppActivity(TypedDict):
    id: str

class OptionalAppActivity(TypedDict, total=False):
    activity_template: AppActivityActivityTemplate

    app: AppMini

    app_group: AppGroupMini

    created_by: FileActivityUser

    # When the `app_activity` object was created.
    occurred_at: datetime

    rendered_text: str

    type: str

class AppActivity(RequiredAppActivity, OptionalAppActivity):
    pass
