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

from box_python_sdk.pydantic.tracking_code import TrackingCode

class PostUsersRequest(BaseModel):
    # The name of the user
    name: str = Field(alias='name')

    # The email address the user uses to log in  Required, unless `is_platform_access_only` is set to `true`.
    login: typing.Optional[str] = Field(None, alias='login')

    # Specifies that the user is an app user.
    is_platform_access_only: typing.Optional[bool] = Field(None, alias='is_platform_access_only')

    # The user’s enterprise role
    role: typing.Optional[Literal["coadmin", "user"]] = Field(None, alias='role')

    # The language of the user, formatted in modified version of the [ISO 639-1](https://raw.githubusercontent.com) format.
    language: typing.Optional[str] = Field(None, alias='language')

    # Whether the user can use Box Sync
    is_sync_enabled: typing.Optional[bool] = Field(None, alias='is_sync_enabled')

    # The user’s job title
    job_title: typing.Optional[str] = Field(None, alias='job_title')

    # The user’s phone number
    phone: typing.Optional[str] = Field(None, alias='phone')

    # The user’s address
    address: typing.Optional[str] = Field(None, alias='address')

    # The user’s total available space in bytes. Set this to `-1` to indicate unlimited storage.
    space_amount: typing.Optional[int] = Field(None, alias='space_amount')

    # Tracking codes allow an admin to generate reports from the admin console and assign an attribute to a specific group of users. This setting must be enabled for an enterprise before it can be used.
    tracking_codes: typing.Optional[typing.List[TrackingCode]] = Field(None, alias='tracking_codes')

    # Whether the user can see other enterprise users in their contact list
    can_see_managed_users: typing.Optional[bool] = Field(None, alias='can_see_managed_users')

    # The user's timezone
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # Whether the user is allowed to collaborate with users outside their enterprise
    is_external_collab_restricted: typing.Optional[bool] = Field(None, alias='is_external_collab_restricted')

    # Whether to exempt the user from enterprise device limits
    is_exempt_from_device_limits: typing.Optional[bool] = Field(None, alias='is_exempt_from_device_limits')

    # Whether the user must use two-factor authentication
    is_exempt_from_login_verification: typing.Optional[bool] = Field(None, alias='is_exempt_from_login_verification')

    # The user's account status
    status: typing.Optional[Literal["active", "inactive", "cannot_delete_edit", "cannot_delete_edit_upload"]] = Field(None, alias='status')

    # An external identifier for an app user, which can be used to look up the user. This can be used to tie user IDs from external identity providers to Box users.
    external_app_user_id: typing.Optional[str] = Field(None, alias='external_app_user_id')
    class Config:
        arbitrary_types_allowed = True
