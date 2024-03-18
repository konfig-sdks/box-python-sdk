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


class FilesUpdateFileRequestPermissions(BaseModel):
    # Defines who is allowed to download this file. The possible values are either `open` for everyone or `company` for the other members of the user's enterprise.  This setting overrides the download permissions that are normally part of the `role` of a collaboration. When set to `company`, this essentially removes the download option for external users with `viewer` or `editor` a roles.
    can_download: typing.Optional[Literal["open", "company"]] = Field(None, alias='can_download')
    class Config:
        arbitrary_types_allowed = True
