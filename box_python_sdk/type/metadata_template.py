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

from box_python_sdk.type.metadata_template_fields import MetadataTemplateFields

class RequiredMetadataTemplate(TypedDict):
    # The ID of the metadata template.
    id: str

    # `metadata_template`
    type: str

class OptionalMetadataTemplate(TypedDict, total=False):
    # The scope of the metadata template can either be `global` or `enterprise_*`. The `global` scope is used for templates that are available to any Box enterprise. The `enterprise_*` scope represents templates that have been created within a specific enterprise, where `*` will be the ID of that enterprise.
    scope: str

    # A unique identifier for the template. This identifier is unique across the `scope` of the enterprise to which the metadata template is being applied, yet is not necessarily unique across different enterprises.
    templateKey: str

    # The display name of the template. This can be seen in the Box web app and mobile apps.
    displayName: str

    # Defines if this template is visible in the Box web app UI, or if it is purely intended for usage through the API.
    hidden: bool

    fields: MetadataTemplateFields

    # Whether or not to include the metadata when a file or folder is copied.
    copyInstanceOnItemCopy: bool

class MetadataTemplate(RequiredMetadataTemplate, OptionalMetadataTemplate):
    pass
