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

from box_python_sdk.pydantic.classification_template_fields_item_options import ClassificationTemplateFieldsItemOptions

class ClassificationTemplateFieldsItem(BaseModel):
    # The unique ID of the field.
    id: str = Field(alias='id')

    # The array item type.
    type: Literal["enum"] = Field(alias='type')

    # Defines classifications  available in the enterprise.
    key: Literal["Box__Security__Classification__Key"] = Field(alias='key')

    # `Classification`
    display_name: Literal["Classification"] = Field(alias='displayName')

    options: ClassificationTemplateFieldsItemOptions = Field(alias='options')

    # Classifications are always visible to web and mobile users.
    hidden: typing.Optional[bool] = Field(None, alias='hidden')
    class Config:
        arbitrary_types_allowed = True
