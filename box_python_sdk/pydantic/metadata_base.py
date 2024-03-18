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


class MetadataBase(BaseModel):
    # The identifier of the item that this metadata instance has been attached to. This combines the `type` and the `id` of the parent in the form `{type}_{id}`.
    $parent_: typing.Optional[str] = Field(None, alias='$parent')

    # The name of the template
    $template_: typing.Optional[str] = Field(None, alias='$template')

    # An ID for the scope in which this template has been applied. This will be `enterprise_{enterprise_id}` for templates defined for use in this enterprise, and `global` for general templates that are available to all enterprises using Box.
    $scope_: typing.Optional[str] = Field(None, alias='$scope')

    # The version of the metadata instance. This version starts at 0 and increases every time a user-defined property is modified.
    $version_: typing.Optional[int] = Field(None, alias='$version')
    class Config:
        arbitrary_types_allowed = True
