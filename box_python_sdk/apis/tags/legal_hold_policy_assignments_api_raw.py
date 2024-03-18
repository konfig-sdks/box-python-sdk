# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.legal_hold_policy_assignments.post import AssignFileLegalHoldRaw
from box_python_sdk.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id.get import GetAssignmentRaw
from box_python_sdk.paths.legal_hold_policy_assignments.get import GetListItemsRaw
from box_python_sdk.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id_files_on_hold.get import ListFileVersionsRaw
from box_python_sdk.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id_file_versions_on_hold.get import ListPreviousFileVersionsRaw
from box_python_sdk.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id.delete import UnassignPolicyRaw


class LegalHoldPolicyAssignmentsApiRaw(
    AssignFileLegalHoldRaw,
    GetAssignmentRaw,
    GetListItemsRaw,
    ListFileVersionsRaw,
    ListPreviousFileVersionsRaw,
    UnassignPolicyRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass