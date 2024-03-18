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

from box_python_sdk.pydantic.metadata_templates_update_schema_request_item_data import MetadataTemplatesUpdateSchemaRequestItemData
from box_python_sdk.pydantic.metadata_templates_update_schema_request_item_enum_option_keys import MetadataTemplatesUpdateSchemaRequestItemEnumOptionKeys
from box_python_sdk.pydantic.metadata_templates_update_schema_request_item_field_keys import MetadataTemplatesUpdateSchemaRequestItemFieldKeys
from box_python_sdk.pydantic.metadata_templates_update_schema_request_item_multi_select_option_keys import MetadataTemplatesUpdateSchemaRequestItemMultiSelectOptionKeys

class MetadataTemplatesUpdateSchemaRequestItem(BaseModel):
    # The type of change to perform on the template. Some of these are hazardous as they will change existing templates.
    op: Literal["editTemplate", "addField", "reorderFields", "addEnumOption", "reorderEnumOptions", "reorderMultiSelectOptions", "addMultiSelectOption", "editField", "removeField", "editEnumOption", "removeEnumOption", "editMultiSelectOption", "removeMultiSelectOption"] = Field(alias='op')

    data: typing.Optional[MetadataTemplatesUpdateSchemaRequestItemData] = Field(None, alias='data')

    # For operations that affect a single field this defines the key of the field that is affected.
    field_key: typing.Optional[str] = Field(None, alias='fieldKey')

    field_keys: typing.Optional[MetadataTemplatesUpdateSchemaRequestItemFieldKeys] = Field(None, alias='fieldKeys')

    # For operations that affect a single `enum` option this defines the key of the option that is affected.
    enum_option_key: typing.Optional[str] = Field(None, alias='enumOptionKey')

    enum_option_keys: typing.Optional[MetadataTemplatesUpdateSchemaRequestItemEnumOptionKeys] = Field(None, alias='enumOptionKeys')

    # For operations that affect a single multi select option this defines the key of the option that is affected.
    multi_select_option_key: typing.Optional[str] = Field(None, alias='multiSelectOptionKey')

    multi_select_option_keys: typing.Optional[MetadataTemplatesUpdateSchemaRequestItemMultiSelectOptionKeys] = Field(None, alias='multiSelectOptionKeys')
    class Config:
        arbitrary_types_allowed = True
