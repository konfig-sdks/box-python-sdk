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

from box_python_sdk.pydantic.sign_request_prefill_tag import SignRequestPrefillTag

class SignRequestBase(BaseModel):
    # Indicates if the sender should receive a `prepare_url` in the response to complete document preparation via UI.
    is_document_preparation_needed: typing.Optional[bool] = Field(None, alias='is_document_preparation_needed')

    # When specified, signature request will be redirected to this url when a document is signed.
    redirect_url: typing.Optional[typing.Optional[str]] = Field(None, alias='redirect_url')

    # The uri that a signer will be redirected to after declining to sign a document.
    declined_redirect_url: typing.Optional[typing.Optional[str]] = Field(None, alias='declined_redirect_url')

    # Disables the usage of signatures generated by typing (text).
    are_text_signatures_enabled: typing.Optional[bool] = Field(None, alias='are_text_signatures_enabled')

    # Subject of sign request email. This is cleaned by sign request. If this field is not passed, a default subject will be used.
    email_subject: typing.Optional[typing.Optional[str]] = Field(None, alias='email_subject')

    # Message to include in sign request email. The field is cleaned through sanitization of specific characters. However, some html tags are allowed. Links included in the message are also converted to hyperlinks in the email. The message may contain the following html tags including `a`, `abbr`, `acronym`, `b`, `blockquote`, `code`, `em`, `i`, `ul`, `li`, `ol`, and `strong`. Be aware that when the text to html ratio is too high, the email may end up in spam filters. Custom styles on these tags are not allowed. If this field is not passed, a default message will be used.
    email_message: typing.Optional[typing.Optional[str]] = Field(None, alias='email_message')

    # Reminds signers to sign a document on day 3, 8, 13 and 18. Reminders are only sent to outstanding signers.
    are_reminders_enabled: typing.Optional[bool] = Field(None, alias='are_reminders_enabled')

    # Name of the sign request.
    name: typing.Optional[str] = Field(None, alias='name')

    # When a document contains sign related tags in the content, you can prefill them using this `prefill_tags` by referencing the 'id' of the tag as the `external_id` field of the prefill tag.
    prefill_tags: typing.Optional[typing.List[SignRequestPrefillTag]] = Field(None, alias='prefill_tags')

    # Set the number of days after which the created signature request will automatically expire if not completed. By default, we do not apply any expiration date on signature requests, and the signature request does not expire.
    days_valid: typing.Optional[typing.Optional[int]] = Field(None, alias='days_valid')

    # This can be used to reference an ID in an external system that the sign request is related to.
    external_id: typing.Optional[typing.Optional[str]] = Field(None, alias='external_id')

    # Forces signers to verify a text message prior to viewing the document. You must specify the phone number of signers to have this setting apply to them.
    is_phone_verification_required_to_view: typing.Optional[typing.Optional[bool]] = Field(None, alias='is_phone_verification_required_to_view')

    # When a signature request is created from a template this field will indicate the id of that template.
    template_id: typing.Optional[typing.Optional[str]] = Field(None, alias='template_id')
    class Config:
        arbitrary_types_allowed = True