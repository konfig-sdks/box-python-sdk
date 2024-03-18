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

from box_python_sdk.type.folders_update_folder_request_collections import FoldersUpdateFolderRequestCollections
from box_python_sdk.type.folders_update_folder_request_parent import FoldersUpdateFolderRequestParent
from box_python_sdk.type.folders_update_folder_request_tags import FoldersUpdateFolderRequestTags

class RequiredFoldersUpdateFolderRequest(TypedDict):
    pass

class OptionalFoldersUpdateFolderRequest(TypedDict, total=False):
    tags: FoldersUpdateFolderRequestTags

    # The optional description of this folder
    description: str

    # The optional new name for this folder.
    name: str

    # Specifies whether a folder should be synced to a user's device or not. This is used by Box Sync (discontinued) and is not used by Box Drive.
    sync_state: str

    # Specifies if users who are not the owner of the folder can invite new collaborators to the folder.
    can_non_owners_invite: bool

    parent: FoldersUpdateFolderRequestParent

    shared_link: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    folder_upload_email: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Specifies if new invites to this folder are restricted to users within the enterprise. This does not affect existing collaborations.
    is_collaboration_restricted_to_enterprise: bool

    collections: FoldersUpdateFolderRequestCollections

    # Restricts collaborators who are not the owner of this folder from viewing other collaborations on this folder.  It also restricts non-owners from inviting new collaborators.  When setting this field to `false`, it is required to also set `can_non_owners_invite_collaborators` to `false` if it has not already been set.
    can_non_owners_view_collaborators: bool

class FoldersUpdateFolderRequest(RequiredFoldersUpdateFolderRequest, OptionalFoldersUpdateFolderRequest):
    pass
