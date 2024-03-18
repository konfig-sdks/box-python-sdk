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


class RequiredPostOAuth2Revoke(TypedDict):
    pass

class OptionalPostOAuth2Revoke(TypedDict, total=False):
    # The Client ID of the application requesting to revoke the access token.
    client_id: str

    # The client secret of the application requesting to revoke an access token.
    client_secret: str

    # The access token to revoke.
    token: str

class PostOAuth2Revoke(RequiredPostOAuth2Revoke, OptionalPostOAuth2Revoke):
    pass
