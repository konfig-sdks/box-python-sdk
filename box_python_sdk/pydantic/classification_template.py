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

from box_python_sdk.pydantic.classification_template_fields import ClassificationTemplateFields

class ClassificationTemplate(BaseModel):
    # The ID of the classification template.
    id: str = Field(alias='id')

    # `metadata_template`
    type: Literal["metadata_template"] = Field(alias='type')

    # The scope of the classification template. This is in the format `enterprise_{id}` where the `id` is the enterprise ID.
    scope: str = Field(alias='scope')

    # `securityClassification-6VMVochwUWo`
    template_key: Literal["securityClassification-6VMVochwUWo"] = Field(alias='templateKey')

    # The name of this template as shown in web and mobile interfaces.
    display_name: Literal["Classification"] = Field(alias='displayName')

    fields: ClassificationTemplateFields = Field(alias='fields')

    # Determines if the template is always available in web and mobile interfaces.
    hidden: typing.Optional[bool] = Field(None, alias='hidden')

    # Determines if  classifications are copied along when the file or folder is copied.
    copy_instance_on_item_copy: typing.Optional[bool] = Field(None, alias='copyInstanceOnItemCopy')
    class Config:
        arbitrary_types_allowed = True
