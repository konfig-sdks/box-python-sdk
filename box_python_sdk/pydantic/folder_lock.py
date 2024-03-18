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

from box_python_sdk.pydantic.folder_lock_locked_operations import FolderLockLockedOperations
from box_python_sdk.pydantic.folder_mini import FolderMini
from box_python_sdk.pydantic.user_base import UserBase

class FolderLock(BaseModel):
    folder: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='folder')

    # The unique identifier for this folder lock.
    id: typing.Optional[str] = Field(None, alias='id')

    # The object type, always `folder_lock`.
    type: typing.Optional[str] = Field(None, alias='type')

    created_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='created_by')

    # When the folder lock object was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    locked_operations: typing.Optional[FolderLockLockedOperations] = Field(None, alias='locked_operations')

    # The lock type, always `freeze`.
    lock_type: typing.Optional[str] = Field(None, alias='lock_type')
    class Config:
        arbitrary_types_allowed = True
