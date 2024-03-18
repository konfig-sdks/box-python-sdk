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


class ClassificationsUpdateLabelsDescriptionsRequestItemDataStaticConfigClassification(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Additional details for the classification.
    """


    class MetaOapg:
        
        class properties:
            classificationDefinition = schemas.StrSchema
            colorID = schemas.Int64Schema
            __annotations__ = {
                "classificationDefinition": classificationDefinition,
                "colorID": colorID,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classificationDefinition"]) -> MetaOapg.properties.classificationDefinition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["colorID"]) -> MetaOapg.properties.colorID: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["classificationDefinition", "colorID", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classificationDefinition"]) -> typing.Union[MetaOapg.properties.classificationDefinition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["colorID"]) -> typing.Union[MetaOapg.properties.colorID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["classificationDefinition", "colorID", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        classificationDefinition: typing.Union[MetaOapg.properties.classificationDefinition, str, schemas.Unset] = schemas.unset,
        colorID: typing.Union[MetaOapg.properties.colorID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClassificationsUpdateLabelsDescriptionsRequestItemDataStaticConfigClassification':
        return super().__new__(
            cls,
            *args,
            classificationDefinition=classificationDefinition,
            colorID=colorID,
            _configuration=_configuration,
            **kwargs,
        )