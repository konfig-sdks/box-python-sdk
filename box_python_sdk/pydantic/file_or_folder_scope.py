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

from box_python_sdk.pydantic.file_mini import FileMini
from box_python_sdk.pydantic.folder_mini import FolderMini

class FileOrFolderScope(BaseModel):
    # The scopes for the resource access
    scope: typing.Optional[Literal["annotation_edit", "annotation_view_all", "annotation_view_self", "base_explorer", "base_picker", "base_preview", "base_upload", "item_delete", "item_download", "item_preview", "item_rename", "item_share"]] = Field(None, alias='scope')

    object: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='object')
    class Config:
        arbitrary_types_allowed = True
