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


class GroupMembershipsUpdateMembershipRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class role(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MEMBER(cls):
                    return cls("member")
                
                @schemas.classproperty
                def ADMIN(cls):
                    return cls("admin")
        
            @staticmethod
            def configurable_permissions() -> typing.Type['GroupMembershipsUpdateMembershipRequestConfigurablePermissions']:
                return GroupMembershipsUpdateMembershipRequestConfigurablePermissions
            __annotations__ = {
                "role": role,
                "configurable_permissions": configurable_permissions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configurable_permissions"]) -> 'GroupMembershipsUpdateMembershipRequestConfigurablePermissions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["role", "configurable_permissions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configurable_permissions"]) -> typing.Union['GroupMembershipsUpdateMembershipRequestConfigurablePermissions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["role", "configurable_permissions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
        configurable_permissions: typing.Union['GroupMembershipsUpdateMembershipRequestConfigurablePermissions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupMembershipsUpdateMembershipRequest':
        return super().__new__(
            cls,
            *args,
            role=role,
            configurable_permissions=configurable_permissions,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.group_memberships_update_membership_request_configurable_permissions import GroupMembershipsUpdateMembershipRequestConfigurablePermissions
