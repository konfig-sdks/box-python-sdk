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


class RecentItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A recent item accessed by a user.
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
            
            
            class item(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class all_of_0(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            @classmethod
                            @functools.lru_cache()
                            def one_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    FileFull,
                                    FolderFull,
                                    WebLink,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'all_of_0':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
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
                ) -> 'item':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class interaction_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "item_preview": "PREVIEW",
                        "item_upload": "UPLOAD",
                        "item_comment": "COMMENT",
                        "item_open": "OPEN",
                        "item_modify": "MODIFY",
                    }
                
                @schemas.classproperty
                def PREVIEW(cls):
                    return cls("item_preview")
                
                @schemas.classproperty
                def UPLOAD(cls):
                    return cls("item_upload")
                
                @schemas.classproperty
                def COMMENT(cls):
                    return cls("item_comment")
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("item_open")
                
                @schemas.classproperty
                def MODIFY(cls):
                    return cls("item_modify")
            interacted_at = schemas.DateTimeSchema
            interaction_shared_link = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "item": item,
                "interaction_type": interaction_type,
                "interacted_at": interacted_at,
                "interaction_shared_link": interaction_shared_link,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item"]) -> MetaOapg.properties.item: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interaction_type"]) -> MetaOapg.properties.interaction_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interacted_at"]) -> MetaOapg.properties.interacted_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interaction_shared_link"]) -> MetaOapg.properties.interaction_shared_link: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "item", "interaction_type", "interacted_at", "interaction_shared_link", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item"]) -> typing.Union[MetaOapg.properties.item, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interaction_type"]) -> typing.Union[MetaOapg.properties.interaction_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interacted_at"]) -> typing.Union[MetaOapg.properties.interacted_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interaction_shared_link"]) -> typing.Union[MetaOapg.properties.interaction_shared_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "item", "interaction_type", "interacted_at", "interaction_shared_link", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        item: typing.Union[MetaOapg.properties.item, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        interaction_type: typing.Union[MetaOapg.properties.interaction_type, str, schemas.Unset] = schemas.unset,
        interacted_at: typing.Union[MetaOapg.properties.interacted_at, str, datetime, schemas.Unset] = schemas.unset,
        interaction_shared_link: typing.Union[MetaOapg.properties.interaction_shared_link, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecentItem':
        return super().__new__(
            cls,
            *args,
            type=type,
            item=item,
            interaction_type=interaction_type,
            interacted_at=interacted_at,
            interaction_shared_link=interaction_shared_link,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.file_full import FileFull
from box_python_sdk.model.folder_full import FolderFull
from box_python_sdk.model.web_link import WebLink