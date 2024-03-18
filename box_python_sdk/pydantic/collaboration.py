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

from box_python_sdk.pydantic.collaboration_acceptance_requirements_status import CollaborationAcceptanceRequirementsStatus
from box_python_sdk.pydantic.file import File
from box_python_sdk.pydantic.folder import Folder
from box_python_sdk.pydantic.group_mini import GroupMini
from box_python_sdk.pydantic.user_collaborations import UserCollaborations
from box_python_sdk.pydantic.web_link import WebLink

class Collaboration(BaseModel):
    # The unique identifier for this collaboration.
    id: str = Field(alias='id')

    # `collaboration`
    type: Literal["collaboration"] = Field(alias='type')

    item: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='item')

    accessible_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='accessible_by')

    # The email address used to invite an unregistered collaborator, if they are not a registered user.
    invite_email: typing.Optional[typing.Optional[str]] = Field(None, alias='invite_email')

    # The level of access granted.
    role: typing.Optional[Literal["editor", "viewer", "previewer", "uploader", "previewer uploader", "viewer uploader", "co-owner", "owner"]] = Field(None, alias='role')

    # When the collaboration will expire, or `null` if no expiration date is set.
    expires_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='expires_at')

    # If set to `true`, collaborators have access to shared items, but such items won't be visible in the All Files list. Additionally, collaborators won't see the the path to the root folder for the shared item.
    is_access_only: typing.Optional[bool] = Field(None, alias='is_access_only')

    # The status of the collaboration invitation. If the status is `pending`, `login` and `name` return an empty string.
    status: typing.Optional[Literal["accepted", "pending", "rejected"]] = Field(None, alias='status')

    # When the `status` of the collaboration object changed to `accepted` or `rejected`.
    acknowledged_at: typing.Optional[datetime] = Field(None, alias='acknowledged_at')

    created_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='created_by')

    # When the collaboration object was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # When the collaboration object was last modified.
    modified_at: typing.Optional[datetime] = Field(None, alias='modified_at')

    acceptance_requirements_status: typing.Optional[CollaborationAcceptanceRequirementsStatus] = Field(None, alias='acceptance_requirements_status')
    class Config:
        arbitrary_types_allowed = True
