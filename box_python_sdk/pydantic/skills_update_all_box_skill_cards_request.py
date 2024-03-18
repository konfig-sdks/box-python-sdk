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

from box_python_sdk.pydantic.skills_update_all_box_skill_cards_request_file import SkillsUpdateAllBoxSkillCardsRequestFile
from box_python_sdk.pydantic.skills_update_all_box_skill_cards_request_file_version import SkillsUpdateAllBoxSkillCardsRequestFileVersion
from box_python_sdk.pydantic.skills_update_all_box_skill_cards_request_metadata import SkillsUpdateAllBoxSkillCardsRequestMetadata
from box_python_sdk.pydantic.skills_update_all_box_skill_cards_request_usage import SkillsUpdateAllBoxSkillCardsRequestUsage

class SkillsUpdateAllBoxSkillCardsRequest(BaseModel):
    # Defines the status of this invocation. Set this to `success` when setting Skill cards.
    status: Literal["invoked", "processing", "success", "transient_failure", "permanent_failure"] = Field(alias='status')

    metadata: SkillsUpdateAllBoxSkillCardsRequestMetadata = Field(alias='metadata')

    file: SkillsUpdateAllBoxSkillCardsRequestFile = Field(alias='file')

    file_version: typing.Optional[SkillsUpdateAllBoxSkillCardsRequestFileVersion] = Field(None, alias='file_version')

    usage: typing.Optional[SkillsUpdateAllBoxSkillCardsRequestUsage] = Field(None, alias='usage')
    class Config:
        arbitrary_types_allowed = True
