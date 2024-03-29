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


class AccessToken(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A token that can be used to make authenticated API calls.
    """


    class MetaOapg:
        
        class properties:
            access_token = schemas.StrSchema
            expires_in = schemas.Int64Schema
            
            
            class token_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BEARER(cls):
                    return cls("bearer")
            
            
            class restricted_to(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FileOrFolderScope']:
                        return FileOrFolderScope
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FileOrFolderScope'], typing.List['FileOrFolderScope']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'restricted_to':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FileOrFolderScope':
                    return super().__getitem__(i)
            refresh_token = schemas.StrSchema
            
            
            class issued_token_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def URNIETFPARAMSOAUTHTOKENTYPEACCESS_TOKEN(cls):
                    return cls("urn:ietf:params:oauth:token-type:access_token")
            __annotations__ = {
                "access_token": access_token,
                "expires_in": expires_in,
                "token_type": token_type,
                "restricted_to": restricted_to,
                "refresh_token": refresh_token,
                "issued_token_type": issued_token_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_token"]) -> MetaOapg.properties.access_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_in"]) -> MetaOapg.properties.expires_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_type"]) -> MetaOapg.properties.token_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restricted_to"]) -> MetaOapg.properties.restricted_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refresh_token"]) -> MetaOapg.properties.refresh_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issued_token_type"]) -> MetaOapg.properties.issued_token_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["access_token", "expires_in", "token_type", "restricted_to", "refresh_token", "issued_token_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_token"]) -> typing.Union[MetaOapg.properties.access_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_in"]) -> typing.Union[MetaOapg.properties.expires_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_type"]) -> typing.Union[MetaOapg.properties.token_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restricted_to"]) -> typing.Union[MetaOapg.properties.restricted_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refresh_token"]) -> typing.Union[MetaOapg.properties.refresh_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issued_token_type"]) -> typing.Union[MetaOapg.properties.issued_token_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["access_token", "expires_in", "token_type", "restricted_to", "refresh_token", "issued_token_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        access_token: typing.Union[MetaOapg.properties.access_token, str, schemas.Unset] = schemas.unset,
        expires_in: typing.Union[MetaOapg.properties.expires_in, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        token_type: typing.Union[MetaOapg.properties.token_type, str, schemas.Unset] = schemas.unset,
        restricted_to: typing.Union[MetaOapg.properties.restricted_to, list, tuple, schemas.Unset] = schemas.unset,
        refresh_token: typing.Union[MetaOapg.properties.refresh_token, str, schemas.Unset] = schemas.unset,
        issued_token_type: typing.Union[MetaOapg.properties.issued_token_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessToken':
        return super().__new__(
            cls,
            *args,
            access_token=access_token,
            expires_in=expires_in,
            token_type=token_type,
            restricted_to=restricted_to,
            refresh_token=refresh_token,
            issued_token_type=issued_token_type,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.file_or_folder_scope import FileOrFolderScope
