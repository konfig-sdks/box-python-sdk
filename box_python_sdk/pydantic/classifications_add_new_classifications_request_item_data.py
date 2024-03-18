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

from box_python_sdk.pydantic.classifications_add_new_classifications_request_item_data_static_config import ClassificationsAddNewClassificationsRequestItemDataStaticConfig

class ClassificationsAddNewClassificationsRequestItemData(BaseModel):
    # The label of the classification as shown in the web and mobile interfaces. This is the only field required to add a classification.
    key: str = Field(alias='key')

    static_config: typing.Optional[ClassificationsAddNewClassificationsRequestItemDataStaticConfig] = Field(None, alias='staticConfig')
    class Config:
        arbitrary_types_allowed = True
