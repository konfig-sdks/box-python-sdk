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

from box_python_sdk.type.classifications_add_new_classifications_request_item_data_static_config_classification import ClassificationsAddNewClassificationsRequestItemDataStaticConfigClassification

class RequiredClassificationsAddNewClassificationsRequestItemDataStaticConfig(TypedDict):
    pass

class OptionalClassificationsAddNewClassificationsRequestItemDataStaticConfig(TypedDict, total=False):
    classification: ClassificationsAddNewClassificationsRequestItemDataStaticConfigClassification

class ClassificationsAddNewClassificationsRequestItemDataStaticConfig(RequiredClassificationsAddNewClassificationsRequestItemDataStaticConfig, OptionalClassificationsAddNewClassificationsRequestItemDataStaticConfig):
    pass
