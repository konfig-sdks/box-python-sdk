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


class SignRequestPrefillTag(BaseModel):
    # This references the ID of a specific tag contained in a file of the sign request.
    document_tag_id: typing.Optional[typing.Optional[str]] = Field(None, alias='document_tag_id')

    # Text prefill value
    text_value: typing.Optional[typing.Optional[str]] = Field(None, alias='text_value')

    # Checkbox prefill value
    checkbox_value: typing.Optional[typing.Optional[bool]] = Field(None, alias='checkbox_value')

    # Date prefill value
    date_value: typing.Optional[typing.Optional[date]] = Field(None, alias='date_value')
    class Config:
        arbitrary_types_allowed = True
