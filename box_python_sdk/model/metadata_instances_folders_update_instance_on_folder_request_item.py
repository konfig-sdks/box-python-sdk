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


class MetadataInstancesFoldersUpdateInstanceOnFolderRequestItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A [JSON-Patch](https://tools.ietf.org/html/rfc6902) operation for a
change to make to the metadata instance.
    """


    class MetaOapg:
        
        class properties:
            
            
            class op(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "add": "ADD",
                        "replace": "REPLACE",
                        "remove": "REMOVE",
                        "test": "TEST",
                        "move": "MOVE",
                        "copy": "COPY",
                    }
                
                @schemas.classproperty
                def ADD(cls):
                    return cls("add")
                
                @schemas.classproperty
                def REPLACE(cls):
                    return cls("replace")
                
                @schemas.classproperty
                def REMOVE(cls):
                    return cls("remove")
                
                @schemas.classproperty
                def TEST(cls):
                    return cls("test")
                
                @schemas.classproperty
                def MOVE(cls):
                    return cls("move")
                
                @schemas.classproperty
                def COPY(cls):
                    return cls("copy")
            path = schemas.StrSchema
            value = schemas.StrSchema
            _from = schemas.StrSchema
            __annotations__ = {
                "op": op,
                "path": path,
                "value": value,
                "from": _from,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["op"]) -> MetaOapg.properties.op: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["op", "path", "value", "from", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["op"]) -> typing.Union[MetaOapg.properties.op, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["op", "path", "value", "from", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        op: typing.Union[MetaOapg.properties.op, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MetadataInstancesFoldersUpdateInstanceOnFolderRequestItem':
        return super().__new__(
            cls,
            *args,
            op=op,
            path=path,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )
