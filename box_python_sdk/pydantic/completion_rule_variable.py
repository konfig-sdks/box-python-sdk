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


class CompletionRuleVariable(BaseModel):
    # Completion Rule object type. 
    type: Literal["variable"] = Field(alias='type')

    # Variable type for the Completion Rule object. 
    variable_type: Literal["task_completion_rule"] = Field(alias='variable_type')

    # Variable values for a completion rule. 
    variable_value: Literal["all_assignees", "any_assignees"] = Field(alias='variable_value')
    class Config:
        arbitrary_types_allowed = True
