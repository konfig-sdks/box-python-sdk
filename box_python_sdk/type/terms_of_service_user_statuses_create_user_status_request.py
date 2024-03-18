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

from box_python_sdk.type.terms_of_service_user_statuses_create_user_status_request_tos import TermsOfServiceUserStatusesCreateUserStatusRequestTos
from box_python_sdk.type.terms_of_service_user_statuses_create_user_status_request_user import TermsOfServiceUserStatusesCreateUserStatusRequestUser

class RequiredTermsOfServiceUserStatusesCreateUserStatusRequest(TypedDict):
    tos: TermsOfServiceUserStatusesCreateUserStatusRequestTos

    user: TermsOfServiceUserStatusesCreateUserStatusRequestUser

    # Whether the user has accepted the terms.
    is_accepted: bool

class OptionalTermsOfServiceUserStatusesCreateUserStatusRequest(TypedDict, total=False):
    pass

class TermsOfServiceUserStatusesCreateUserStatusRequest(RequiredTermsOfServiceUserStatusesCreateUserStatusRequest, OptionalTermsOfServiceUserStatusesCreateUserStatusRequest):
    pass
