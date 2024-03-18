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

from box_python_sdk.type.invite_invited_to import InviteInvitedTo
from box_python_sdk.type.user_mini import UserMini

class RequiredInvite(TypedDict):
    # The unique identifier for this invite
    id: str

    # `invite`
    type: str

class OptionalInvite(TypedDict, total=False):
    invited_to: InviteInvitedTo

    actionable_by: UserMini

    invited_by: UserMini

    # The status of the invite
    status: str

    # When the invite was created
    created_at: datetime

    # When the invite was modified.
    modified_at: datetime

class Invite(RequiredInvite, OptionalInvite):
    pass
