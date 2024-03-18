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

from box_python_sdk.pydantic.web_links_create_object_request_parent import WebLinksCreateObjectRequestParent

class WebLinksCreateObjectRequest(BaseModel):
    # The URL that this web link links to. Must start with `\"http://\"` or `\"https://\"`.
    url: str = Field(alias='url')

    parent: WebLinksCreateObjectRequestParent = Field(alias='parent')

    # Description of the web link.
    description: typing.Optional[str] = Field(None, alias='description')

    # Name of the web link. Defaults to the URL if not set.
    name: typing.Optional[str] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
