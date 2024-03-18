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


class RequiredTrackingCode(TypedDict):
    pass

class OptionalTrackingCode(TypedDict, total=False):
    # `tracking_code`
    type: str

    # The name of the tracking code, which must be preconfigured in the Admin Console
    name: str

    # The value of the tracking code
    value: str

class TrackingCode(RequiredTrackingCode, OptionalTrackingCode):
    pass
