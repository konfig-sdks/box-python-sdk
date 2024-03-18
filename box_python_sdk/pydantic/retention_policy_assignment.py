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

from box_python_sdk.pydantic.retention_policy_assignment_assigned_to import RetentionPolicyAssignmentAssignedTo
from box_python_sdk.pydantic.retention_policy_assignment_filter_fields import RetentionPolicyAssignmentFilterFields
from box_python_sdk.pydantic.retention_policy_mini import RetentionPolicyMini
from box_python_sdk.pydantic.user_mini import UserMini

class RetentionPolicyAssignment(BaseModel):
    # The unique identifier for a retention policy assignment.
    id: str = Field(alias='id')

    # `retention_policy_assignment`
    type: Literal["retention_policy_assignment"] = Field(alias='type')

    retention_policy: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='retention_policy')

    assigned_to: typing.Optional[RetentionPolicyAssignmentAssignedTo] = Field(None, alias='assigned_to')

    filter_fields: typing.Optional[RetentionPolicyAssignmentFilterFields] = Field(None, alias='filter_fields')

    assigned_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='assigned_by')

    # When the retention policy assignment object was created.
    assigned_at: typing.Optional[datetime] = Field(None, alias='assigned_at')

    # The date the retention policy assignment begins. If the `assigned_to` type is `metadata_template`, this field can be a date field's metadata attribute key id.
    start_date_field: typing.Optional[str] = Field(None, alias='start_date_field')
    class Config:
        arbitrary_types_allowed = True
