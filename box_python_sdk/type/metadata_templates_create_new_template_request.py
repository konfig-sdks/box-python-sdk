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

from box_python_sdk.type.metadata_templates_create_new_template_request_fields import MetadataTemplatesCreateNewTemplateRequestFields

class RequiredMetadataTemplatesCreateNewTemplateRequest(TypedDict):
    # The scope of the metadata template to create. Applications can only create templates for use within the authenticated user's enterprise.  This value needs to be set to `enterprise`, as `global` scopes can not be created by applications.
    scope: str

    # The display name of the template.
    displayName: str

class OptionalMetadataTemplatesCreateNewTemplateRequest(TypedDict, total=False):
    # A unique identifier for the template. This identifier needs to be unique across the enterprise for which the metadata template is being created.  When not provided, the API will create a unique `templateKey` based on the value of the `displayName`.
    templateKey: str

    # Defines if this template is visible in the Box web app UI, or if it is purely intended for usage through the API.
    hidden: bool

    fields: MetadataTemplatesCreateNewTemplateRequestFields

    # Whether or not to copy any metadata attached to a file or folder when it is copied. By default, metadata is not copied along with a file or folder when it is copied.
    copyInstanceOnItemCopy: bool

class MetadataTemplatesCreateNewTemplateRequest(RequiredMetadataTemplatesCreateNewTemplateRequest, OptionalMetadataTemplatesCreateNewTemplateRequest):
    pass
