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

from box_python_sdk.pydantic.file import File
from box_python_sdk.pydantic.folder import Folder
from box_python_sdk.pydantic.user_mini import UserMini
from box_python_sdk.pydantic.webhook import Webhook

class WebhookInvocation(BaseModel):
    # The unique identifier for this webhook invocation
    id: typing.Optional[str] = Field(None, alias='id')

    # `webhook_event`
    type: typing.Optional[Literal["webhook_event"]] = Field(None, alias='type')

    webhook: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='webhook')

    created_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='created_by')

    # A timestamp identifying the time that the webhook event was triggered.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    trigger: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='trigger')

    source: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='source')
    class Config:
        arbitrary_types_allowed = True
