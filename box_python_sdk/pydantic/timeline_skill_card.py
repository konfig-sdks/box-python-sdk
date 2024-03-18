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

from box_python_sdk.pydantic.timeline_skill_card_entries import TimelineSkillCardEntries
from box_python_sdk.pydantic.timeline_skill_card_invocation import TimelineSkillCardInvocation
from box_python_sdk.pydantic.timeline_skill_card_skill import TimelineSkillCardSkill
from box_python_sdk.pydantic.timeline_skill_card_skill_card_title import TimelineSkillCardSkillCardTitle

class TimelineSkillCard(BaseModel):
    # `skill_card`
    type: Literal["skill_card"] = Field(alias='type')

    # `timeline`
    skill_card_type: Literal["timeline"] = Field(alias='skill_card_type')

    skill: TimelineSkillCardSkill = Field(alias='skill')

    invocation: TimelineSkillCardInvocation = Field(alias='invocation')

    entries: TimelineSkillCardEntries = Field(alias='entries')

    # The optional date and time this card was created at.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    skill_card_title: typing.Optional[TimelineSkillCardSkillCardTitle] = Field(None, alias='skill_card_title')

    # An total duration in seconds of the timeline.
    duration: typing.Optional[int] = Field(None, alias='duration')
    class Config:
        arbitrary_types_allowed = True
