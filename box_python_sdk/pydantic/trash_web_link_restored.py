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

from box_python_sdk.pydantic.folder_mini import FolderMini
from box_python_sdk.pydantic.user_mini import UserMini

class TrashWebLinkRestored(BaseModel):
    sequence_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='sequence_id')

    path_collection: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='path_collection')

    # The description accompanying the web link. This is visible within the Box web application.
    description: typing.Optional[str] = Field(None, alias='description')

    # `web_link`
    type: typing.Optional[Literal["web_link"]] = Field(None, alias='type')

    # The unique identifier for this web link
    id: typing.Optional[str] = Field(None, alias='id')

    # The entity tag of this web link. Used with `If-Match` headers.
    etag: typing.Optional[str] = Field(None, alias='etag')

    # The name of the web link
    name: typing.Optional[str] = Field(None, alias='name')

    # The URL this web link points to
    url: typing.Optional[str] = Field(None, alias='url')

    parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='parent')

    # When this file was created on Box’s servers.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # When this file was last updated on the Box servers.
    modified_at: typing.Optional[datetime] = Field(None, alias='modified_at')

    # The time at which this bookmark was put in the trash - becomes `null` after restore.
    trashed_at: typing.Optional[typing.Optional[str]] = Field(None, alias='trashed_at')

    # The time at which this bookmark will be permanently deleted - becomes `null` after restore.
    purged_at: typing.Optional[typing.Optional[str]] = Field(None, alias='purged_at')

    created_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='created_by')

    modified_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='modified_by')

    owned_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='owned_by')

    # The shared link for this bookmark. This will be `null` if a bookmark had been trashed, even though the original shared link does become active again.
    shared_link: typing.Optional[typing.Optional[str]] = Field(None, alias='shared_link')

    # Whether this item is deleted or not. Values include `active`, `trashed` if the file has been moved to the trash, and `deleted` if the file has been permanently deleted
    item_status: typing.Optional[Literal["active", "trashed", "deleted"]] = Field(None, alias='item_status')
    class Config:
        arbitrary_types_allowed = True
