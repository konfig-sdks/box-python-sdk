# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.legal_hold_policy_assignments.post import AssignFileLegalHold
from box_python_sdk.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id.get import GetAssignment
from box_python_sdk.paths.legal_hold_policy_assignments.get import GetListItems
from box_python_sdk.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id_files_on_hold.get import ListFileVersions
from box_python_sdk.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id_file_versions_on_hold.get import ListPreviousFileVersions
from box_python_sdk.paths.legal_hold_policy_assignments_legal_hold_policy_assignment_id.delete import UnassignPolicy
from box_python_sdk.apis.tags.legal_hold_policy_assignments_api_raw import LegalHoldPolicyAssignmentsApiRaw


class LegalHoldPolicyAssignmentsApi(
    AssignFileLegalHold,
    GetAssignment,
    GetListItems,
    ListFileVersions,
    ListPreviousFileVersions,
    UnassignPolicy,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LegalHoldPolicyAssignmentsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LegalHoldPolicyAssignmentsApiRaw(api_client)