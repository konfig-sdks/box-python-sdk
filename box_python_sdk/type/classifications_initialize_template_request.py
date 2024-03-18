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

from box_python_sdk.type.classifications_initialize_template_request_fields import ClassificationsInitializeTemplateRequestFields

class RequiredClassificationsInitializeTemplateRequest(TypedDict):
    # The scope in which to create the classifications. This should be `enterprise` or `enterprise_{id}` where `id` is the unique ID of the enterprise.
    scope: str

    # Defines the list of metadata templates.
    templateKey: str

    # The name of the template as shown in web and mobile interfaces.
    displayName: str

    fields: ClassificationsInitializeTemplateRequestFields

class OptionalClassificationsInitializeTemplateRequest(TypedDict, total=False):
    # Determines if the classification template is hidden or available on web and mobile devices.
    hidden: bool

    # Determines if classifications are copied along when the file or folder is copied.
    copyInstanceOnItemCopy: bool

class ClassificationsInitializeTemplateRequest(RequiredClassificationsInitializeTemplateRequest, OptionalClassificationsInitializeTemplateRequest):
    pass
