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


class TaskLinksEntriesItemTarget(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
            id = schemas.StrSchema
            sequence_id = schemas.StrSchema
            etag = schemas.StrSchema
            sha1 = schemas.StrSchema
            name = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "id": id,
                "sequence_id": sequence_id,
                "etag": etag,
                "sha1": sha1,
                "name": name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequence_id"]) -> MetaOapg.properties.sequence_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["etag"]) -> MetaOapg.properties.etag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sha1"]) -> MetaOapg.properties.sha1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "sequence_id", "etag", "sha1", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequence_id"]) -> typing.Union[MetaOapg.properties.sequence_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["etag"]) -> typing.Union[MetaOapg.properties.etag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sha1"]) -> typing.Union[MetaOapg.properties.sha1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "sequence_id", "etag", "sha1", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        sequence_id: typing.Union[MetaOapg.properties.sequence_id, str, schemas.Unset] = schemas.unset,
        etag: typing.Union[MetaOapg.properties.etag, str, schemas.Unset] = schemas.unset,
        sha1: typing.Union[MetaOapg.properties.sha1, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskLinksEntriesItemTarget':
        return super().__new__(
            cls,
            *args,
            type=type,
            id=id,
            sequence_id=sequence_id,
            etag=etag,
            sha1=sha1,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )