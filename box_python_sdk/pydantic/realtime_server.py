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


class RealtimeServer(BaseModel):
    # `realtime_server`
    type: typing.Optional[str] = Field(None, alias='type')

    # The URL for the server.
    url: typing.Optional[str] = Field(None, alias='url')

    # The time in minutes for which this server is available
    ttl: typing.Optional[int] = Field(None, alias='ttl')

    # The maximum number of retries this server will allow before a new long poll should be started by getting a [new list of server](https://raw.githubusercontent.com).
    max_retries: typing.Optional[int] = Field(None, alias='max_retries')

    # The maximum number of seconds without a response after which you should retry the long poll connection.  This helps to overcome network issues where the long poll looks to be working but no packages are coming through.
    retry_timeout: typing.Optional[int] = Field(None, alias='retry_timeout')
    class Config:
        arbitrary_types_allowed = True
