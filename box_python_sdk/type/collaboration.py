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

from box_python_sdk.type.collaboration_acceptance_requirements_status import CollaborationAcceptanceRequirementsStatus
from box_python_sdk.type.file import File
from box_python_sdk.type.folder import Folder
from box_python_sdk.type.group_mini import GroupMini
from box_python_sdk.type.user_collaborations import UserCollaborations
from box_python_sdk.type.web_link import WebLink

class RequiredCollaboration(TypedDict):
    # The unique identifier for this collaboration.
    id: str

    # `collaboration`
    type: str

class OptionalCollaboration(TypedDict, total=False):
    item: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    accessible_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The email address used to invite an unregistered collaborator, if they are not a registered user.
    invite_email: typing.Optional[str]

    # The level of access granted.
    role: str

    # When the collaboration will expire, or `null` if no expiration date is set.
    expires_at: typing.Optional[datetime]

    # If set to `true`, collaborators have access to shared items, but such items won't be visible in the All Files list. Additionally, collaborators won't see the the path to the root folder for the shared item.
    is_access_only: bool

    # The status of the collaboration invitation. If the status is `pending`, `login` and `name` return an empty string.
    status: str

    # When the `status` of the collaboration object changed to `accepted` or `rejected`.
    acknowledged_at: datetime

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # When the collaboration object was created.
    created_at: datetime

    # When the collaboration object was last modified.
    modified_at: datetime

    acceptance_requirements_status: CollaborationAcceptanceRequirementsStatus

class Collaboration(RequiredCollaboration, OptionalCollaboration):
    pass
