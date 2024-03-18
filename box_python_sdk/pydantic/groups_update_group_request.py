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


class GroupsUpdateGroupRequest(BaseModel):
    # A human readable description of the group.
    description: typing.Optional[str] = Field(None, alias='description')

    # The name of the new group to be created. Must be unique within the enterprise.
    name: typing.Optional[str] = Field(None, alias='name')

    # Keeps track of which external source this group is coming, for example `Active Directory`, or `Okta`.  Setting this will also prevent Box admins from editing the group name and its members directly via the Box web application.  This is desirable for one-way syncing of groups.
    provenance: typing.Optional[str] = Field(None, alias='provenance')

    # An arbitrary identifier that can be used by external group sync tools to link this Box Group to an external group.  Example values of this field could be an **Active Directory Object ID** or a **Google Group ID**.  We recommend you use of this field in order to avoid issues when group names are updated in either Box or external systems.
    external_sync_identifier: typing.Optional[str] = Field(None, alias='external_sync_identifier')

    # Specifies who can invite the group to collaborate on folders.  When set to `admins_only` the enterprise admin, co-admins, and the group's admin can invite the group.  When set to `admins_and_members` all the admins listed above and group members can invite the group.  When set to `all_managed_users` all managed users in the enterprise can invite the group.
    invitability_level: typing.Optional[Literal["admins_only", "admins_and_members", "all_managed_users"]] = Field(None, alias='invitability_level')

    # Specifies who can see the members of the group.  * `admins_only` - the enterprise admin, co-admins, group's   group admin * `admins_and_members` - all admins and group members * `all_managed_users` - all managed users in the   enterprise
    member_viewability_level: typing.Optional[Literal["admins_only", "admins_and_members", "all_managed_users"]] = Field(None, alias='member_viewability_level')
    class Config:
        arbitrary_types_allowed = True
