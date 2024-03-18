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


class RequiredLegalHoldPoliciesCreateNewPolicyRequest(TypedDict):
    # The name of the policy.
    policy_name: str

class OptionalLegalHoldPoliciesCreateNewPolicyRequest(TypedDict, total=False):
    # A description for the policy.
    description: str

    # The filter start date.  When this policy is applied using a `custodian` legal hold assignments, it will only apply to file versions created or uploaded inside of the date range. Other assignment types, such as folders and files, will ignore the date filter.  Required if `is_ongoing` is set to `false`.
    filter_started_at: datetime

    # The filter end date.  When this policy is applied using a `custodian` legal hold assignments, it will only apply to file versions created or uploaded inside of the date range. Other assignment types, such as folders and files, will ignore the date filter.  Required if `is_ongoing` is set to `false`.
    filter_ended_at: datetime

    # Whether new assignments under this policy should continue applying to files even after initialization.  When this policy is applied using a legal hold assignment, it will continue applying the policy to any new file versions even after it has been applied.  For example, if a legal hold assignment is placed on a user today, and that user uploads a file tomorrow, that file will get held. This will continue until the policy is retired.  Required if no filter dates are set.
    is_ongoing: bool

class LegalHoldPoliciesCreateNewPolicyRequest(RequiredLegalHoldPoliciesCreateNewPolicyRequest, OptionalLegalHoldPoliciesCreateNewPolicyRequest):
    pass
