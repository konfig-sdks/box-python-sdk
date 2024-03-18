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

from box_python_sdk.pydantic.zip_download_name_conflicts import ZipDownloadNameConflicts

class ZipDownload(BaseModel):
    # The URL that can be used to download the `zip` archive. A `Get` request to this URL will start streaming the items requested. By default, this URL is only valid for a few seconds, until the `expires_at` time, unless a download is started after which it is valid for the duration of the download.  It is important to note that the domain and path of this URL might change between API calls, and therefore it's important to use this URL as-is.
    download_url: typing.Optional[str] = Field(None, alias='download_url')

    # The URL that can be used to get the status of the `zip` archive being downloaded. A `Get` request to this URL will return the number of files in the archive as well as the number of items already downloaded or skipped. By default, this URL is only valid for a few seconds, until the `expires_at` time, unless a download is started after which the URL is valid for 12 hours from the start of the download.  It is important to note that the domain and path of this URL might change between API calls, and therefore it's important to use this URL as-is.
    status_url: typing.Optional[str] = Field(None, alias='status_url')

    # The time and date when this archive will expire. After this time the `status_url` and `download_url` will return an error.  By default, these URLs are only valid for a few seconds, unless a download is started after which the `download_url` is valid for the duration of the download, and the `status_url` is valid for 12 hours from the start of the download.
    expires_at: typing.Optional[datetime] = Field(None, alias='expires_at')

    name_conflicts: typing.Optional[ZipDownloadNameConflicts] = Field(None, alias='name_conflicts')
    class Config:
        arbitrary_types_allowed = True
