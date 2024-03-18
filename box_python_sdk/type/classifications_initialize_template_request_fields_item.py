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

from box_python_sdk.type.classifications_initialize_template_request_fields_item_options import ClassificationsInitializeTemplateRequestFieldsItemOptions

class RequiredClassificationsInitializeTemplateRequestFieldsItem(TypedDict):
    # The type of the field that is always enum.
    type: str

    # Defines classifications  available in the enterprise.
    key: str

    # A display name for the classification.
    displayName: str

    options: ClassificationsInitializeTemplateRequestFieldsItemOptions

class OptionalClassificationsInitializeTemplateRequestFieldsItem(TypedDict, total=False):
    # Determines if the classification template is hidden or available on web and mobile devices.
    hidden: bool

class ClassificationsInitializeTemplateRequestFieldsItem(RequiredClassificationsInitializeTemplateRequestFieldsItem, OptionalClassificationsInitializeTemplateRequestFieldsItem):
    pass
