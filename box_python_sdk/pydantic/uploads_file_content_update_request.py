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

from box_python_sdk.pydantic.uploads_file_content_update_request_attributes import UploadsFileContentUpdateRequestAttributes

class UploadsFileContentUpdateRequest(BaseModel):
    attributes: UploadsFileContentUpdateRequestAttributes = Field(alias='attributes')

    # The content of the file to upload to Box.  <Message warning>    The `attributes` part of the body must come **before** the   `file` part. Requests that do not follow this format when   uploading the file will receive a HTTP `400` error with a   `metadata_after_file_contents` error code.  </Message>
    file: typing.IO = Field(alias='file')
    class Config:
        arbitrary_types_allowed = True
