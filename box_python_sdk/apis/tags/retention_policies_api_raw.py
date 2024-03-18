# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.retention_policies.post import CreatePolicyRaw
from box_python_sdk.paths.retention_policies_retention_policy_id.delete import DeletePolicyRaw
from box_python_sdk.paths.retention_policies_retention_policy_id.get import GetPolicyRaw
from box_python_sdk.paths.retention_policies.get import ListAllRaw
from box_python_sdk.paths.retention_policies_retention_policy_id.put import UpdatePolicyRaw


class RetentionPoliciesApiRaw(
    CreatePolicyRaw,
    DeletePolicyRaw,
    GetPolicyRaw,
    ListAllRaw,
    UpdatePolicyRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
