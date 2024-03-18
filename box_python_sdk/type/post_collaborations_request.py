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

from box_python_sdk.type.post_collaborations_request_accessible_by import PostCollaborationsRequestAccessibleBy
from box_python_sdk.type.post_collaborations_request_item import PostCollaborationsRequestItem

class RequiredPostCollaborationsRequest(TypedDict):
    item: PostCollaborationsRequestItem

    accessible_by: PostCollaborationsRequestAccessibleBy

    # The level of access granted.
    role: str

class OptionalPostCollaborationsRequest(TypedDict, total=False):
    # If set to `true`, collaborators have access to shared items, but such items won't be visible in the All Files list. Additionally, collaborators won't see the the path to the root folder for the shared item.
    is_access_only: bool

    # Determines if the invited users can see the entire parent path to the associated folder. The user will not gain privileges in any parent folder and therefore can not see content the user is not collaborated on.  Be aware that this meaningfully increases the time required to load the invitee's **All Files** page. We recommend you limit the number of collaborations with `can_view_path` enabled to 1,000 per user.  Only owner or co-owners can invite collaborators with a `can_view_path` of `true`.  `can_view_path` can only be used for folder collaborations.
    can_view_path: bool

    # Set the expiration date for the collaboration. At this date, the collaboration will be automatically removed from the item.  This feature will only work if the **Automatically remove invited collaborators: Allow folder owners to extend the expiry date** setting has been enabled in the **Enterprise Settings** of the **Admin Console**. When the setting is not enabled, collaborations can not have an expiry date and a value for this field will be result in an error.
    expires_at: datetime

class PostCollaborationsRequest(RequiredPostCollaborationsRequest, OptionalPostCollaborationsRequest):
    pass
