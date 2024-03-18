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

from box_python_sdk.type.file_activity_user import FileActivityUser
from box_python_sdk.type.reply_parent import ReplyParent

class RequiredReply(TypedDict):
    pass

class OptionalReply(TypedDict, total=False):
    # reply object id.
    id: str

    # When the reply object was created.
    created_at: datetime

    created_by: FileActivityUser

    # Reply message
    message: str

    parent: ReplyParent

    # Reply type
    type: str

class Reply(RequiredReply, OptionalReply):
    pass
