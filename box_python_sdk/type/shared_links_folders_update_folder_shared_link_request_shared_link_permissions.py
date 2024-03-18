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


class RequiredSharedLinksFoldersUpdateFolderSharedLinkRequestSharedLinkPermissions(TypedDict):
    pass

class OptionalSharedLinksFoldersUpdateFolderSharedLinkRequestSharedLinkPermissions(TypedDict, total=False):
    # If the shared link allows for downloading of files. This can only be set when `access` is set to `open` or `company`.
    can_download: bool

    # If the shared link allows for previewing of files. This value is always `true`. For shared links on folders this also applies to any items in the folder.
    can_preview: bool

    # This value can only be `false` for items with a `type` of `folder`.
    can_edit: bool

class SharedLinksFoldersUpdateFolderSharedLinkRequestSharedLinkPermissions(RequiredSharedLinksFoldersUpdateFolderSharedLinkRequestSharedLinkPermissions, OptionalSharedLinksFoldersUpdateFolderSharedLinkRequestSharedLinkPermissions):
    pass
