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
from pydantic import BaseModel, Field, RootModel

from box_python_sdk.pydantic.retention_policy_assignments_create_retention_assignment_request_assign_to import RetentionPolicyAssignmentsCreateRetentionAssignmentRequestAssignTo
from box_python_sdk.pydantic.retention_policy_assignments_create_retention_assignment_request_filter_fields import RetentionPolicyAssignmentsCreateRetentionAssignmentRequestFilterFields

class RetentionPolicyAssignmentsCreateRetentionAssignmentRequest(BaseModel):
    # The ID of the retention policy to assign
    policy_id: str = Field(alias='policy_id')

    assign_to: RetentionPolicyAssignmentsCreateRetentionAssignmentRequestAssignTo = Field(alias='assign_to')

    filter_fields: typing.Optional[RetentionPolicyAssignmentsCreateRetentionAssignmentRequestFilterFields] = Field(None, alias='filter_fields')

    # The date the retention policy assignment begins.  If the `assigned_to` type is `metadata_template`, this field can be a date field's metadata attribute key id.
    start_date_field: typing.Optional[str] = Field(None, alias='start_date_field')
    class Config:
        arbitrary_types_allowed = True
