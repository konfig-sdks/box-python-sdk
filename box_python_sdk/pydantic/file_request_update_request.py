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


class FileRequestUpdateRequest(BaseModel):
    # An optional new title for the file request. This can be used to change the title of the file request.  This will default to the value on the existing file request.
    title: typing.Optional[str] = Field(None, alias='title')

    # An optional new description for the file request. This can be used to change the description of the file request.  This will default to the value on the existing file request.
    description: typing.Optional[str] = Field(None, alias='description')

    # An optional new status of the file request.  When the status is set to `inactive`, the file request will no longer accept new submissions, and any visitor to the file request URL will receive a `HTTP 404` status code.  This will default to the value on the existing file request.
    status: typing.Optional[Literal["active", "inactive"]] = Field(None, alias='status')

    # Whether a file request submitter is required to provide their email address.  When this setting is set to true, the Box UI will show an email field on the file request form.  This will default to the value on the existing file request.
    is_email_required: typing.Optional[bool] = Field(None, alias='is_email_required')

    # Whether a file request submitter is required to provide a description of the files they are submitting.  When this setting is set to true, the Box UI will show a description field on the file request form.  This will default to the value on the existing file request.
    is_description_required: typing.Optional[bool] = Field(None, alias='is_description_required')

    # The date after which a file request will no longer accept new submissions.  After this date, the `status` will automatically be set to `inactive`.  This will default to the value on the existing file request.
    expires_at: typing.Optional[datetime] = Field(None, alias='expires_at')
    class Config:
        arbitrary_types_allowed = True
