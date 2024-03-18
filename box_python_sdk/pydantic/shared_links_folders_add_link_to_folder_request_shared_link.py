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

from box_python_sdk.pydantic.shared_links_folders_add_link_to_folder_request_shared_link_permissions import SharedLinksFoldersAddLinkToFolderRequestSharedLinkPermissions

class SharedLinksFoldersAddLinkToFolderRequestSharedLink(BaseModel):
    # The level of access for the shared link. This can be restricted to anyone with the link (`open`), only people within the company (`company`) and only those who have been invited to the folder (`collaborators`).  If not set, this field defaults to the access level specified by the enterprise admin. To create a shared link with this default setting pass the `shared_link` object with no `access` field, for example `{ \"shared_link\": {} }`.  The `company` access level is only available to paid accounts.
    access: typing.Optional[Literal["open", "company", "collaborators"]] = Field(None, alias='access')

    # The password required to access the shared link. Set the password to `null` to remove it. Passwords must now be at least eight characters long and include a number, upper case letter, or a non-numeric or non-alphabetic character. A password can only be set when `access` is set to `open`.
    password: typing.Optional[str] = Field(None, alias='password')

    # Defines a custom vanity name to use in the shared link URL, for example `https://app.box.com/v/my-shared-link`.  Custom URLs should not be used when sharing sensitive content as vanity URLs are a lot easier to guess than regular shared links.
    vanity_name: typing.Optional[str] = Field(None, alias='vanity_name')

    # The timestamp at which this shared link will expire. This field can only be set by users with paid accounts. The value must be greater than the current date and time.
    unshared_at: typing.Optional[datetime] = Field(None, alias='unshared_at')

    permissions: typing.Optional[SharedLinksFoldersAddLinkToFolderRequestSharedLinkPermissions] = Field(None, alias='permissions')
    class Config:
        arbitrary_types_allowed = True
