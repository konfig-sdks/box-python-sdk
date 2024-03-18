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


class MetadataFull(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An instance of a metadata template, which has been applied to a file or
folder.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                    can_edit = schemas.BoolSchema
                    
                    
                    class id(
                        schemas.UUIDSchema
                    ):
                    
                    
                        class MetaOapg:
                            format = 'uuid'
                            max_length = 36
                    type = schemas.StrSchema
                    type_version = schemas.IntSchema
                    __annotations__ = {
                        "$canEdit": can_edit,
                        "$id": id,
                        "$type": type,
                        "$typeVersion": type_version,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["$canEdit"]) -> MetaOapg.properties.can_edit: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["$id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["$type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["$typeVersion"]) -> MetaOapg.properties.type_version: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["$canEdit", "$id", "$type", "$typeVersion", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["$canEdit"]) -> typing.Union[MetaOapg.properties.can_edit, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["$id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["$type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["$typeVersion"]) -> typing.Union[MetaOapg.properties.type_version, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["$canEdit", "$id", "$type", "$typeVersion", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class all_of_2(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                
                class additional_properties(
                    schemas.ComposedSchema,
                ):
                
                
                    class MetaOapg:
                        all_of_0 = schemas.AnyTypeSchema
                        all_of_1 = schemas.AnyTypeSchema
                        all_of_2 = schemas.AnyTypeSchema
                        
                        @classmethod
                        @functools.lru_cache()
                        def all_of(cls):
                            # we need this here to make our import statements work
                            # we must store _composed_schemas in here so the code is only run
                            # when we invoke this method. If we kept this at the class
                            # level we would get an error because the class level
                            # code would be run when this module is imported, and these composed
                            # classes don't exist yet because their module has not finished
                            # loading
                            return [
                                cls.all_of_0,
                                cls.all_of_1,
                                cls.all_of_2,
                            ]
                
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'additional_properties':
                        return super().__new__(
                            cls,
                            *args,
                            _configuration=_configuration,
                            **kwargs,
                        )
            
            def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                return super().get_item_oapg(name)
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
            ) -> 'all_of_2':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                MetadataBase,
                cls.all_of_1,
                cls.all_of_2,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MetadataFull':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.metadata_base import MetadataBase
