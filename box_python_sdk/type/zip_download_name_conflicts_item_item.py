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


class RequiredZipDownloadNameConflictsItemItem(TypedDict):
    pass

class OptionalZipDownloadNameConflictsItemItem(TypedDict, total=False):
    # The identifier of the item
    id: str

    # The type of this item
    type: str

    # The original name of this item
    original_name: str

    # The new name of this item as it will appear in the downloaded `zip` archive.
    download_name: str

class ZipDownloadNameConflictsItemItem(RequiredZipDownloadNameConflictsItemItem, OptionalZipDownloadNameConflictsItemItem):
    pass
