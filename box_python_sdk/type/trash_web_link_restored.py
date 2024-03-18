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

from box_python_sdk.type.folder_mini import FolderMini
from box_python_sdk.type.user_mini import UserMini

class RequiredTrashWebLinkRestored(TypedDict):
    sequence_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    path_collection: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class OptionalTrashWebLinkRestored(TypedDict, total=False):
    # The description accompanying the web link. This is visible within the Box web application.
    description: str

    # `web_link`
    type: str

    # The unique identifier for this web link
    id: str

    # The entity tag of this web link. Used with `If-Match` headers.
    etag: str

    # The name of the web link
    name: str

    # The URL this web link points to
    url: str

    parent: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # When this file was created on Box’s servers.
    created_at: datetime

    # When this file was last updated on the Box servers.
    modified_at: datetime

    # The time at which this bookmark was put in the trash - becomes `null` after restore.
    trashed_at: typing.Optional[str]

    # The time at which this bookmark will be permanently deleted - becomes `null` after restore.
    purged_at: typing.Optional[str]

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    modified_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    owned_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The shared link for this bookmark. This will be `null` if a bookmark had been trashed, even though the original shared link does become active again.
    shared_link: typing.Optional[str]

    # Whether this item is deleted or not. Values include `active`, `trashed` if the file has been moved to the trash, and `deleted` if the file has been permanently deleted
    item_status: str

class TrashWebLinkRestored(RequiredTrashWebLinkRestored, OptionalTrashWebLinkRestored):
    pass
