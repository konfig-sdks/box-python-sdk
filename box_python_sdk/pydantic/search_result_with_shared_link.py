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

from box_python_sdk.pydantic.file_full import FileFull
from box_python_sdk.pydantic.folder_full import FolderFull
from box_python_sdk.pydantic.web_link import WebLink

class SearchResultWithSharedLink(BaseModel):
    # The optional shared link through which the user has access to this item. This value is only returned for items for which the user has recently accessed the file through a shared link. For all other items this value will return `null`.
    accessible_via_shared_link: typing.Optional[str] = Field(None, alias='accessible_via_shared_link')

    item: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='item')

    # The result type. The value is always `search_result`.
    type: typing.Optional[str] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
