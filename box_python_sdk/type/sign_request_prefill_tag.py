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


class RequiredSignRequestPrefillTag(TypedDict):
    pass

class OptionalSignRequestPrefillTag(TypedDict, total=False):
    # This references the ID of a specific tag contained in a file of the sign request.
    document_tag_id: typing.Optional[str]

    # Text prefill value
    text_value: typing.Optional[str]

    # Checkbox prefill value
    checkbox_value: typing.Optional[bool]

    # Date prefill value
    date_value: typing.Optional[date]

class SignRequestPrefillTag(RequiredSignRequestPrefillTag, OptionalSignRequestPrefillTag):
    pass
