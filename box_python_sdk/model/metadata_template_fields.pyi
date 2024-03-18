# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from box_python_sdk import schemas  # noqa: F401


class MetadataTemplateFields(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An ordered list of template fields which are part of the template. Each
field can be a regular text field, date field, number field, as well as a
single or multi-select list.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['MetadataTemplateFieldsItem']:
            return MetadataTemplateFieldsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['MetadataTemplateFieldsItem'], typing.List['MetadataTemplateFieldsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MetadataTemplateFields':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'MetadataTemplateFieldsItem':
        return super().__getitem__(i)

from box_python_sdk.model.metadata_template_fields_item import MetadataTemplateFieldsItem
