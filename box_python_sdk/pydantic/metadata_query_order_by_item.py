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


class MetadataQueryOrderByItem(BaseModel):
    # The metadata template field to order by.  The `field_key` represents the `key` value of a field from the metadata template being searched for.
    field_key: typing.Optional[str] = Field(None, alias='field_key')

    # The direction to order by, either ascending or descending.  The `ordering` direction must be the same for each item in the array.
    direction: typing.Optional[Literal["ASC", "DESC", "asc", "desc"]] = Field(None, alias='direction')
    class Config:
        arbitrary_types_allowed = True
