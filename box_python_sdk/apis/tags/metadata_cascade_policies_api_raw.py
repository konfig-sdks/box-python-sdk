# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.metadata_cascade_policies_metadata_cascade_policy_id_apply.post import ApplyToChildrenRaw
from box_python_sdk.paths.metadata_cascade_policies.post import CreatePolicyRaw
from box_python_sdk.paths.metadata_cascade_policies_metadata_cascade_policy_id.get import GetPolicyAssignedToFolderRaw
from box_python_sdk.paths.metadata_cascade_policies.get import ListRaw
from box_python_sdk.paths.metadata_cascade_policies_metadata_cascade_policy_id.delete import RemovePolicyRaw


class MetadataCascadePoliciesApiRaw(
    ApplyToChildrenRaw,
    CreatePolicyRaw,
    GetPolicyAssignedToFolderRaw,
    ListRaw,
    RemovePolicyRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
