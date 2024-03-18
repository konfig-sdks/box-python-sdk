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

from box_python_sdk.type.status_skill_card_invocation import StatusSkillCardInvocation
from box_python_sdk.type.status_skill_card_skill import StatusSkillCardSkill
from box_python_sdk.type.status_skill_card_skill_card_title import StatusSkillCardSkillCardTitle
from box_python_sdk.type.status_skill_card_status import StatusSkillCardStatus

class RequiredStatusSkillCard(TypedDict):
    # `skill_card`
    type: str

    # `status`
    skill_card_type: str

    status: StatusSkillCardStatus

    skill: StatusSkillCardSkill

    invocation: StatusSkillCardInvocation

class OptionalStatusSkillCard(TypedDict, total=False):
    # The optional date and time this card was created at.
    created_at: datetime

    skill_card_title: StatusSkillCardSkillCardTitle

class StatusSkillCard(RequiredStatusSkillCard, OptionalStatusSkillCard):
    pass
