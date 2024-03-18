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


class RequiredCollaborationAllowlistEntry(TypedDict):
    pass

class OptionalCollaborationAllowlistEntry(TypedDict, total=False):
    # The unique identifier for this entry
    id: str

    # `collaboration_whitelist_entry`
    type: str

    # The whitelisted domain
    domain: str

    # The direction of the collaborations to allow.
    direction: str

    enterprise: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The time the entry was created at
    created_at: datetime

class CollaborationAllowlistEntry(RequiredCollaborationAllowlistEntry, OptionalCollaborationAllowlistEntry):
    pass
