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

from box_python_sdk.type.collaboration_acceptance_requirements_status_strong_password_requirement import CollaborationAcceptanceRequirementsStatusStrongPasswordRequirement
from box_python_sdk.type.collaboration_acceptance_requirements_status_terms_of_service_requirement import CollaborationAcceptanceRequirementsStatusTermsOfServiceRequirement
from box_python_sdk.type.collaboration_acceptance_requirements_status_two_factor_authentication_requirement import CollaborationAcceptanceRequirementsStatusTwoFactorAuthenticationRequirement

class RequiredCollaborationAcceptanceRequirementsStatus(TypedDict):
    pass

class OptionalCollaborationAcceptanceRequirementsStatus(TypedDict, total=False):
    terms_of_service_requirement: CollaborationAcceptanceRequirementsStatusTermsOfServiceRequirement

    strong_password_requirement: CollaborationAcceptanceRequirementsStatusStrongPasswordRequirement

    two_factor_authentication_requirement: CollaborationAcceptanceRequirementsStatusTwoFactorAuthenticationRequirement

class CollaborationAcceptanceRequirementsStatus(RequiredCollaborationAcceptanceRequirementsStatus, OptionalCollaborationAcceptanceRequirementsStatus):
    pass
