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

from box_python_sdk.type.classification_template_fields import ClassificationTemplateFields

class RequiredClassificationTemplate(TypedDict):
    # The ID of the classification template.
    id: str

    # `metadata_template`
    type: str

    # The scope of the classification template. This is in the format `enterprise_{id}` where the `id` is the enterprise ID.
    scope: str

    # `securityClassification-6VMVochwUWo`
    templateKey: str

    # The name of this template as shown in web and mobile interfaces.
    displayName: str

    fields: ClassificationTemplateFields

class OptionalClassificationTemplate(TypedDict, total=False):
    # Determines if the template is always available in web and mobile interfaces.
    hidden: bool

    # Determines if  classifications are copied along when the file or folder is copied.
    copyInstanceOnItemCopy: bool

class ClassificationTemplate(RequiredClassificationTemplate, OptionalClassificationTemplate):
    pass
