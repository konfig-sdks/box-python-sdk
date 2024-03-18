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

from box_python_sdk.pydantic.skill_cards_metadata_cards import SkillCardsMetadataCards

class SkillCardsMetadata(BaseModel):
    # Whether the user can edit this metadata
    $can_edit_: typing.Optional[bool] = Field(None, alias='$canEdit')

    # A UUID to identify the metadata object
    $id_: typing.Optional[str] = Field(None, alias='$id')

    # An ID for the parent folder
    $parent_: typing.Optional[str] = Field(None, alias='$parent')

    # An ID for the scope in which this template has been applied
    $scope_: typing.Optional[str] = Field(None, alias='$scope')

    # The name of the template
    $template_: typing.Optional[str] = Field(None, alias='$template')

    # A unique identifier for the \"type\" of this instance. This is an internal system property and should not be used by a client application.
    $type_: typing.Optional[str] = Field(None, alias='$type')

    # The last-known version of the template of the object. This is an internal system property and should not be used by a client application.
    $type_version_: typing.Optional[int] = Field(None, alias='$typeVersion')

    # The version of the metadata object. Starts at 0 and increases every time a user-defined property is modified.
    $version_: typing.Optional[int] = Field(None, alias='$version')

    cards: typing.Optional[SkillCardsMetadataCards] = Field(None, alias='cards')
    class Config:
        arbitrary_types_allowed = True
