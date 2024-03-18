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

from box_python_sdk.pydantic.group_memberships_update_membership_request_configurable_permissions import GroupMembershipsUpdateMembershipRequestConfigurablePermissions

class GroupMembershipsUpdateMembershipRequest(BaseModel):
    # The role of the user in the group.
    role: typing.Optional[Literal["member", "admin"]] = Field(None, alias='role')

    configurable_permissions: typing.Optional[GroupMembershipsUpdateMembershipRequestConfigurablePermissions] = Field(None, alias='configurable_permissions')
    class Config:
        arbitrary_types_allowed = True
