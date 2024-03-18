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


class RequiredSkillInvocationTokenWrite(TypedDict):
    pass

class OptionalSkillInvocationTokenWrite(TypedDict, total=False):
    # The requested access token.
    access_token: str

    # The time in seconds by which this token will expire.
    expires_in: int

    # The type of access token returned.
    token_type: str

    # The permissions that this access token permits, providing a list of resources (files, folders, etc) and the scopes permitted for each of those resources.
    restricted_to: str

class SkillInvocationTokenWrite(RequiredSkillInvocationTokenWrite, OptionalSkillInvocationTokenWrite):
    pass