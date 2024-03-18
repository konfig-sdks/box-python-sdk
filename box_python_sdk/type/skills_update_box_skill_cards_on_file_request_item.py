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

from box_python_sdk.type.keyword_skill_card import KeywordSkillCard
from box_python_sdk.type.status_skill_card import StatusSkillCard
from box_python_sdk.type.timeline_skill_card import TimelineSkillCard
from box_python_sdk.type.transcript_skill_card import TranscriptSkillCard

class RequiredSkillsUpdateBoxSkillCardsOnFileRequestItem(TypedDict):
    pass

class OptionalSkillsUpdateBoxSkillCardsOnFileRequestItem(TypedDict, total=False):
    # `replace`
    op: str

    # The JSON Path that represents the card to replace. In most cases this will be in the format `/cards/{index}` where `index` is the zero-indexed position of the card in the list of cards.
    path: str

    value: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class SkillsUpdateBoxSkillCardsOnFileRequestItem(RequiredSkillsUpdateBoxSkillCardsOnFileRequestItem, OptionalSkillsUpdateBoxSkillCardsOnFileRequestItem):
    pass
