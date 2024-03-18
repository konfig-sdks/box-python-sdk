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

from box_python_sdk.type.metadata_field_filter_date_range import MetadataFieldFilterDateRange
from box_python_sdk.type.metadata_field_filter_float import MetadataFieldFilterFloat
from box_python_sdk.type.metadata_field_filter_float_range import MetadataFieldFilterFloatRange
from box_python_sdk.type.metadata_field_filter_multi_select import MetadataFieldFilterMultiSelect
from box_python_sdk.type.metadata_field_filter_string import MetadataFieldFilterString

class RequiredMetadataFilter(TypedDict):
    pass

class OptionalMetadataFilter(TypedDict, total=False):
    # Specifies the scope of the template to filter search results by.  This will be `enterprise_{enterprise_id}` for templates defined for use in this enterprise, and `global` for general templates that are available to all enterprises using Box.
    scope: str

    # The key of the template to filter search results by.  In many cases the template key is automatically derived of its display name, for example `Contract Template` would become `contractTemplate`. In some cases the creator of the template will have provided its own template key.  Please [list the templates for an enterprise][list], or get all instances on a [file][file] or [folder][folder] to inspect a template's key.  [list]: e://get-metadata-templates-enterprise [file]: e://get-files-id-metadata [folder]: e://get-folders-id-metadata
    templateKey: str

    filters: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class MetadataFilter(RequiredMetadataFilter, OptionalMetadataFilter):
    pass
