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

from box_python_sdk.type.terms_of_service_base import TermsOfServiceBase

class RequiredCollaborationAcceptanceRequirementsStatusTermsOfServiceRequirement(TypedDict):
    pass

class OptionalCollaborationAcceptanceRequirementsStatusTermsOfServiceRequirement(TypedDict, total=False):
    # Whether or not the terms of service have been accepted.  The field is `null` when there is no terms of service required.
    is_accepted: typing.Optional[bool]

    terms_of_service: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class CollaborationAcceptanceRequirementsStatusTermsOfServiceRequirement(RequiredCollaborationAcceptanceRequirementsStatusTermsOfServiceRequirement, OptionalCollaborationAcceptanceRequirementsStatusTermsOfServiceRequirement):
    pass
