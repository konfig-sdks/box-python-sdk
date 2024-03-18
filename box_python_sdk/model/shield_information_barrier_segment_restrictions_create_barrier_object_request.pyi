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


class ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "restricted_segment",
            "shield_information_barrier_segment",
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SHIELD_INFORMATION_BARRIER_SEGMENT_RESTRICTION(cls):
                    return cls("shield_information_barrier_segment_restriction")
        
            @staticmethod
            def shield_information_barrier_segment() -> typing.Type['ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestShieldInformationBarrierSegment']:
                return ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestShieldInformationBarrierSegment
        
            @staticmethod
            def restricted_segment() -> typing.Type['ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestRestrictedSegment']:
                return ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestRestrictedSegment
        
            @staticmethod
            def shield_information_barrier() -> typing.Type['ShieldInformationBarrierBase']:
                return ShieldInformationBarrierBase
            __annotations__ = {
                "type": type,
                "shield_information_barrier_segment": shield_information_barrier_segment,
                "restricted_segment": restricted_segment,
                "shield_information_barrier": shield_information_barrier,
            }
    
    restricted_segment: 'ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestRestrictedSegment'
    shield_information_barrier_segment: 'ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestShieldInformationBarrierSegment'
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shield_information_barrier_segment"]) -> 'ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestShieldInformationBarrierSegment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restricted_segment"]) -> 'ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestRestrictedSegment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shield_information_barrier"]) -> 'ShieldInformationBarrierBase': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "shield_information_barrier_segment", "restricted_segment", "shield_information_barrier", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shield_information_barrier_segment"]) -> 'ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestShieldInformationBarrierSegment': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restricted_segment"]) -> 'ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestRestrictedSegment': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shield_information_barrier"]) -> typing.Union['ShieldInformationBarrierBase', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "shield_information_barrier_segment", "restricted_segment", "shield_information_barrier", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        restricted_segment: 'ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestRestrictedSegment',
        shield_information_barrier_segment: 'ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestShieldInformationBarrierSegment',
        type: typing.Union[MetaOapg.properties.type, str, ],
        shield_information_barrier: typing.Union['ShieldInformationBarrierBase', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequest':
        return super().__new__(
            cls,
            *args,
            restricted_segment=restricted_segment,
            shield_information_barrier_segment=shield_information_barrier_segment,
            type=type,
            shield_information_barrier=shield_information_barrier,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.shield_information_barrier_base import ShieldInformationBarrierBase
from box_python_sdk.model.shield_information_barrier_segment_restrictions_create_barrier_object_request_restricted_segment import ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestRestrictedSegment
from box_python_sdk.model.shield_information_barrier_segment_restrictions_create_barrier_object_request_shield_information_barrier_segment import ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestShieldInformationBarrierSegment
