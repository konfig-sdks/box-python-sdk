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

from box_python_sdk.type.uploads_small_file_request_attributes_parent import UploadsSmallFileRequestAttributesParent

class RequiredUploadsSmallFileRequestAttributes(TypedDict):
    # The name of the file
    name: str

    parent: UploadsSmallFileRequestAttributesParent

class OptionalUploadsSmallFileRequestAttributes(TypedDict, total=False):
    # Defines the time the file was originally created at.  If not set, the upload time will be used.
    content_created_at: datetime

    # Defines the time the file was last modified at.  If not set, the upload time will be used.
    content_modified_at: datetime

class UploadsSmallFileRequestAttributes(RequiredUploadsSmallFileRequestAttributes, OptionalUploadsSmallFileRequestAttributes):
    pass
