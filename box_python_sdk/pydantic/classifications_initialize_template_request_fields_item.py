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

from box_python_sdk.pydantic.classifications_initialize_template_request_fields_item_options import ClassificationsInitializeTemplateRequestFieldsItemOptions

class ClassificationsInitializeTemplateRequestFieldsItem(BaseModel):
    # The type of the field that is always enum.
    type: Literal["enum"] = Field(alias='type')

    # Defines classifications  available in the enterprise.
    key: Literal["Box__Security__Classification__Key"] = Field(alias='key')

    # A display name for the classification.
    display_name: Literal["Classification"] = Field(alias='displayName')

    options: ClassificationsInitializeTemplateRequestFieldsItemOptions = Field(alias='options')

    # Determines if the classification template is hidden or available on web and mobile devices.
    hidden: typing.Optional[bool] = Field(None, alias='hidden')
    class Config:
        arbitrary_types_allowed = True
