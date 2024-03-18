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

from box_python_sdk.pydantic.outcome import Outcome
from box_python_sdk.pydantic.workflows_start_based_on_request_request_files import WorkflowsStartBasedOnRequestRequestFiles
from box_python_sdk.pydantic.workflows_start_based_on_request_request_flow import WorkflowsStartBasedOnRequestRequestFlow
from box_python_sdk.pydantic.workflows_start_based_on_request_request_folder import WorkflowsStartBasedOnRequestRequestFolder

class WorkflowsStartBasedOnRequestRequest(BaseModel):
    flow: WorkflowsStartBasedOnRequestRequestFlow = Field(alias='flow')

    files: WorkflowsStartBasedOnRequestRequestFiles = Field(alias='files')

    folder: WorkflowsStartBasedOnRequestRequestFolder = Field(alias='folder')

    # The type of the parameters object
    type: typing.Optional[Literal["workflow_parameters"]] = Field(None, alias='type')

    # A configurable outcome the workflow should complete.
    outcomes: typing.Optional[typing.List[Outcome]] = Field(None, alias='outcomes')
    class Config:
        arbitrary_types_allowed = True
