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


class PostOAuth2TokenRefreshAccessToken(BaseModel):
    # The type of request being made, in this case a refresh request.
    grant_type: Literal["refresh_token"] = Field(alias='grant_type')

    # The client ID of the application requesting to refresh the token.
    client_id: str = Field(alias='client_id')

    # The client secret of the application requesting to refresh the token.
    client_secret: str = Field(alias='client_secret')

    # The refresh token to refresh.
    refresh_token: str = Field(alias='refresh_token')
    class Config:
        arbitrary_types_allowed = True
