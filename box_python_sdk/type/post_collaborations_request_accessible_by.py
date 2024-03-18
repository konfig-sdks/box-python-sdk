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


class RequiredPostCollaborationsRequestAccessibleBy(TypedDict):
    # The type of collaborator to invite.
    type: str

class OptionalPostCollaborationsRequestAccessibleBy(TypedDict, total=False):
    # The ID of the user or group.  Alternatively, use `login` to specify a user by email address.
    id: str

    # The email address of the user to grant access to the item.  Alternatively, use `id` to specify a user by user ID.
    login: str

class PostCollaborationsRequestAccessibleBy(RequiredPostCollaborationsRequestAccessibleBy, OptionalPostCollaborationsRequestAccessibleBy):
    pass
