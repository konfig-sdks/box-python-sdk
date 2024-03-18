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

from box_python_sdk.type.user_mini import UserMini

class RequiredRetentionPoliciesCreatePolicyRequest(TypedDict):
    # The name for the retention policy
    policy_name: str

    # The type of the retention policy. A retention policy type can either be `finite`, where a specific amount of time to retain the content is known upfront, or `indefinite`, where the amount of time to retain the content is still unknown.
    policy_type: str

    # The disposition action of the retention policy. `permanently_delete` deletes the content retained by the policy permanently. `remove_retention` lifts retention policy from the content, allowing it to be deleted by users once the retention policy has expired.
    disposition_action: str

class OptionalRetentionPoliciesCreatePolicyRequest(TypedDict, total=False):
    # The additional text description of the retention policy.
    description: str

    # The length of the retention policy. This value specifies the duration in days that the retention policy will be active for after being assigned to content.  If the policy has a `policy_type` of `indefinite`, the `retention_length` will also be `indefinite`.
    retention_length: typing.Union[typing.Optional[str], typing.Union[int, float]]

    # Specifies the retention type:  * `modifiable`: You can modify the retention policy. For example, you can add or remove folders, shorten or lengthen the policy duration, or delete the assignment. Use this type if your retention policy is not related to any regulatory purposes.  * `non_modifiable`: You can modify the retention policy only in a limited way: add a folder, lengthen the duration, retire the policy, change the disposition action or notification settings. You cannot perform other actions, such as deleting the assignment or shortening the policy duration. Use this type to ensure compliance with regulatory retention policies.
    retention_type: str

    # Whether the owner of a file will be allowed to extend the retention.
    can_owner_extend_retention: bool

    # Whether owner and co-owners of a file are notified when the policy nears expiration.
    are_owners_notified: bool

    # A list of users notified when the retention policy duration is about to end.
    custom_notification_recipients: typing.List[UserMini]

class RetentionPoliciesCreatePolicyRequest(RequiredRetentionPoliciesCreatePolicyRequest, OptionalRetentionPoliciesCreatePolicyRequest):
    pass
