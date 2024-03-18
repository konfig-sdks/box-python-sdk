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

from box_python_sdk.pydantic.transcript_skill_card_entries_item_appears import TranscriptSkillCardEntriesItemAppears

class TranscriptSkillCardEntriesItem(BaseModel):
    # The text of the entry. This would be the transcribed text assigned to the entry on the timeline.
    text: typing.Optional[str] = Field(None, alias='text')

    appears: typing.Optional[TranscriptSkillCardEntriesItemAppears] = Field(None, alias='appears')
    class Config:
        arbitrary_types_allowed = True
