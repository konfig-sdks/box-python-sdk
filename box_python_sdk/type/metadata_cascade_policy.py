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

from box_python_sdk.type.metadata_cascade_policy_owner_enterprise import MetadataCascadePolicyOwnerEnterprise
from box_python_sdk.type.metadata_cascade_policy_parent import MetadataCascadePolicyParent

class RequiredMetadataCascadePolicy(TypedDict):
    # The ID of the metadata cascade policy object
    id: str

    # `metadata_cascade_policy`
    type: str

class OptionalMetadataCascadePolicy(TypedDict, total=False):
    owner_enterprise: MetadataCascadePolicyOwnerEnterprise

    parent: MetadataCascadePolicyParent

    # The scope of the metadata cascade policy can either be `global` or `enterprise_*`. The `global` scope is used for policies that are available to any Box enterprise. The `enterprise_*` scope represents policies that have been created within a specific enterprise, where `*` will be the ID of that enterprise.
    scope: str

    # The key of the template that is cascaded down to the folder's children.  In many cases the template key is automatically derived of its display name, for example `Contract Template` would become `contractTemplate`. In some cases the creator of the template will have provided its own template key.  Please [list the templates for an enterprise][list], or get all instances on a [file][file] or [folder][folder] to inspect a template's key.  [list]: e://get-metadata-templates-enterprise [file]: e://get-files-id-metadata [folder]: e://get-folders-id-metadata
    templateKey: str

class MetadataCascadePolicy(RequiredMetadataCascadePolicy, OptionalMetadataCascadePolicy):
    pass
