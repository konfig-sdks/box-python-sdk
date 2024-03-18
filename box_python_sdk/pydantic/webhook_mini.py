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

from box_python_sdk.pydantic.webhook_mini_target import WebhookMiniTarget

class WebhookMini(BaseModel):
    # The unique identifier for this webhook.
    id: typing.Optional[str] = Field(None, alias='id')

    # `webhook`
    type: typing.Optional[Literal["webhook"]] = Field(None, alias='type')

    target: typing.Optional[WebhookMiniTarget] = Field(None, alias='target')
    class Config:
        arbitrary_types_allowed = True
