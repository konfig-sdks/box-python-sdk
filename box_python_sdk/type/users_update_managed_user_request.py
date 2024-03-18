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

from box_python_sdk.type.tracking_code import TrackingCode
from box_python_sdk.type.users_update_managed_user_request_notification_email import UsersUpdateManagedUserRequestNotificationEmail

class RequiredUsersUpdateManagedUserRequest(TypedDict):
    pass

class OptionalUsersUpdateManagedUserRequest(TypedDict, total=False):
    # Set this to `null` to roll the user out of the enterprise and make them a free user
    enterprise: typing.Optional[str]

    # Whether the user should receive an email when they are rolled out of an enterprise
    notify: bool

    # The name of the user
    name: str

    # The email address the user uses to log in  Note: If the target user's email is not confirmed, then the primary login address cannot be changed.
    login: str

    # The user’s enterprise role
    role: str

    # The language of the user, formatted in modified version of the [ISO 639-1](https://raw.githubusercontent.com) format.
    language: str

    # Whether the user can use Box Sync
    is_sync_enabled: bool

    # The user’s job title
    job_title: str

    # The user’s phone number
    phone: str

    # The user’s address
    address: str

    # Tracking codes allow an admin to generate reports from the admin console and assign an attribute to a specific group of users. This setting must be enabled for an enterprise before it can be used.
    tracking_codes: typing.List[TrackingCode]

    # Whether the user can see other enterprise users in their contact list
    can_see_managed_users: bool

    # The user's timezone
    timezone: str

    # Whether the user is allowed to collaborate with users outside their enterprise
    is_external_collab_restricted: bool

    # Whether to exempt the user from enterprise device limits
    is_exempt_from_device_limits: bool

    # Whether the user must use two-factor authentication
    is_exempt_from_login_verification: bool

    # Whether the user is required to reset their password
    is_password_reset_required: bool

    # The user's account status
    status: str

    # The user’s total available space in bytes. Set this to `-1` to indicate unlimited storage.
    space_amount: int

    notification_email: UsersUpdateManagedUserRequestNotificationEmail

    # An external identifier for an app user, which can be used to look up the user. This can be used to tie user IDs from external identity providers to Box users.  Note: In order to update this field, you need to request a token using the application that created the app user.
    external_app_user_id: str

class UsersUpdateManagedUserRequest(RequiredUsersUpdateManagedUserRequest, OptionalUsersUpdateManagedUserRequest):
    pass
