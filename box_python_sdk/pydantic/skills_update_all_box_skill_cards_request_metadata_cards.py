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

from box_python_sdk.pydantic.keyword_skill_card import KeywordSkillCard
from box_python_sdk.pydantic.status_skill_card import StatusSkillCard
from box_python_sdk.pydantic.timeline_skill_card import TimelineSkillCard
from box_python_sdk.pydantic.transcript_skill_card import TranscriptSkillCard

SkillsUpdateAllBoxSkillCardsRequestMetadataCards = typing.List[typing.Union[typing.List[KeywordSkillCard], typing.List[TimelineSkillCard], typing.List[TranscriptSkillCard], typing.List[StatusSkillCard]]]
