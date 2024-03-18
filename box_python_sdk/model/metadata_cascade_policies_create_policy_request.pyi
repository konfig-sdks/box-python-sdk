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


class MetadataCascadePoliciesCreatePolicyRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "scope",
            "folder_id",
            "templateKey",
        }
        
        class properties:
            folder_id = schemas.StrSchema
            
            
            class scope(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GLOBAL(cls):
                    return cls("global")
                
                @schemas.classproperty
                def ENTERPRISE(cls):
                    return cls("enterprise")
            templateKey = schemas.StrSchema
            __annotations__ = {
                "folder_id": folder_id,
                "scope": scope,
                "templateKey": templateKey,
            }
    
    scope: MetaOapg.properties.scope
    folder_id: MetaOapg.properties.folder_id
    templateKey: MetaOapg.properties.templateKey
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_id"]) -> MetaOapg.properties.folder_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateKey"]) -> MetaOapg.properties.templateKey: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["folder_id", "scope", "templateKey", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_id"]) -> MetaOapg.properties.folder_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateKey"]) -> MetaOapg.properties.templateKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["folder_id", "scope", "templateKey", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        scope: typing.Union[MetaOapg.properties.scope, str, ],
        folder_id: typing.Union[MetaOapg.properties.folder_id, str, ],
        templateKey: typing.Union[MetaOapg.properties.templateKey, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MetadataCascadePoliciesCreatePolicyRequest':
        return super().__new__(
            cls,
            *args,
            scope=scope,
            folder_id=folder_id,
            templateKey=templateKey,
            _configuration=_configuration,
            **kwargs,
        )
