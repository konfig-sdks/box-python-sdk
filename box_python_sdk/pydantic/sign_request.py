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

from box_python_sdk.pydantic.file_base import FileBase
from box_python_sdk.pydantic.file_mini import FileMini
from box_python_sdk.pydantic.folder_mini import FolderMini
from box_python_sdk.pydantic.sign_request_base import SignRequestBase
from box_python_sdk.pydantic.sign_request_signer import SignRequestSigner

SignRequest = typing.Union[SignRequestBase,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
SignRequest = object
