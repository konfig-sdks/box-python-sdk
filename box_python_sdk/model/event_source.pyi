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


class EventSource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The source file or folder that triggered an event in
the event stream.
    """


    class MetaOapg:
        required = {
            "item_id",
            "item_type",
            "item_name",
        }
        
        class properties:
            
            
            class item_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FILE(cls):
                    return cls("file")
                
                @schemas.classproperty
                def FOLDER(cls):
                    return cls("folder")
            item_id = schemas.StrSchema
            item_name = schemas.StrSchema
        
            @staticmethod
            def classification() -> typing.Type['EventSourceClassification']:
                return EventSourceClassification
            
            
            class parent(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
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
                            FolderMini,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'parent':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class owned_by(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
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
                            UserMini,
                            cls.all_of_1,
                            cls.all_of_2,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'owned_by':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "item_type": item_type,
                "item_id": item_id,
                "item_name": item_name,
                "classification": classification,
                "parent": parent,
                "owned_by": owned_by,
            }
    
    item_id: MetaOapg.properties.item_id
    item_type: MetaOapg.properties.item_type
    item_name: MetaOapg.properties.item_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_type"]) -> MetaOapg.properties.item_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_name"]) -> MetaOapg.properties.item_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classification"]) -> 'EventSourceClassification': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owned_by"]) -> MetaOapg.properties.owned_by: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["item_type", "item_id", "item_name", "classification", "parent", "owned_by", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_type"]) -> MetaOapg.properties.item_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_id"]) -> MetaOapg.properties.item_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_name"]) -> MetaOapg.properties.item_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classification"]) -> typing.Union['EventSourceClassification', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union[MetaOapg.properties.parent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owned_by"]) -> typing.Union[MetaOapg.properties.owned_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["item_type", "item_id", "item_name", "classification", "parent", "owned_by", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        item_id: typing.Union[MetaOapg.properties.item_id, str, ],
        item_type: typing.Union[MetaOapg.properties.item_type, str, ],
        item_name: typing.Union[MetaOapg.properties.item_name, str, ],
        classification: typing.Union['EventSourceClassification', schemas.Unset] = schemas.unset,
        parent: typing.Union[MetaOapg.properties.parent, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        owned_by: typing.Union[MetaOapg.properties.owned_by, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventSource':
        return super().__new__(
            cls,
            *args,
            item_id=item_id,
            item_type=item_type,
            item_name=item_name,
            classification=classification,
            parent=parent,
            owned_by=owned_by,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.event_source_classification import EventSourceClassification
from box_python_sdk.model.folder_mini import FolderMini
from box_python_sdk.model.user_mini import UserMini