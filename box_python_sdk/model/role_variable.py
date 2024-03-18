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


class RoleVariable(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Determines if the
workflow outcome
affects a specific
collaborator role.
    """


    class MetaOapg:
        required = {
            "variable_value",
            "variable_type",
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "variable": "VARIABLE",
                    }
                
                @schemas.classproperty
                def VARIABLE(cls):
                    return cls("variable")
            
            
            class variable_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "collaborator_role": "COLLABORATOR_ROLE",
                    }
                
                @schemas.classproperty
                def COLLABORATOR_ROLE(cls):
                    return cls("collaborator_role")
            
            
            class variable_value(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class all_of_0(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "editor": "EDITOR",
                                "viewer": "VIEWER",
                                "previewer": "PREVIEWER",
                                "uploader": "UPLOADER",
                                "previewer uploader": "PREVIEWER_UPLOADER",
                                "viewer uploader": "VIEWER_UPLOADER",
                                "co-owner": "COOWNER",
                            }
                        
                        @schemas.classproperty
                        def EDITOR(cls):
                            return cls("editor")
                        
                        @schemas.classproperty
                        def VIEWER(cls):
                            return cls("viewer")
                        
                        @schemas.classproperty
                        def PREVIEWER(cls):
                            return cls("previewer")
                        
                        @schemas.classproperty
                        def UPLOADER(cls):
                            return cls("uploader")
                        
                        @schemas.classproperty
                        def PREVIEWER_UPLOADER(cls):
                            return cls("previewer uploader")
                        
                        @schemas.classproperty
                        def VIEWER_UPLOADER(cls):
                            return cls("viewer uploader")
                        
                        @schemas.classproperty
                        def COOWNER(cls):
                            return cls("co-owner")
                    all_of_1 = schemas.AnyTypeSchema
                    
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
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'variable_value':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "variable_type": variable_type,
                "variable_value": variable_value,
            }
    
    variable_value: MetaOapg.properties.variable_value
    variable_type: MetaOapg.properties.variable_type
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable_type"]) -> MetaOapg.properties.variable_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable_value"]) -> MetaOapg.properties.variable_value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "variable_type", "variable_value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable_type"]) -> MetaOapg.properties.variable_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable_value"]) -> MetaOapg.properties.variable_value: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "variable_type", "variable_value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        variable_value: typing.Union[MetaOapg.properties.variable_value, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        variable_type: typing.Union[MetaOapg.properties.variable_type, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RoleVariable':
        return super().__new__(
            cls,
            *args,
            variable_value=variable_value,
            variable_type=variable_type,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )