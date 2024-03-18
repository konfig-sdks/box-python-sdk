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

from box_python_sdk.type.event import Event
from box_python_sdk.type.file import File
from box_python_sdk.type.folder import Folder
from box_python_sdk.type.skill_invocation_status import SkillInvocationStatus
from box_python_sdk.type.skill_invocation_token import SkillInvocationToken

class RequiredSkillInvocation(TypedDict):
    pass

class OptionalSkillInvocation(TypedDict, total=False):
    # `skill_invocation`
    type: str

    # Unique identifier for the invocation request.
    id: str

    skill: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    token: SkillInvocationToken

    status: SkillInvocationStatus

    # The time this invocation was created.
    created_at: datetime

    # Action that triggered the invocation
    trigger: str

    enterprise: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    source: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    event: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class SkillInvocation(RequiredSkillInvocation, OptionalSkillInvocation):
    pass
