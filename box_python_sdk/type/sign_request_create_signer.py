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


class RequiredSignRequestCreateSigner(TypedDict):
    pass

class OptionalSignRequestCreateSigner(TypedDict, total=False):
    # Email address of the signer. The email address of the signer is required when making signature requests, except when using templates that are configured to include emails.
    email: typing.Optional[str]

    # Defines the role of the signer in the sign request. A `signer` must sign the document and an `approver` must approve the document. A `final_copy_reader` only receives the final signed document and signing log.
    role: str

    # Used in combination with an embed URL for a sender. After the sender signs, they are redirected to the next `in_person` signer.
    is_in_person: bool

    # Order of the signer
    order: int

    # User ID for the signer in an external application responsible for authentication when accessing the embed URL.
    embed_url_external_user_id: typing.Optional[str]

    # The URL that a signer will be redirected to after signing a document. Defining this URL overrides default or global redirect URL settings for a specific signer. If no declined redirect URL is specified, this URL will be used for decline actions as well.
    redirect_url: typing.Optional[str]

    # The URL that a signer will be redirect to after declining to sign a document. Defining this URL overrides default or global declined redirect URL settings for a specific signer.
    declined_redirect_url: typing.Optional[str]

    # If set to true, signer will need to login to a Box account before signing the request. If the signer does not have an existing account, they will have an option to create a free Box account.
    login_required: typing.Optional[bool]

    # If set, this phone number is be used to verify the signer via two factor authentication before they are able to sign the document.
    verification_phone_number: typing.Optional[str]

    # If set, the signer is required to enter the password before they are able to sign a document. This field is write only.
    password: typing.Optional[str]

    # If set, signers who have the same value will be assigned to the same input and to the same signer group. A signer group is not a Box Group. It is an entity that belongs to a Sign Request and can only be used/accessed within this Sign Request. A signer group is expected to have more than one signer. If the provided value is only used for one signer, this value will be ignored and request will be handled as it was intended for an individual signer. The value provided can be any string and only used to determine which signers belongs to same group. A successful response will provide a generated UUID value instead for signers in the same signer group.
    signer_group_id: typing.Optional[str]

class SignRequestCreateSigner(RequiredSignRequestCreateSigner, OptionalSignRequestCreateSigner):
    pass
