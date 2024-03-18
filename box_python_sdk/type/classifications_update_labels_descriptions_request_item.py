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

from box_python_sdk.type.classifications_update_labels_descriptions_request_item_data import ClassificationsUpdateLabelsDescriptionsRequestItemData

class RequiredClassificationsUpdateLabelsDescriptionsRequestItem(TypedDict):
    # The type of change to perform on the classification object.
    op: str

    # Defines classifications  available in the enterprise.
    fieldKey: str

    # The original label of the classification to change.
    enumOptionKey: str

    data: ClassificationsUpdateLabelsDescriptionsRequestItemData

class OptionalClassificationsUpdateLabelsDescriptionsRequestItem(TypedDict, total=False):
    pass

class ClassificationsUpdateLabelsDescriptionsRequestItem(RequiredClassificationsUpdateLabelsDescriptionsRequestItem, OptionalClassificationsUpdateLabelsDescriptionsRequestItem):
    pass
