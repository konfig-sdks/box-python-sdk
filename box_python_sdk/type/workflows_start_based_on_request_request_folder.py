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


class RequiredWorkflowsStartBasedOnRequestRequestFolder(TypedDict):
    pass

class OptionalWorkflowsStartBasedOnRequestRequestFolder(TypedDict, total=False):
    # The type of the folder object
    type: str

    # The id of the folder
    id: str

class WorkflowsStartBasedOnRequestRequestFolder(RequiredWorkflowsStartBasedOnRequestRequestFolder, OptionalWorkflowsStartBasedOnRequestRequestFolder):
    pass
