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


class RequiredFolderBase(TypedDict):
    # The unique identifier that represent a folder.  The ID for any folder can be determined by visiting a folder in the web application and copying the ID from the URL. For example, for the URL `https://*.app.box.com/folders/123` the `folder_id` is `123`.
    id: str

    # `folder`
    type: str

class OptionalFolderBase(TypedDict, total=False):
    # The HTTP `etag` of this folder. This can be used within some API endpoints in the `If-Match` and `If-None-Match` headers to only perform changes on the folder if (no) changes have happened.
    etag: typing.Optional[str]

class FolderBase(RequiredFolderBase, OptionalFolderBase):
    pass
