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

from box_python_sdk.type.metadata_templates_update_schema_request_item_data import MetadataTemplatesUpdateSchemaRequestItemData
from box_python_sdk.type.metadata_templates_update_schema_request_item_enum_option_keys import MetadataTemplatesUpdateSchemaRequestItemEnumOptionKeys
from box_python_sdk.type.metadata_templates_update_schema_request_item_field_keys import MetadataTemplatesUpdateSchemaRequestItemFieldKeys
from box_python_sdk.type.metadata_templates_update_schema_request_item_multi_select_option_keys import MetadataTemplatesUpdateSchemaRequestItemMultiSelectOptionKeys

class RequiredMetadataTemplatesUpdateSchemaRequestItem(TypedDict):
    # The type of change to perform on the template. Some of these are hazardous as they will change existing templates.
    op: str

class OptionalMetadataTemplatesUpdateSchemaRequestItem(TypedDict, total=False):
    data: MetadataTemplatesUpdateSchemaRequestItemData

    # For operations that affect a single field this defines the key of the field that is affected.
    fieldKey: str

    fieldKeys: MetadataTemplatesUpdateSchemaRequestItemFieldKeys

    # For operations that affect a single `enum` option this defines the key of the option that is affected.
    enumOptionKey: str

    enumOptionKeys: MetadataTemplatesUpdateSchemaRequestItemEnumOptionKeys

    # For operations that affect a single multi select option this defines the key of the option that is affected.
    multiSelectOptionKey: str

    multiSelectOptionKeys: MetadataTemplatesUpdateSchemaRequestItemMultiSelectOptionKeys

class MetadataTemplatesUpdateSchemaRequestItem(RequiredMetadataTemplatesUpdateSchemaRequestItem, OptionalMetadataTemplatesUpdateSchemaRequestItem):
    pass
