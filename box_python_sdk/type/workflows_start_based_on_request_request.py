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

from box_python_sdk.type.outcome import Outcome
from box_python_sdk.type.workflows_start_based_on_request_request_files import WorkflowsStartBasedOnRequestRequestFiles
from box_python_sdk.type.workflows_start_based_on_request_request_flow import WorkflowsStartBasedOnRequestRequestFlow
from box_python_sdk.type.workflows_start_based_on_request_request_folder import WorkflowsStartBasedOnRequestRequestFolder

class RequiredWorkflowsStartBasedOnRequestRequest(TypedDict):
    flow: WorkflowsStartBasedOnRequestRequestFlow

    files: WorkflowsStartBasedOnRequestRequestFiles

    folder: WorkflowsStartBasedOnRequestRequestFolder

class OptionalWorkflowsStartBasedOnRequestRequest(TypedDict, total=False):
    # The type of the parameters object
    type: str

    # A configurable outcome the workflow should complete.
    outcomes: typing.List[Outcome]

class WorkflowsStartBasedOnRequestRequest(RequiredWorkflowsStartBasedOnRequestRequest, OptionalWorkflowsStartBasedOnRequestRequest):
    pass
