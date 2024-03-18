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


class PostOAuth2Token(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A request for a new OAuth 2.0 token
    """


    class MetaOapg:
        required = {
            "grant_type",
        }
        
        class properties:
            
            
            class grant_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'urn'
                    enum_value_to_name = {
                        "authorization_code": "AUTHORIZATION_CODE",
                        "refresh_token": "REFRESH_TOKEN",
                        "client_credentials": "CLIENT_CREDENTIALS",
                        "urn:ietf:params:oauth:grant-type:jwt-bearer": "URNIETFPARAMSOAUTHGRANTTYPEJWTBEARER",
                        "urn:ietf:params:oauth:grant-type:token-exchange": "URNIETFPARAMSOAUTHGRANTTYPETOKENEXCHANGE",
                    }
                
                @schemas.classproperty
                def AUTHORIZATION_CODE(cls):
                    return cls("authorization_code")
                
                @schemas.classproperty
                def REFRESH_TOKEN(cls):
                    return cls("refresh_token")
                
                @schemas.classproperty
                def CLIENT_CREDENTIALS(cls):
                    return cls("client_credentials")
                
                @schemas.classproperty
                def URNIETFPARAMSOAUTHGRANTTYPEJWTBEARER(cls):
                    return cls("urn:ietf:params:oauth:grant-type:jwt-bearer")
                
                @schemas.classproperty
                def URNIETFPARAMSOAUTHGRANTTYPETOKENEXCHANGE(cls):
                    return cls("urn:ietf:params:oauth:grant-type:token-exchange")
            client_id = schemas.StrSchema
            client_secret = schemas.StrSchema
            code = schemas.StrSchema
            refresh_token = schemas.StrSchema
            assertion = schemas.StrSchema
            subject_token = schemas.StrSchema
            
            
            class subject_token_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "urn:ietf:params:oauth:token-type:access_token": "URNIETFPARAMSOAUTHTOKENTYPEACCESS_TOKEN",
                    }
                
                @schemas.classproperty
                def URNIETFPARAMSOAUTHTOKENTYPEACCESS_TOKEN(cls):
                    return cls("urn:ietf:params:oauth:token-type:access_token")
            actor_token = schemas.StrSchema
            
            
            class actor_token_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'urn'
                    enum_value_to_name = {
                        "urn:ietf:params:oauth:token-type:id_token": "URNIETFPARAMSOAUTHTOKENTYPEID_TOKEN",
                    }
                
                @schemas.classproperty
                def URNIETFPARAMSOAUTHTOKENTYPEID_TOKEN(cls):
                    return cls("urn:ietf:params:oauth:token-type:id_token")
            scope = schemas.StrSchema
            resource = schemas.StrSchema
            
            
            class box_subject_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "enterprise": "ENTERPRISE",
                        "user": "USER",
                    }
                
                @schemas.classproperty
                def ENTERPRISE(cls):
                    return cls("enterprise")
                
                @schemas.classproperty
                def USER(cls):
                    return cls("user")
            box_subject_id = schemas.StrSchema
            box_shared_link = schemas.StrSchema
            __annotations__ = {
                "grant_type": grant_type,
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "refresh_token": refresh_token,
                "assertion": assertion,
                "subject_token": subject_token,
                "subject_token_type": subject_token_type,
                "actor_token": actor_token,
                "actor_token_type": actor_token_type,
                "scope": scope,
                "resource": resource,
                "box_subject_type": box_subject_type,
                "box_subject_id": box_subject_id,
                "box_shared_link": box_shared_link,
            }
    
    grant_type: MetaOapg.properties.grant_type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grant_type"]) -> MetaOapg.properties.grant_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_secret"]) -> MetaOapg.properties.client_secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refresh_token"]) -> MetaOapg.properties.refresh_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assertion"]) -> MetaOapg.properties.assertion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject_token"]) -> MetaOapg.properties.subject_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject_token_type"]) -> MetaOapg.properties.subject_token_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actor_token"]) -> MetaOapg.properties.actor_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actor_token_type"]) -> MetaOapg.properties.actor_token_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource"]) -> MetaOapg.properties.resource: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["box_subject_type"]) -> MetaOapg.properties.box_subject_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["box_subject_id"]) -> MetaOapg.properties.box_subject_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["box_shared_link"]) -> MetaOapg.properties.box_shared_link: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["grant_type", "client_id", "client_secret", "code", "refresh_token", "assertion", "subject_token", "subject_token_type", "actor_token", "actor_token_type", "scope", "resource", "box_subject_type", "box_subject_id", "box_shared_link", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grant_type"]) -> MetaOapg.properties.grant_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_secret"]) -> typing.Union[MetaOapg.properties.client_secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refresh_token"]) -> typing.Union[MetaOapg.properties.refresh_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assertion"]) -> typing.Union[MetaOapg.properties.assertion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject_token"]) -> typing.Union[MetaOapg.properties.subject_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject_token_type"]) -> typing.Union[MetaOapg.properties.subject_token_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actor_token"]) -> typing.Union[MetaOapg.properties.actor_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actor_token_type"]) -> typing.Union[MetaOapg.properties.actor_token_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> typing.Union[MetaOapg.properties.scope, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource"]) -> typing.Union[MetaOapg.properties.resource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["box_subject_type"]) -> typing.Union[MetaOapg.properties.box_subject_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["box_subject_id"]) -> typing.Union[MetaOapg.properties.box_subject_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["box_shared_link"]) -> typing.Union[MetaOapg.properties.box_shared_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["grant_type", "client_id", "client_secret", "code", "refresh_token", "assertion", "subject_token", "subject_token_type", "actor_token", "actor_token_type", "scope", "resource", "box_subject_type", "box_subject_id", "box_shared_link", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        grant_type: typing.Union[MetaOapg.properties.grant_type, str, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        client_secret: typing.Union[MetaOapg.properties.client_secret, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        refresh_token: typing.Union[MetaOapg.properties.refresh_token, str, schemas.Unset] = schemas.unset,
        assertion: typing.Union[MetaOapg.properties.assertion, str, schemas.Unset] = schemas.unset,
        subject_token: typing.Union[MetaOapg.properties.subject_token, str, schemas.Unset] = schemas.unset,
        subject_token_type: typing.Union[MetaOapg.properties.subject_token_type, str, schemas.Unset] = schemas.unset,
        actor_token: typing.Union[MetaOapg.properties.actor_token, str, schemas.Unset] = schemas.unset,
        actor_token_type: typing.Union[MetaOapg.properties.actor_token_type, str, schemas.Unset] = schemas.unset,
        scope: typing.Union[MetaOapg.properties.scope, str, schemas.Unset] = schemas.unset,
        resource: typing.Union[MetaOapg.properties.resource, str, schemas.Unset] = schemas.unset,
        box_subject_type: typing.Union[MetaOapg.properties.box_subject_type, str, schemas.Unset] = schemas.unset,
        box_subject_id: typing.Union[MetaOapg.properties.box_subject_id, str, schemas.Unset] = schemas.unset,
        box_shared_link: typing.Union[MetaOapg.properties.box_shared_link, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostOAuth2Token':
        return super().__new__(
            cls,
            *args,
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            refresh_token=refresh_token,
            assertion=assertion,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            actor_token=actor_token,
            actor_token_type=actor_token_type,
            scope=scope,
            resource=resource,
            box_subject_type=box_subject_type,
            box_subject_id=box_subject_id,
            box_shared_link=box_shared_link,
            _configuration=_configuration,
            **kwargs,
        )
