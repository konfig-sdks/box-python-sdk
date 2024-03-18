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

from box_python_sdk.type.retention_policy_assignments_create_retention_assignment_request_assign_to import RetentionPolicyAssignmentsCreateRetentionAssignmentRequestAssignTo
from box_python_sdk.type.retention_policy_assignments_create_retention_assignment_request_filter_fields import RetentionPolicyAssignmentsCreateRetentionAssignmentRequestFilterFields

class RequiredRetentionPolicyAssignmentsCreateRetentionAssignmentRequest(TypedDict):
    # The ID of the retention policy to assign
    policy_id: str

    assign_to: RetentionPolicyAssignmentsCreateRetentionAssignmentRequestAssignTo

class OptionalRetentionPolicyAssignmentsCreateRetentionAssignmentRequest(TypedDict, total=False):
    filter_fields: RetentionPolicyAssignmentsCreateRetentionAssignmentRequestFilterFields

    # The date the retention policy assignment begins.  If the `assigned_to` type is `metadata_template`, this field can be a date field's metadata attribute key id.
    start_date_field: str

class RetentionPolicyAssignmentsCreateRetentionAssignmentRequest(RequiredRetentionPolicyAssignmentsCreateRetentionAssignmentRequest, OptionalRetentionPolicyAssignmentsCreateRetentionAssignmentRequest):
    pass
