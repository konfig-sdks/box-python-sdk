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


class Events(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of event objects
    """


    class MetaOapg:
        
        class properties:
            chunk_size = schemas.Int64Schema
            next_stream_position = schemas.StrSchema
            
            
            class entries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Event']:
                        return Event
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Event'], typing.List['Event']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entries':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Event':
                    return super().__getitem__(i)
            __annotations__ = {
                "chunk_size": chunk_size,
                "next_stream_position": next_stream_position,
                "entries": entries,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chunk_size"]) -> MetaOapg.properties.chunk_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_stream_position"]) -> MetaOapg.properties.next_stream_position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entries"]) -> MetaOapg.properties.entries: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["chunk_size", "next_stream_position", "entries", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chunk_size"]) -> typing.Union[MetaOapg.properties.chunk_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_stream_position"]) -> typing.Union[MetaOapg.properties.next_stream_position, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entries"]) -> typing.Union[MetaOapg.properties.entries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["chunk_size", "next_stream_position", "entries", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        chunk_size: typing.Union[MetaOapg.properties.chunk_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        next_stream_position: typing.Union[MetaOapg.properties.next_stream_position, str, schemas.Unset] = schemas.unset,
        entries: typing.Union[MetaOapg.properties.entries, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Events':
        return super().__new__(
            cls,
            *args,
            chunk_size=chunk_size,
            next_stream_position=next_stream_position,
            entries=entries,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.event import Event
