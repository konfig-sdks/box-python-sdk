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


class ShieldInformationBarrierSegmentMembersCreateNewMemberRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "shield_information_barrier_segment",
            "user",
        }
        
        class properties:
        
            @staticmethod
            def shield_information_barrier_segment() -> typing.Type['ShieldInformationBarrierSegmentMembersCreateNewMemberRequestShieldInformationBarrierSegment']:
                return ShieldInformationBarrierSegmentMembersCreateNewMemberRequestShieldInformationBarrierSegment
        
            @staticmethod
            def user() -> typing.Type['UserBase']:
                return UserBase
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SHIELD_INFORMATION_BARRIER_SEGMENT_MEMBER(cls):
                    return cls("shield_information_barrier_segment_member")
        
            @staticmethod
            def shield_information_barrier() -> typing.Type['ShieldInformationBarrierBase']:
                return ShieldInformationBarrierBase
            __annotations__ = {
                "shield_information_barrier_segment": shield_information_barrier_segment,
                "user": user,
                "type": type,
                "shield_information_barrier": shield_information_barrier,
            }
    
    shield_information_barrier_segment: 'ShieldInformationBarrierSegmentMembersCreateNewMemberRequestShieldInformationBarrierSegment'
    user: 'UserBase'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shield_information_barrier_segment"]) -> 'ShieldInformationBarrierSegmentMembersCreateNewMemberRequestShieldInformationBarrierSegment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'UserBase': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shield_information_barrier"]) -> 'ShieldInformationBarrierBase': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["shield_information_barrier_segment", "user", "type", "shield_information_barrier", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shield_information_barrier_segment"]) -> 'ShieldInformationBarrierSegmentMembersCreateNewMemberRequestShieldInformationBarrierSegment': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'UserBase': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shield_information_barrier"]) -> typing.Union['ShieldInformationBarrierBase', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["shield_information_barrier_segment", "user", "type", "shield_information_barrier", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        shield_information_barrier_segment: 'ShieldInformationBarrierSegmentMembersCreateNewMemberRequestShieldInformationBarrierSegment',
        user: 'UserBase',
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        shield_information_barrier: typing.Union['ShieldInformationBarrierBase', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShieldInformationBarrierSegmentMembersCreateNewMemberRequest':
        return super().__new__(
            cls,
            *args,
            shield_information_barrier_segment=shield_information_barrier_segment,
            user=user,
            type=type,
            shield_information_barrier=shield_information_barrier,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.shield_information_barrier_base import ShieldInformationBarrierBase
from box_python_sdk.model.shield_information_barrier_segment_members_create_new_member_request_shield_information_barrier_segment import ShieldInformationBarrierSegmentMembersCreateNewMemberRequestShieldInformationBarrierSegment
from box_python_sdk.model.user_base import UserBase
