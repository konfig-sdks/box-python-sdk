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

from box_python_sdk.type.file import File
from box_python_sdk.type.folder import Folder
from box_python_sdk.type.user_mini import UserMini
from box_python_sdk.type.webhook import Webhook

class RequiredWebhookInvocation(TypedDict):
    pass

class OptionalWebhookInvocation(TypedDict, total=False):
    # The unique identifier for this webhook invocation
    id: str

    # `webhook_event`
    type: str

    webhook: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    created_by: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # A timestamp identifying the time that the webhook event was triggered.
    created_at: datetime

    trigger: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    source: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class WebhookInvocation(RequiredWebhookInvocation, OptionalWebhookInvocation):
    pass
