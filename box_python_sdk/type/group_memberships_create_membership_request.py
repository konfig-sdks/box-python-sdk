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

from box_python_sdk.type.group_memberships_create_membership_request_configurable_permissions import GroupMembershipsCreateMembershipRequestConfigurablePermissions
from box_python_sdk.type.group_memberships_create_membership_request_group import GroupMembershipsCreateMembershipRequestGroup
from box_python_sdk.type.group_memberships_create_membership_request_user import GroupMembershipsCreateMembershipRequestUser

class RequiredGroupMembershipsCreateMembershipRequest(TypedDict):
    user: GroupMembershipsCreateMembershipRequestUser

    group: GroupMembershipsCreateMembershipRequestGroup

class OptionalGroupMembershipsCreateMembershipRequest(TypedDict, total=False):
    # The role of the user in the group.
    role: str

    configurable_permissions: GroupMembershipsCreateMembershipRequestConfigurablePermissions

class GroupMembershipsCreateMembershipRequest(RequiredGroupMembershipsCreateMembershipRequest, OptionalGroupMembershipsCreateMembershipRequest):
    pass
