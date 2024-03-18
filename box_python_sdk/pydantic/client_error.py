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

from box_python_sdk.pydantic.client_error_context_info import ClientErrorContextInfo

class ClientError(BaseModel):
    # error
    type: typing.Optional[Literal["error"]] = Field(None, alias='type')

    # The HTTP status of the response.
    status: typing.Optional[int] = Field(None, alias='status')

    # A Box-specific error code
    code: typing.Optional[Literal["created", "accepted", "no_content", "redirect", "not_modified", "bad_request", "unauthorized", "forbidden", "not_found", "method_not_allowed", "conflict", "precondition_failed", "too_many_requests", "internal_server_error", "unavailable", "item_name_invalid", "insufficient_scope"]] = Field(None, alias='code')

    # A short message describing the error.
    message: typing.Optional[str] = Field(None, alias='message')

    context_info: typing.Optional[ClientErrorContextInfo] = Field(None, alias='context_info')

    # A URL that links to more information about why this error occurred.
    help_url: typing.Optional[str] = Field(None, alias='help_url')

    # A unique identifier for this response, which can be used when contacting Box support.
    request_id: typing.Optional[str] = Field(None, alias='request_id')
    class Config:
        arbitrary_types_allowed = True
