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


class ClassificationTemplateFieldsItemOptionsItemStaticConfigClassification(BaseModel):
    # A longer description of the classification.
    classification_definition: typing.Optional[str] = Field(None, alias='classificationDefinition')

    # An internal Box identifier used to assign a color to a classification label.  Mapping between a `colorID` and a color may change without notice. Currently, the color mappings are as follows.  * `0`: Yellow * `1`: Orange * `2`: Watermelon red * `3`: Purple rain * `4`: Light blue * `5`: Dark blue * `6`: Light green * `7`: Gray
    color_i_d: typing.Optional[int] = Field(None, alias='colorID')
    class Config:
        arbitrary_types_allowed = True
