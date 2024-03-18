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


class FileRequestUpdateRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The request body to update a file request.
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("inactive")
            is_email_required = schemas.BoolSchema
            is_description_required = schemas.BoolSchema
            expires_at = schemas.DateTimeSchema
            __annotations__ = {
                "title": title,
                "description": description,
                "status": status,
                "is_email_required": is_email_required,
                "is_description_required": is_description_required,
                "expires_at": expires_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_email_required"]) -> MetaOapg.properties.is_email_required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_description_required"]) -> MetaOapg.properties.is_description_required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_at"]) -> MetaOapg.properties.expires_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "status", "is_email_required", "is_description_required", "expires_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_email_required"]) -> typing.Union[MetaOapg.properties.is_email_required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_description_required"]) -> typing.Union[MetaOapg.properties.is_description_required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_at"]) -> typing.Union[MetaOapg.properties.expires_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "status", "is_email_required", "is_description_required", "expires_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        is_email_required: typing.Union[MetaOapg.properties.is_email_required, bool, schemas.Unset] = schemas.unset,
        is_description_required: typing.Union[MetaOapg.properties.is_description_required, bool, schemas.Unset] = schemas.unset,
        expires_at: typing.Union[MetaOapg.properties.expires_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FileRequestUpdateRequest':
        return super().__new__(
            cls,
            *args,
            title=title,
            description=description,
            status=status,
            is_email_required=is_email_required,
            is_description_required=is_description_required,
            expires_at=expires_at,
            _configuration=_configuration,
            **kwargs,
        )