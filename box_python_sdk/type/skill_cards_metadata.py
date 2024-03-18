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

from box_python_sdk.type.skill_cards_metadata_cards import SkillCardsMetadataCards

RequiredSkillCardsMetadata = TypedDict("RequiredSkillCardsMetadata", {
    })

OptionalSkillCardsMetadata = TypedDict("OptionalSkillCardsMetadata", {
    # Whether the user can edit this metadata
    "$canEdit": bool,

    # A UUID to identify the metadata object
    "$id": str,

    # An ID for the parent folder
    "$parent": str,

    # An ID for the scope in which this template has been applied
    "$scope": str,

    # The name of the template
    "$template": str,

    # A unique identifier for the \"type\" of this instance. This is an internal system property and should not be used by a client application.
    "$type": str,

    # The last-known version of the template of the object. This is an internal system property and should not be used by a client application.
    "$typeVersion": int,

    # The version of the metadata object. Starts at 0 and increases every time a user-defined property is modified.
    "$version": int,

    "cards": SkillCardsMetadataCards,
    }, total=False)

class SkillCardsMetadata(RequiredSkillCardsMetadata, OptionalSkillCardsMetadata):
    pass
