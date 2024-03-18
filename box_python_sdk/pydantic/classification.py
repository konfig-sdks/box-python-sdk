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


class Classification(BaseModel):
    # The name of the classification applied to the item.
    box___security___classification___key: typing.Optional[str] = Field(None, alias='Box__Security__Classification__Key')

    # The identifier of the item that this metadata instance has been attached to. This combines the `type` and the `id` of the parent in the form `{type}_{id}`.
    $parent_: typing.Optional[str] = Field(None, alias='$parent')

    # `securityClassification-6VMVochwUWo`
    $template_: typing.Optional[Literal["securityClassification-6VMVochwUWo"]] = Field(None, alias='$template')

    # The scope of the enterprise that this classification has been applied for.  This will be in the format `enterprise_{enterprise_id}`.
    $scope_: typing.Optional[str] = Field(None, alias='$scope')

    # The version of the metadata instance. This version starts at 0 and increases every time a classification is updated.
    $version_: typing.Optional[int] = Field(None, alias='$version')

    # The unique ID of this classification instance. This will be include the name of the classification template and a unique ID.
    $type_: typing.Optional[str] = Field(None, alias='$type')

    # The version of the metadata template. This version starts at 0 and increases every time the template is updated. This is mostly for internal use.
    $type_version_: typing.Optional[typing.Union[int, float]] = Field(None, alias='$typeVersion')

    # Whether an end user can change the classification.
    $can_edit_: typing.Optional[bool] = Field(None, alias='$canEdit')
    class Config:
        arbitrary_types_allowed = True
