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

from box_python_sdk.pydantic.metadata_templates_create_new_template_request_fields_item_options import MetadataTemplatesCreateNewTemplateRequestFieldsItemOptions

class MetadataTemplatesCreateNewTemplateRequestFieldsItem(BaseModel):
    # The type of field. The basic fields are a `string` field for text, a `float` field for numbers, and a `date` fields to present the user with a date-time picker.  Additionally, metadata templates support an `enum` field for a basic list of items, and ` multiSelect` field for a similar list of items where the user can select more than one value.
    type: Literal["string", "float", "date", "enum", "multiSelect"] = Field(alias='type')

    # A unique identifier for the field. The identifier must be unique within the template to which it belongs.
    key: str = Field(alias='key')

    # The display name of the field as it is shown to the user in the web and mobile apps.
    display_name: str = Field(alias='displayName')

    # A description of the field. This is not shown to the user.
    description: typing.Optional[str] = Field(None, alias='description')

    # Whether this field is hidden in the UI for the user and can only be set through the API instead.
    hidden: typing.Optional[bool] = Field(None, alias='hidden')

    options: typing.Optional[MetadataTemplatesCreateNewTemplateRequestFieldsItemOptions] = Field(None, alias='options')
    class Config:
        arbitrary_types_allowed = True
