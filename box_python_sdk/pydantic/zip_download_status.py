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


class ZipDownloadStatus(BaseModel):
    # The total number of files in the archive.
    total_file_count: typing.Optional[int] = Field(None, alias='total_file_count')

    # The number of files that have already been downloaded.
    downloaded_file_count: typing.Optional[int] = Field(None, alias='downloaded_file_count')

    # The number of files that have been skipped as they could not be downloaded. In many cases this is due to permission issues that have surfaced between the creation of the request for the archive and the archive being downloaded.
    skipped_file_count: typing.Optional[int] = Field(None, alias='skipped_file_count')

    # The number of folders that have been skipped as they could not be downloaded. In many cases this is due to permission issues that have surfaced between the creation of the request for the archive and the archive being downloaded.
    skipped_folder_count: typing.Optional[int] = Field(None, alias='skipped_folder_count')

    # The state of the archive being downloaded.
    state: typing.Optional[Literal["in_progress", "failed", "succeeded"]] = Field(None, alias='state')
    class Config:
        arbitrary_types_allowed = True
