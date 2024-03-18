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

from box_python_sdk.pydantic.transcript_skill_card_entries import TranscriptSkillCardEntries
from box_python_sdk.pydantic.transcript_skill_card_invocation import TranscriptSkillCardInvocation
from box_python_sdk.pydantic.transcript_skill_card_skill import TranscriptSkillCardSkill
from box_python_sdk.pydantic.transcript_skill_card_skill_card_title import TranscriptSkillCardSkillCardTitle

class TranscriptSkillCard(BaseModel):
    # `skill_card`
    type: Literal["skill_card"] = Field(alias='type')

    # `transcript`
    skill_card_type: Literal["transcript"] = Field(alias='skill_card_type')

    skill: TranscriptSkillCardSkill = Field(alias='skill')

    invocation: TranscriptSkillCardInvocation = Field(alias='invocation')

    entries: TranscriptSkillCardEntries = Field(alias='entries')

    # The optional date and time this card was created at.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    skill_card_title: typing.Optional[TranscriptSkillCardSkillCardTitle] = Field(None, alias='skill_card_title')

    # An optional total duration in seconds.  Used with a `skill_card_type` of `transcript` or `timeline`.
    duration: typing.Optional[int] = Field(None, alias='duration')
    class Config:
        arbitrary_types_allowed = True
