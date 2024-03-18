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

from box_python_sdk.pydantic.integration_mapping_box_item_slack import IntegrationMappingBoxItemSlack
from box_python_sdk.pydantic.integration_mapping_slack_options import IntegrationMappingSlackOptions

class IntegrationMappingsUpdateSlackMappingRequest(BaseModel):
    box_item: typing.Optional[IntegrationMappingBoxItemSlack] = Field(None, alias='box_item')

    options: typing.Optional[IntegrationMappingSlackOptions] = Field(None, alias='options')
    class Config:
        arbitrary_types_allowed = True
