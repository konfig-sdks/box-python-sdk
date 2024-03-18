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


class RequiredZipDownloadStatus(TypedDict):
    pass

class OptionalZipDownloadStatus(TypedDict, total=False):
    # The total number of files in the archive.
    total_file_count: int

    # The number of files that have already been downloaded.
    downloaded_file_count: int

    # The number of files that have been skipped as they could not be downloaded. In many cases this is due to permission issues that have surfaced between the creation of the request for the archive and the archive being downloaded.
    skipped_file_count: int

    # The number of folders that have been skipped as they could not be downloaded. In many cases this is due to permission issues that have surfaced between the creation of the request for the archive and the archive being downloaded.
    skipped_folder_count: int

    # The state of the archive being downloaded.
    state: str

class ZipDownloadStatus(RequiredZipDownloadStatus, OptionalZipDownloadStatus):
    pass
