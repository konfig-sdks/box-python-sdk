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

from box_python_sdk.pydantic.folders_update_folder_request_collections import FoldersUpdateFolderRequestCollections
from box_python_sdk.pydantic.folders_update_folder_request_parent import FoldersUpdateFolderRequestParent
from box_python_sdk.pydantic.folders_update_folder_request_tags import FoldersUpdateFolderRequestTags

class FoldersUpdateFolderRequest(BaseModel):
    tags: typing.Optional[FoldersUpdateFolderRequestTags] = Field(None, alias='tags')

    # The optional description of this folder
    description: typing.Optional[str] = Field(None, alias='description')

    # The optional new name for this folder.
    name: typing.Optional[str] = Field(None, alias='name')

    # Specifies whether a folder should be synced to a user's device or not. This is used by Box Sync (discontinued) and is not used by Box Drive.
    sync_state: typing.Optional[Literal["synced", "not_synced", "partially_synced"]] = Field(None, alias='sync_state')

    # Specifies if users who are not the owner of the folder can invite new collaborators to the folder.
    can_non_owners_invite: typing.Optional[bool] = Field(None, alias='can_non_owners_invite')

    parent: typing.Optional[FoldersUpdateFolderRequestParent] = Field(None, alias='parent')

    shared_link: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='shared_link')

    folder_upload_email: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='folder_upload_email')

    # Specifies if new invites to this folder are restricted to users within the enterprise. This does not affect existing collaborations.
    is_collaboration_restricted_to_enterprise: typing.Optional[bool] = Field(None, alias='is_collaboration_restricted_to_enterprise')

    collections: typing.Optional[FoldersUpdateFolderRequestCollections] = Field(None, alias='collections')

    # Restricts collaborators who are not the owner of this folder from viewing other collaborations on this folder.  It also restricts non-owners from inviting new collaborators.  When setting this field to `false`, it is required to also set `can_non_owners_invite_collaborators` to `false` if it has not already been set.
    can_non_owners_view_collaborators: typing.Optional[bool] = Field(None, alias='can_non_owners_view_collaborators')
    class Config:
        arbitrary_types_allowed = True
