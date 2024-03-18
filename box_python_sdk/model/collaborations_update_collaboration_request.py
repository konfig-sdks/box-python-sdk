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


class CollaborationsUpdateCollaborationRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "role",
        }
        
        class properties:
            
            
            class role(
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
                        "owner": "OWNER",
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
                
                @schemas.classproperty
                def OWNER(cls):
                    return cls("owner")
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "pending": "PENDING",
                        "accepted": "ACCEPTED",
                        "rejected": "REJECTED",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending")
                
                @schemas.classproperty
                def ACCEPTED(cls):
                    return cls("accepted")
                
                @schemas.classproperty
                def REJECTED(cls):
                    return cls("rejected")
            expires_at = schemas.DateTimeSchema
            can_view_path = schemas.BoolSchema
            __annotations__ = {
                "role": role,
                "status": status,
                "expires_at": expires_at,
                "can_view_path": can_view_path,
            }
    
    role: MetaOapg.properties.role
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expires_at"]) -> MetaOapg.properties.expires_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["can_view_path"]) -> MetaOapg.properties.can_view_path: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["role", "status", "expires_at", "can_view_path", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expires_at"]) -> typing.Union[MetaOapg.properties.expires_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["can_view_path"]) -> typing.Union[MetaOapg.properties.can_view_path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["role", "status", "expires_at", "can_view_path", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        role: typing.Union[MetaOapg.properties.role, str, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        expires_at: typing.Union[MetaOapg.properties.expires_at, str, datetime, schemas.Unset] = schemas.unset,
        can_view_path: typing.Union[MetaOapg.properties.can_view_path, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CollaborationsUpdateCollaborationRequest':
        return super().__new__(
            cls,
            *args,
            role=role,
            status=status,
            expires_at=expires_at,
            can_view_path=can_view_path,
            _configuration=_configuration,
            **kwargs,
        )
