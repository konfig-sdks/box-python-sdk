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


class PostOAuth2Token(BaseModel):
    # The type of request being made, either using a client-side obtained authorization code, a refresh token, a JWT assertion, client credentials grant or another access token for the purpose of downscoping a token.
    grant_type: Literal["authorization_code", "refresh_token", "client_credentials", "urn:ietf:params:oauth:grant-type:jwt-bearer", "urn:ietf:params:oauth:grant-type:token-exchange"] = Field(alias='grant_type')

    # The Client ID of the application requesting an access token.  Used in combination with `authorization_code`, `client_credentials`, or `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`.
    client_id: typing.Optional[str] = Field(None, alias='client_id')

    # The client secret of the application requesting an access token.  Used in combination with `authorization_code`, `client_credentials`, or `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`.
    client_secret: typing.Optional[str] = Field(None, alias='client_secret')

    # The client-side authorization code passed to your application by Box in the browser redirect after the user has successfully granted your application permission to make API calls on their behalf.  Used in combination with `authorization_code` as the `grant_type`.
    code: typing.Optional[str] = Field(None, alias='code')

    # A refresh token used to get a new access token with.  Used in combination with `refresh_token` as the `grant_type`.
    refresh_token: typing.Optional[str] = Field(None, alias='refresh_token')

    # A JWT assertion for which to request a new access token.  Used in combination with `urn:ietf:params:oauth:grant-type:jwt-bearer` as the `grant_type`.
    assertion: typing.Optional[str] = Field(None, alias='assertion')

    # The token to exchange for a downscoped token. This can be a regular access token, a JWT assertion, or an app token.  Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange` as the `grant_type`.
    subject_token: typing.Optional[str] = Field(None, alias='subject_token')

    # The type of `subject_token` passed in.  Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange` as the `grant_type`.
    subject_token_type: typing.Optional[Literal["urn:ietf:params:oauth:token-type:access_token"]] = Field(None, alias='subject_token_type')

    # The token used to create an annotator token. This is a JWT assertion.  Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange` as the `grant_type`.
    actor_token: typing.Optional[str] = Field(None, alias='actor_token')

    # The type of `actor_token` passed in.  Used in combination with `urn:ietf:params:oauth:grant-type:token-exchange` as the `grant_type`.
    actor_token_type: typing.Optional[Literal["urn:ietf:params:oauth:token-type:id_token"]] = Field(None, alias='actor_token_type')

    # The space-delimited list of scopes that you want apply to the new access token.  The `subject_token` will need to have all of these scopes or the call will error with **401 Unauthorized**.
    scope: typing.Optional[str] = Field(None, alias='scope')

    # Full URL for the file that the token should be generated for.
    resource: typing.Optional[str] = Field(None, alias='resource')

    # Used in combination with `client_credentials` as the `grant_type`.
    box_subject_type: typing.Optional[Literal["enterprise", "user"]] = Field(None, alias='box_subject_type')

    # Used in combination with `client_credentials` as the `grant_type`. Value is determined by `box_subject_type`. If `user` use user ID and if `enterprise` use enterprise ID.
    box_subject_id: typing.Optional[str] = Field(None, alias='box_subject_id')

    # Full URL of the shared link on the file or folder that the token should be generated for.
    box_shared_link: typing.Optional[str] = Field(None, alias='box_shared_link')
    class Config:
        arbitrary_types_allowed = True
