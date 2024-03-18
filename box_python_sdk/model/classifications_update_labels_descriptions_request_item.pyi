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


class ClassificationsUpdateLabelsDescriptionsRequestItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A single classification to update.
    """


    class MetaOapg:
        required = {
            "op",
            "data",
            "fieldKey",
            "enumOptionKey",
        }
        
        class properties:
            
            
            class op(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EDIT_ENUM_OPTION(cls):
                    return cls("editEnumOption")
            
            
            class fieldKey(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BOX__SECURITY__CLASSIFICATION__KEY(cls):
                    return cls("Box__Security__Classification__Key")
            enumOptionKey = schemas.StrSchema
        
            @staticmethod
            def data() -> typing.Type['ClassificationsUpdateLabelsDescriptionsRequestItemData']:
                return ClassificationsUpdateLabelsDescriptionsRequestItemData
            __annotations__ = {
                "op": op,
                "fieldKey": fieldKey,
                "enumOptionKey": enumOptionKey,
                "data": data,
            }
    
    op: MetaOapg.properties.op
    data: 'ClassificationsUpdateLabelsDescriptionsRequestItemData'
    fieldKey: MetaOapg.properties.fieldKey
    enumOptionKey: MetaOapg.properties.enumOptionKey
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["op"]) -> MetaOapg.properties.op: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldKey"]) -> MetaOapg.properties.fieldKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enumOptionKey"]) -> MetaOapg.properties.enumOptionKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'ClassificationsUpdateLabelsDescriptionsRequestItemData': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["op", "fieldKey", "enumOptionKey", "data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["op"]) -> MetaOapg.properties.op: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldKey"]) -> MetaOapg.properties.fieldKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enumOptionKey"]) -> MetaOapg.properties.enumOptionKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'ClassificationsUpdateLabelsDescriptionsRequestItemData': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["op", "fieldKey", "enumOptionKey", "data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        op: typing.Union[MetaOapg.properties.op, str, ],
        data: 'ClassificationsUpdateLabelsDescriptionsRequestItemData',
        fieldKey: typing.Union[MetaOapg.properties.fieldKey, str, ],
        enumOptionKey: typing.Union[MetaOapg.properties.enumOptionKey, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClassificationsUpdateLabelsDescriptionsRequestItem':
        return super().__new__(
            cls,
            *args,
            op=op,
            data=data,
            fieldKey=fieldKey,
            enumOptionKey=enumOptionKey,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.classifications_update_labels_descriptions_request_item_data import ClassificationsUpdateLabelsDescriptionsRequestItemData
