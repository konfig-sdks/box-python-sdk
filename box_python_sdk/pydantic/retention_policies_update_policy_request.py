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

from box_python_sdk.pydantic.user_base import UserBase

class RetentionPoliciesUpdatePolicyRequest(BaseModel):
    # The additional text description of the retention policy.
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    # The name for the retention policy
    policy_name: typing.Optional[typing.Optional[str]] = Field(None, alias='policy_name')

    # The disposition action of the retention policy. This action can be `permanently_delete`, which will cause the content retained by the policy to be permanently deleted, or `remove_retention`, which will lift the retention policy from the content, allowing it to be deleted by users, once the retention policy has expired. You can use \"null\" if you don't want to change `disposition_action`.
    disposition_action: typing.Optional[typing.Union[str, typing.Optional[str]]] = Field(None, alias='disposition_action')

    # Specifies the retention type:  * `modifiable`: You can modify the retention policy. For example, you can add or remove folders, shorten or lengthen the policy duration, or delete the assignment. Use this type if your retention policy is not related to any regulatory purposes. * `non-modifiable`: You can modify the retention policy only in a limited way: add a folder, lengthen the duration, retire the policy, change the disposition action or notification settings. You cannot perform other actions, such as deleting the assignment or shortening the policy duration. Use this type to ensure compliance with regulatory retention policies.  When updating a retention policy, you can use `non-modifiable` type only. You can convert a `modifiable` policy to `non-modifiable`, but not the other way around.
    retention_type: typing.Optional[typing.Optional[str]] = Field(None, alias='retention_type')

    # The length of the retention policy. This value specifies the duration in days that the retention policy will be active for after being assigned to content.  If the policy has a `policy_type` of `indefinite`, the `retention_length` will also be `indefinite`.
    retention_length: typing.Optional[typing.Union[typing.Optional[str], typing.Union[int, float]]] = Field(None, alias='retention_length')

    # Used to retire a retention policy.  If not retiring a policy, do not include this parameter or set it to `null`.
    status: typing.Optional[typing.Optional[str]] = Field(None, alias='status')

    # Determines if the owner of items under the policy can extend the retention when the original retention duration is about to end.
    can_owner_extend_retention: typing.Optional[typing.Optional[bool]] = Field(None, alias='can_owner_extend_retention')

    # Determines if owners and co-owners of items under the policy are notified when the retention duration is about to end.
    are_owners_notified: typing.Optional[typing.Optional[bool]] = Field(None, alias='are_owners_notified')

    # A list of users notified when the retention duration is about to end.
    custom_notification_recipients: typing.Optional[typing.Optional[typing.List[UserBase]]] = Field(None, alias='custom_notification_recipients')
    class Config:
        arbitrary_types_allowed = True
