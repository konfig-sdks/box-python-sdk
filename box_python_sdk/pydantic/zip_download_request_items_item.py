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


class ZipDownloadRequestItemsItem(BaseModel):
    # The type of the item to add to the archive.
    type: Literal["file", "folder"] = Field(alias='type')

    # The identifier of the item to add to the archive. When this item is a folder then this can not be the root folder with ID `0`.
    id: str = Field(alias='id')
    class Config:
        arbitrary_types_allowed = True
