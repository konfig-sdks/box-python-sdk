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


class SignRequestSignerInput(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Input created by a Signer on a Sign Request
    """


    class MetaOapg:
        required = {
            "page_index",
        }
        
        
        class all_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
                    class type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def SIGNATURE(cls):
                            return cls("signature")
                        
                        @schemas.classproperty
                        def DATE(cls):
                            return cls("date")
                        
                        @schemas.classproperty
                        def TEXT(cls):
                            return cls("text")
                        
                        @schemas.classproperty
                        def CHECKBOX(cls):
                            return cls("checkbox")
                        
                        @schemas.classproperty
                        def RADIO(cls):
                            return cls("radio")
                        
                        @schemas.classproperty
                        def DROPDOWN(cls):
                            return cls("dropdown")
                    
                    
                    class content_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def SIGNATURE(cls):
                            return cls("signature")
                        
                        @schemas.classproperty
                        def INITIAL(cls):
                            return cls("initial")
                        
                        @schemas.classproperty
                        def STAMP(cls):
                            return cls("stamp")
                        
                        @schemas.classproperty
                        def DATE(cls):
                            return cls("date")
                        
                        @schemas.classproperty
                        def CHECKBOX(cls):
                            return cls("checkbox")
                        
                        @schemas.classproperty
                        def TEXT(cls):
                            return cls("text")
                        
                        @schemas.classproperty
                        def FULL_NAME(cls):
                            return cls("full_name")
                        
                        @schemas.classproperty
                        def FIRST_NAME(cls):
                            return cls("first_name")
                        
                        @schemas.classproperty
                        def LAST_NAME(cls):
                            return cls("last_name")
                        
                        @schemas.classproperty
                        def COMPANY(cls):
                            return cls("company")
                        
                        @schemas.classproperty
                        def TITLE(cls):
                            return cls("title")
                        
                        @schemas.classproperty
                        def EMAIL(cls):
                            return cls("email")
                        
                        @schemas.classproperty
                        def ATTACHMENT(cls):
                            return cls("attachment")
                        
                        @schemas.classproperty
                        def RADIO(cls):
                            return cls("radio")
                        
                        @schemas.classproperty
                        def DROPDOWN(cls):
                            return cls("dropdown")
                    page_index = schemas.IntSchema
                    read_only = schemas.BoolSchema
                    __annotations__ = {
                        "type": type,
                        "content_type": content_type,
                        "page_index": page_index,
                        "read_only": read_only,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["content_type"]) -> MetaOapg.properties.content_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["page_index"]) -> MetaOapg.properties.page_index: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["read_only"]) -> MetaOapg.properties.read_only: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "content_type", "page_index", "read_only", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["content_type"]) -> typing.Union[MetaOapg.properties.content_type, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["page_index"]) -> typing.Union[MetaOapg.properties.page_index, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["read_only"]) -> typing.Union[MetaOapg.properties.read_only, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "content_type", "page_index", "read_only", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                content_type: typing.Union[MetaOapg.properties.content_type, str, schemas.Unset] = schemas.unset,
                page_index: typing.Union[MetaOapg.properties.page_index, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                read_only: typing.Union[MetaOapg.properties.read_only, bool, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    type=type,
                    content_type=content_type,
                    page_index=page_index,
                    read_only=read_only,
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
                SignRequestPrefillTag,
                cls.all_of_1,
            ]

    
    page_index: schemas.AnyTypeSchema

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SignRequestSignerInput':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.sign_request_prefill_tag import SignRequestPrefillTag
