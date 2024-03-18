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

from box_python_sdk.type.annotation_base import AnnotationBase
from box_python_sdk.type.annotation_target import AnnotationTarget
from box_python_sdk.type.file_activity_user import FileActivityUser
from box_python_sdk.type.reply import Reply

Annotation = typing.Union[AnnotationBase,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
Annotation = object
