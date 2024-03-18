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


class RequiredMetadataCascadePoliciesCreatePolicyRequest(TypedDict):
    # The ID of the folder to apply the policy to. This folder will need to already have an instance of the targeted metadata template applied to it.
    folder_id: str

    # The scope of the targeted metadata template. This template will need to already have an instance applied to the targeted folder.
    scope: str

    # The key of the targeted metadata template. This template will need to already have an instance applied to the targeted folder.  In many cases the template key is automatically derived of its display name, for example `Contract Template` would become `contractTemplate`. In some cases the creator of the template will have provided its own template key.  Please [list the templates for an enterprise][list], or get all instances on a [file][file] or [folder][folder] to inspect a template's key.  [list]: e://get-metadata-templates-enterprise [file]: e://get-files-id-metadata [folder]: e://get-folders-id-metadata
    templateKey: str

class OptionalMetadataCascadePoliciesCreatePolicyRequest(TypedDict, total=False):
    pass

class MetadataCascadePoliciesCreatePolicyRequest(RequiredMetadataCascadePoliciesCreatePolicyRequest, OptionalMetadataCascadePoliciesCreatePolicyRequest):
    pass
