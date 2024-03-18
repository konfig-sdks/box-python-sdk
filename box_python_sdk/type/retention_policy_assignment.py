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

from box_python_sdk.type.retention_policy_assignment_assigned_to import RetentionPolicyAssignmentAssignedTo
from box_python_sdk.type.retention_policy_assignment_filter_fields import RetentionPolicyAssignmentFilterFields
from box_python_sdk.type.retention_policy_mini import RetentionPolicyMini
from box_python_sdk.type.user_mini import UserMini

class RequiredRetentionPolicyAssignment(TypedDict):
    # The unique identifier for a retention policy assignment.
    id: str

    # `retention_policy_assignment`
    type: str

class OptionalRetentionPolicyAssignment(TypedDict, total=False):
    retention_policy: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    assigned_to: RetentionPolicyAssignmentAssignedTo

    filter_fields: RetentionPolicyAssignmentFilterFields

    assigned_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # When the retention policy assignment object was created.
    assigned_at: datetime

    # The date the retention policy assignment begins. If the `assigned_to` type is `metadata_template`, this field can be a date field's metadata attribute key id.
    start_date_field: str

class RetentionPolicyAssignment(RequiredRetentionPolicyAssignment, OptionalRetentionPolicyAssignment):
    pass
