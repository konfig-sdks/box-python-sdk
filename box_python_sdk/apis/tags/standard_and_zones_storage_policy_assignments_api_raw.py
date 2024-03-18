# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.storage_policy_assignments.post import CreateAssignmentRaw
from box_python_sdk.paths.storage_policy_assignments_storage_policy_assignment_id.get import GetSpecificAssignmentRaw
from box_python_sdk.paths.storage_policy_assignments.get import ListAssignmentsRaw
from box_python_sdk.paths.storage_policy_assignments_storage_policy_assignment_id.delete import UnassignStoragePolicyRaw
from box_python_sdk.paths.storage_policy_assignments_storage_policy_assignment_id.put import UpdateSpecificAssignmentRaw


class StandardAndZonesStoragePolicyAssignmentsApiRaw(
    CreateAssignmentRaw,
    GetSpecificAssignmentRaw,
    ListAssignmentsRaw,
    UnassignStoragePolicyRaw,
    UpdateSpecificAssignmentRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
