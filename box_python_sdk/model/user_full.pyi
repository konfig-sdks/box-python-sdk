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


class UserFull(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A full representation of a user, as can be returned from any
user API endpoint.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
                    class role(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ADMIN(cls):
                            return cls("admin")
                        
                        @schemas.classproperty
                        def COADMIN(cls):
                            return cls("coadmin")
                        
                        @schemas.classproperty
                        def USER(cls):
                            return cls("user")
                    
                    
                    class tracking_codes(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['TrackingCode']:
                                return TrackingCode
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['TrackingCode'], typing.List['TrackingCode']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'tracking_codes':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'TrackingCode':
                            return super().__getitem__(i)
                    can_see_managed_users = schemas.BoolSchema
                    is_sync_enabled = schemas.BoolSchema
                    is_external_collab_restricted = schemas.BoolSchema
                    is_exempt_from_device_limits = schemas.BoolSchema
                    is_exempt_from_login_verification = schemas.BoolSchema
                    
                    
                    class enterprise(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class all_of_0(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        id = schemas.StrSchema
                                        
                                        
                                        class type(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                            
                                            @schemas.classproperty
                                            def ENTERPRISE(cls):
                                                return cls("enterprise")
                                        name = schemas.StrSchema
                                        __annotations__ = {
                                            "id": id,
                                            "type": type,
                                            "name": name,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "name", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "name", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, ],
                                    id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                                    type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'all_of_0':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        id=id,
                                        type=type,
                                        name=name,
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
                        ) -> 'enterprise':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class my_tags(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'my_tags':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    hostname = schemas.StrSchema
                    is_platform_access_only = schemas.BoolSchema
                    external_app_user_id = schemas.StrSchema
                    __annotations__ = {
                        "role": role,
                        "tracking_codes": tracking_codes,
                        "can_see_managed_users": can_see_managed_users,
                        "is_sync_enabled": is_sync_enabled,
                        "is_external_collab_restricted": is_external_collab_restricted,
                        "is_exempt_from_device_limits": is_exempt_from_device_limits,
                        "is_exempt_from_login_verification": is_exempt_from_login_verification,
                        "enterprise": enterprise,
                        "my_tags": my_tags,
                        "hostname": hostname,
                        "is_platform_access_only": is_platform_access_only,
                        "external_app_user_id": external_app_user_id,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["tracking_codes"]) -> MetaOapg.properties.tracking_codes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["can_see_managed_users"]) -> MetaOapg.properties.can_see_managed_users: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_sync_enabled"]) -> MetaOapg.properties.is_sync_enabled: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_external_collab_restricted"]) -> MetaOapg.properties.is_external_collab_restricted: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_exempt_from_device_limits"]) -> MetaOapg.properties.is_exempt_from_device_limits: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_exempt_from_login_verification"]) -> MetaOapg.properties.is_exempt_from_login_verification: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["enterprise"]) -> MetaOapg.properties.enterprise: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["my_tags"]) -> MetaOapg.properties.my_tags: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_platform_access_only"]) -> MetaOapg.properties.is_platform_access_only: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["external_app_user_id"]) -> MetaOapg.properties.external_app_user_id: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["role", "tracking_codes", "can_see_managed_users", "is_sync_enabled", "is_external_collab_restricted", "is_exempt_from_device_limits", "is_exempt_from_login_verification", "enterprise", "my_tags", "hostname", "is_platform_access_only", "external_app_user_id", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["tracking_codes"]) -> typing.Union[MetaOapg.properties.tracking_codes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["can_see_managed_users"]) -> typing.Union[MetaOapg.properties.can_see_managed_users, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_sync_enabled"]) -> typing.Union[MetaOapg.properties.is_sync_enabled, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_external_collab_restricted"]) -> typing.Union[MetaOapg.properties.is_external_collab_restricted, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_exempt_from_device_limits"]) -> typing.Union[MetaOapg.properties.is_exempt_from_device_limits, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_exempt_from_login_verification"]) -> typing.Union[MetaOapg.properties.is_exempt_from_login_verification, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["enterprise"]) -> typing.Union[MetaOapg.properties.enterprise, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["my_tags"]) -> typing.Union[MetaOapg.properties.my_tags, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_platform_access_only"]) -> typing.Union[MetaOapg.properties.is_platform_access_only, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["external_app_user_id"]) -> typing.Union[MetaOapg.properties.external_app_user_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["role", "tracking_codes", "can_see_managed_users", "is_sync_enabled", "is_external_collab_restricted", "is_exempt_from_device_limits", "is_exempt_from_login_verification", "enterprise", "my_tags", "hostname", "is_platform_access_only", "external_app_user_id", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
                tracking_codes: typing.Union[MetaOapg.properties.tracking_codes, list, tuple, schemas.Unset] = schemas.unset,
                can_see_managed_users: typing.Union[MetaOapg.properties.can_see_managed_users, bool, schemas.Unset] = schemas.unset,
                is_sync_enabled: typing.Union[MetaOapg.properties.is_sync_enabled, bool, schemas.Unset] = schemas.unset,
                is_external_collab_restricted: typing.Union[MetaOapg.properties.is_external_collab_restricted, bool, schemas.Unset] = schemas.unset,
                is_exempt_from_device_limits: typing.Union[MetaOapg.properties.is_exempt_from_device_limits, bool, schemas.Unset] = schemas.unset,
                is_exempt_from_login_verification: typing.Union[MetaOapg.properties.is_exempt_from_login_verification, bool, schemas.Unset] = schemas.unset,
                enterprise: typing.Union[MetaOapg.properties.enterprise, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                my_tags: typing.Union[MetaOapg.properties.my_tags, list, tuple, schemas.Unset] = schemas.unset,
                hostname: typing.Union[MetaOapg.properties.hostname, str, schemas.Unset] = schemas.unset,
                is_platform_access_only: typing.Union[MetaOapg.properties.is_platform_access_only, bool, schemas.Unset] = schemas.unset,
                external_app_user_id: typing.Union[MetaOapg.properties.external_app_user_id, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    role=role,
                    tracking_codes=tracking_codes,
                    can_see_managed_users=can_see_managed_users,
                    is_sync_enabled=is_sync_enabled,
                    is_external_collab_restricted=is_external_collab_restricted,
                    is_exempt_from_device_limits=is_exempt_from_device_limits,
                    is_exempt_from_login_verification=is_exempt_from_login_verification,
                    enterprise=enterprise,
                    my_tags=my_tags,
                    hostname=hostname,
                    is_platform_access_only=is_platform_access_only,
                    external_app_user_id=external_app_user_id,
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
                User,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserFull':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.tracking_code import TrackingCode
from box_python_sdk.model.user import User
